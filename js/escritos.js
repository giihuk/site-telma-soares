/* Página de Escritos: lista todos os textos ou abre um ensaio (?t=slug). */
(function () {
  "use strict";
  var D = window.TelmaDados, T = D.T, esc = D.esc, alvo = document.getElementById("leitura");
  var en = (document.documentElement.lang || "").indexOf("en") === 0;
  var slug = new URLSearchParams(location.search).get("t");
  var SETA = '<svg class="ir" aria-hidden="true" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M19 12H5"/><path d="M11 6l-6 6 6 6"/></svg>';

  /* Markdown mínimo e seguro: o texto é escapado antes de qualquer marcação. */
  function inline(s) {
    return esc(s)
      .replace(/\[([^\]]+)\]\(([^)\s]+)\)/g, function (_, a, u) { return '<a href="' + D.urlSegura(u.replace(/&amp;/g, "&")).replace(/"/g, "%22") + '" rel="noopener">' + a + "</a>"; })
      .replace(/\*\*([^*]+)\*\*/g, "<strong>$1</strong>")
      .replace(/(^|[^*])\*([^*]+)\*/g, "$1<em>$2</em>");
  }
  function md(txt) {
    var out = [], lista = null, tipo = "";
    function fecha() { if (lista) { out.push("<" + tipo + ">" + lista.join("") + "</" + tipo + ">"); lista = null; } }
    String(txt || "").replace(/\r/g, "").split(/\n{2,}/).forEach(function (b) {
      b = b.trim(); if (!b) return;
      var ls = b.split("\n");
      if (/^#{1,3} /.test(b)) { fecha(); var n = b.match(/^#+/)[0].length; out.push("<h" + (n + 1) + ">" + inline(b.replace(/^#+ /, "")) + "</h" + (n + 1) + ">"); return; }
      if (ls.every(function (l) { return /^[-*] /.test(l); })) { fecha(); tipo = "ul"; lista = ls.map(function (l) { return "<li>" + inline(l.slice(2)) + "</li>"; }); fecha(); return; }
      if (ls.every(function (l) { return /^\d+\. /.test(l); })) { fecha(); tipo = "ol"; lista = ls.map(function (l) { return "<li>" + inline(l.replace(/^\d+\. /, "")) + "</li>"; }); fecha(); return; }
      if (ls.every(function (l) { return /^> ?/.test(l); })) { fecha(); out.push("<blockquote>" + inline(ls.map(function (l) { return l.replace(/^> ?/, ""); }).join(" ")) + "</blockquote>"); return; }
      fecha(); out.push("<p>" + inline(ls.join(" ")) + "</p>");
    });
    return out.join("\n");
  }
  function dataLonga(iso) {
    var d = new Date(iso + "T12:00:00"); if (isNaN(d)) return iso || "";
    return d.toLocaleDateString(en ? "en-GB" : "pt-BR", { day: "numeric", month: "long", year: "numeric" });
  }

  Promise.all([D.busca("content/escritos.json", "dados-escritos"), D.busca("content/publicacoes.json", "dados-publicacoes")]).then(function (r) {
    var ens = (r[0] && r[0].ensaios) || [], pubs = (r[1] && r[1].publicacoes) || [];
    if (slug) {
      var e = ens.filter(function (x) { return x.slug === slug; })[0];
      if (!e) { alvo.innerHTML = '<p class="olho">' + esc(T.titulo) + "</p><h1>" + esc(T.nao) + '</h1><p style="margin-top:24px"><a class="seta" href="index.html">' + SETA + esc(T.voltar) + "</a></p>"; return; }
      var tit = (en && e.titulo_en) || e.titulo, res = (en && e.resumo_en) || e.resumo || "", corpo = (en && e.corpo_en) || e.corpo || "";
      document.title = tit + " | Telma Soares";
      alvo.innerHTML = '<p class="nao-imprime"><a class="seta" href="index.html">' + SETA + esc(T.voltar) + '</a></p><p class="olho">' + esc(T.ensaio) + " · " + esc(dataLonga(e.data)) + "</p><h1>" + esc(tit) + "</h1>" +
        (res ? '<p class="resumo">' + esc(res) + "</p>" : "") + '<p style="margin-top:14px;font-weight:600">' + esc(T.por) + "</p>" +
        '<div class="acoes">' + (e.pdf ? '<a class="btn" href="' + esc(D.urlSegura(D.BASE + String(e.pdf).replace(/^\//, ""))) + '" download>' + esc(T.baixar) + "</a>" : "") +
        '<button type="button" class="btn ' + (e.pdf ? "contorno" : "") + '" id="salvar-pdf">' + esc(T.salvar) + "</button></div>" +
        '<div class="prosa" id="prosa"></div>';
      /* o texto já é escapado antes da marcação; onde existe, a Sanitizer API faz uma segunda barreira (Modern Web Guidance: sanitize-untrusted-html) */
      var pr = document.getElementById("prosa"), marc = md(corpo);
      if (typeof pr.setHTML === "function") pr.setHTML(marc); else pr.innerHTML = marc;
      document.getElementById("salvar-pdf").addEventListener("click", function () { window.print(); });
      return;
    }
    function li(ano, tit, det, url, ext) {
      return '<li class="escrito"><a href="' + esc(D.urlSegura(url)) + '"' + (ext ? ' target="_blank" rel="noopener"' : "") + '><span class="ano">' + esc(ano) + '</span><span><span class="tit">' + esc(tit) + '</span><span class="det">' + esc(det) + "</span></span></a></li>";
    }
    var h = '<p class="olho">Telma Soares</p><h1>' + esc(T.titulo) + '</h1><p class="resumo">' + esc(T.intro) + "</p>";
    if (ens.length) {
      h += '<h2 style="font-size:1.6rem;margin-top:56px">' + esc(T.ensaios) + '</h2><ul style="margin-top:16px">';
      ens.slice().sort(function (a, b) { return (a.data || "") < (b.data || "") ? 1 : -1; }).forEach(function (e) {
        h += li((e.data || "").slice(0, 4), (en && e.titulo_en) || e.titulo, (en && e.resumo_en) || e.resumo || T.ensaio, "index.html?t=" + encodeURIComponent(e.slug), false);
      });
      h += '</ul><h2 style="font-size:1.6rem;margin-top:56px">' + esc(T.pubs) + "</h2>";
    }
    h += '<ul style="margin-top:' + (ens.length ? 16 : 40) + 'px">';
    pubs.forEach(function (p) { h += li(String(p.ano), p.titulo, ((en && p.tipo_en) || p.tipo) + " · " + p.veiculo + (p.coautores ? " · " + T.com + " " + p.coautores : ""), p.url, true); });
    alvo.innerHTML = h + "</ul>";
  });
})();
