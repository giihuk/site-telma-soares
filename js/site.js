/* Telma Soares · comportamento do site. Sem dependências externas.
   Tudo é opcional: sem JavaScript o conteúdo continua visível. */
(function () {
  "use strict";
  var d = document, root = d.documentElement;
  var reduz = window.matchMedia("(prefers-reduced-motion: reduce)");
  var T = window.SITE_TEXTOS || {};
  var CFG = window.SITE_CONFIG || {};
  var BASE = root.getAttribute("data-base") || "";
  function $(s, c) { return (c || d).querySelector(s); }
  function $$(s, c) { return Array.prototype.slice.call((c || d).querySelectorAll(s)); }
  function esc(s) { return String(s == null ? "" : s).replace(/[&<>"']/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]; }); }
  function urlSegura(u) { return /^(https?:\/\/|\/|\.\.?\/|#|[a-z0-9_\-]+[\/.?])/i.test(u || "") && !/^javascript:/i.test(u) ? u : "#"; }
  function guarda(k, v) { try { if (v === undefined) return localStorage.getItem(k); localStorage.setItem(k, v); } catch (e) { return null; } }

  /* pausa: o motor TelmaMotion cuida dos fundos e dos botões; aqui só guardamos a escolha e pausamos o letreiro junto */
  var ctl = window.telmaMotionController, toggles = $$("[data-telma-motion-toggle]");
  function sincPausa() {
    var on = toggles.some(function (b) { return b.getAttribute("aria-pressed") === "true"; });
    root.classList.toggle("pausado", on); return on;
  }
  if (ctl && ctl.setPaused && guarda("telma-pausa") === "1") ctl.setPaused(true);
  toggles.forEach(function (b) { b.addEventListener("click", function () { setTimeout(function () { guarda("telma-pausa", sincPausa() ? "1" : "0"); }, 0); }); });
  sincPausa();

  /* menu móvel */
  var menuBtn = $(".menu-btn"), nav = $("#nav");
  function fechaMenu() { if (!nav) return; nav.classList.remove("aberto"); menuBtn.setAttribute("aria-expanded", "false"); menuBtn.setAttribute("aria-label", T.abrirMenu); }
  if (menuBtn && nav) {
    menuBtn.addEventListener("click", function () {
      var a = !nav.classList.contains("aberto");
      nav.classList.toggle("aberto", a);
      menuBtn.setAttribute("aria-expanded", a ? "true" : "false");
      menuBtn.setAttribute("aria-label", a ? T.fecharMenu : T.abrirMenu);
    });
    nav.addEventListener("click", function (e) { if (e.target.closest("a")) fechaMenu(); });
    d.addEventListener("keydown", function (e) { if (e.key === "Escape" && nav.classList.contains("aberto")) { fechaMenu(); menuBtn.focus(); } });
  }

  /* cabeçalho, barra de progresso, voltar ao topo, frase que acende, linha do tempo */
  var topo = $(".topo"), barra = $(".progresso"), subir = $(".subir");
  var frase = $(".frase.acende"), palavras = [];
  if (frase && !reduz.matches) {
    var txt = frase.textContent.trim().split(/\s+/);
    frase.setAttribute("aria-label", txt.join(" "));
    frase.innerHTML = txt.map(function (p) { return '<span class="p" aria-hidden="true">' + esc(p) + "</span>"; }).join(" ");
    palavras = $$(".p", frase);
  } else if (frase) { frase.classList.remove("acende"); }
  var tempo = $(".tempo");
  var barraCss = !reduz.matches && window.CSS && CSS.supports && CSS.supports("animation-timeline: scroll()");
  var tic = false;
  function aoRolar() {
    tic = false;
    var y = window.scrollY, h = d.documentElement.scrollHeight - window.innerHeight, vh = window.innerHeight;
    if (topo) topo.classList.toggle("rolou", y > 24);
    if (barra && !barraCss) barra.style.transform = "scaleX(" + (h > 0 ? Math.min(1, y / h) : 0) + ")";
    if (subir) {
      var mostra = y > vh;
      /* se o botão some enquanto está em foco, o foco vai para o conteúdo (Modern Web Guidance: scroll-position-aware-elements) */
      if (!mostra && d.activeElement === subir) { var m = d.getElementById("conteudo"); if (m) { m.setAttribute("tabindex", "-1"); m.focus({ preventScroll: true }); } }
      subir.classList.toggle("on", mostra);
    }
    if (palavras.length) {
      var r = frase.getBoundingClientRect();
      var p = (vh * 0.85 - r.top) / (r.height + vh * 0.35);
      var n = Math.round(Math.max(0, Math.min(1, p)) * palavras.length);
      palavras.forEach(function (el, i) { el.classList.toggle("on", i < n); });
    }
    if (tempo) {
      var t = tempo.getBoundingClientRect();
      tempo.style.setProperty("--prog", Math.max(0, Math.min(1, (vh * 0.6 - t.top) / t.height)).toFixed(3));
    }
  }
  window.addEventListener("scroll", function () { if (!tic) { tic = true; requestAnimationFrame(aoRolar); } }, { passive: true });
  window.addEventListener("resize", aoRolar);
  aoRolar();

  /* entradas ao rolar e contadores */
  function conta(el) {
    var alvo = +el.getAttribute("data-conta"), pre = el.getAttribute("data-prefixo") || "", suf = el.getAttribute("data-sufixo") || "";
    var fmt = function (n) { return pre + n.toLocaleString(root.lang || "pt-BR") + suf; };
    if (reduz.matches) { el.textContent = fmt(alvo); return; }
    var t0 = null, dur = 1400;
    function passo(t) {
      if (!t0) t0 = t;
      var k = Math.min(1, (t - t0) / dur), e = 1 - Math.pow(1 - k, 3);
      el.textContent = fmt(Math.round(alvo * e));
      if (k < 1) requestAnimationFrame(passo);
    }
    requestAnimationFrame(passo);
  }
  function tracaLettering(svg) {
    var at = 0;
    $$("path", svg).forEach(function (p) {
      var len = Math.ceil(p.getTotalLength()) + 40, dur = Math.max(0.25, len / 2600);
      p.style.setProperty("--len", len); p.style.setProperty("--dur", dur + "s"); p.style.setProperty("--at", at + "s");
      at += dur * 0.82;
    });
  }
  $$(".lettering").forEach(tracaLettering);
  if ("IntersectionObserver" in window) {
    var io = new IntersectionObserver(function (es) {
      es.forEach(function (e) {
        if (!e.isIntersecting) return;
        e.target.classList.add("in");
        $$("[data-conta]", e.target).forEach(conta);
        if (e.target.hasAttribute("data-conta")) conta(e.target);
        io.unobserve(e.target);
      });
    }, { rootMargin: "0px 0px -8% 0px", threshold: 0.12 });
    $$(".anim,.pilar,.faixa,.num,.assina .lettering").forEach(function (el) { io.observe(el); });
  } else {
    $$(".anim,.pilar,.faixa,.assina .lettering").forEach(function (el) { el.classList.add("in"); });
  }
  var hl = $(".hero .lettering");
  if (hl) setTimeout(function () { hl.classList.add("in"); }, reduz.matches ? 0 : 1300);

  /* seção ativa no menu */
  var links = $$("#nav a.link[href^='#']");
  if (links.length && "IntersectionObserver" in window) {
    var mapa = {};
    links.forEach(function (a) { mapa[a.getAttribute("href").slice(1)] = a; });
    var so = new IntersectionObserver(function (es) {
      es.forEach(function (e) {
        if (!e.isIntersecting) return;
        links.forEach(function (a) { a.classList.remove("ativo"); a.removeAttribute("aria-current"); });
        var a = mapa[e.target.id]; if (a) { a.classList.add("ativo"); a.setAttribute("aria-current", "true"); }
      });
    }, { rootMargin: "-45% 0px -50% 0px" });
    Object.keys(mapa).forEach(function (id) { var s = d.getElementById(id); if (s) so.observe(s); });
  }

  /* imprensa: filtros, busca e temas, combinados */
  (function () {
    var lista = $("#lista-imprensa"); if (!lista) return;
    var itens = $$("li", lista), filtros = $$("[data-filtro]"), input = $("#busca-imprensa-input"),
      limpa = $("#limpa-busca-btn"), vazio = $("#imprensa-vazio"), limpar = $("#limpar-imprensa"), temas = $$(".temas button");
    var tipo = "todos";
    function norm(s) { return (s || "").toLowerCase().normalize("NFD").replace(/[̀-ͯ]/g, ""); }
    filtros.forEach(function (b) {
      var f = b.getAttribute("data-filtro"), n = f === "todos" ? itens.length : itens.filter(function (li) { return li.getAttribute("data-tipo") === f; }).length;
      var c = $("b", b); if (c) c.textContent = n;
    });
    function aplica() {
      var q = norm(input.value.trim()), vis = 0;
      itens.forEach(function (li) {
        var ok = (tipo === "todos" || li.getAttribute("data-tipo") === tipo) &&
          (!q || norm(li.textContent + " " + li.getAttribute("data-tags")).indexOf(q) > -1);
        li.hidden = !ok; if (ok) vis++;
      });
      vazio.classList.toggle("on", vis === 0);
      input.parentNode.classList.toggle("tem", !!input.value);
      temas.forEach(function (t) { t.setAttribute("aria-pressed", norm(t.getAttribute("data-busca")) === q ? "true" : "false"); });
    }
    filtros.forEach(function (b) {
      b.addEventListener("click", function () {
        tipo = b.getAttribute("data-filtro");
        filtros.forEach(function (x) { x.setAttribute("aria-pressed", x === b ? "true" : "false"); });
        aplica();
      });
    });
    input.addEventListener("input", aplica);
    limpa.addEventListener("click", function () { input.value = ""; aplica(); input.focus(); });
    limpar.addEventListener("click", function () { input.value = ""; tipo = "todos"; filtros.forEach(function (x) { x.setAttribute("aria-pressed", x.getAttribute("data-filtro") === "todos" ? "true" : "false"); }); aplica(); });
    temas.forEach(function (t) {
      t.addEventListener("click", function () {
        var v = t.getAttribute("data-busca");
        input.value = norm(input.value.trim()) === norm(v) ? "" : v; aplica();
        lista.scrollIntoView({ block: "nearest", behavior: reduz.matches ? "auto" : "smooth" });
      });
    });
    aplica();
  })();

  /* escritos na página inicial: publicações e ensaios vêm de content/*.json (ou do retrato embutido) */
  function embutido(id) { var el = d.getElementById(id); if (!el) return null; try { return JSON.parse(el.textContent); } catch (e) { return null; } }
  function busca(caminho, id) {
    var local = embutido(id);
    if (location.protocol === "file:" || !window.fetch) return Promise.resolve(local);
    return fetch(BASE + caminho, { cache: "no-cache" }).then(function (r) { if (!r.ok) throw 0; return r.json(); }).catch(function () { return local; });
  }
  window.TelmaDados = { busca: busca, esc: esc, urlSegura: urlSegura, T: T, BASE: BASE };
  (function () {
    var alvo = $("#lista-escritos"); if (!alvo) return;
    var en = (root.lang || "").indexOf("en") === 0;
    Promise.all([busca("content/publicacoes.json", "dados-publicacoes"), busca("content/escritos.json", "dados-escritos")]).then(function (r) {
      var pubs = (r[0] && r[0].publicacoes) || [], ens = (r[1] && r[1].ensaios) || [];
      var linhas = [];
      ens.forEach(function (e) {
        linhas.push({ k: "ensaio", ano: (e.data || "").slice(0, 4), data: e.data || "", tit: (en && e.titulo_en) || e.titulo, det: T.ensaio, url: BASE + (en ? "en/" : "") + "escritos/index.html?t=" + encodeURIComponent(e.slug), ext: false });
      });
      pubs.slice().sort(function (a, b) { return b.ano - a.ano; }).slice(0, 6).forEach(function (p) {
        linhas.push({ k: "publicacao", ano: String(p.ano), data: String(p.ano), tit: p.titulo, det: ((en && p.tipo_en) || p.tipo) + " · " + p.veiculo, url: p.url, ext: true });
      });
      linhas.sort(function (a, b) { return a.data < b.data ? 1 : a.data > b.data ? -1 : 0; });
      var html = linhas.map(function (l) {
        return '<li class="escrito" data-k="' + l.k + '"><a href="' + esc(urlSegura(l.url)) + '"' + (l.ext ? ' target="_blank" rel="noopener"' : "") + '><span class="ano">' + esc(l.ano) + '</span><span><span class="tit">' + esc(l.tit) + '</span><span class="det">' + esc(l.det) + "</span></span></a></li>";
      }).join("");
      alvo.innerHTML = html;
      var bs = $$("[data-escrito]");
      function f(k) {
        $$("li", alvo).forEach(function (li) {
          var vz = li.hasAttribute("data-vazio");
          li.hidden = vz ? k !== "ensaio" : !(k === "todos" || li.getAttribute("data-k") === k);
        });
      }
      bs.forEach(function (b) {
        var k = b.getAttribute("data-escrito"), c = $("b", b);
        if (c) c.textContent = k === "todos" ? ens.length + pubs.length : k === "ensaio" ? ens.length : pubs.length;
        b.addEventListener("click", function () { bs.forEach(function (x) { x.setAttribute("aria-pressed", x === b ? "true" : "false"); }); f(k); });
      });
      f("todos");
      /* o ensaio mais recente assume o destaque */
      var dq = $("#destaque-escrito");
      if (dq && ens.length) {
        var e = ens.slice().sort(function (a, b) { return (a.data || "") < (b.data || "") ? 1 : -1; })[0];
        var u = BASE + (en ? "en/" : "") + "escritos/index.html?t=" + encodeURIComponent(e.slug);
        $(".olho", dq).textContent = T.ensaioDestaque;
        $("h3", dq).textContent = (en && e.titulo_en) || e.titulo;
        $("p", dq).textContent = (en && e.resumo_en) || e.resumo || "";
        $(".acoes", dq).innerHTML = '<a class="btn claro" href="' + esc(u) + '">' + esc(T.lerEnsaio) + "</a>" + (e.pdf ? '<a class="seta" href="' + esc(urlSegura(BASE + e.pdf.replace(/^\//, ""))) + '" download>' + esc(T.baixarPdf) + "</a>" : "");
      }
    });
  })();

  /* feed do LinkedIn a partir de posts.json */
  (function () {
    var alvo = $("#feed"); if (!alvo) return;
    busca("posts.json", "dados-posts").then(function (j) {
      var ps = (j && j.posts) || [];
      if (!ps.length) { alvo.innerHTML = '<p>' + esc(T.feedVazio) + ' <a href="https://www.linkedin.com/in/telma-soares/recent-activity/all/" target="_blank" rel="noopener">' + esc(T.abrirLinkedin) + "</a></p>"; return; }
      alvo.innerHTML = ps.slice(0, 3).map(function (p) {
        return '<a href="' + esc(urlSegura(p.url)) + '" target="_blank" rel="noopener"><time>' + esc(p.data) + "</time><span>" + esc(p.texto) + "</span><em>" + esc(T.verPost) + "</em></a>";
      }).join("");
    });
  })();

  /* galeria com <dialog> */
  (function () {
    var dlg = $("dialog.luz"); if (!dlg || !dlg.showModal) return;
    var bs = $$(".mosaico button"), img = $("img", dlg), cap = $("p", dlg), i = 0, origem = null;
    function mostra(n) { i = (n + bs.length) % bs.length; var im = $("img", bs[i]); img.src = im.src; img.alt = im.alt; cap.textContent = $("span", bs[i]).textContent; }
    bs.forEach(function (b, n) { b.addEventListener("click", function () { origem = b; mostra(n); dlg.showModal(); }); });
    $("[data-luz=ant]", dlg).addEventListener("click", function () { mostra(i - 1); });
    $("[data-luz=prox]", dlg).addEventListener("click", function () { mostra(i + 1); });
    $("[data-luz=fechar]", dlg).addEventListener("click", function () { dlg.close(); });
    dlg.addEventListener("click", function (e) { if (e.target === dlg) dlg.close(); });
    dlg.addEventListener("keydown", function (e) { if (e.key === "ArrowLeft") mostra(i - 1); if (e.key === "ArrowRight") mostra(i + 1); });
    dlg.addEventListener("close", function () { if (origem) origem.focus(); });
  })();

  /* kit de imprensa: copiar bio */
  $$("[data-copia]").forEach(function (b) {
    b.addEventListener("click", function () {
      var t = d.getElementById(b.getAttribute("data-copia")).textContent.trim(), rot = b.textContent;
      function ok() { b.textContent = T.copiado; setTimeout(function () { b.textContent = rot; }, 1800); }
      if (navigator.clipboard && navigator.clipboard.writeText) navigator.clipboard.writeText(t).then(ok, function () {});
    });
  });

  /* newsletter: encaminha para o serviço configurado em js/config.js */
  (function () {
    var f = $("#form-news"); if (!f) return;
    /* a seção só aparece quando o serviço de newsletter está configurado em js/config.js */
    if (CFG.newsletterEndpoint) { var sec = $("#newsletter"); if (sec) sec.hidden = false; $$("[data-news]").forEach(function (x) { x.hidden = false; }); }
    var st = $("[role=status]", f), bt = $("button", f), em = $("input[type=email]", f);
    f.addEventListener("submit", function (e) {
      e.preventDefault();
      if (!em.checkValidity()) { st.textContent = T.newsInvalido; em.focus(); return; }
      if (!CFG.newsletterEndpoint) { st.textContent = T.newsInativa; return; }
      bt.disabled = true; st.textContent = T.newsEnviando;
      var corpo = new FormData(); corpo.append(CFG.newsletterCampo || "email", em.value);
      fetch(CFG.newsletterEndpoint, { method: "POST", body: corpo, mode: CFG.newsletterModo || "no-cors" })
        .then(function () { st.textContent = T.newsOk; f.reset(); })
        .catch(function () { st.textContent = T.newsErro; })
        .then(function () { bt.disabled = false; });
    });
  })();
})();
