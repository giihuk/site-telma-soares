# Gera o site estático (PT e EN) a partir de um único conjunto de textos.
# Uso: python3 build.py <pasta-do-site>
import sys, json, html
OUT = sys.argv[1]
URL = "https://giihuk.github.io/site-telma-soares/"
LATTES = "http://lattes.cnpq.br/6296363436468330"
DBLP = "https://dblp.org/pid/82/137"
LINKEDIN = "https://www.linkedin.com/in/telma-soares/"
LINKEDIN_ALL = "https://www.linkedin.com/in/telma-soares/recent-activity/all/"
INSTA = "https://www.instagram.com/telmawoerle/"
TALENTOS = "https://portal.ceia.inf.ufg.br/banco-de-talentos"
ITF = "https://itforum.com.br/noticias/telma-soares-mulheres-protagonismo/"
PODCAST = "https://podcasts.apple.com/us/podcast/telma-soares-do-ceia-ia-soberania-e-o-futuro-do-desenvolvedor/id1555721098?i=1000777255360"
ICML = "https://proceedings.mlr.press/v267/de-oliveira25a.html"
TESE = "https://teses.usp.br/teses/disponiveis/55/55134/tde-28052009-163303/pt-br.html"
DISS = "https://teses.usp.br/teses/disponiveis/55/55134/tde-30092006-110850/pt-br.html"
EX1 = "https://exame.com/inteligencia-artificial/por-que-a-ia-no-brasil-pode-dar-certo-mesmo-sem-um-concorrente-do-chatgpt/"
EX2 = "https://exame.com/inteligencia-artificial/brasil-esta-atras-na-corrida-por-uma-ia-propria-diz-diretora-do-ceia/"
EX3 = "https://exame.com/inteligencia-artificial/frear-ritmo-da-ia-pode-consolidar-quem-ja-esta-na-frente-diz-diretora-do-ceia/"
EX4 = "https://exame.com/inteligencia-artificial/por-que-um-centro-de-ia-em-goias-compra-tantos-chips-da-nvidia/"
WA = "https://wa.me/5562981008111?text="

IR = '<svg class="ir" aria-hidden="true" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14"/><path d="M13 6l6 6-6 6"/></svg>'
FORA = '<svg class="ir" aria-hidden="true" width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M7 17L17 7"/><path d="M8 7h9v9"/></svg>'
BAIXA = '<svg aria-hidden="true" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 4v12"/><path d="M6 11l6 6 6-6"/><path d="M5 20h14"/></svg>'
LETTERING = '''<svg class="lettering{cls}" viewBox="20 -490 1230 540" {aria}><g transform="skewX(-12)"><path d="M 30 -270 C 60 -320, 160 -362, 260 -392 C 330 -412, 400 -430, 456 -452"/><path d="M 245 -384 C 243 -300, 240 -130, 236 -42 C 234 4, 276 18, 312 -6 C 350 -30, 390 -70, 420 -104 C 460 -128, 506 -166, 486 -198 C 466 -226, 404 -204, 392 -140 C 382 -80, 404 -6, 456 0 C 500 4, 540 -40, 568 -96"/><g transform="translate(60 0)"><path d="M 508 -96 C 534 -160, 584 -330, 570 -404 C 560 -452, 498 -442, 492 -380 C 486 -300, 488 -120, 494 -46 C 498 2, 536 8, 564 -18 C 582 -40, 590 -120, 592 -178 L 592 0"/><path d="M 592 -118 C 604 -176, 634 -196, 658 -196 C 684 -196, 692 -172, 692 -140 L 692 0"/><path d="M 692 -118 C 704 -176, 734 -196, 758 -196 C 784 -196, 792 -172, 792 -140 L 792 -44 C 792 -4, 816 6, 844 -12 C 856 -20, 864 -32, 870 -46"/><path d="M 994 -168 C 964 -202, 904 -198, 884 -150 C 864 -104, 868 -16, 914 -6 C 958 4, 986 -60, 996 -150"/><path d="M 996 -190 L 990 -44 C 988 0, 1018 6, 1046 -14 C 1070 -32, 1092 -64, 1108 -98"/></g></g></svg>'''

LETTERING_NAV = LETTERING.replace('class="lettering{cls}" ', '').replace(' {aria}', ' aria-hidden="true" focusable="false"')
def e(s): return html.escape(s, quote=True)
def emb(i, o):
    j = json.dumps(o, ensure_ascii=False).replace("</", "<\\/")
    return '<script type="application/json" id="' + i + '">' + j + '</script>'


import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import pubs
PUBS = {"publicacoes": pubs.lista()}
ESCRITOS = {"ensaios": []}
POSTS = json.load(open(OUT + "/posts.json"))

