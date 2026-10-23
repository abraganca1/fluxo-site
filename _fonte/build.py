# Para editar textos das práticas: altere a lista P abaixo e rode "python _fonte/build.py" dentro de 3_Site.
# Gera index.html e praticas/*.html do site Fluxo v5 a partir de um único template.
import html, os
OUT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # grava em 3_Site/
SITE = "https://www.consultoriafluxo.com.br/"
WA = "https://wa.me/5571997123637?text=Ol%C3%A1%2C%20%C3%81lvaro.%20Vim%20pelo%20site%20da%20Consultoria%20Fluxo%20e%20gostaria%20de%20conversar."
WA_PATH = "M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2Zm0 18.2a8.2 8.2 0 0 1-4.2-1.2l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2Zm4.5-6.1c-.2-.1-1.5-.7-1.7-.8-.2-.1-.4-.1-.6.1l-.8 1c-.1.2-.3.2-.5.1a6.7 6.7 0 0 1-3.3-2.9c-.2-.4.2-.4.7-1.3.1-.2 0-.3 0-.4l-.8-1.8c-.2-.5-.4-.4-.6-.4h-.5a1 1 0 0 0-.7.3 3 3 0 0 0-.9 2.2 5.2 5.2 0 0 0 1.1 2.7 11.8 11.8 0 0 0 4.5 4c1.7.7 2.3.8 3.2.6a2.7 2.7 0 0 0 1.8-1.3 2.2 2.2 0 0 0 .2-1.3c-.1-.1-.3-.2-.5-.3Z"
ARROW = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>'
CHECK = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M5 12.5l4.5 4.5L19 7"/></svg>'
X = '<svg class="xmark"{attrs} viewBox="0 0 600 600" aria-hidden="true"><path class="b" d="M420 0h100L187 600H87z"/><path class="a" d="M80 0h100l333 600H413z"/></svg>'
XS = '<svg class="xs" viewBox="0 0 600 600" aria-hidden="true"><path d="M420 0h100L187 600H87z" fill="#5E86C1" opacity=".35"/><path d="M80 0h100l333 600H413z" fill="none" stroke="rgba(255,255,255,.3)"/></svg>'
e = lambda s: html.escape(s, quote=False)

STATS = {
    "ma": ("+R$", "100", "M", "em operações de M&A e captação estruturadas"),
    "val": ("+", "50", "", "valuations de empresas realizados"),
    "tes": ("+R$", "50", "M", "em fluxo de tesouraria já operados"),
    "zero": ("+", "10", "", "empresas estruturadas do zero"),
}
CAREER = {
    "mckinsey": ("McKinsey & Company", "Estratégia, due diligence e transformação operacional"),
    "newbay": ("Newbay", "Private equity e M&A: valuations e negociações"),
    "squadra": ("Squadra Sports", "CFO: tesouraria, controladoria, governança, aquisições e fundraising"),
    "ambev": ("Ambev", "Estratégia comercial e operações"),
    "bahia": ("Esporte Clube Bahia", "Coordenador administrativo e financeiro: tesouraria, controladoria e estratégia"),
    "ufba": ("UFBA", "Engenharia Elétrica pela UFBA"),
}

