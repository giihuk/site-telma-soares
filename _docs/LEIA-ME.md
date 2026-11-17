# Site de Telma Soares · versão B2 (17/11/2026)

Site estático, sem etapa de build obrigatória e sem dependências externas no site público.
Abra `index.html` no navegador para ver. Nada aqui foi publicado no endereço oficial.

## O que há na pasta

| Caminho | Para que serve |
| --- | --- |
| `index.html`, `en/index.html` | Página principal em português e em inglês |
| `escritos/`, `en/escritos/` | Lista completa das publicações (e a página de leitura de ensaios, se um dia houver) |
| `content/escritos.json` | Ensaios (editados pelo painel) |
| `content/publicacoes.json` | Bibliografia científica (42 registros) |
| `admin/` | Painel de administração (Decap CMS) |
| `js/config.js` | Endereço do serviço de newsletter |
| `css/site.css`, `js/site.js`, `js/escritos.js` | Layout e comportamento novos |
| `css/paleta.css`, `css/paletas/`, `css/telma-motion.css`, `js/telma-motion.js`, `js/telma-brand-geometry.js`, `assets/` | Marca, paleta e motor de fundos do repositório original, sem alteração |
| `card/` | Cartão digital original, sem alteração |
| `_ferramentas/` | Gerador das páginas (`python3 build.py <pasta-do-site>`). Edite os textos em `build.py` para manter PT e EN em sincronia |

## Como publicar no GitHub Pages

A pasta já é o site pronto: não há build. No Terminal, dentro de `site-telma-b2`:

```sh
git init -b main
git add .
git commit -m "Novo site de Telma Soares (B2)"
git remote add origin https://github.com/USUARIO/REPOSITORIO.git
git push -u origin main
```

Depois, no GitHub: Settings › Pages › Source "Deploy from a branch" › `main` e `/ (root)`. O endereço fica `https://USUARIO.github.io/REPOSITORIO/`.

Se o endereço não for `telmaw.github.io/siteTelma`, troque esse endereço em quatro lugares, para os metadados apontarem para o lugar certo:
`URL` no início de `_ferramentas/build.py` (e rode o gerador), `robots.txt`, `sitemap.xml`, o link do `404.html` e `site_url` em `admin/config.yml`.
As páginas funcionam em qualquer endereço mesmo sem essa troca: todos os caminhos internos são relativos.

As pastas `_docs` e `_ferramentas` não são servidas pelo GitHub Pages, mas ficam visíveis no repositório se ele for público.

## Pendências antes de publicar no endereço oficial

1. **Tradução para o inglês:** feita por Claude a partir do texto do pacote. Precisa da revisão da Telma.
2. **Bibliografia:** a lista veio do registro DBLP dela (via csauthors.net), que aponta para o Lattes 6296363436468330. Cinco links foram abertos e conferidos (ICML, dois arXiv, tese e dissertação). Os outros 37 levam à busca do título no DBLP: trocar pelo DOI de cada um quando possível. Conferir com a Telma se falta ou sobra algum trabalho.
3. **ORCID 0000-0002-4927-2221:** aparece no registro DBLP, mas não foi possível abrir a página do ORCID para confirmar. Por isso não está no site.
4. **Área de administração:** falta o serviço de login do GitHub (`base_url` em `admin/config.yml`). Sem ele o painel abre, mas não conclui o login. Para testar no computador: `npx decap-server` na pasta do site.
5. **Newsletter:** escolher o serviço e colar o endereço em `js/config.js`. Enquanto estiver vazio, a seção aparece como demonstração: ao clicar em Assinar, o site avisa que a newsletter ainda não está ativa e não guarda nem envia nenhum e-mail. Ativar antes de publicar no endereço oficial, ou ocultar a seção.
6. **Ensaios:** não há nenhum, então o site mostra só as publicações científicas. Se um ensaio for publicado pelo painel, ele passa a aparecer na lista e no destaque automaticamente.
7. **Indicadores do CEIA:** são os seis valores de outubro de 2026, não reapurados.
8. **Fotos:** todas do acervo que já estava no repositório. As legendas e os textos alternativos vieram do histórico do site.

## Diferenças em relação ao pacote de 15/11/2026

O pacote pedia uma atualização editorial sobre o site existente. Esta versão refaz o layout, a pedido, e mantém do pacote:
todos os textos, as atribuições (CEIA × pessoal), a ordem das seções, todos os IDs públicos, os seis contadores com os mesmos
atributos, o letreiro com duas listas (a segunda `aria-hidden`), busca e filtros da imprensa com os mesmos IDs, `posts.json`,
`/card/`, o mecanismo `?paleta=`, o motor TelmaMotion 1.0.0 com seus atributos e botões, e os contatos.

Mudanças deliberadas:
- Layout, tipografia de títulos (DM Serif Display) e componentes novos.
- Lettering "Telma" desenhado à mão no cabeçalho, sobre a foto da abertura e no contato.
- Seções novas: Escritos, kit de imprensa, newsletter, perfis acadêmicos e versão em inglês.
- Reconhecimentos em ordem decrescente de ano.
- Feed do LinkedIn em cartões com link, sem os iframes de incorporação (menos peso e sem rastreadores de terceiros).
- A pausa dos fundos também pausa o letreiro e fica guardada no navegador.
- Abertura: o parágrafo principal desceu para a Trajetória.

## O que foi verificado

Renderização em 1440 px e 390 px sem rolagem horizontal; console sem erros do site (só imagens externas da Exame e do
Correio, que têm foto reserva); IDs sem duplicata; nenhum link interno quebrado; todas as imagens com texto alternativo.
Não foram testados: leitores de tela, Safari e Firefox, o painel de administração com login real e o envio da newsletter.

### Modern Web Guidance

Alvo de compatibilidade assumido: Baseline amplamente disponível, com melhorias progressivas onde há suporte.

- `scroll-progress-indicator`: barra de progresso por animação guiada pela rolagem em CSS, com `@supports` e movimento reduzido; o JavaScript só atua onde não há suporte.
- `shrinking-header-on-scroll`: `scroll-padding-top` para o foco não ficar sob o cabeçalho fixo.
- `scroll-position-aware-elements`: o botão "voltar ao topo" devolve o foco ao conteúdo quando some.
- `optimize-image-priority`: `fetchpriority="high"` só na foto da abertura; as demais com `loading="lazy"`.
- `sanitize-untrusted-html`: o texto dos ensaios é escapado e, onde existe, passa pela Sanitizer API.

Guias listados e não consultados: os demais (formulários, passkeys, web components etc.), por não se aplicarem.