def page(lang):
    en = lang == "en"
    def t(pt, en_): return en_ if en else pt
    B = "../" if en else ""           # caminho até a raiz do site
    outro = ("../" if en else "en/")
    canon = URL + ("en/" if en else "")
    def ext(href, label, cls="seta"):
        return f'<a class="{cls}" href="{e(href)}" target="_blank" rel="noopener">{label}{FORA}<span class="so-leitor"> {t("(abre em nova aba)","(opens in a new tab)")}</span></a>'
    def loc(href, label, cls="seta"):
        return f'<a class="{cls}" href="{href}">{label}{IR}</a>'

    textos = {
      "pausar": t("Pausar o movimento dos fundos", "Pause background motion"),
      "retomar": t("Retomar o movimento dos fundos", "Resume background motion"),
      "abrirMenu": t("Abrir menu", "Open menu"), "fecharMenu": t("Fechar menu", "Close menu"),
      "ensaio": t("Ensaio", "Essay"), "ensaioDestaque": t("Ensaio em destaque", "Featured essay"),
      "lerEnsaio": t("Ler o ensaio", "Read the essay"), "baixarPdf": t("Baixar PDF", "Download PDF"),
      "semEnsaios": t("Os primeiros ensaios serão publicados aqui em breve.", "The first essays will be published here soon."),
      "feedVazio": t("Acompanhe minhas publicações diretamente no LinkedIn.", "Follow my posts directly on LinkedIn."),
      "abrirLinkedin": t("Abrir LinkedIn", "Open LinkedIn"), "verPost": t("Ver no LinkedIn", "View on LinkedIn"),
      "copiado": t("Copiado", "Copied"),
      "newsInvalido": t("Informe um e-mail válido.", "Please enter a valid email address."),
      "newsInativa": t("A newsletter ainda não está ativa. Enquanto isso, acompanhe as publicações no LinkedIn.", "The newsletter is not active yet. Meanwhile, follow the posts on LinkedIn."),
      "newsEnviando": t("Enviando…", "Sending…"),
      "newsOk": t("Inscrição enviada. Confira seu e-mail para confirmar.", "Subscription sent. Check your inbox to confirm."),
      "newsErro": t("Não foi possível concluir a inscrição. Tente novamente.", "We could not complete the subscription. Please try again."),
    }
    titulo = t("Telma Soares | Pesquisa, formação e liderança em IA", "Telma Soares | AI research, education and leadership")
    desc = t("Telma Soares, professora e pesquisadora da UFG. Trajetória, pesquisa e formação em inteligência artificial. Cofundadora e diretora executiva do CEIA.",
             "Telma Soares, professor and researcher at the Federal University of Goiás (UFG), Brazil. Career, research and education in artificial intelligence. Co-founder and executive director of CEIA.")
    ogdesc = t("Conheça minha trajetória na computação, minhas pesquisas e contribuições à formação de pessoas. Professora da UFG, cofundadora e diretora executiva do CEIA.",
               "My path in computing, my research and my work in educating people. Professor at UFG, co-founder and executive director of CEIA.")
    ld = {"@context": "https://schema.org", "@type": "Person", "name": "Telma Soares", "alternateName": "Telma Woerle de Lima Soares", "url": canon,
          "image": URL + "img/foto-perfil.jpg",
          "jobTitle": t("Professora, pesquisadora e diretora executiva", "Professor, researcher and executive director"),
          "description": desc,
          "affiliation": [{"@type": "CollegeOrUniversity", "name": "Universidade Federal de Goiás", "url": "https://ufg.br/"},
                          {"@type": "Organization", "name": "Centro de Excelência em Inteligência Artificial (CEIA)", "url": "https://ceia.ufg.br/"}],
          "alumniOf": [{"@type": "CollegeOrUniversity", "name": "Universidade de São Paulo"}, {"@type": "CollegeOrUniversity", "name": "Universidade Estadual Paulista"}],
          "knowsAbout": ["Reinforcement learning", "Evolutionary algorithms", "Optimization", "Artificial intelligence"],
          "sameAs": [LATTES, DBLP, LINKEDIN, INSTA]}

    nav = [("#sobre", t("Trajetória", "Career")), ("#pesquisa", t("Pesquisa", "Research")), ("#escritos", t("Publicações", "Publications")),
           ("#formacao", t("Formação", "Education")), ("#aplicada", t("Ideias", "Ideas")), ("#numeros", t("Liderança", "Leadership")), ("#imprensa", t("Conversas", "Press"))]
    navhtml = "".join(f'<a class="link" href="{h}">{l}</a>' for h, l in nav)

    h1 = t(["Pesquisa, formação", "de pessoas e liderança em", "<em>inteligência artificial.</em>"],
           ["Research, educating", "people and leadership in", "<em>artificial intelligence.</em>"])
    h1html = "".join(f'<span class="l" style="--i:{i}">{l}</span> ' for i, l in enumerate(h1))

    faixa = [(t("Docência", "Teaching"), t("Professora da UFG", "Professor at UFG"), t("desde 2009", "since 2009")),
             (t("Pesquisa", "Research"), t("Doutora pela USP", "PhD from USP"), t("Computação e Matemática Computacional", "Computer Science and Computational Mathematics")),
             (t("Liderança", "Leadership"), t("Cofundadora do CEIA", "Co-founder of CEIA"), t("Diretora executiva desde 2022", "Executive director since 2022")),
             (t("Reconhecimento", "Recognition"), t("Pesquisadora de Destaque", "Outstanding Researcher"), t("2º lugar no Prêmio Embrapii 2025", "2nd place, Embrapii Award 2025"))]
    faixahtml = "".join(f'<li style="--d:{i}"><b>{a}</b><strong>{b}</strong><span>{c}</span></li>' for i, (a, b, c) in enumerate(faixa))

    tempo = [("1995", t("Primeiro contato com a computação", "First contact with computing"), t("Iniciei um curso técnico de processamento de dados.", "I started a technical course in data processing.")),
             ("2006", t("Pesquisa em proteínas", "Research on proteins"), t("Defendi na USP o mestrado sobre algoritmos evolutivos para predição de estruturas de proteínas.", "I defended my master's at USP on evolutionary algorithms for protein structure prediction.")),
             ("2009", t("Doutorado e docência na UFG", "PhD and teaching at UFG"), t("Concluí o doutorado na USP e passei a integrar o Instituto de Informática da UFG.", "I completed my PhD at USP and joined the Institute of Informatics at UFG.")),
             (t("2018 e 2019", "2018–2019"), t("Formação de pesquisadores", "Training researchers"), t("Atuei na liderança da criação do doutorado próprio em Ciência da Computação da UFG, aprovado em 2018 e iniciado em março de 2019.", "I helped lead the creation of UFG's own PhD programme in Computer Science, approved in 2018 and started in March 2019.")),
             ("2019", t("Construção de novas iniciativas", "Building new initiatives"), t("Participei da criação do Bacharelado em Inteligência Artificial e da fundação do CEIA. A primeira turma do bacharelado começou em 2020.", "I took part in creating the Bachelor's degree in Artificial Intelligence and in founding CEIA. The first bachelor's class started in 2020.")),
             ("2022", t("Direção executiva", "Executive direction"), t("Assumi a direção executiva do CEIA.", "I became executive director of CEIA.")),
             ("2025", t("Pesquisa em aprendizado por reforço", "Research in reinforcement learning"), t("Fui coautora de um trabalho sobre representação visual publicado na ICML, conferência internacional de aprendizado de máquina.", "I co-authored a paper on visual representation published at ICML, the International Conference on Machine Learning."))]
    tempohtml = "".join(f'<li class="anim"><time>{a}</time><div><h3>{b}</h3><p>{c}</p></div></li>' for a, b, c in tempo)

    sintese = [(t("Formação", "Education"), t("Graduação em Ciência da Computação pela Unesp. Mestrado, doutorado e pós-doutorado pela USP.", "BSc in Computer Science from Unesp. Master's, PhD and postdoctoral research at USP.")),
               (t("Docência e pesquisa", "Teaching and research"), t("Professora do Instituto de Informática da UFG desde 2009. Pesquisa em algoritmos evolutivos, aprendizado por reforço e otimização.", "Professor at the Institute of Informatics, UFG, since 2009. Research in evolutionary algorithms, reinforcement learning and optimization.")),
               (t("Gestão acadêmica", "Academic management"), t("Atuação na coordenação e na vice-coordenação da pós-graduação em Ciência da Computação, com participação na criação do doutorado próprio do instituto.", "Served as coordinator and vice-coordinator of the graduate programme in Computer Science, taking part in the creation of the institute's own PhD.")),
               (t("Liderança", "Leadership"), t("Cofundadora do CEIA, criado em 2019, e diretora executiva desde 2022.", "Co-founder of CEIA, created in 2019, and executive director since 2022."))]
    sintesehtml = "".join(f"<div><dt>{a}</dt><dd>{b}</dd></div>" for a, b in sintese)

    pil = [(t("Pesquisa", "Research"), t("Investigar como os sistemas aprendem e decidem", "Investigating how systems learn and decide"),
            t("Trabalho com algoritmos evolutivos, aprendizado por reforço e otimização. São abordagens para explorar soluções, aprender com a interação e comparar alternativas em problemas complexos. Minha produção inclui estudos sobre proteínas, redes e representação visual para agentes de inteligência artificial.",
              "I work with evolutionary algorithms, reinforcement learning and optimization: approaches for exploring solutions, learning from interaction and comparing alternatives in complex problems. My work includes studies on proteins, networks and visual representation for AI agents."),
            t("Conheça pesquisas selecionadas", "See selected research"), "#pesquisa"),
           (t("Formação", "Education"), t("Ensinar, orientar e abrir caminhos", "Teaching, advising and opening paths"),
            t("Dou aulas e oriento estudantes na UFG. Minha atuação também passou pela Olimpíada Brasileira de Robótica em Goiás, pela gestão da pós-graduação e pela construção do Bacharelado em Inteligência Artificial.",
              "I teach and advise students at UFG. My work has also included the Brazilian Robotics Olympiad in Goiás, graduate programme management and building the Bachelor's degree in Artificial Intelligence."),
            t("Explore a frente de formação", "Explore the education work"), "#formacao"),
           (t("Liderança", "Leadership"), t("Construir iniciativas com outras pessoas", "Building initiatives with other people"),
            t("Sou cofundadora e diretora executiva do CEIA. Também liderei, em 2023, a candidatura que deu origem ao AKCIT, centro de competência Embrapii em tecnologias imersivas. São iniciativas construídas com pesquisadores, estudantes, parceiros e instituições públicas.",
              "I am co-founder and executive director of CEIA. In 2023 I also led the application that gave rise to AKCIT, the Embrapii competence centre in immersive technologies. These initiatives are built with researchers, students, partners and public institutions."),
            t("Conheça minha atuação no CEIA", "See my work at CEIA"), "#numeros")]
    pilfotos = [("foto-original-197.jpg", t("Telma Soares sentada ao lado de um robô humanoide do CEIA","Telma Soares sitting next to a CEIA humanoid robot"), "50% 40%"),
                ("foto-laboratorio.jpg", t("Telma Soares acompanha o trabalho de estudantes no laboratório do CEIA","Telma Soares following students' work in the CEIA lab"), "50% 40%"),
                ("foto-evento-5.jpg", t("Telma Soares fala ao microfone no palco, em pé, com telão do CEIA ao fundo","Telma Soares speaking on stage, standing, with a CEIA screen behind her"), "30% 40%")]
    pilhtml = "".join(f'<article class="pilar" style="--d:{i}"><img class="pfoto" src="{B}img/{pilfotos[i][0]}" alt="{e(pilfotos[i][1])}" style="object-position:{pilfotos[i][2]}" loading="lazy" width="1600" height="1067"><div class="olho"><span>{a}</span><i aria-hidden="true">0{i+1}</i></div><h3>{b}</h3><p>{c}</p>{loc(h, d)}</article>' for i, (a, b, c, d, h) in enumerate(pil))

    pesq = [(t("Artigo científico · ICML · 2025", "Conference paper · ICML · 2025"), "Sliding Puzzles Gym", t("Um ambiente para avaliar representação visual no aprendizado por reforço", "An environment for evaluating visual representation in reinforcement learning"),
             t("Trabalho em coautoria que propõe um ambiente de testes baseado em quebra-cabeças. Ele permite estudar como agentes de inteligência artificial extraem informações de imagens para tomar decisões.",
               "Co-authored work proposing a puzzle-based test environment. It makes it possible to study how AI agents extract information from images to make decisions."),
             "Bryan Lincoln Marques de Oliveira, Luana Guedes Barros Martins, Bruno Brandão, Murilo Lopes da Luz, Telma Woerle de Lima Soares " + t("e", "and") + " Luckeciano Carvalho Melo.",
             t("Leia o artigo nos anais da ICML", "Read the paper in the ICML proceedings"), ICML),
            (t("Tese de doutorado · USP · 2009", "Doctoral thesis · USP · 2009"), "Estruturas de dados eficientes para algoritmos evolutivos aplicados a projeto de redes", t("", "Efficient data structures for evolutionary algorithms applied to network design"),
             t("Pesquisa sobre formas de representar redes para tornar algoritmos de otimização mais eficientes. A tese inclui aplicação à reconfiguração de sistemas de distribuição de energia.",
               "Research on ways of representing networks to make optimization algorithms more efficient. The thesis includes an application to the reconfiguration of power distribution systems."),
             t("Autoria: Telma Woerle de Lima Soares. Orientação: Alexandre Cláudio Botazzo Delbem.", "Author: Telma Woerle de Lima Soares. Advisor: Alexandre Cláudio Botazzo Delbem."),
             t("Consulte a tese", "See the thesis"), TESE),
            (t("Dissertação de mestrado · USP · 2006", "Master's dissertation · USP · 2006"), "Algoritmos evolutivos para predição de estruturas de proteínas", t("", "Evolutionary algorithms for protein structure prediction"),
             t("Investigação de métodos computacionais para estimar a estrutura tridimensional de proteínas a partir de sua sequência. O trabalho utiliza algoritmos evolutivos, que exploram alternativas por sucessivas modificações e seleção de soluções.",
               "An investigation of computational methods for estimating the three-dimensional structure of proteins from their sequence. The work uses evolutionary algorithms, which explore alternatives through successive modification and selection of solutions."),
             t("Autoria: Telma Woerle de Lima. Orientação: Alexandre Cláudio Botazzo Delbem.", "Author: Telma Woerle de Lima. Advisor: Alexandre Cláudio Botazzo Delbem."),
             t("Consulte a dissertação", "See the dissertation"), DISS)]
    pesqhtml = "".join(f'<article class="cartao anim" style="--d:{i}"><span class="meta">{m}</span><h3 lang="{"en" if i==0 else "pt-BR"}">{ti}</h3>{f"<p class=sub>{su}</p>" if su else ""}<p>{r}</p><p class="credito">{c}</p>{ext(u, cta)}</article>' for i, (m, ti, su, r, c, cta, u) in enumerate(pesq))

    inic = [(t("Bacharelado em Inteligência Artificial", "Bachelor's degree in Artificial Intelligence"),
             t("Participei da construção do bacharelado da UFG, criado em 2019 e com a primeira turma iniciada em 2020. O curso reúne fundamentos de computação e matemática, métodos de IA e atividades de integração.",
               "I took part in building UFG's bachelor's degree, created in 2019, with its first class starting in 2020. The course brings together foundations of computing and mathematics, AI methods and integration activities."),
             t("Conheça o curso na UFG", "See the course at UFG"), "https://inf.ufg.br/p/44958-inteligencia-artificial"),
            (t("Pós-graduação em Ciência da Computação", "Graduate programme in Computer Science"),
             t("Atuei na gestão da pós-graduação do Instituto de Informática e na criação do doutorado próprio da UFG. O programa reúne pesquisa, orientação e formação de profissionais para a academia e o desenvolvimento tecnológico.",
               "I worked in the management of the Institute of Informatics' graduate programme and in creating UFG's own PhD. The programme combines research, advising and the training of professionals for academia and technological development."),
             t("Conheça o programa", "See the programme"), "https://ppgcc.inf.ufg.br/p/35367-apresentacao?atr=pt-BR"),
            (t("Robótica e educação básica", "Robotics and school education"),
             t("Coordenei a etapa goiana da Olimpíada Brasileira de Robótica. A atividade aproxima estudantes da construção de robôs, da resolução de problemas e do ambiente universitário.",
               "I coordinated the Goiás stage of the Brazilian Robotics Olympiad. The activity brings students closer to building robots, solving problems and the university environment."),
             t("Leia um registro da atividade", "Read a record of the activity"), "https://ufg.br/n/100000-etapa-estadual-da-olimpiada-de-robotica-premia-vencedores"),
            (t("IA nas Escolas", "IA nas Escolas (AI in Schools)"),
             t("Conheça os materiais e as iniciativas de formação do programa IA nas Escolas, voltado à educação básica.", "Explore the materials and training initiatives of the IA nas Escolas programme, aimed at school education."),
             t("Acesse o IA nas Escolas", "Visit IA nas Escolas"), "https://ianasescolas.com.br/")]
    inichtml = "".join(f'<article class="anim" style="--d:{i}"><h3>{a}</h3><p>{b}</p>{ext(u, c)}</article>' for i, (a, b, c, u) in enumerate(inic))
    fotosform = [("foto-original-239.jpg", t("Telma Soares orienta um estudante em laboratório de computadores do INF/UFG", "Telma Soares advises a student in a computer lab at INF/UFG")),
                 ("foto-original-225.jpg", t("Telma Soares em aula para turma de estudantes, com apresentação do CEIA ao fundo", "Telma Soares teaching a class of students, with a CEIA presentation in the background")),
                 ("foto-original-221.jpg", t("Telma Soares trabalha no notebook vestindo a camisa do CEIA e do INF", "Telma Soares working on a laptop wearing a CEIA and INF shirt"))]
    fotosformhtml = "".join(f'<figure class="anim" style="--d:{i}"><img src="{B}img/{f}" alt="{e(a)}" loading="lazy" width="1067" height="1600"></figure>' for i, (f, a) in enumerate(fotosform))

    ideias = [(t("Desenvolver IA a partir de problemas brasileiros", "Developing AI from Brazilian problems"),
               t("Saúde, biodiversidade e questões ambientais oferecem problemas e dados próprios do país. Nas entrevistas, discuto possibilidades de desenvolver soluções para essas necessidades e os limites de infraestrutura envolvidos.",
                 "Health, biodiversity and environmental issues offer problems and data that are specific to the country. In interviews I discuss the possibilities of developing solutions for these needs and the infrastructure limits involved."),
               t("Exame, outubro de 2026", "Exame, October 2026"), t("Leia a reportagem", "Read the report"), EX1),
              (t("Infraestrutura e dados definem o que conseguimos pesquisar", "Infrastructure and data define what we can research"),
               t("Treinar sistemas de inteligência artificial exige capacidade computacional e dados adequados. Na conversa com a Exame, explico como essas condições afetam o desenvolvimento de modelos no Brasil e por que o desafio varia conforme a aplicação.",
                 "Training AI systems requires computing capacity and suitable data. In my conversation with Exame, I explain how these conditions affect model development in Brazil and why the challenge varies by application."),
               t("Exame, julho de 2026", "Exame, July 2026"), t("Leia a entrevista", "Read the interview"), EX2),
              (t("Avaliar riscos exige acesso para pesquisar", "Assessing risks requires access for research"),
               t("No debate sobre o ritmo de desenvolvimento da IA, chamo atenção para a necessidade de auditoria independente, transparência e acesso das universidades aos sistemas. São condições para estudar riscos com participação de diferentes pesquisadores.",
                 "In the debate on the pace of AI development, I draw attention to the need for independent auditing, transparency and university access to the systems. These are conditions for studying risks with the participation of different researchers."),
               t("Exame, setembro de 2026", "Exame, September 2026"), t("Leia a entrevista", "Read the interview"), EX3),
              (t("A trajetória também passa pelas pessoas formadas", "A career is also about the people we educate"),
               t("No perfil do IT Forum, retomo minha entrada na computação, a escolha pela carreira acadêmica e a importância das pessoas formadas ao longo desse caminho. A conversa também aborda a presença das mulheres na tecnologia.",
                 "In the IT Forum profile, I look back on how I entered computing, my choice of an academic career and the importance of the people educated along the way. The conversation also addresses the presence of women in technology."),
               t("IT Forum Mulheres, novembro de 2026", "IT Forum Mulheres, November 2026"), t("Leia o perfil", "Read the profile"), ITF)]
    ideiashtml = "".join(f'<article class="anim"><h3>{a}</h3><p>{b}</p><span class="fonte">{f}</span>{ext(u, c, "seta")}</article>' for a, b, f, c, u in ideias)

    ceia = t("CEIA e parceiros", "CEIA and partners"); pess = t("Atuação pessoal", "Personal work")
    nums = [(ceia, "", '+150', 'data-conta="150" data-prefixo="+"', t("projetos de pesquisa, desenvolvimento e inovação executados pelo CEIA", "research, development and innovation projects carried out by CEIA")),
            (ceia, "", t('+R$ 500 mi', '+R$ 500 M'), f'data-conta="500" data-prefixo="+R$ " data-sufixo="{t(" mi"," M")}"', t("captados em parcerias de pesquisa, desenvolvimento e inovação nos cinco anos anteriores à referência de outubro de 2026", "raised in research, development and innovation partnerships in the five years before the October 2026 reference date")),
            (ceia, "", t('+1.000', '+1,000'), 'data-conta="1000" data-prefixo="+"', t("pesquisadores envolvidos nas iniciativas do CEIA", "researchers involved in CEIA's initiatives")),
            (ceia, "", t('+150 mi', '+150 M'), f'data-conta="150" data-prefixo="+" data-sufixo="{t(" mi"," M")}"', t("de brasileiros atendidos por meio dos parceiros do CEIA", "Brazilians served through CEIA's partners")),
            (pess, " pessoal", '+15', 'data-conta="15" data-prefixo="+"', t("projetos de pesquisa, desenvolvimento e inovação coordenados diretamente por mim", "research, development and innovation projects coordinated directly by me")),
            (pess, " pessoal", t('+20 anos', '+20 years'), f'data-conta="20" data-prefixo="+" data-sufixo="{t(" anos"," years")}"', t("de trabalho com inovação, tecnologia e inteligência artificial", "working with innovation, technology and artificial intelligence"))]
    numshtml = "".join(f'<div class="num{c}"><span class="de">{de}</span><strong><span {attr}>{v}</span></strong><span class="rot">{r}</span></div>' for de, c, v, attr, r in nums)
    parceiros = ["Embrapii", "NVIDIA AI Nations", "Google · GAIA", "AI for Good · ONU", "iFood", "Copel Distribuição", "Bancorbrás", "Acordo Certo", "Governo de Goiás", "UFG"]
    pl = "".join(f"<li>{p}</li>" for p in parceiros)

    prem_p = [("2026", t("Governo de Goiás", "Government of Goiás"), t("Ordem do Mérito Anhanguera", "Order of Merit Anhanguera"),
               t("Recebi a honraria na edição de 2026, em que Anderson Soares também foi homenageado por sua atuação no CEIA.", "I received the honour in the 2026 edition, in which Anderson Soares was also honoured for his work at CEIA."),
               t("Honraria concedida individualmente.", "Honour awarded individually."), t("Leia a notícia", "Read the news"),
               "https://www.jornalopcao.com.br/ultimas-noticias/diretores-do-ceia-da-ufg-recebem-ordem-do-merito-anhanguera-apos-transformar-goias-em-polo-nacional-de-inteligencia-artificial-849704/"),
              ("2026", "IT Forum", "IT Forum Mulheres",
               t("Integrei a seleção de profissionais reconhecidas pelo IT Forum Mulheres na edição de 2026.", "I was part of the selection of professionals recognised by IT Forum Mulheres in the 2026 edition."),
               t("Reconhecimento pessoal.", "Personal recognition."), t("Veja a seleção do IT Forum", "See the IT Forum selection"),
               "https://itforum.com.br/it-forum-mulheres-2026-conheca-as-profissionais-reconhecidas-nesta-edicao/"),
              ("2025", "Embrapii", t("2º lugar em Pesquisadora de Destaque", "2nd place, Outstanding Researcher"),
               t("Distinção na categoria Pesquisadora de Destaque do Prêmio Embrapii 2025, representando a Unidade CEIA/UFG.", "Distinction in the Outstanding Researcher category of the Embrapii Award 2025, representing the CEIA/UFG Unit."),
               t("Premiada: Telma Woerle de Lima Soares.", "Awardee: Telma Woerle de Lima Soares."), t("Consulte a premiação", "See the award"),
               "https://embrapii.org.br/premio-embrapii-2025-reconhece-destaques-na-inovacao-industrial/"),
              ("2024", t("Fapeg · Prêmio Goiano de Ciência, Tecnologia e Inovação · Edição 2024", "Fapeg · Goiás Science, Technology and Innovation Award · 2024 edition"), t("1º lugar em inovação para o setor público", "1st place in innovation for the public sector"),
               t("Reconhecimento na categoria Pesquisador Inovador, subcategoria Inovação para o setor público. A cerimônia de entrega aconteceu em fevereiro de 2025.", "Recognition in the Innovative Researcher category, Innovation for the public sector subcategory. The award ceremony took place in February 2025."),
               t("Premiada: Telma Woerle de Lima Soares.", "Awardee: Telma Woerle de Lima Soares."), t("Consulte o resultado", "See the result"),
               "https://goias.gov.br/fapeg/wp-content/uploads/sites/5/2025/02/RESULTADO_FINAL_CHAMADA_PuBLICA_FAPEG_N__27_2024.pdf")]
    prem_c = [("2024", "Embrapii", t("Projeto de PD&amp;I mais inovador", "Most innovative RD&amp;I project"),
               t("Reconhecimento a um projeto desenvolvido no CEIA. A distinção integra a trajetória coletiva de pesquisadores, estudantes e parceiros do centro.", "Recognition of a project developed at CEIA. The distinction is part of the collective path of the centre's researchers, students and partners."),
               t("Reconhecimento de projeto do CEIA, não prêmio pessoal.", "Recognition of a CEIA project, not a personal award."), t("Consulte o registro institucional", "See the institutional record"),
               "https://if.ufg.br/n/205373-da-fisica-a-inteligencia-artificial-aprender-prever-e-controlar-o-mundo"),
              ("2022", "Embrapii", t("Unidade mais bem avaliada pelas empresas", "Unit best rated by companies"),
               t("O CEIA/UFG recebeu o primeiro lugar na avaliação das empresas que contrataram projetos com as Unidades Embrapii. Recebi o prêmio como diretora executiva, representando a equipe.", "CEIA/UFG took first place in the evaluation by companies that contracted projects with Embrapii Units. I received the award as executive director, representing the team."),
               t("Reconhecimento da Unidade CEIA/UFG.", "Recognition of the CEIA/UFG Unit."), t("Leia o registro da UFG", "Read UFG's record"),
               "https://ufg.br/n/162070-ceia-ufg-conquista-1-lugar-no-premio-embrapii-2022-em-fortaleza")]
    def premios(ls): return "".join(f'<li class="anim"><span class="ano">{a}</span><div class="c"><span class="inst">{i}</span><h3>{ti}</h3><p>{tx}</p><p class="atr">{at}</p></div>{ext(u, c)}</li>' for a, i, ti, tx, at, c, u in ls)

    dest = [(t("Perfil · IT Forum Mulheres · Novembro de 2026", "Profile · IT Forum Mulheres · November 2026"), "IT Forum Mulheres: Telma Soares e o protagonismo feminino na computação",
             t("Do curso técnico iniciado em 1995 à atuação na UFG, o perfil aborda carreira acadêmica, formação de pessoas e presença feminina na tecnologia.", "From the technical course started in 1995 to her work at UFG, the profile covers academic career, educating people and women's presence in technology."),
             t("Leia no IT Forum", "Read at IT Forum"), ITF),
            (t("Podcast · IT Forum Líderes · 3 de junho de 2026", "Podcast · IT Forum Líderes · 3 June 2026"), "Telma Soares, do CEIA: IA, soberania e o futuro do desenvolvedor brasileiro",
             t("Uma conversa sobre pesquisa, formação e o desenvolvimento da inteligência artificial no país.", "A conversation about research, education and the development of artificial intelligence in Brazil."),
             t("Ouça o episódio", "Listen to the episode"), PODCAST),
            (t("Pesquisa · ICML · 2025", "Research · ICML · 2025"), t("Aprendizado por reforço a partir de imagens", "Reinforcement learning from images"),
             t("Conheça o Sliding Puzzles Gym, trabalho em coautoria sobre a avaliação de representações visuais em agentes de inteligência artificial.", "Meet Sliding Puzzles Gym, co-authored work on evaluating visual representations in AI agents."),
             t("Leia o artigo", "Read the paper"), ICML)]
    desthtml = "".join(f'<article class="cartao anim" style="--d:{i}"><span class="meta">{m}</span><h3{"" if i==2 else " lang=pt-BR"}>{ti}</h3><p>{tx}</p>{ext(u, c)}</article>' for i, (m, ti, tx, c, u) in enumerate(dest))

    R, E, P = t("Reportagem", "Report"), t("Entrevista", "Interview"), t("Perfil", "Profile")
    ler = t("Ler matéria", "Read the story")
    imp = [("perfil", "trajetória formação de talentos mulheres na tecnologia liderança carreira acadêmica processamento de dados career women in technology", ITF, f"{B}img/estudio-1951.jpg", "", t("Telma Soares de blazer preto e braços cruzados, sorrindo, em retrato de estúdio", "Telma Soares in a black blazer with arms crossed, smiling, in a studio portrait"), "50% 30%",
            "IT Forum", t("Novembro de 2026", "November 2026"), P, "IT Forum Mulheres: Telma Soares e o protagonismo feminino na computação",
            t("Perfil sobre a entrada de Telma na computação, a escolha pela carreira acadêmica, a formação de pessoas e a participação das mulheres na tecnologia.", "A profile on how Telma entered computing, her choice of an academic career, educating people and women's participation in technology."), t("Leia o perfil", "Read the profile")),
           ("reportagem", "soberania com foco em nichos pdi com empresas modelos aplicados chatgpt sovereignty", EX1, "https://classic.exame.com/wp-content/uploads/2026/07/123072.jpg?ims=750x/filters:quality(85):format(webp)", f"{B}img/foto-sala-aula.jpg", t("Reportagem da Exame sobre inteligência artificial aplicada no Brasil", "Exame report on applied artificial intelligence in Brazil"), "",
            "Exame", t("1 out 2026", "1 Oct 2026"), R, "Por que a IA no Brasil pode dar certo mesmo sem um concorrente do ChatGPT",
            "<q lang=\"pt-BR\">Existem outros tipos de IAs brasileiras que a gente poderia desenvolver.</q>", ler),
           ("entrevista", "regulação superinteligência governança regulation governance", EX3, "https://classic.exame.com/wp-content/uploads/2026/07/Prof-Telma-Soares-diretora-do-CEIA-UFG.-Dino-Arato-Divulgacao-1.jpg.jpeg?ims=750x/filters:quality(85):format(webp)", f"{B}img/foto-entrevista-exame.jpg", t("Telma Soares em entrevista à Exame sobre o ritmo de avanço da inteligência artificial", "Telma Soares in an interview with Exame on the pace of AI progress"), "",
            "Exame", t("14 set 2026", "14 Sep 2026"), E, "Frear ritmo da IA pode consolidar quem já está na frente, diz diretora do CEIA",
            "<q lang=\"pt-BR\">Eu teria muito cuidado em transformar superinteligência em uma categoria técnica ou jurídica neste momento.</q>", ler),
           ("reportagem", "pdi com empresas formação de talentos governo de goiás ufg", "https://www.correiobraziliense.com.br/brasil/2026/08/7490336-ufg-amplia-aposta-em-inteligencia-artificial.html", "https://midias.correiobraziliense.com.br/_midias/jpg/2026/08/30/675x450/1_novo-67557551-67557564.jpg", f"{B}img/foto-grupo-2.jpg", t("Reportagem do Correio Braziliense sobre a aposta da UFG e do CEIA em inteligência artificial", "Correio Braziliense report on UFG and CEIA's bet on artificial intelligence"), "",
            "Correio Braziliense", t("31 ago 2026", "31 Aug 2026"), R, "UFG amplia aposta em inteligência artificial",
            t("Sobre o convênio do CEIA com o Governo de Goiás e o lugar do Brasil na cadeia da IA. ", "On CEIA's agreement with the Government of Goiás and Brazil's place in the AI chain. ") + "<q lang=\"pt-BR\">Se analisarmos historicamente, o Brasil cresceu muito como fornecedor de commodities.</q>", ler),
           ("entrevista", "infraestrutura de ia no brasil dado em português soberania com foco em nichos saúde biodiversidade infrastructure", EX2, f"{B}img/foto-original-187.jpg", "", t("Telma Soares sentada ao lado de um robô humanoide e de um robô quadrúpede do CEIA", "Telma Soares sitting next to a humanoid robot and a quadruped robot from CEIA"), "50% 55%",
            "Exame", t("14 jul 2026", "14 Jul 2026"), E, "Brasil está atrás na corrida por uma IA própria, diz diretora do CEIA",
            t("Faltam infraestrutura e dado público em português, mas há espaço para IA soberana em nichos como saúde e biodiversidade, onde o dado é brasileiro.", "Infrastructure and public data in Portuguese are lacking, but there is room for sovereign AI in niches such as health and biodiversity, where the data is Brazilian."), ler),
           ("entrevista", "infraestrutura de ia no brasil gpus supercomputador hardware nvidia infrastructure", EX4, "https://classic.exame.com/wp-content/uploads/2026/07/ia_f4348d.png?ims=750x/filters:quality(85):format(webp)", f"{B}img/foto-robo.jpg", t("Matéria da Exame sobre infraestrutura de chips Nvidia no CEIA-UFG", "Exame story on Nvidia chip infrastructure at CEIA-UFG"), "",
            "Exame", t("14 jul 2026", "14 Jul 2026"), E, "Por que um centro de IA em Goiás compra tantos chips da Nvidia",
            "<q lang=\"pt-BR\">Toda vez que chega um novo equipamento, existe uma curva de aprendizado para adaptar as IAs a essas novas arquiteturas.</q>", ler),
           ("entrevista", "podcast entrevista formação de talentos soberania pesquisa desenvolvedor carreira", PODCAST, f"{B}img/foto-original-1.jpg", "", t("Telma Soares sorrindo, de frente, no corredor do Instituto de Informática da UFG", "Telma Soares smiling, facing the camera, in the corridor of UFG's Institute of Informatics"), "50% 25%",
            "IT Forum Líderes", t("3 jun 2026", "3 Jun 2026"), "Podcast", "Telma Soares, do CEIA: IA, soberania e o futuro do desenvolvedor brasileiro",
            t("Episódio com Telma Soares sobre formação, pesquisa, soberania tecnológica e o perfil do desenvolvedor brasileiro.", "Episode with Telma Soares on education, research, technological sovereignty and the profile of the Brazilian developer."), t("Ouça o episódio", "Listen to the episode")),
           ("perfil", "formação de talentos bacharelado mulheres na tecnologia liderança", "https://opopular.com.br/economia/o-cerebro-que-comanda-o-centro-de-ia-da-ufg-1.3116875", f"{B}img/estudio-1910.jpg", "", t("Telma Soares sorri, sentada, em retrato de estúdio", "Telma Soares smiling, seated, in a studio portrait"), "50% 22%",
            "O Popular", "", P, "O cérebro que comanda o centro de IA da UFG",
            t("Perfil sobre a criação do primeiro Bacharelado em IA do Brasil e a liderança de uma mulher em uma área com predominância masculina.", "A profile on the creation of Brazil's first Bachelor's degree in AI and a woman's leadership in a predominantly male field."), ler)]
    def imp_li(tp, tags, u, src, fb, alt, pos, v, dt, rot, ti, tx, cta):
        oe = f' onerror="this.onerror=null;this.src=\'{fb}\'"' if fb else ""
        st = f' style="object-position:{pos}"' if pos else ""
        dth = f"<span>{dt}</span>" if dt else ""
        return f'<li data-tipo="{tp}" data-tags="{e(tags)}"><a href="{e(u)}" target="_blank" rel="noopener"><div class="thumb"><img src="{e(src)}"{oe} alt="{e(alt)}" loading="lazy" width="750" height="500"{st}></div><div class="c"><span class="meta"><span class="v">{v}</span>{dth}<span>{rot}</span></span><h3 lang="pt-BR">{ti}</h3><p>{tx}</p><span class="ir">{cta}</span></div></a></li>'
    imphtml = "".join(imp_li(*x) for x in imp)
    temas = ["Infraestrutura de IA no Brasil", "Dado em português", "Soberania com foco em nichos", "Formação de talentos", "PD&I com empresas"]
    temas_en = ["AI infrastructure in Brazil", "Data in Portuguese", "Sovereignty focused on niches", "Talent development", "RD&I with companies"]
    temashtml = "".join(f'<button type="button" data-busca="{e(a)}" aria-pressed="false">{e(b if en else a)}</button>' for a, b in zip(temas, temas_en))

    bio_c = t("Telma Soares é professora e pesquisadora do Instituto de Informática da UFG. É cofundadora do CEIA e diretora executiva do centro desde 2022.",
              "Telma Soares is a professor and researcher at the Institute of Informatics of the Federal University of Goiás (UFG), Brazil. She is co-founder of CEIA, the Center of Excellence in Artificial Intelligence, and has been its executive director since 2022.")
    bio_m = t("Telma Soares é professora e pesquisadora do Instituto de Informática da Universidade Federal de Goiás (UFG) desde 2009. Graduada em Ciência da Computação pela Unesp, é mestre e doutora pela USP. Pesquisa algoritmos evolutivos, aprendizado por reforço e otimização. Atuou na gestão da pós-graduação em Ciência da Computação e participou da construção do Bacharelado em Inteligência Artificial da UFG. É cofundadora do Centro de Excelência em Inteligência Artificial (CEIA), criado em 2019, e diretora executiva do centro desde 2022. Em 2025, recebeu o 2º lugar na categoria Pesquisadora de Destaque do Prêmio Embrapii.",
              "Telma Soares has been a professor and researcher at the Institute of Informatics of the Federal University of Goiás (UFG), Brazil, since 2009. She holds a BSc in Computer Science from Unesp and a master's and PhD from the University of São Paulo (USP). Her research covers evolutionary algorithms, reinforcement learning and optimization. She worked in the management of the graduate programme in Computer Science and took part in building UFG's Bachelor's degree in Artificial Intelligence. She is co-founder of the Center of Excellence in Artificial Intelligence (CEIA), created in 2019, and has been its executive director since 2022. In 2025 she placed 2nd in the Outstanding Researcher category of the Embrapii Award.")
    citar = t("Telma Soares, professora e pesquisadora da UFG, cofundadora e diretora executiva do CEIA.", "Telma Soares, professor and researcher at UFG, co-founder and executive director of CEIA.")
    kitfotos = [("foto-perfil.jpg", t("Retrato com fundo escuro", "Portrait on a dark background")), ("estudio-1951.jpg", t("Retrato de estúdio", "Studio portrait")), ("foto-original-1.jpg", t("Retrato na UFG", "Portrait at UFG"))]
    kitfotoshtml = "".join(f'<a href="{B}img/{f}" download aria-label="{e(t("Baixar foto: ","Download photo: ")+a)}"><img src="{B}img/{f}" alt="{e(a)}" loading="lazy" width="300" height="400"></a>' for f, a in kitfotos)

    canais = [("LinkedIn", t("Conversas sobre pesquisa, formação e inteligência artificial", "Conversations on research, education and artificial intelligence"), t("Acompanhe", "Follow"), LINKEDIN),
              ("Instagram", t("Bastidores, encontros e atividades", "Behind the scenes, meetings and activities"), t("Acompanhe", "Follow"), INSTA),
              (t("Currículo Lattes", "Lattes CV"), t("Formação e produção acadêmica", "Education and academic output"), t("Consulte", "View"), LATTES)]
    canaishtml = "".join(f'<a class="anim" style="--d:{i}" href="{u}" target="_blank" rel="noopener"><strong>{a}</strong><span>{b}</span><em>{c}</em></a>' for i, (a, b, c, u) in enumerate(canais))

    gal = [("foto-evento-4.jpg", t("Telma Soares com os demais participantes do painel sobre IA para infraestrutura crítica, no palco da Rio Innovation Week", "Telma Soares with the other panellists on AI for critical infrastructure, on stage at Rio Innovation Week"), t("Painel sobre IA para infraestrutura crítica, Rio Innovation Week 2026", "Panel on AI for critical infrastructure, Rio Innovation Week 2026")),
           ("foto-grupo-2.jpg", t("Telma Soares com gestores públicos no lançamento do convênio CEIA 2.0 com o Governo de Goiás", "Telma Soares with public officials at the launch of the CEIA 2.0 agreement with the Government of Goiás"), t("Lançamento do convênio CEIA 2.0 com o Governo de Goiás", "Launch of the CEIA 2.0 agreement with the Government of Goiás")),
           ("foto-robo.jpg", t("Telma Soares sorri ao lado de robô humanoide do CEIA", "Telma Soares smiling next to a CEIA humanoid robot"), t("Robótica e IA no CEIA", "Robotics and AI at CEIA")),
           ("foto-evento-3.jpg", t("Telma Soares fala ao microfone no palco da Rio Innovation Week 2026, com projetos do CEIA no telão ao fundo", "Telma Soares speaking on stage at Rio Innovation Week 2026, with CEIA projects on the screen behind her"), t("Apresentação de projetos do CEIA, Rio Innovation Week 2026", "Presentation of CEIA projects, Rio Innovation Week 2026")),
           ("foto-institucional.jpg", t("Telma Soares discursa no lançamento do convênio CEIA 2.0, com as bandeiras do Brasil e de Goiás", "Telma Soares speaking at the launch of the CEIA 2.0 agreement, with the flags of Brazil and Goiás"), t("Discurso no lançamento do convênio CEIA 2.0", "Speech at the launch of the CEIA 2.0 agreement")),
           ("foto-evento-6.jpg", t("Telma Soares ao lado de outro participante, em frente ao painel da Rio Innovation Week", "Telma Soares next to another participant, in front of the Rio Innovation Week backdrop"), "Rio Innovation Week 2026"),
           ("foto-evento-1.jpg", t("Palco do painel sobre IA na Rio Innovation Week, com Telma Soares entre os participantes", "Stage of the AI panel at Rio Innovation Week, with Telma Soares among the participants"), "Rio Innovation Week 2026"),
           ("foto-palestra.jpg", t("Telma Soares fala ao microfone em painel no palco da Rio Innovation Week", "Telma Soares speaking into a microphone on a panel on stage at Rio Innovation Week"), "Rio Innovation Week 2026"),
           ("foto-original-187.jpg", t("Telma Soares sentada ao lado de um robô humanoide e de um robô quadrúpede do CEIA", "Telma Soares sitting next to a humanoid robot and a quadruped robot from CEIA"), t("Robótica e IA no CEIA", "Robotics and AI at CEIA"))]
    galhtml = "".join(f'<button type="button" class="anim" aria-label="{e(t("Ampliar fotografia: ","Enlarge photograph: ")+c)}"><img src="{B}img/{f}" alt="{e(a)}" loading="lazy" width="1600" height="1200"><span>{c}</span></button>' for f, a, c in gal)

    from urllib.parse import quote
    m1 = t("Olá, Telma. Gostaria de apresentar um convite para entrevista, palestra ou debate.", "Hello, Telma. I would like to send an invitation for an interview, talk or debate.")
    m2 = t("Olá, Telma. Gostaria de apresentar uma proposta relacionada a pesquisa ou formação.", "Hello, Telma. I would like to present a proposal related to research or education.")
    m3 = t("Olá, Telma. Gostaria de apresentar uma demanda de projeto de inteligência artificial ao CEIA.", "Hello, Telma. I would like to present an artificial intelligence project request to CEIA.")
    wa = lambda m: WA + quote(m, safe="")
    cam = f'''<article class="cartao anim"><span class="meta">{t("Conversas públicas","Public conversations")}</span><h3>{t("Entrevistas, palestras e debates","Interviews, talks and debates")}</h3><p>{t("Informe o assunto, o público e a data. Para entrevistas, inclua também o veículo e o prazo da pauta.","Tell me the topic, the audience and the date. For interviews, also include the outlet and the deadline.")}</p><a class="btn" href="{wa(m1)}" target="_blank" rel="noopener">{t("Envie um convite ou uma pauta","Send an invitation or a pitch")}</a></article>
<article class="cartao anim" style="--d:1"><span class="meta">{t("Colaboração acadêmica","Academic collaboration")}</span><h3>{t("Pesquisa e formação","Research and education")}</h3><p>{t("Apresente sua instituição, o tema e a proposta que gostaria de discutir sobre pesquisa, ensino ou formação de pessoas.","Introduce your institution, the topic and the proposal you would like to discuss on research, teaching or educating people.")}</p><a class="btn" href="{wa(m2)}" target="_blank" rel="noopener">{t("Converse sobre pesquisa ou formação","Talk about research or education")}</a></article>
<article class="cartao anim" style="--d:2"><span class="meta">{t("Encaminhamentos institucionais","Institutional routes")}</span><h3>{t("Projetos e oportunidades no CEIA","Projects and opportunities at CEIA")}</h3><p>{t("Para uma demanda de projeto, apresente a organização, o problema e o contexto. Para oportunidades nas equipes do centro, consulte o banco de talentos.","For a project request, introduce the organisation, the problem and the context. For opportunities in the centre's teams, see the talent bank.")}</p><a class="btn" href="{wa(m3)}" target="_blank" rel="noopener">{t("Apresente uma demanda ao CEIA","Present a request to CEIA")}</a>{ext(TALENTOS, t("Consulte o banco de talentos","See the talent bank"), "seta cobre-t")}</article>'''


    return f'''<!DOCTYPE html>
<html lang="{t("pt-BR","en")}" data-base="{B}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{titulo}</title>
<meta name="description" content="{e(desc)}">
<link rel="canonical" href="{canon}">
<link rel="alternate" hreflang="pt-BR" href="{URL}">
<link rel="alternate" hreflang="en" href="{URL}en/">
<link rel="alternate" hreflang="x-default" href="{URL}">
<meta property="og:title" content="{e(titulo)}">
<meta property="og:description" content="{e(ogdesc)}">
<meta property="og:type" content="website">
<meta property="og:locale" content="{t("pt_BR","en_US")}">
<meta property="og:url" content="{canon}">
<meta property="og:image" content="{URL}assets/social/capa-compartilhamento-1200x630.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="Telma Soares">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:image" content="{URL}assets/social/capa-compartilhamento-1200x630.png">
<meta name="theme-color" content="#143F49">
<link rel="icon" href="{B}assets/icones/favicon.ico" sizes="48x48">
<link rel="icon" href="{B}assets/icones/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="{B}assets/icones/apple-touch-icon.png">
<link rel="preload" href="{B}assets/fontes/DMSerifDisplay-Regular.woff" as="font" type="font/woff" crossorigin>
<link rel="preload" href="{B}assets/fontes/Inter-Variable.woff" as="font" type="font/woff" crossorigin>
<link id="paleta" rel="stylesheet" href="{B}css/paleta.css">
<script>/* teste de paletas: ?paleta=nome carrega css/paletas/nome.css */
(function(){{var n=new URLSearchParams(location.search).get("paleta"),l=document.getElementById("paleta");if(n&&/^[a-z0-9-]+$/.test(n)){{l.href=l.href.replace(/paleta[.]css$/,"paletas/"+n+".css?v="+Date.now());document.documentElement.setAttribute("data-paleta",n);}}}})();</script>
<link rel="stylesheet" href="{B}css/telma-motion.css">
<link rel="stylesheet" href="{B}css/site.css">
<script>document.documentElement.classList.add("js")</script>
<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
</head>
<body>
<a class="pular" href="#conteudo">{t("Pular para o conteúdo","Skip to content")}</a>

<header class="topo" id="topo">
  <div class="wrap">
    <a class="marca" href="#topo" aria-label="{t("Telma Soares, início","Telma Soares, home")}">{LETTERING_NAV}<span aria-hidden="true">Soares</span></a>
    <button type="button" class="menu-btn" aria-controls="nav" aria-expanded="false" aria-label="{textos["abrirMenu"]}"><svg aria-hidden="true" width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M4 7h16M4 12h16M4 17h16"/></svg></button>
    <nav class="nav" id="nav" aria-label="{t("Principal","Main")}">
      {navhtml}
      <span class="idioma" role="group" aria-label="{t("Idioma","Language")}"><a href="{"../index.html" if en else "index.html"}" lang="pt-BR" hreflang="pt-BR"{"" if en else ' aria-current="true"'}><abbr title="Português" style="text-decoration:none">PT</abbr></a><a href="{"index.html" if en else "en/index.html"}" lang="en" hreflang="en"{' aria-current="true"' if en else ""}><abbr title="English" style="text-decoration:none">EN</abbr></a></span>
      <a class="btn contorno" href="#contato">{t("Contato","Contact")}</a>
      <button type="button" class="pausa" data-telma-motion-toggle data-label-running="{textos["pausar"]}" data-label-paused="{textos["retomar"]}" data-label-unavailable="{t("Fundos estáticos","Static backgrounds")}" aria-pressed="false" hidden><svg class="parar" aria-hidden="true" width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><rect x="6" y="5" width="4" height="14" rx="1"/><rect x="14" y="5" width="4" height="14" rx="1"/></svg><svg class="tocar" aria-hidden="true" width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M8 5v14l11-7z"/></svg><span class="so-leitor" data-telma-motion-label>{textos["pausar"]}</span></button>
    </nav>
  </div>
  <div class="progresso" aria-hidden="true"></div>
</header>

<main id="conteudo">
<section class="hero" aria-labelledby="h1" data-telma-motion="signature" data-telma-surface="dark" data-telma-intensity="normal">
  <div class="wrap grade">
    <div class="texto">
      <p class="olho ent" style="--i:0">{t("Professora e pesquisadora · UFG","Professor and researcher · UFG")}</p>
      <h1 id="h1">{h1html}</h1>
      <p class="vinculo ent" style="--i:5">{t("Sou cofundadora do CEIA e diretora executiva do centro desde 2022.","I am co-founder of CEIA and have been the centre's executive director since 2022.")}</p>
      <div class="acoes ent" style="--i:6">
        {loc("#sobre", t("Conheça minha trajetória","Explore my career"), "btn claro")}
        {loc("#pesquisa", t("Conheça minhas pesquisas","Explore my research"))}
      </div>
    </div>
    <figure>
      <div class="foto"><img src="{B}img/foto-perfil.jpg" alt="{t("Telma Soares de camisa verde, sorrindo, com as mãos nos bolsos, em retrato com fundo escuro","Telma Soares in a green shirt, smiling, hands in her pockets, in a portrait on a dark background")}" width="1067" height="1600" fetchpriority="high"></div>
      {LETTERING.format(cls="", aria='aria-hidden="true"')}
      <figcaption class="selo"><b>{t("Prêmio Embrapii 2025","Embrapii Award 2025")}</b><strong>{t("Pesquisadora de Destaque","Outstanding Researcher")}</strong><span>{t("2º lugar","2nd place")}</span></figcaption>
    </figure>
  </div>
</section>

<section class="faixa" aria-label="{t("Credenciais","Credentials")}"><div class="wrap"><ul>{faixahtml}</ul></div></section>

<section class="sec" id="sobre">
  <div class="wrap">
    <div class="duas">
      <div class="rotulo"><p class="olho">{t("Trajetória","Career")}</p>
        <figure class="retrato anim"><img src="{B}img/estudio-1910.jpg" alt="{t("Telma Soares sorri, sentada, em retrato de estúdio","Telma Soares smiling, seated, in a studio portrait")}" loading="lazy" width="1067" height="1600"><figcaption>Telma Woerle de Lima Soares<small>{t("Professora e pesquisadora da UFG","Professor and researcher at UFG")}</small></figcaption></figure></div>
      <div class="corpo">
        <p class="frase acende">{t("Minha trajetória reúne pesquisa em computação, orientação de estudantes e liderança de iniciativas que aproximam ciência, educação e aplicação da inteligência artificial.","My career brings together research in computing, advising students and leading initiatives that connect science, education and the application of artificial intelligence.")}</p>
        <h2 class="anim" style="font-size:clamp(1.6rem,2.6vw,2.1rem);margin-top:56px">{t("Meu caminho na computação","My path in computing")}</h2>
        <div class="bio anim">
          <p>{t("Meu caminho na computação começou em 1995, em um curso técnico de processamento de dados. Mais tarde, escolhi seguir pela carreira acadêmica. Sou graduada em Ciência da Computação pela Unesp, mestre e doutora pela USP e professora da UFG desde 2009.","My path in computing began in 1995, in a technical course in data processing. Later, I chose an academic career. I hold a BSc in Computer Science from Unesp and a master's and PhD from USP, and I have been a professor at UFG since 2009.")}</p>
          <p>{t("Minha atuação reúne pesquisa, orientação e gestão acadêmica. No mestrado, investiguei algoritmos para prever estruturas de proteínas. No doutorado, trabalhei com estruturas de dados para algoritmos aplicados a problemas de redes. Hoje, meus temas de pesquisa incluem aprendizado por reforço e otimização.","My work combines research, advising and academic management. In my master's, I investigated algorithms for predicting protein structures. In my PhD, I worked on data structures for algorithms applied to network problems. Today, my research topics include reinforcement learning and optimization.")}</p>
          <p>{t("Também atuei na gestão da pós-graduação em Computação e na criação de novas oportunidades de formação. Participei da construção do Bacharelado em Inteligência Artificial da UFG e da fundação do CEIA, em 2019. Desde 2022, sou diretora executiva do centro.","I have also worked in the management of the graduate programme in Computing and in creating new educational opportunities. I took part in building UFG's Bachelor's degree in Artificial Intelligence and in founding CEIA in 2019. Since 2022, I have been the centre's executive director.")}</p>
        </div>
        <div class="ids anim" aria-label="{t("Perfis acadêmicos","Academic profiles")}">
          {ext(LATTES, t("Currículo Lattes","Lattes CV"), "")}
          {ext(DBLP, "DBLP", "")}
          {ext(ITF, t("Meu perfil no IT Forum","My IT Forum profile"), "")}
        </div>
        <ol class="tempo"><span class="fio" aria-hidden="true"></span>{tempohtml}</ol>
        <dl class="sintese anim">{sintesehtml}</dl>
      </div>
    </div>
  </div>
</section>

<section class="sec areia" id="frentes">
  <div class="wrap">
    <p class="olho">{t("Contribuições","Contributions")}</p>
    <h2 class="anim">{t("Pesquisa, formação e liderança","Research, education and leadership")}</h2>
    <p class="lead anim">{t("Essas três frentes se encontram no meu trabalho: investigar problemas, orientar pessoas e participar da construção de condições para que a pesquisa aconteça.","These three fronts meet in my work: investigating problems, advising people and helping to build the conditions for research to happen.")}</p>
    <div class="pilares">{pilhtml}</div>
  </div>
</section>

<section class="sec" id="pesquisa">
  <div class="wrap">
    <p class="olho">{t("Pesquisa","Research")}</p>
    <h2 class="anim">{t("Problemas que investigo","Problems I investigate")}</h2>
    <p class="lead anim" style="margin-bottom:44px">{t("Minha pesquisa reúne algoritmos evolutivos, aprendizado por reforço e otimização. Estes trabalhos mostram alguns dos problemas que investiguei, com acesso às publicações e identificação das contribuições em coautoria.","My research brings together evolutionary algorithms, reinforcement learning and optimization. These works show some of the problems I have investigated, with access to the publications and identification of co-authored contributions.")}</p>
    <div class="grade3">{pesqhtml}</div>
    <p class="fecho">{ext(LATTES, t("Consulte a produção acadêmica completa no Lattes","See the full academic output on Lattes"), "seta sub")}</p>
  </div>
</section>

<section class="sec areia" id="escritos">
  <div class="wrap">
    <div class="cabeca">
      <div><p class="olho">{t("Publicações","Publications")}</p><h2 class="anim">{t("Produção científica","Scientific output")}</h2></div>
      <p class="lead" style="margin:0;max-width:44ch">{t("Artigos, preprints, tese e dissertação. Cada título leva à publicação ou ao seu registro.","Papers, preprints, thesis and dissertation. Each title links to the publication or to its record.")}</p>
    </div>
    <div class="escritos-grade">
      <article class="destaque-escrito anim" id="destaque-escrito">
        <img src="{B}assets/marca/ts-cobre.svg" alt="" aria-hidden="true">
        <div>
          <span class="olho">{t("Publicação em destaque · ICML · 2025","Featured publication · ICML · 2025")}</span>
          <h3>Sliding Puzzles Gym</h3>
          <p>{t("Um ambiente para avaliar representação visual no aprendizado por reforço. Trabalho em coautoria publicado nos anais da ICML.","An environment for evaluating visual representation in reinforcement learning. Co-authored work published in the ICML proceedings.")}</p>
        </div>
        <div class="acoes">{ext(ICML, t("Ler o artigo","Read the paper"), "btn claro")}</div>
      </article>
      <div class="lista-escritos">
        <span class="olho">{t("Do mais recente ao mais antigo","Newest first")}</span>
        <ul id="lista-escritos" aria-live="polite"></ul>
        <noscript><p>{t("Consulte as publicações no","See the publications on")} <a href="{LATTES}">Lattes</a>.</p></noscript>
        <p style="margin-top:18px">{loc(f"{B}{'en/' if en else ''}escritos/index.html", t("Ver todas as publicações","See all publications"))}</p>
      </div>
    </div>
  </div>
</section>

<section class="sec escuro" id="formacao" data-telma-motion="field" data-telma-surface="dark" data-telma-intensity="quiet">
  <div class="wrap">
    <p class="olho">{t("Formação de pessoas","Educating people")}</p>
    <h2 class="anim">{t("Ensinar, orientar e abrir caminhos","Teaching, advising and opening paths")}</h2>
    <p class="lead anim">{t("Minha atuação na educação reúne docência, orientação de estudantes e participação em iniciativas de formação. Esse trabalho passa pela educação básica, pela graduação e pela pós-graduação.","My work in education combines teaching, advising students and taking part in training initiatives. It spans school education, undergraduate and graduate studies.")}</p>
    <div class="fotos3">{fotosformhtml}</div>
    <div class="iniciativas">{inichtml}</div>
  </div>
</section>

<section class="sec" id="aplicada">
  <div class="wrap">
    <p class="olho">{t("Ideias em conversa","Ideas in conversation")}</p>
    <h2 class="anim">{t("Temas que tenho levado ao debate público","Themes I have brought to public debate")}</h2>
    <p class="lead anim">{t("Sínteses de entrevistas sobre pesquisa, infraestrutura, participação e inteligência artificial no Brasil. Cada tema leva à conversa em que foi desenvolvido.","Summaries of interviews on research, infrastructure, participation and artificial intelligence in Brazil. Each theme links to the conversation in which it was developed.")}</p>
    <div class="ideias-wrap">
      <figure class="lateral anim"><img src="{B}img/foto-evento-2.jpg" alt="{t("Telma Soares fala ao microfone, sentada, em painel da Rio Innovation Week","Telma Soares speaking into a microphone, seated, on a panel at Rio Innovation Week")}" loading="lazy" width="1067" height="1600"><figcaption>{t("Telma Soares, professora e pesquisadora da UFG","Telma Soares, professor and researcher at UFG")}</figcaption></figure>
      <div class="ideias">{ideiashtml}</div>
    </div>
  </div>
</section>

<section class="sec escuro numeros" id="numeros" data-telma-motion="field" data-telma-surface="dark" data-telma-intensity="quiet">
  <div class="wrap">
    <div class="com-figura"><div class="tx">
    <p class="olho">{t("Minha atuação no CEIA","My work at CEIA")}</p>
    <h2 class="anim">{t("Construção e liderança do CEIA","Building and leading CEIA")}</h2>
    <div class="texto anim">
      <p>{t("Participei da fundação do Centro de Excelência em Inteligência Artificial em 2019, na UFG, em parceria com a Fapeg. Desde 2022, atuo na direção executiva, com responsabilidades na gestão e na articulação das iniciativas do centro.","I took part in founding the Center of Excellence in Artificial Intelligence in 2019, at UFG, in partnership with Fapeg. Since 2022 I have served as executive director, with responsibilities in managing and coordinating the centre's initiatives.")}</p>
      <p>{t("As pesquisas, os programas e os resultados do CEIA são trabalho de muitas pessoas. Os indicadores abaixo distinguem resultados do centro e de seus parceiros dos dados da minha atuação pessoal.","CEIA's research, programmes and results are the work of many people. The indicators below distinguish the results of the centre and its partners from data on my personal work.")}</p>
    </div>
    <div class="acoes-linha">{ext("https://ceia.ufg.br/", t("Visite o site do CEIA","Visit the CEIA website"), "btn claro")}{loc("#contato", t("Converse sobre um projeto","Talk about a project"))}</div>
    </div><figure class="arco anim"><img src="{B}img/foto-corredor-ceia.jpg" alt="{t("Telma Soares sorri, com a camisa polo do CEIA, em um corredor","Telma Soares smiling, wearing a CEIA polo shirt, in a corridor")}" loading="lazy" width="1067" height="1600"><figcaption>{t("Telma Soares, diretora executiva do CEIA","Telma Soares, executive director of CEIA")}</figcaption></figure></div>
    <div class="grade-num">{numshtml}</div>
    <p class="nota">{t("Referência: outubro de 2026. Os indicadores do CEIA e de seus parceiros representam resultados coletivos.","Reference: October 2026. The indicators for CEIA and its partners represent collective results.")}</p>
  </div>
</section>

<div class="parceiros">
  <p class="rot">{t("Projetos, programas e parcerias do CEIA","CEIA projects, programmes and partnerships")}</p>
  <div class="marquee"><ul>{pl}</ul><ul aria-hidden="true">{pl}</ul></div>
</div>

<section class="sec" id="reconhecimentos">
  <div class="wrap">
    <div class="com-figura"><div class="tx">
    <p class="olho">{t("Reconhecimentos","Recognition")}</p>
    <h2 class="anim">{t("Distinções ao longo da trajetória","Distinctions along the way")}</h2>
    <p class="lead anim">{t("Reúno aqui reconhecimentos à minha atuação e a trabalhos coletivos dos quais participo. Cada registro identifica quem recebeu a distinção e a instituição responsável pela premiação.","Here I gather recognition of my own work and of collective work I take part in. Each record identifies who received the distinction and the institution responsible for the award.")}</p>
    </div><figure class="quadro anim"><img src="{B}img/ordem-merito-anhanguera.jpg" alt="{t("Telma Soares com a medalha da Ordem do Mérito Anhanguera, ao lado de outros participantes da cerimônia","Telma Soares with the Order of Merit Anhanguera medal, next to other participants at the ceremony")}" style="object-position:50% 30%" loading="lazy" width="720" height="1280"><figcaption>{t("Ordem do Mérito Anhanguera, 2026","Order of Merit Anhanguera, 2026")}</figcaption></figure></div>
    <h3 class="grupo-t">{t("Reconhecimentos pessoais","Personal recognition")}</h3>
    <ul class="premios" style="margin-top:16px">{premios(prem_p)}</ul>
    <h3 class="grupo-t">{t("Reconhecimentos de trabalhos coletivos","Recognition of collective work")}</h3>
    <ul class="premios" style="margin-top:16px">{premios(prem_c)}</ul>
  </div>
</section>

<section class="sec areia" id="destaques">
  <div class="wrap">
    <p class="olho">{t("Em destaque","Highlights")}</p>
    <h2 class="anim">{t("Uma seleção para conhecer meu trabalho","A selection to get to know my work")}</h2>
    <p class="lead anim" style="margin-bottom:44px">{t("Um perfil, uma conversa e uma pesquisa para explorar minha trajetória e os temas com que trabalho.","A profile, a conversation and a piece of research to explore my career and the themes I work with.")}</p>
    <div class="grade3">{desthtml}</div>
    <p class="fecho">{loc("#imprensa", t("Veja o arquivo de entrevistas e reportagens","See the archive of interviews and reports"), "seta sub")}</p>
  </div>
</section>

<section class="sec" id="imprensa">
  <div class="wrap">
    <div class="com-figura"><div class="tx">
    <p class="olho">{t("Na imprensa","In the press")}</p>
    <h2 class="anim">{t("Entrevistas, perfis e conversas","Interviews, profiles and conversations")}</h2>
    <p class="lead anim">{t("Participações sobre pesquisa, formação, infraestrutura e inteligência artificial no Brasil. Os links levam aos conteúdos originais de cada veículo.","Appearances on research, education, infrastructure and artificial intelligence in Brazil. The links lead to each outlet's original content, in Portuguese.")}</p>
    <figure class="citacao anim"><blockquote lang="pt-BR">Você faz a sua inteligência própria, você resolve um problema regional, um problema do país.</blockquote><figcaption><cite>{t("Exame, outubro de 2026","Exame, October 2026")}</cite></figcaption></figure>
    </div><figure class="arco anim"><img src="{B}img/estudio-1951.jpg" alt="{t("Telma Soares de blazer preto e braços cruzados, sorrindo, em retrato de estúdio","Telma Soares in a black blazer with arms crossed, smiling, in a studio portrait")}" style="object-position:50% 45%" loading="lazy" width="1067" height="1600"></figure></div>
    <div class="barra">
      <div class="filtros" role="group" aria-label="{t("Filtrar por tipo","Filter by type")}">
        <button type="button" data-filtro="todos" aria-pressed="true">{t("Todas","All")} <b></b></button>
        <button type="button" data-filtro="entrevista" aria-pressed="false">{t("Entrevistas","Interviews")} <b></b></button>
        <button type="button" data-filtro="reportagem" aria-pressed="false">{t("Reportagens","Reports")} <b></b></button>
        <button type="button" data-filtro="perfil" aria-pressed="false">{t("Perfis","Profiles")} <b></b></button>
      </div>
      <div class="busca">
        <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M15.5 14h-.79l-.28-.27a6.5 6.5 0 1 0-.7.7l.27.28v.79l5 4.99L20.49 19l-4.99-5zm-6 0a4.5 4.5 0 1 1 0-9 4.5 4.5 0 0 1 0 9z"/></svg>
        <input type="search" id="busca-imprensa-input" placeholder="{t("Buscar por tema, veículo ou palavra-chave…","Search by theme, outlet or keyword…")}" aria-label="{t("Buscar participações na imprensa","Search press appearances")}" autocomplete="off">
        <button type="button" id="limpa-busca-btn" aria-label="{t("Limpar busca","Clear search")}">×</button>
      </div>
    </div>
    <ul class="lista-imprensa" id="lista-imprensa">{imphtml}</ul>
    <div class="vazio" id="imprensa-vazio" role="status">{t("Nenhuma participação encontrada para essa busca.","No appearances found for this search.")}<button type="button" id="limpar-imprensa">{t("Limpar filtros e busca","Clear filters and search")}</button></div>
    <div class="rodape-imp">
      <p>{t("Jornalistas: consulte os temas das entrevistas ou envie uma pauta.","Journalists: browse the interview themes or send a pitch.")}</p>
      <div class="temas">{temashtml}</div>
      {loc("#contato", t("Propor uma pauta","Pitch a story"), "btn")}
    </div>

    <div class="kit anim" id="kit">
      <p class="olho">{t("Kit de imprensa","Press kit")}</p>
      <h3>{t("Bio, fotos e forma de citar","Bio, photos and how to cite")}</h3>
      <p>{t("Material para veículos, eventos e organizadores. Fotos: acervo pessoal e CEIA.","Material for media outlets, events and organisers. Photos: personal archive and CEIA.")}</p>
      <div class="kit-grade">
        <div class="kit-item"><h4>{t("Bio curta","Short bio")}</h4><p id="bio-curta">{bio_c}</p><button type="button" data-copia="bio-curta">{t("Copiar texto","Copy text")}</button></div>
        <div class="kit-item"><h4>{t("Bio completa","Full bio")}</h4><p id="bio-media">{bio_m}</p><button type="button" data-copia="bio-media">{t("Copiar texto","Copy text")}</button></div>
        <div class="kit-item"><h4>{t("Como citar","How to cite")}</h4><p id="citar">{citar}</p><button type="button" data-copia="citar">{t("Copiar texto","Copy text")}</button>
          <h4 style="margin-top:14px">{t("Fotos para download","Photos to download")}</h4><div class="kit-fotos">{kitfotoshtml}</div></div>
      </div>
    </div>
  </div>
</section>

<section class="sec" id="redes" style="padding-top:0">
  <div class="wrap">
    <p class="olho">{t("Redes e produção","Networks and output")}</p>
    <h2 class="anim">{t("Continue a conversa","Continue the conversation")}</h2>
    <p class="lead anim">{t("Compartilho participações, pesquisas, atividades de formação e registros do trabalho cotidiano. O currículo Lattes reúne minha produção acadêmica.","I share appearances, research, educational activities and records of everyday work. My Lattes CV gathers my academic output.")}</p>
    <div class="canais">{canaishtml}</div>
    <div class="feed-cab"><div><h3>{t("Publicações no LinkedIn","Posts on LinkedIn")}</h3><p style="color:var(--tinta-suave)">{t("Uma seleção de publicações para acompanhar os temas do meu trabalho.","A selection of posts to follow the themes of my work.")}</p></div>{ext(LINKEDIN_ALL, t("Veja todas no LinkedIn","See all on LinkedIn"))}</div>
    <div class="feed" id="feed" aria-live="polite"><p>{t("Carregando publicações…","Loading posts…")}</p></div>
  </div>
</section>

<section class="sec areia" id="bastidores">
  <div class="wrap">
    <p class="olho">{t("Bastidores","Behind the scenes")}</p>
    <h2 class="anim">{t("Pessoas, pesquisa e encontros","People, research and gatherings")}</h2>
    <p class="lead anim">{t("Registros do trabalho no laboratório, de encontros e de conversas públicas sobre inteligência artificial.","Records of lab work, gatherings and public conversations about artificial intelligence.")}</p>
    <div class="mosaico">{galhtml}</div>
  </div>
</section>

<section class="sec escuro news" id="newsletter" data-telma-motion="field" data-telma-surface="dark" data-telma-intensity="normal">
  <div class="wrap">
    <div class="t"><p class="olho">Newsletter</p><h2>{t("Receba novidades por e-mail","Get updates by email")}</h2><p class="lead">{t("Pesquisas, publicações e participações, enviadas quando houver algo novo.","Research, publications and appearances, sent when there is something new.")}</p></div>
    <form id="form-news" novalidate>
      <label for="news-email">{t("Seu e-mail","Your email")}</label>
      <div class="linha"><input id="news-email" name="email" type="email" required autocomplete="email" placeholder="{t("nome@exemplo.com","name@example.com")}"><button type="submit" class="btn cobre">{t("Assinar","Subscribe")}</button></div>
      <small>{t("Você pode cancelar a qualquer momento.","You can unsubscribe at any time.")}</small>
      <p role="status" aria-live="polite"></p>
    </form>
  </div>
</section>

<section class="sec" id="contato">
  <div class="wrap">
    <div class="com-figura"><div class="tx">
    <p class="olho">{t("Contato","Contact")}</p>
    <h2 class="anim">{t("Vamos conversar","Let's talk")}</h2>
    <p class="lead anim">{t("Apresente o assunto e o contexto da conversa. Para projetos e oportunidades no CEIA, use os encaminhamentos específicos abaixo.","Tell me the subject and the context of the conversation. For projects and opportunities at CEIA, use the specific routes below.")}</p>
    </div><figure class="arco pequeno anim"><img src="{B}img/estudio-1921.jpg" alt="{t("Telma Soares sorrindo, apoiada no encosto de uma cadeira, em retrato de estúdio","Telma Soares smiling, leaning on the back of a chair, in a studio portrait")}" style="object-position:45% 20%" loading="lazy" width="1067" height="1600"></figure></div>
    <div class="caminhos">{cam}</div>
    <div class="assina">
      {LETTERING.format(cls="", aria=f'role="img" aria-label="Telma"')}
      <ul><li><a href="tel:+5562981008111">WhatsApp: (62) 98100-8111</a></li><li><a href="{LINKEDIN}" target="_blank" rel="noopener">LinkedIn</a></li><li><a href="{INSTA}" target="_blank" rel="noopener">Instagram</a></li><li><a href="{LATTES}" target="_blank" rel="noopener">{t("Currículo Lattes","Lattes CV")}</a></li><li><a href="{B}card/index.html">{t("Cartão digital","Digital card")}</a></li></ul>
    </div>
  </div>
</section>
</main>

<footer>
  <div class="wrap">
    <div class="g">
      <div class="id"><a class="marca" href="#topo" aria-label="{t("Telma Soares, voltar ao início","Telma Soares, back to top")}">{LETTERING_NAV}<span aria-hidden="true">Soares</span></a><p class="nome">Telma Woerle de Lima Soares</p><p>{t("Professora e pesquisadora do Instituto de Informática da UFG. Cofundadora do CEIA e diretora executiva desde 2022.","Professor and researcher at the Institute of Informatics, UFG. Co-founder of CEIA and executive director since 2022.")}</p><p>{loc("#contato", t("Entrar em contato","Get in touch"), "btn cobre")}</p></div>
      <nav aria-label="{t("Perfis pessoais","Personal profiles")}"><h2>{t("Perfis","Profiles")}</h2><ul><li><a href="{LINKEDIN}" target="_blank" rel="noopener">LinkedIn</a></li><li><a href="{INSTA}" target="_blank" rel="noopener">Instagram</a></li><li><a href="{LATTES}" target="_blank" rel="noopener">{t("Currículo Lattes","Lattes CV")}</a></li><li><a href="{DBLP}" target="_blank" rel="noopener">DBLP</a></li></ul></nav>
      <nav aria-label="CEIA"><h2>CEIA</h2><ul><li><a href="https://ceia.ufg.br/" target="_blank" rel="noopener">CEIA/UFG</a></li><li><a href="{TALENTOS}" target="_blank" rel="noopener">{t("Banco de talentos do CEIA","CEIA talent bank")}</a></li><li><a href="https://www.linkedin.com/company/centrodeexcelenciaemia" target="_blank" rel="noopener">{t("LinkedIn do CEIA","CEIA on LinkedIn")}</a></li><li><a href="https://www.instagram.com/ceiaufg/" target="_blank" rel="noopener">{t("Instagram do CEIA","CEIA on Instagram")}</a></li></ul></nav>
      <nav aria-label="{t("Neste site","On this site")}"><h2>{t("Neste site","On this site")}</h2><ul><li><a href="{B}{'en/' if en else ''}escritos/index.html">{t("Publicações","Publications")}</a></li><li><a href="#kit">{t("Kit de imprensa","Press kit")}</a></li><li data-news><a href="#newsletter">Newsletter</a></li><li><a href="{B}card/index.html">{t("Cartão digital","Digital card")}</a></li></ul></nav>
    </div>
    <div class="fim"><span>{t("Site pessoal de Telma Woerle de Lima Soares.","Personal website of Telma Woerle de Lima Soares.")}</span><span>{t("Fotos: acervo pessoal e CEIA.","Photos: personal archive and CEIA.")}</span><span class="idioma" role="group" aria-label="{t("Idioma","Language")}"><a href="{"../index.html" if en else "index.html"}" lang="pt-BR" hreflang="pt-BR"{"" if en else ' aria-current="true"'}>Português</a><a href="{"index.html" if en else "en/index.html"}" lang="en" hreflang="en"{' aria-current="true"' if en else ""}>English</a></span></div>
  </div>
</footer>
<a class="subir" href="#topo" aria-label="{t("Voltar ao topo","Back to top")}"><svg aria-hidden="true" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M12 19V5"/><path d="M5 12l7-7 7 7"/></svg></a>

<dialog class="luz" aria-label="{t("Fotografia ampliada","Enlarged photograph")}">
  <img src="" alt=""><p></p>
  <div class="ctl">
    <button type="button" data-luz="ant" aria-label="{t("Fotografia anterior","Previous photograph")}"><svg aria-hidden="true" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M15 6l-6 6 6 6"/></svg></button>
    <button type="button" data-luz="fechar" aria-label="{t("Fechar fotografia ampliada","Close enlarged photograph")}"><svg aria-hidden="true" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M6 6l12 12M18 6L6 18"/></svg></button>
    <button type="button" data-luz="prox" aria-label="{t("Próxima fotografia","Next photograph")}"><svg aria-hidden="true" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M9 6l6 6-6 6"/></svg></button>
  </div>
</dialog>

{emb("dados-publicacoes", PUBS)}
{emb("dados-escritos", ESCRITOS)}
{emb("dados-posts", {"posts": POSTS["posts"]})}
<script>window.SITE_TEXTOS={json.dumps(textos, ensure_ascii=False)};</script>
<script src="{B}js/telma-brand-geometry.js"></script>
<script src="{B}js/telma-motion.js"></script>
<script>(function(){{if(!window.TelmaMotion||window.telmaMotionController)return;window.telmaMotionController=window.TelmaMotion.mountAll({{root:document,selector:"[data-telma-motion]"}});document.querySelectorAll("[data-telma-motion-toggle]").forEach(function(b){{b.hidden=false;}});}})();</script>
<script src="{B}js/config.js"></script>
<script src="{B}js/site.js"></script>
</body>
</html>
'''