P = [
 dict(slug="ma", n="01", t="M&A", q="Quanto vale a empresa e quando vender ou comprar?",
  meta="Assessoria em M&A para fundadores, acionistas e fundos: buy-side e sell-side, valuation, due diligence e negociação.",
  intro="Comprar, vender ou trazer um sócio são decisões que acontecem poucas vezes na vida de uma empresa e definem boa parte do seu valor. Apoiamos fundadores, acionistas e fundos do diagnóstico à assinatura, com números defensáveis e presença na mesa de negociação.",
  svc=[("Assessoria buy-side e sell-side","Tese da transação, mapeamento e abordagem de contrapartes, condução do processo e coordenação com assessores jurídicos e contábeis, do lado de quem compra ou de quem vende."),
       ("Valuation técnico e defensável","Avaliação por fluxo de caixa descontado e múltiplos de mercado, com premissas documentadas e faixas de valor que sustentam a conversa com investidores, sócios e conselho."),
       ("Due diligence e data room","Organização das informações financeiras, operacionais e societárias, identificação antecipada de riscos e montagem do data room para um processo mais rápido e com menos surpresas."),
       ("Negociação com fundadores e fundos","Apoio na definição de estrutura, preço e condições, como earn-out, governança e cláusulas de saída, e participação nas rodadas de negociação.")],
  when=["Recebeu uma proposta e quer saber se o preço é justo","Pretende vender ou trazer um sócio nos próximos anos e precisa se preparar","Avalia comprar um concorrente, fornecedor ou negócio complementar"],
  stats=["ma","val"], career=["newbay","mckinsey","squadra"]),
 dict(slug="estruturacao-e-modelagem", n="02", t="Estruturação e modelagem", q="Este novo negócio fecha a conta? Com que premissas?",
  meta="Business plan, modelagem financeira, unit economics, venture building e materiais para captação.",
  intro="Antes de investir tempo e capital, a pergunta é direta: o negócio fecha a conta? Construímos o modelo econômico-financeiro que responde a isso, com premissas explícitas e cenários que mostram o que precisa ser verdade para dar certo.",
  svc=[("Business plan e modelagem financeira","Projeção integrada de resultado, caixa e balanço, com cenários conservador, base e otimista e análise de sensibilidade das premissas que mais mexem no valor."),
       ("Unit economics e modelo de receita","Margem por produto, cliente ou canal, custo de aquisição, payback e ponto de equilíbrio, para saber quais vendas criam valor e quais só aumentam a receita."),
       ("Venture building","Estruturação de novos negócios do zero: tese, modelo operacional, plano de lançamento e indicadores dos primeiros meses."),
       ("Materiais para captação","Modelo, teaser e apresentação para investidores e bancos, coerentes entre si e prontos para a diligência.")],
  when=["Vai lançar uma nova unidade, produto ou empresa","Precisa apresentar o plano a investidores, bancos ou ao conselho","Cresce em receita, mas não sabe se cresce em margem"],
  stats=["zero","ma"], career=["squadra","newbay"]),
 dict(slug="estrategia", n="03", t="Estratégia", q="Qual é o tamanho real do mercado e onde está o valor?",
  meta="Planejamento estratégico, market sizing (TAM, SAM, SOM), go-to-market, pricing, expansão e benchmarking.",
  intro="Uma boa estratégia cabe em poucas escolhas: onde jogar, como ganhar e o que deixar de fazer. Partimos do tamanho real do mercado e da posição da empresa para chegar a prioridades claras e a um plano que a liderança consegue executar.",
  svc=[("Planejamento estratégico","Diagnóstico, definição de ambição e prioridades, e desdobramento em metas e iniciativas com responsáveis e calendário."),
       ("Market sizing (TAM, SAM, SOM)","Dimensionamento do mercado com abordagem top-down e bottom-up, para separar o mercado teórico do que a empresa pode de fato capturar."),
       ("Go-to-market e pricing","Segmentação, proposta de valor, canais e política de preços, testados contra a economia de cada cliente."),
       ("Expansão e benchmarking","Avaliação de novas praças, segmentos ou produtos e comparação com referências do setor para calibrar metas.")],
  when=["Vai definir o plano dos próximos anos","Avalia entrar em um novo mercado, região ou segmento","Precisa revisar preços ou o modelo comercial"],
  stats=[], career=["mckinsey","ambev"]),
 dict(slug="processos", n="04", t="Processos", q="Como crescer sem que custo e complexidade cresçam junto?",
  meta="Diagnóstico e desenho de processos, transformação operacional, gestão estratégica de custos e governança.",
  intro="Crescer costuma trazer mais pessoas, mais sistemas e mais exceções. Redesenhamos processos e rotinas de gestão para que a operação ganhe escala sem que custo e complexidade cresçam no mesmo ritmo.",
  svc=[("Diagnóstico e desenho de processos","Mapeamento do fluxo atual, identificação de gargalos, retrabalho e pontos de controle, e desenho do processo futuro com papéis claros."),
       ("Transformação operacional","Implementação das mudanças com a equipe, priorizando ganhos rápidos e acompanhando indicadores de produtividade e nível de serviço."),
       ("Gestão estratégica de custos","Análise da base de custos por natureza e por atividade, para cortar o que não gera valor e proteger o que gera."),
       ("Governança e rituais de gestão","Reuniões, indicadores e alçadas de decisão que dão ritmo à execução e visibilidade à liderança.")],
  when=["A margem caiu enquanto a receita subia","A operação depende demais de poucas pessoas","Decisões se perdem entre áreas e reuniões"],
  stats=[], career=["mckinsey","ambev"]),
 dict(slug="ia-para-negocios", n="05", t="IA para negócios", q="Onde a IA gera margem na operação e por onde começar?",
  meta="Mapa de oportunidades de IA, agentes e automações sob medida, workshops para lideranças, governança e adoção.",
  intro="A IA gera valor quando resolve um problema concreto da operação, não quando vira um projeto paralelo. Identificamos onde ela traz margem, construímos as primeiras soluções e preparamos a equipe para usá-las no dia a dia.",
  svc=[("Mapa de oportunidades de IA","Levantamento dos processos com maior potencial, estimativa de impacto e esforço, e priorização em um roadmap realista."),
       ("Agentes e automações sob medida","Desenvolvimento de assistentes e automações conectados aos sistemas e documentos da empresa, começando pelos casos de uso de retorno mais rápido."),
       ("Workshops para lideranças","Sessões práticas para que diretores e gestores entendam o que a IA faz bem, onde ela erra e como aplicá-la nas suas áreas."),
       ("Governança e adoção","Regras de uso, segurança de dados, métricas de adoção e acompanhamento para que as soluções saiam do piloto.")],
  when=["Quer usar IA, mas não sabe por onde começar","Tem tarefas repetitivas com documentos, planilhas ou atendimento","Já testou ferramentas, mas a adoção não aconteceu"],
  stats=[], career=["mckinsey"]),
 dict(slug="controladoria", n="06", t="Controladoria", q="Os números chegam ao conselho confiáveis e a tempo?",
  meta="Orçamento, orçado x realizado, FP&A, projeções financeiras, relatórios gerenciais, KPIs e dashboards para o conselho.",
  intro="Conselho e diretoria só decidem bem com números confiáveis e no tempo certo. Estruturamos a controladoria, do orçamento ao relatório mensal, para que a gestão enxergue o resultado e aja antes que o problema apareça no caixa.",
  svc=[("Orçamento e orçado x realizado","Construção do orçamento anual com as áreas e rotina mensal de comparação, com explicação dos desvios e plano de correção."),
       ("FP&A e projeções financeiras","Projeções de resultado e caixa atualizadas ao longo do ano, para antecipar necessidades de capital e apoiar decisões."),
       ("Relatórios gerenciais e KPIs","Os indicadores certos para cada nível de gestão, com definições únicas e fonte de dados conhecida."),
       ("Dashboards para o conselho","Painéis claros e periódicos que levam ao conselho o que importa: resultado, caixa, riscos e andamento das prioridades.")],
  when=["O fechamento do mês demora ou muda depois de apresentado","O conselho pede números que a empresa não consegue produzir","Não há orçamento, ou ele não é acompanhado"],
  stats=["tes"], career=["squadra","bahia"]),
]

def head(title, desc, canon, pre):
    return f'''<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{e(title)}</title>
<meta name="description" content="{html.escape(desc)}">
<link rel="canonical" href="{canon}">
<meta property="og:type" content="website">
<meta property="og:title" content="{html.escape(title)}">
<meta property="og:description" content="{html.escape(desc)}">
<meta property="og:image" content="{SITE}assets/img/alvaro-perfil.jpg">
<meta property="og:locale" content="pt_BR">
<meta name="theme-color" content="#112546">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' rx='6' fill='%23112546'/%3E%3Cpath d='M8 7h6l10 18h-6z' fill='%23fff'/%3E%3Cpath d='M24 7h-5L9 25h5z' fill='%235E86C1'/%3E%3C/svg%3E">
<script>document.documentElement.classList.add('js');setTimeout(function(){{if(!window.__fx)document.documentElement.classList.remove('js')}},2500)</script>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Source+Serif+4:opsz,wght@8..60,300;8..60,400;8..60,500;8..60,600&family=Albert+Sans:wght@400;500;600;700&family=Saira:wght@500;600;700&display=swap">
<link rel="stylesheet" href="{pre}assets/css/fluxo.css">
<script src="{pre}assets/js/fluxo.js" defer></script>
'''

def header(pre, home, current=None):
    h = "" if home else pre + "index.html"
    mega = "".join(f'<a href="{pre}praticas/{p["slug"]}.html"{" aria-current=\"page\"" if p["slug"]==current else ""}><i>{p["n"]}</i><b>{e(p["t"])}</b><span>{e(p["q"])}</span></a>' for p in P)
    msub = "".join(f'<a href="{pre}praticas/{p["slug"]}.html">{p["n"]} · {e(p["t"])}</a>' for p in P)
    return f'''</head>
<body>
<a class="skip" href="#conteudo">Pular para o conteúdo</a>
<header class="top">
  <div class="wrap">
    <a class="brand" href="{h}#inicio" aria-label="Consultoria Fluxo, início"><img src="{pre}assets/img/logo-azul.png" alt="Consultoria Fluxo" width="80" height="34"></a>
    <nav class="nav" aria-label="Principal">
      <div class="dd"><a href="{h}#praticas"{' aria-current="true"' if current else ''}>Práticas</a><div class="mega">{mega}</div></div>
      <a href="{h}#abordagem">Abordagem</a>
      <a href="{h}#clientes">Clientes</a>
      <a href="{h}#fundador">Fundador</a>
      <a class="btn btn-navy" href="{h}#contato">Fale conosco</a>
      <button class="burger" aria-label="Abrir menu" aria-expanded="false" aria-controls="mnav"><span></span></button>
    </nav>
  </div>
  <span class="progress" aria-hidden="true"></span>
</header>
<nav class="mnav" id="mnav" aria-label="Menu">
  <a href="{h}#praticas">Práticas</a><div class="sub">{msub}</div>
  <a href="{h}#abordagem">Abordagem</a><a href="{h}#clientes">Clientes</a><a href="{h}#fundador">Fundador</a><a href="{h}#contato">Contato</a>
</nav>
'''