def leitura(lang):
    en = lang == "en"
    def t(pt, en_): return en_ if en else pt
    B = "../../" if en else "../"
    home = B + ("en/" if en else "") + "index.html"
    tx = {"ensaio": t("Ensaio", "Essay"), "voltar": t("Todas as publicações", "All publications"), "salvar": t("Salvar em PDF", "Save as PDF"), "baixar": t("Baixar PDF", "Download PDF"),
          "nao": t("Este texto não foi encontrado.", "This text was not found."), "ensaios": t("Ensaios", "Essays"), "pubs": t("Publicações científicas", "Scientific publications"),
          "sem": t("Os primeiros ensaios serão publicados aqui em breve.", "The first essays will be published here soon."), "titulo": t("Publicações", "Publications"),
          "intro": t("A bibliografia científica de Telma Soares, do trabalho mais recente ao mais antigo. Cada título leva à publicação ou ao seu registro.", "The scientific bibliography of Telma Soares, newest first. Each title links to the publication or to its record."), "por": t("Por Telma Soares", "By Telma Soares"), "com": t("Com", "With")}
    return f'''<!DOCTYPE html>
<html lang="{t("pt-BR","en")}" data-base="{B}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{t("Publicações | Telma Soares","Publications | Telma Soares")}</title>
<meta name="description" content="{tx["intro"]}">
<link rel="canonical" href="{URL}{"en/" if en else ""}escritos/">
<link rel="alternate" hreflang="pt-BR" href="{URL}escritos/">
<link rel="alternate" hreflang="en" href="{URL}en/escritos/">
<meta name="theme-color" content="#143F49">
<link rel="icon" href="{B}assets/icones/favicon.ico" sizes="48x48">
<link rel="icon" href="{B}assets/icones/favicon.svg" type="image/svg+xml">
<link id="paleta" rel="stylesheet" href="{B}css/paleta.css">
<script>/* teste de paletas: ?paleta=nome carrega css/paletas/nome.css */
(function(){{var n=new URLSearchParams(location.search).get("paleta"),l=document.getElementById("paleta");if(n&&/^[a-z0-9-]+$/.test(n)){{l.href=l.href.replace(/paleta[.]css$/,"paletas/"+n+".css?v="+Date.now());document.documentElement.setAttribute("data-paleta",n);}}}})();</script>
<link rel="stylesheet" href="{B}css/telma-motion.css">
<link rel="stylesheet" href="{B}css/site.css">
<script>document.documentElement.classList.add("js")</script>
</head>
<body>
<a class="pular" href="#conteudo">{t("Pular para o conteúdo","Skip to content")}</a>
<header class="topo" id="topo"><div class="wrap">
  <a class="marca" href="{home}" aria-label="{t("Telma Soares, início","Telma Soares, home")}">{LETTERING_NAV}<span aria-hidden="true">Soares</span></a>
  <nav class="nav" style="display:flex;position:static;flex-direction:row;background:none;padding:0" aria-label="{t("Principal","Main")}">
    <span class="idioma" role="group" aria-label="{t("Idioma","Language")}"><a href="{B}escritos/index.html" lang="pt-BR"{"" if en else ' aria-current="true"'}>PT</a><a href="{B}en/escritos/index.html" lang="en"{' aria-current="true"' if en else ""}>EN</a></span>
    <a class="btn contorno" href="{home}#contato">{t("Contato","Contact")}</a>
  </nav>
</div></header>
<main id="conteudo"><article class="leitura" id="leitura" aria-live="polite"></article></main>
<footer><div class="wrap"><div class="fim" style="margin-top:0;border-top:0;padding-top:0"><span>{t("Site pessoal de Telma Woerle de Lima Soares.","Personal website of Telma Woerle de Lima Soares.")}</span><a href="{home}">{t("Voltar ao início","Back to home")}</a></div></div></footer>
{emb("dados-publicacoes", PUBS)}
{emb("dados-escritos", ESCRITOS)}
<script>window.SITE_TEXTOS={json.dumps(tx, ensure_ascii=False)};</script>
<script src="{B}js/config.js"></script>
<script src="{B}js/site.js"></script>
<script src="{B}js/escritos.js"></script>
</body>
</html>
'''

open(OUT + "/index.html", "w").write(page("pt"))
open(OUT + "/en/index.html", "w").write(page("en"))
open(OUT + "/escritos/index.html", "w").write(leitura("pt"))
open(OUT + "/en/escritos/index.html", "w").write(leitura("en"))
json.dump(PUBS, open(OUT + "/content/publicacoes.json", "w"), ensure_ascii=False, indent=2)
import os
if not os.path.exists(OUT + "/content/escritos.json"):
    json.dump(ESCRITOS, open(OUT + "/content/escritos.json", "w"), ensure_ascii=False, indent=2)
print("ok")