def contact(pre, after_mist=False, title='Qual é a próxima <span class="accent">grande decisão</span> da sua empresa?'):
    return f'''
  <section class="contact on-navy cut-top{' after-mist' if after_mist else ''}" id="contato">
    <div class="bg" aria-hidden="true">{X.format(attrs=' data-parallax=".08"')}</div>
    <div class="wrap">
      <div>
        <p class="label" data-reveal>Contato</p>
        <h2 data-split>{title}</h2>
        <p class="lede" data-reveal>Uma conversa inicial, sem compromisso. Se fizer sentido, voltamos com escopo, prazo e investimento.</p>
        <div class="ctas" data-reveal>
          <a class="btn btn-white" href="mailto:alvaro@consultoriafluxo.com.br?subject=Conversa%20com%20a%20Consultoria%20Fluxo">Agendar uma conversa {ARROW}</a>
          <a class="btn btn-ghost" href="{WA}" target="_blank" rel="noopener"><svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="{WA_PATH}"/></svg> WhatsApp</a>
        </div>
      </div>
      <ul class="info" data-stagger>
        <li data-reveal><span class="label">E-mail</span><a href="mailto:alvaro@consultoriafluxo.com.br">alvaro@consultoriafluxo.com.br</a></li>
        <li data-reveal><span class="label">WhatsApp</span><a href="https://wa.me/5571997123637" target="_blank" rel="noopener">(71) 9 9712-3637</a></li>
        <li data-reveal><span class="label">Escritório</span><a href="https://www.google.com/maps/search/?api=1&amp;query=Av.+da+Fran%C3%A7a+Com%C3%A9rcio+Salvador+BA+40010-000" target="_blank" rel="noopener">Av. da França, S/N · Comércio · Salvador, BA</a></li>
      </ul>
    </div>
  </section>
'''

def footer(pre, home):
    h = "" if home else pre + "index.html"
    return f'''</main>
<footer>
  <div class="wrap">
    <img src="{pre}assets/img/logo-branca.png" alt="Consultoria Fluxo" width="70" height="30">
    <nav aria-label="Rodapé"><a href="{h}#praticas">Práticas</a><a href="{h}#abordagem">Abordagem</a><a href="{h}#clientes">Clientes</a><a href="{h}#fundador">Fundador</a><a href="{h}#contato">Contato</a></nav>
    <span>© 2026 Consultoria Fluxo</span>
  </div>
</footer>
<a class="wa-float" href="{WA}" target="_blank" rel="noopener" aria-label="Conversar no WhatsApp"><svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="{WA_PATH}"/></svg></a>
</body>
</html>
'''

def stat_html(k):
    pre_, num, suf, d = STATS[k]
    return f'<div class="stat"><b><small>{e(pre_)}</small><span data-count="{num}">{num}</span>{suf}</b><span class="d">{e(d)}</span></div>'

def pcard(p, pre, small=False):
    q = "" if small else f'<p>{e(p["q"])}</p>'
    return f'''<a class="pcard" href="{pre}praticas/{p["slug"]}.html" data-reveal>{XS}<span class="num">{p["n"]}</span><h3>{e(p["t"])}</h3>{q}<span class="go">{'Ver detalhamento' if not small else 'Ver'} {ARROW}</span></a>'''

# ---------------- HOME ----------------
def home():
    pre = ""
    logos = [("petrobahia","Petrobahia",""),("prima","Prima Empreendimentos",""),("intermaritima","Intermarítima Portos e Logística","tall"),("isb","ISB","tall"),("syntropy","Syntropy Agricultura Integrada",""),("inhire","Inhire","clip"),("footure","Footure Football Company","faint"),("hike","Hike","clip"),("cantina-volpi","Cantina Volpi","tall clip")]
    lg = "\n        ".join(f'<img{(" class=%s" % chr(34)+c+chr(34)) if c else ""} src="assets/img/clientes/{f}.png" alt="{e(a)}" loading="lazy" data-reveal>' for f,a,c in logos)
    car = "\n          ".join(f'<li data-reveal><img src="assets/img/carreira/{k}.png" alt="{e(CAREER[k][0])}"><span>{e(CAREER[k][1])}</span></li>' for k in ["mckinsey","newbay","squadra","ambev","bahia","ufba"])
    cards = "\n        ".join(pcard(p, pre) for p in P)
    s = head("Consultoria Fluxo | Consultoria estratégica, M&A e IA para negócios",
             "Consultoria estratégica para fundadores, conselhos e executivos: M&A, estruturação e modelagem de negócios, estratégia, processos, IA para negócios e controladoria.", SITE, pre)
    s += '<script type="application/ld+json">{"@context":"https://schema.org","@type":"ProfessionalService","name":"Consultoria Fluxo","url":"https://www.consultoriafluxo.com.br","email":"alvaro@consultoriafluxo.com.br","telephone":"+55-71-99712-3637","founder":{"@type":"Person","name":"Álvaro Bragança"},"address":{"@type":"PostalAddress","streetAddress":"Av. da França, S/N, Comércio","addressLocality":"Salvador","addressRegion":"BA","postalCode":"40010-000","addressCountry":"BR"}}</script>\n'
    s += header(pre, True)
    tags = "".join(f'<a href="praticas/{p["slug"]}.html">{e(p["t"]) if p["slug"]!="estruturacao-e-modelagem" else "Modelagem"}</a>' for p in P)
    s += f'''
<main id="inicio">
  <section class="hero on-navy" id="conteudo">
    {X.format(attrs=' data-parallax=".15"')}
    <div class="wrap">
      <p class="label" data-reveal>Consultoria estratégica · Salvador, Brasil</p>
      <h1 data-split>Estratégia com rigor para decisões que <span class="accent">definem o valor</span> da sua empresa.</h1>
      <p class="lede" data-reveal style="--d:4">Apoiamos fundadores, conselhos e executivos em crescimento, transações e transformação, com método de consultoria global e execução próxima do negócio.</p>
      <div class="ctas" data-reveal style="--d:6">
        <a class="btn btn-white" href="#contato">Discutir um desafio {ARROW}</a>
        <a class="more" href="#praticas">Conheça as seis práticas</a>
      </div>
      <p class="tags" aria-label="Práticas" data-reveal style="--d:8">{tags}</p>
    </div>
    <span class="scroll-cue" aria-hidden="true"></span>
  </section>

  <section class="sec" id="quem-somos">
    <div class="wrap">
      <div class="sec-head">
        <p class="label" data-reveal>Quem somos</p>
        <h2 data-split>Apoiamos fundadores, conselhos e executivos em <span class="accent">crescimento, transações e transformação</span></h2>
        <p class="lede" data-reveal>Método de consultoria global, profundidade em finanças corporativas e execução próxima do negócio.</p>
      </div>
      <div class="stats" data-stagger>
        {"".join(stat_html(k).replace('<div class="stat">','<div class="stat" data-reveal>') for k in ["ma","tes","val","zero"])}
      </div>
    </div>
  </section>

  <section class="clients mist" id="clientes" aria-labelledby="clientes-t">
    <div class="wrap">
      <div class="clients-head" data-reveal>
        <p id="clientes-t">Companhias de alcance regional e nacional que <span class="accent">estruturam e escalam</span> suas operações com a Fluxo.</p>
        <span class="label">Clientes</span>
      </div>
      <div class="logos" data-stagger>
        {lg}
      </div>
    </div>
  </section>

  <section class="sec" id="praticas">
    <div class="wrap">
      <div class="sec-head">
        <p class="label" data-reveal>Áreas de atuação</p>
        <h2 data-split>Seis práticas, combinadas conforme a <span class="accent">pergunta que chega à mesa</span></h2>
        <p class="lede" data-reveal>Escolha uma prática para ver o que entregamos, quando faz sentido e como trabalhamos.</p>
      </div>
      <div class="pgrid" data-stagger>
        {cards}
      </div>
    </div>
  </section>

  <section class="sec approach on-navy cut-top" id="abordagem">
    <div class="bg" aria-hidden="true">{X.format(attrs=' data-parallax=".1"')}</div>
    <div class="wrap">
      <div class="sec-head">
        <p class="label" data-reveal>Abordagem</p>
        <h2 data-split>Começamos pelas perguntas certas e terminamos com <span class="accent">uma recomendação clara</span></h2>
      </div>
      <ol class="phases" data-stagger>
        <li class="phase" data-reveal><span class="rule"></span><div class="n"><b>1</b><span>Fase</span></div><h3>Imersão</h3><p>Negócio, materiais existentes e árvore de questões-chave.</p><p class="out"><b>Saída</b>Perguntas e premissas validadas</p></li>
        <li class="phase" data-reveal><span class="rule"></span><div class="n"><b>2</b><span>Fase</span></div><h3>Análise</h3><p>Dados, benchmark e modelagem top-down e bottom-up.</p><p class="out"><b>Saída</b>Modelo aberto e documentado</p></li>
        <li class="phase" data-reveal><span class="rule"></span><div class="n"><b>3</b><span>Fase</span></div><h3>Recomendação</h3><p>Cenários, riscos e a decisão recomendada.</p><p class="out"><b>Saída</b>Deck executivo para o conselho</p></li>
        <li class="phase" data-reveal><span class="rule"></span><div class="n"><b>4</b><span>Fase</span></div><h3>Implementação</h3><p>Plano de ação, governança e indicadores.</p><p class="out"><b>Saída</b>Rituais de gestão em operação</p></li>
      </ol>
    </div>
  </section>

  <section class="sec" id="formato">
    <div class="wrap">
      <div class="sec-head">
        <p class="label" data-reveal>Formato dos projetos</p>
        <h2 data-split>Escopo, prazo e investimento <span class="accent">definidos antes do início</span></h2>
      </div>
      <div class="format-grid">
        <div class="principles" data-stagger>
          <div class="principle" data-reveal><i>a.</i><h3>Senioridade</h3><p>Conduzido pelo fundador, do kick-off à recomendação final.</p></div>
          <div class="principle" data-reveal><i>b.</i><h3>Números que se sustentam</h3><p>Cada premissa com fonte, racional e faixa: conservador, base e otimista.</p></div>
          <div class="principle" data-reveal><i>c.</i><h3>Sem caixa-preta</h3><p>Checkpoints combinados com a liderança e entregas semanais.</p></div>
        </div>
        <div class="deliver" data-reveal style="--d:2">
          <span class="label">O que o cliente recebe</span>
          <ul>
            {"".join(f"<li>{CHECK}<span>{t}</span></li>" for t in ["Deck executivo com recomendação e cenários","Modelo em Excel aberto, que é do cliente","Caderno de premissas com fontes","Reuniões de alinhamento e validação","Uma rodada de ajustes após a entrega final"])}
          </ul>
        </div>
      </div>
    </div>
  </section>

  <section class="sec mist" id="fundador">
    <div class="wrap founder">
      <figure><div class="ph" data-wipe><img src="assets/img/alvaro-perfil.jpg" alt="Álvaro Bragança, fundador da Consultoria Fluxo" width="1000" height="1500"></div></figure>
      <div>
        <p class="label" data-reveal>Fundador</p>
        <h2 data-split><span class="accent">10 anos de carreira</span> dos dois lados da mesa</h2>
        <p class="name" data-reveal>Álvaro Bragança</p>
        <p class="label role" data-reveal>Fundador e sócio-diretor</p>
        <ul class="career" data-stagger>
          {car}
        </ul>
      </div>
    </div>
  </section>
'''
    s += contact(pre, after_mist=True)
    s += footer(pre, True)
    open(os.path.join(OUT, "index.html"), "w").write(s)

# ---------------- PRÁTICAS ----------------
STEPS = [("Imersão","Negócio, materiais existentes e árvore de questões-chave."),("Análise","Dados, benchmark e modelagem top-down e bottom-up."),("Recomendação","Cenários, riscos e a decisão recomendada."),("Implementação","Plano de ação, governança e indicadores.")]

def practice(p):
    pre = "../"
    url = f'{SITE}praticas/{p["slug"]}.html'
    s = head(f'{p["t"]} | Consultoria Fluxo', p["meta"], url, pre)
    s += ('<script type="application/ld+json">{"@context":"https://schema.org","@type":"Service","name":"' + p["t"] + '","serviceType":"' + p["t"] + '","provider":{"@type":"ProfessionalService","name":"Consultoria Fluxo","url":"https://www.consultoriafluxo.com.br"},"areaServed":"BR","url":"' + url + '"}</script>\n')
    s += header(pre, False, p["slug"])
    svc = "\n        ".join(f'<article data-reveal><i>{chr(97+i)}.</i><h3>{e(t)}</h3><p>{e(d)}</p></article>' for i,(t,d) in enumerate(p["svc"]))
    when = "".join(f'<li data-reveal>{e(w)}</li>' for w in p["when"])
    stats = ""
    if p["stats"]:
        cls = {1:" n1",2:" n2"}.get(len(p["stats"]), "")
        stats = f'''
  <section class="sec" style="padding-top:0">
    <div class="wrap">
      <p class="label" data-reveal style="margin-bottom:28px">Em números</p>
      <div class="stats{cls}" data-stagger>{"".join(stat_html(k).replace('<div class="stat">','<div class="stat" data-reveal>') for k in p["stats"])}</div>
    </div>
  </section>'''
    car = "".join(f'<li>{e(CAREER[k][0])}: {e(CAREER[k][1])}</li>' for k in p["career"])
    others = "\n        ".join(pcard(o, pre, small=True) for o in P if o is not p)
    steps = "".join(f'<li data-reveal><b>{i+1}</b><h3>{t}</h3><p>{d}</p></li>' for i,(t,d) in enumerate(STEPS))
    s += f'''
<main id="inicio">
  <section class="phero on-navy" id="conteudo">
    {X.format(attrs=' data-parallax=".15"')}
    <div class="wrap">
      <nav class="crumbs" aria-label="Você está em" data-reveal><a href="../index.html">Início</a><span aria-hidden="true">/</span><a href="../index.html#praticas">Práticas</a><span aria-hidden="true">/</span><span>{e(p["t"])}</span></nav>
      <span class="bignum" data-reveal style="--d:1">{p["n"]}</span>
      <h1 data-split>{e(p["t"])}</h1>
      <p class="q" data-reveal style="--d:3">{e(p["q"])}</p>
    </div>
  </section>

  <section class="sec">
    <div class="wrap intro">
      <div><p class="label" data-reveal>Visão geral</p></div>
      <p class="big" data-reveal>{e(p["intro"])}</p>
    </div>
  </section>

  <section class="sec" style="padding-top:0" id="como-ajudamos">
    <div class="wrap">
      <div class="sec-head">
        <p class="label" data-reveal>Como ajudamos</p>
        <h2 data-split>O que a prática de {e(p["t"])} <span class="accent">entrega</span></h2>
      </div>
      <div class="svc" data-stagger>
        {svc}
      </div>
    </div>
  </section>
{stats}
  <section class="sec mist">
    <div class="wrap">
      <div class="sec-head">
        <p class="label" data-reveal>Quando faz sentido</p>
        <h2 data-split>Situações em que <span class="accent">costumamos ser chamados</span></h2>
      </div>
      <ul class="when" data-stagger>{when}</ul>
    </div>
  </section>

  <section class="sec">
    <div class="wrap">
      <div class="sec-head">
        <p class="label" data-reveal>Quem conduz</p>
        <h2 data-split>Senioridade do <span class="accent">início ao fim</span></h2>
      </div>
      <div class="lead" data-reveal>
        <div data-wipe><img src="../assets/img/alvaro-perfil.jpg" alt="Álvaro Bragança" width="1000" height="1500" loading="lazy"></div>
        <div>
          <p class="name">Álvaro Bragança</p>
          <p class="label" style="margin-top:8px">Fundador e sócio-diretor</p>
          <ul>{car}<li>Conduz o projeto do kick-off à recomendação final</li></ul>
        </div>
      </div>
    </div>
  </section>

  <section class="sec on-navy cut-top">
    <div class="bg" aria-hidden="true">{X.format(attrs=' data-parallax=".08"')}</div>
    <div class="wrap">
      <div class="sec-head">
        <p class="label" data-reveal>Como trabalhamos</p>
        <h2 data-split>Das perguntas certas a <span class="accent">uma recomendação clara</span></h2>
      </div>
      <ol class="steps" data-stagger>{steps}</ol>
      <p data-reveal style="margin-top:56px"><a class="more" href="../index.html#abordagem">Ver a abordagem completa</a></p>
    </div>
  </section>

  <section class="sec">
    <div class="wrap">
      <div class="sec-head">
        <p class="label" data-reveal>Outras práticas</p>
        <h2 data-split>Práticas que costumam <span class="accent">andar juntas</span></h2>
      </div>
      <div class="others" data-stagger>
        {others}
      </div>
    </div>
  </section>
'''
    s += contact(pre, title=f'Vamos conversar sobre <span class="accent">{e(p["t"])}</span> na sua empresa?')
    s += footer(pre, False)
    os.makedirs(os.path.join(OUT, "praticas"), exist_ok=True)
    open(os.path.join(OUT, "praticas", p["slug"] + ".html"), "w").write(s)

home()
for p in P: practice(p)
print("ok")
