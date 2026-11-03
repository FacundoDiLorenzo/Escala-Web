"""Generates the static Escala Web pages (shared header/footer) into the repo root.

Usage: python3 scripts/build.py .   (run from the repo root)
Page texts in Spanish live here; EN/IT translations live in assets/i18n.js."""
import sys, pathlib
OUT = pathlib.Path(sys.argv[1])

IC = {
 'arrow': '<svg class="ico ico-arrow" viewBox="0 0 24 24" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>',
 'down': '<svg class="ico ico-down" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 5v14M6 13l6 6 6-6"/></svg>',
 'back': '<svg class="ico" viewBox="0 0 24 24" aria-hidden="true"><path d="M19 12H5M11 18l-6-6 6-6"/></svg>',
 'chat': '<svg class="ico" viewBox="0 0 24 24" aria-hidden="true"><path d="M4 20l1.2-4A8 8 0 1 1 8 18.8z"/></svg>',
 'check': '<svg class="ico" viewBox="0 0 24 24" aria-hidden="true"><path d="M5 12.5l4.5 4.5L19 7.5"/></svg>',
 'pin': '<svg class="ico" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 21s-7-6.2-7-11.5a7 7 0 0 1 14 0C19 14.8 12 21 12 21z"/><circle cx="12" cy="9.5" r="2.5"/></svg>',
 'flip': '<svg class="ico" viewBox="0 0 24 24" aria-hidden="true"><path d="M3 12a9 9 0 0 1 15.4-6.4L21 8M21 3v5h-5M21 12a9 9 0 0 1-15.4 6.4L3 16M3 21v-5h5"/></svg>',
 's1': '<svg class="ico" viewBox="0 0 24 24" aria-hidden="true"><rect x="3" y="4" width="18" height="16" rx="2.5"/><path d="M3 9h18M7 13h6M7 16h4"/></svg>',
 's2': '<svg class="ico" viewBox="0 0 24 24" aria-hidden="true"><rect x="5" y="3" width="14" height="18" rx="2.5"/><path d="M9 8h6M9 11.5h6"/><rect x="9" y="15" width="6" height="2.5" rx="1.25"/></svg>',
 's3': '<svg class="ico" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c2.5 2.6 3.8 5.6 3.8 9s-1.3 6.4-3.8 9c-2.5-2.6-3.8-5.6-3.8-9S9.5 5.6 12 3z"/></svg>',
 's4': '<svg class="ico" viewBox="0 0 24 24" aria-hidden="true"><path d="M20 11a8 8 0 0 0-14.6-4.5L3.5 8.5M3.5 4v4.5H8M4 13a8 8 0 0 0 14.6 4.5l1.9-2M20.5 20v-4.5H16"/></svg>',
}
NAV = [('servicios.html','navServices','Servicios'),('sobre-mi.html','navAbout','Sobre mí'),('preguntas-frecuentes.html','navFaq','Preguntas'),('contacto.html','navContact','Contacto')]

def t(key, es, tag='span', cls='', extra=''):
    c = f' class="{cls}"' if cls else ''
    return f'<{tag}{c} data-i18n="{key}"{extra}>{es}</{tag}>'

def scalebar(draw=True, ticks=True):
    tk = '<div class="ticks"><span>0</span><span>1</span><span>2</span></div>' if ticks else ''
    unit = '<span class="unit">km</span>' if ticks else ''
    return f'<div class="scalebar{" draw" if draw else ""}" aria-hidden="true"><div><div class="sb"><i></i><i></i><i></i><i></i><i></i></div>{tk}</div>{unit}</div>'

def header(cur):
    links = ''.join(f'<a href="{h}" data-i18n="{k}"{" aria-current=\"page\"" if h==cur else ""}>{es}</a>' for h,k,es in NAV)
    mlinks = ''.join(f'<li><a href="{h}" style="--i:{i}"{" aria-current=\"page\"" if h==cur else ""}><span data-i18n="{k}">{es}</span>{IC["arrow"]}</a></li>' for i,(h,k,es) in enumerate(NAV))
    return f'''<a class="skip" href="#contenido" data-i18n="skip">Saltar al contenido</a>
<header class="site">
  <div class="wrap bar">
    <a class="name" href="index.html"{' aria-current="page"' if cur=='index.html' else ''}><span class="mark" aria-hidden="true"><i></i><i></i><i></i></span>Escala Web</a>
    <nav class="main" aria-label="Principal">
      <div class="links">{links}</div>
      <div class="lang" role="group" aria-label="Idioma / Language / Lingua">
        <span class="lang-ind" aria-hidden="true"></span>
        <button type="button" id="lang-es" data-lang="es" aria-pressed="true">ES</button>
        <button type="button" id="lang-en" data-lang="en" aria-pressed="false">EN</button>
        <button type="button" id="lang-it" data-lang="it" aria-pressed="false">IT</button>
      </div>
      <button type="button" class="menu-btn" id="menu-btn" aria-expanded="false" aria-controls="menu-panel"><span class="burger" aria-hidden="true"><i></i><i></i></span><span data-i18n="menu">Menú</span></button>
    </nav>
  </div>
  <div class="menu-panel" id="menu-panel"><ul class="wrap">{mlinks}</ul></div>
</header>'''

def footer():
    links = ''.join(f'<a href="{h}" data-i18n="{k}">{es}</a>' for h,k,es in NAV)
    return f'''<footer class="site">
  <div class="wrap">
    <p class="foot-mark" aria-hidden="true" data-rv>Escala Web</p>
    <nav class="foot-nav" aria-label="Pie">{links}</nav>
    <div class="foot-row">
      <span>© 2026 Escala Web · Facundo Di Lorenzo · <span data-i18n="footer">Diseño web · Málaga</span></span>
      <span class="foot-legal"><a href="aviso-legal.html" data-i18n="legalNotice">Aviso legal</a><a href="privacidad.html" data-i18n="privacy">Política de privacidad</a></span>
    </div>
  </div>
</footer>'''

WA = f'<a class="wa-float" id="wa-float" href="https://wa.me/34663625836" target="_blank" rel="noopener" tabindex="-1">{IC["chat"]}<span data-i18n="waBtn">Escríbeme por WhatsApp</span></a>'

def page(fname, title_key, title_es, desc, body, wa=True):
    html = f'''<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title_es}</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#F3F0E8" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#0F1012" media="(prefers-color-scheme: dark)">
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="preload" href="assets/fonts/archivo-latin.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="assets/styles.css">
<script>document.documentElement.classList.add('js')</script>
</head>
<body data-title="{title_key}">
{header(fname)}
<main id="contenido">
{body}
</main>
{WA if wa else ''}
{footer()}
<script src="assets/i18n.js"></script>
<script src="assets/main.js"></script>
</body>
</html>
'''
    (OUT/fname).write_text(html)

def page_head(title_key, title_es, lead_key=None, lead_es='', crumb=True):
    c = f'<a class="crumb fade" href="index.html">{IC["back"]}<span data-i18n="home">Inicio</span></a>' if crumb else ''
    lead = f'<p class="lead fade d1" data-i18n="{lead_key}">{lead_es}</p>' if lead_key else ''
    return f'''<div class="wrap page-head">
  {c}
  <h1><span class="ln"><span class="ln-in" data-i18n="{title_key}">{title_es}</span></span></h1>
  {lead}
  {scalebar(True, False)}
</div>'''

SERV = [
 ('s1','Web corporativa','Una web completa para presentar tu empresa, tus servicios y tu forma de contacto.'),
 ('s2','Landing page','Una sola página enfocada en un producto, una campaña o captar clientes.'),
 ('s3','Web multilingüe','Tu web en español, inglés o italiano, pensada para clientes de distintos países.'),
 ('s4','Renovación de tu web','Actualizo tu web actual para que se vea moderna y funcione bien en el móvil.'),
]
FAQ = [
 ('q1','¿Cuánto cuesta una web?','a1','Depende de lo que necesites: cada proyecto es distinto. Escríbeme, cuéntame tu idea y te digo cuánto costaría.'),
 ('q2','¿Cuánto tiempo tarda?','a2','Una web puede estar lista en unos 2 días desde que tengo toda la información.'),
 ('q3','¿Qué tengo que darte?','a3','Toda la información que quieras que salga en tu web: textos, fotos, servicios y datos de contacto. Cuanta más información me des, mejor quedará tu web.'),
 ('q4','¿Tengo que encargarme del dominio y del alojamiento?','a4','No. Me ocupo yo del dominio y de dar de alta la web, y esos gastos están incluidos en la tarifa.'),
 ('q5','¿La web se verá bien en el móvil?','a5','Sí. Cada web se diseña pensando primero en el teléfono, que es desde donde la mayoría de tus clientes la verán.'),
 ('q6','¿En qué idiomas puede estar mi web?','a6','En español, inglés e italiano, o en varios a la vez con un selector de idioma como el de esta web.'),
 ('q7','¿Qué significa que la web se crea con inteligencia artificial?','a7','Uso herramientas de inteligencia artificial para diseñar y programar más rápido. Yo dirijo el proyecto y reviso el resultado, para que la web quede como la necesitas.'),
 ('q8','¿Trabajas solo en Málaga?','a8','Estoy en Málaga, pero también trabajo a distancia con clientes de otros lugares.'),
]
def faq_list(items, rv=True):
    r = ' data-rv' if rv else ''
    return '<div class="faq">' + ''.join(f'<details{r}><summary>{t(q,qe)}<span class="plus" aria-hidden="true"></span></summary><div class="answer"><p data-i18n="{a}">{ae}</p></div></details>' for q,qe,a,ae in items) + '</div>'

def services_list():
    return '<ul class="services">' + ''.join(f'<li class="service" data-rv>{IC[k]}<h3 data-i18n="{k}t">{n}</h3><p data-i18n="{k}d">{d}</p></li>' for k,n,d in SERV) + '</ul>'

PHOTO = '<img src="assets/facundo.webp" alt="Facundo Di Lorenzo" width="560" height="700"'

# ───────── index ─────────
page('index.html','tHome','Escala Web · Diseño web en Málaga','Escala Web: páginas web profesionales en Málaga y a distancia, en español, inglés e italiano.', f'''
  <div class="wrap hero" id="inicio">
    <h1><span class="ln"><span class="ln-in" data-i18n="heroA">Tu web profesional,</span></span><span class="ln ln-serif"><span class="ln-in" data-i18n="heroB">sin complicaciones.</span></span></h1>
    <div class="hero-foot">
      <div>
        <p class="hero-sub fade d1" data-i18n="heroSub">Páginas web profesionales creadas con inteligencia artificial.</p>
        <div class="actions fade d2">
          <a class="btn solid" href="contacto.html"><span data-i18n="ctaTalk">Hablemos de tu proyecto</span>{IC["arrow"]}</a>
          <a class="btn ghost" href="#servicios"><span data-i18n="ctaServices">Ver servicios</span>{IC["down"]}</a>
        </div>
      </div>
      <div class="hero-meta">
        {scalebar()}
        <p class="fade d3"><span data-i18n="heroEyebrow">Diseño web</span> · Málaga, España · ES / EN / IT</p>
      </div>
    </div>
  </div>

  <section id="servicios" class="ruled">
    <div class="wrap section">
      <p class="sec-label" data-i18n="servEyebrow">Servicios</p>
      <h2 data-i18n="servTitle" data-rv>Lo que puedo hacer por tu empresa</h2>
      <div class="sec-content">
        {services_list()}
        <p class="note" data-rv>{IC["chat"]}<span data-i18n="servNote">Cada proyecto es distinto. Escríbeme y consúltame lo que necesites.</span></p>
        <a class="more" href="servicios.html" data-rv><span data-i18n="seeServices">Ver los servicios en detalle</span>{IC["arrow"]}</a>
      </div>
    </div>
  </section>

  <section id="sobre-mi" class="ruled">
    <div class="wrap section">
      <p class="sec-label" data-i18n="aboutEyebrow">Sobre mí</p>
      <h2 data-i18n="aboutTitle" data-rv>Comercio internacional e inteligencia artificial</h2>
      <div class="sec-content">
        <div class="teaser">
          <div class="portrait" data-rv>{PHOTO} loading="lazy"></div>
          <div class="teaser-body">
            <p data-i18n="aboutTeaser" data-rv>Soy Facundo Di Lorenzo, tengo 19 años y diseño webs desde Málaga para empresas de aquí y de fuera, en español, inglés e italiano.</p>
            <a class="more" href="sobre-mi.html" data-rv><span data-i18n="meetMe">Conóceme</span>{IC["arrow"]}</a>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section id="preguntas" class="ruled">
    <div class="wrap section">
      <p class="sec-label" data-i18n="faqEyebrow">Preguntas frecuentes</p>
      <h2 data-i18n="faqTitle" data-rv>Lo que suelen preguntarme</h2>
      <div class="sec-content">
        {faq_list([FAQ[0], FAQ[1], FAQ[3]])}
        <a class="more" href="preguntas-frecuentes.html" data-rv><span data-i18n="seeFaq">Ver todas las preguntas</span>{IC["arrow"]}</a>
      </div>
    </div>
  </section>

  <section class="project-slide opens" data-wa-hide>
    <div class="wrap slide">
      <h2 data-i18n="contTitle" data-rv>Hablemos de tu proyecto</h2>
      <p class="slide-intro" data-i18n="panelIntro" data-rv>Escríbeme, cuéntame qué necesitas y lo vemos juntos.</p>
      <div class="actions" data-rv>
        <a class="btn light" href="contacto.html"><span data-i18n="toContact">Ver mis datos de contacto</span>{IC["arrow"]}</a>
        <a class="btn outline-light" href="https://wa.me/34663625836" target="_blank" rel="noopener">{IC["chat"]}<span data-i18n="waBtn">Escríbeme por WhatsApp</span></a>
      </div>
    </div>
  </section>''')

# ───────── servicios ─────────
SDET = {
 's1': ('Una web con varias secciones que presenta tu empresa: quién eres, qué ofreces y cómo pueden contactarte.','Empresas y profesionales que necesitan una presencia seria y cuidada en internet.',
        ['Diseño a medida, pensado primero para el móvil','Las secciones que necesites: inicio, servicios, sobre vosotros, contacto…','Botones para llamar, escribir por WhatsApp o enviar un email','Dominio y alta de la web incluidos en la tarifa']),
 's2': ('Una sola página pensada para un único objetivo: vender un producto, anunciar una campaña o conseguir nuevos clientes.','Lanzamientos, promociones y negocios que quieren empezar con algo sencillo y directo.',
        ['Un mensaje claro y un único objetivo','Llamadas a la acción siempre a mano','Diseño pensado primero para el móvil','Dominio y alta de la web incluidos en la tarifa']),
 's3': ('Tu web en español, inglés o italiano, con un selector para que cada visitante elija su idioma.','Negocios con clientes de otros países, como los que trabajan con el turismo en la Costa del Sol.',
        ['Textos adaptados a cada idioma, no traducidos palabra por palabra','Selector de idioma que recuerda la elección del visitante','Diseño pensado primero para el móvil','Dominio y alta de la web incluidos en la tarifa']),
 's4': ('Actualizo tu web actual para que se vea moderna, se entienda mejor y funcione bien en el móvil.','Empresas con una web antigua o que no se ve bien en el teléfono.',
        ['Diseño nuevo a partir de tu contenido actual','Adaptación completa al móvil','Textos y estructura más claros','Publicación incluida en la tarifa']),
}
blocks = ''
for i,(k,n,_) in enumerate(SERV):
    what, who, inc = SDET[k]
    lis = ''.join(f'<li>{IC["check"]}<span data-i18n="{k}i{j+1}">{x}</span></li>' for j,x in enumerate(inc))
    blocks += f'''
  <section class="ruled" id="{k}">
    <div class="wrap svc">
      <div class="svc-icon" data-rv>{IC[k]}</div>
      <div class="svc-main">
        <h2 data-i18n="{k}t" data-rv>{n}</h2>
        <p class="what" data-i18n="{k}what" data-rv>{what}</p>
        <div class="svc-cols">
          <div data-rv><h3 data-i18n="lblFor">Para quién es</h3><p data-i18n="{k}for">{who}</p></div>
          <div data-rv><h3 data-i18n="lblIncl">Qué incluye</h3><ul class="checks">{lis}</ul></div>
        </div>
      </div>
    </div>
  </section>'''
STEPS = [('st1','Me escribes','Me cuentas qué necesitas por WhatsApp, teléfono o email.'),('st2','Me envías la información','Todo lo que quieras que salga en tu web: textos, fotos, servicios y datos.'),('st3','Diseño tu web','Puede estar lista en unos 2 días desde que tengo toda la información.'),('st4','La revisamos juntos','Me dices qué te gusta y qué cambiarías.'),('st5','La publico','Me encargo del dominio y de dar de alta la web.')]
steps = ''.join(f'<li data-rv><strong data-i18n="{k}t">{a}</strong><span data-i18n="{k}d">{b}</span></li>' for k,a,b in STEPS)
page('servicios.html','tServ','Servicios · Escala Web','Webs corporativas, landing pages, webs multilingües y renovación de webs, desde Málaga y a distancia.', f'''
{page_head('servTitle','Lo que puedo hacer por tu empresa','svcLead','Diseño webs profesionales con ayuda de la inteligencia artificial. Pueden estar listas en unos 2 días desde que tengo toda tu información.')}
{blocks}
  <section class="ruled">
    <div class="wrap section">
      <p class="sec-label" data-i18n="procLabel">Proceso</p>
      <h2 data-i18n="procTitle" data-rv>Cómo trabajamos</h2>
      <div class="sec-content">
        <ol class="steps">{steps}</ol>
        <p class="note" data-rv>{IC["chat"]}<span data-i18n="servNote">Cada proyecto es distinto. Escríbeme y consúltame lo que necesites.</span></p>
        <a class="btn solid" href="contacto.html" data-rv><span data-i18n="ctaTalk">Hablemos de tu proyecto</span>{IC["arrow"]}</a>
      </div>
    </div>
  </section>''')

# ───────── sobre mí ─────────
page('sobre-mi.html','tAbout','Sobre mí · Escala Web','Facundo Di Lorenzo: diseño web con inteligencia artificial desde Málaga, en español, inglés e italiano.', f'''
{page_head('aboutTitle','Comercio internacional e inteligencia artificial','aboutLead','Diseño webs desde Málaga para empresas de aquí y de fuera.')}
  <div class="wrap about-grid">
    <div class="flip-slot" data-rv>
      <button type="button" class="flip" id="flip-card" aria-pressed="false" data-i18n-label="flipLabel" aria-label="Girar la tarjeta para ver más sobre Facundo">
        <span class="flip-inner">
          <span class="flip-face flip-front">
            {PHOTO}>
            <span class="flip-hint">{IC["flip"].replace('class="ico"','class="ico"')}<span data-i18n="flipHint">Pasa el cursor o toca para girar</span></span>
          </span>
          <span class="flip-face flip-back">
            <span class="flip-name">Facundo Di Lorenzo</span>
            <span class="flip-text" data-i18n="flipText">Soy Facundo Di Lorenzo y tengo 19 años. Soy graduado en Bachillerato de Letras y actualmente estudio Comercio Internacional y curso un máster de Inteligencia Artificial y sus skills.</span>
            <span class="flip-ask" data-i18n="flipAsk">Si necesitas algo más, pregúntame.</span>
          </span>
        </span>
      </button>
    </div>
    <div class="about-body">
      <div class="prose" data-rv><h2 data-i18n="bioTitle">Quién soy</h2><p data-i18n="bio1">Soy Facundo Di Lorenzo, tengo 19 años y vivo en Málaga. Me gradué en Bachillerato de Letras y ahora estudio Comercio Internacional mientras curso un máster de Inteligencia Artificial y sus skills.</p></div>
      <div class="prose" data-rv><h2 data-i18n="whyTitle">Por qué trabajo con inteligencia artificial</h2><p data-i18n="why1">Uso la inteligencia artificial para diseñar y construir webs más rápido, sin renunciar al cuidado. Así tu web puede estar lista en unos 2 días, y cada detalle lo reviso yo.</p></div>
      <div class="prose" data-rv><h2 data-i18n="langTitle">Clientes de cualquier lugar</h2><p data-i18n="lang1">Hablo español, inglés e italiano. Estoy en Málaga, pero también trabajo a distancia, así que puedo atenderte estés donde estés.</p></div>
      <dl class="facts" data-rv>
        <div class="fact"><dt data-i18n="fBase">Base</dt><dd>Málaga, España</dd></div>
        <div class="fact"><dt data-i18n="fLang">Idiomas</dt><dd data-i18n="fLangV">Español, inglés, italiano</dd></div>
        <div class="fact"><dt data-i18n="fStudy">Formación</dt><dd data-i18n="fStudyV">Comercio Internacional · Máster en IA</dd></div>
        <div class="fact"><dt data-i18n="fRemote">Modalidad</dt><dd data-i18n="fRemoteV">En Málaga y a distancia</dd></div>
      </dl>
      <div class="actions" data-rv>
        <a class="btn solid" href="contacto.html"><span data-i18n="ctaTalk">Hablemos de tu proyecto</span>{IC["arrow"]}</a>
      </div>
    </div>
  </div>''')

# ───────── preguntas frecuentes ─────────
page('preguntas-frecuentes.html','tFaq','Preguntas frecuentes · Escala Web','Precio, plazos, dominio, idiomas y cómo trabajo: respuestas a las dudas más habituales.', f'''
{page_head('faqEyebrow','Preguntas frecuentes','faqLead','Si tu duda no está aquí, escríbeme y consúltame.')}
  <div class="wrap section" style="padding-top:0">
    <div class="sec-content" style="grid-column:1/-1">
      {faq_list(FAQ)}
      <div class="actions" data-rv>
        <a class="btn solid" href="contacto.html"><span data-i18n="ctaTalk">Hablemos de tu proyecto</span>{IC["arrow"]}</a>
      </div>
    </div>
  </div>''')

# ───────── contacto ─────────
COPY_ICO = '<span class="copy-ico" aria-hidden="true"><svg class="ico i-copy" viewBox="0 0 24 24"><rect x="8" y="8" width="12" height="12" rx="2.5"/><path d="M16 8V6.5A2.5 2.5 0 0 0 13.5 4h-7A2.5 2.5 0 0 0 4 6.5v7A2.5 2.5 0 0 0 6.5 16H8"/></svg><svg class="ico i-check" viewBox="0 0 24 24"><path d="M5 12.5l4.5 4.5L19 7.5"/></svg></span>'
page('contacto.html','tContact','Contacto · Escala Web','Cuéntame tu proyecto: teléfono y WhatsApp +34 663 625 836, email dilorenzo.facundo19@gmail.com.', f'''
  <section class="project-slide contact-hero">
    <div class="wrap slide">
      <a class="crumb fade" href="index.html">{IC["back"]}<span data-i18n="home">Inicio</span></a>
      <h1><span class="ln" style="display:block"><span class="ln-in" data-i18n="contTitle">Hablemos de tu proyecto</span></span></h1>
      <p class="slide-intro fade d1" data-i18n="briefIntro">Para que tu web sea realmente buena, cuando me escribas cuéntame:</p>
      <ul class="asks">
        <li class="fade d1"><strong data-i18n="b1t">Qué quieres</strong><span data-i18n="b1d">el tipo de web y para qué la necesitas.</span></li>
        <li class="fade d2"><strong data-i18n="b2t">Cómo la imaginas</strong><span data-i18n="b2d">estilo, colores, webs que te gusten como referencia.</span></li>
        <li class="fade d3"><strong data-i18n="b3t">Todo sobre ti</strong><span data-i18n="b3d">los detalles personales y profesionales de tu empresa: historia, servicios, clientes y lo que te diferencia.</span></li>
      </ul>
      <div class="slide-end fade d3">
        <p class="slide-outro" data-i18n="briefOutro">Cuanta más información me des, mejor quedará tu web.</p>
        <a class="btn light" href="#datos"><span data-i18n="toContact">Ver mis datos de contacto</span>{IC["down"]}</a>
      </div>
    </div>
  </section>

  <section id="datos">
    <div class="wrap section">
      <p class="sec-label" data-i18n="dataEyebrow">Datos de contacto</p>
      <h2 data-i18n="dataTitle" data-rv>Escríbeme o llámame</h2>
      <div class="sec-content">
        <div class="contact-list">
          <div class="contact-row" data-rv>
            <div><span class="lbl" data-i18n="cPhone">Teléfono y WhatsApp</span><span class="val" id="phone">+34 663 625 836</span></div>
            <button class="copy" type="button" id="copy-phone" data-copy="+34663625836">{COPY_ICO}<span class="copy-txt" data-i18n="copy" aria-live="polite">Copiar</span></button>
          </div>
          <div class="contact-row" data-rv>
            <div><span class="lbl" data-i18n="cMail">Email</span><span class="val" id="mail">dilorenzo.facundo19@gmail.com</span></div>
            <button class="copy" type="button" id="copy-mail" data-copy="dilorenzo.facundo19@gmail.com">{COPY_ICO}<span class="copy-txt" data-i18n="copy" aria-live="polite">Copiar</span></button>
          </div>
        </div>
        <a class="btn solid" href="https://wa.me/34663625836" target="_blank" rel="noopener" data-rv>{IC["chat"]}<span data-i18n="waBtn">Escríbeme por WhatsApp</span></a>
        <p class="contact-place" data-rv>{IC["pin"]}<span data-i18n="place">En Málaga y también a distancia</span></p>
      </div>
    </div>
  </section>''', wa=False)

# ───────── legal ─────────
LEGAL = {
'es': '''<dl class="legal-table"><dt>Titular</dt><dd>Facundo Di Lorenzo</dd><dt>Actividad</dt><dd>Diseño de páginas web (Escala Web)</dd><dt>Localidad</dt><dd>Málaga, España</dd><dt>Email</dt><dd>dilorenzo.facundo19@gmail.com</dd><dt>Teléfono</dt><dd>+34 663 625 836</dd></dl>
<h2>Objeto</h2><p>Esta web presenta los servicios de diseño web de Escala Web y la forma de contactar con su titular. Su uso implica la aceptación de este aviso legal.</p>
<h2>Propiedad intelectual</h2><p>Los textos, el diseño, la marca Escala Web y la fotografía de esta web pertenecen a su titular. No se pueden copiar ni reutilizar sin su permiso.</p>
<h2>Responsabilidad</h2><p>El titular procura que la información de esta web sea correcta y esté actualizada, pero no se responsabiliza de errores puntuales ni del contenido de webs externas enlazadas, como WhatsApp.</p>
<h2>Legislación aplicable</h2><p>Este aviso legal se rige por la legislación española, en particular por la Ley 34/2002 de servicios de la sociedad de la información y de comercio electrónico (LSSI).</p>''',
'en': '''<dl class="legal-table"><dt>Owner</dt><dd>Facundo Di Lorenzo</dd><dt>Activity</dt><dd>Web design (Escala Web)</dd><dt>Location</dt><dd>Málaga, Spain</dd><dt>Email</dt><dd>dilorenzo.facundo19@gmail.com</dd><dt>Phone</dt><dd>+34 663 625 836</dd></dl>
<h2>Purpose</h2><p>This website presents Escala Web's web design services and how to contact its owner. Using it implies accepting this legal notice.</p>
<h2>Intellectual property</h2><p>The texts, design, the Escala Web brand and the photograph on this website belong to its owner. They may not be copied or reused without permission.</p>
<h2>Liability</h2><p>The owner tries to keep the information on this website accurate and up to date, but is not responsible for occasional errors or for the content of linked external websites, such as WhatsApp.</p>
<h2>Applicable law</h2><p>This legal notice is governed by Spanish law, in particular Law 34/2002 on information society services and electronic commerce (LSSI).</p>''',
'it': '''<dl class="legal-table"><dt>Titolare</dt><dd>Facundo Di Lorenzo</dd><dt>Attività</dt><dd>Progettazione di siti web (Escala Web)</dd><dt>Località</dt><dd>Málaga, Spagna</dd><dt>Email</dt><dd>dilorenzo.facundo19@gmail.com</dd><dt>Telefono</dt><dd>+34 663 625 836</dd></dl>
<h2>Oggetto</h2><p>Questo sito presenta i servizi di web design di Escala Web e come contattarne il titolare. Il suo utilizzo implica l'accettazione di queste note legali.</p>
<h2>Proprietà intellettuale</h2><p>I testi, il design, il marchio Escala Web e la fotografia di questo sito appartengono al titolare. Non possono essere copiati né riutilizzati senza il suo permesso.</p>
<h2>Responsabilità</h2><p>Il titolare cerca di mantenere le informazioni di questo sito corrette e aggiornate, ma non è responsabile di errori occasionali né del contenuto dei siti esterni collegati, come WhatsApp.</p>
<h2>Legge applicabile</h2><p>Queste note legali sono regolate dalla legge spagnola, in particolare dalla Legge 34/2002 sui servizi della società dell'informazione e il commercio elettronico (LSSI).</p>''',
}
PRIV = {
'es': '''<dl class="legal-table"><dt>Responsable</dt><dd>Facundo Di Lorenzo (Escala Web), Málaga, España</dd><dt>Contacto</dt><dd>dilorenzo.facundo19@gmail.com</dd></dl>
<h2>Qué datos se tratan</h2><p>Esta web no tiene formularios ni pide datos. Solo se tratan los datos que tú decides enviar al escribir por email o WhatsApp o al llamar: tu nombre, tus datos de contacto y la información de tu proyecto.</p>
<h2>Para qué se usan</h2><p>Para responderte, preparar tu web y mantener el contacto durante el proyecto. La base legal es tu consentimiento al escribir y la aplicación de medidas precontractuales que tú solicitas.</p>
<h2>Cuánto tiempo se guardan</h2><p>Mientras dure la relación y, después, solo el tiempo que exija la ley.</p>
<h2>Con quién se comparten</h2><p>Con nadie, salvo los proveedores del canal que elijas para escribir (por ejemplo, WhatsApp o el proveedor de correo), que tratan los datos según sus propias políticas.</p>
<h2>Cookies y almacenamiento</h2><p>Esta web no usa cookies ni herramientas de analítica. Solo guarda en tu navegador el idioma que eliges, para recordarlo en la siguiente visita. Las tipografías se sirven desde la propia web.</p>
<h2>Tus derechos</h2><p>Puedes pedir acceder a tus datos, corregirlos, borrarlos, oponerte a su uso, limitarlo o llevarlos a otro servicio escribiendo a dilorenzo.facundo19@gmail.com. Si crees que no se han respetado tus derechos, puedes reclamar ante la Agencia Española de Protección de Datos (aepd.es).</p>''',
'en': '''<dl class="legal-table"><dt>Controller</dt><dd>Facundo Di Lorenzo (Escala Web), Málaga, Spain</dd><dt>Contact</dt><dd>dilorenzo.facundo19@gmail.com</dd></dl>
<h2>What data is processed</h2><p>This website has no forms and does not ask for data. Only the data you choose to send when you write by email or WhatsApp or call is processed: your name, your contact details and the information about your project.</p>
<h2>What it is used for</h2><p>To reply to you, prepare your website and stay in touch during the project. The legal basis is your consent when you write and pre-contractual steps taken at your request.</p>
<h2>How long it is kept</h2><p>For as long as the working relationship lasts and, after that, only as long as the law requires.</p>
<h2>Who it is shared with</h2><p>Nobody, except the providers of the channel you choose to write through (for example WhatsApp or your email provider), which process data under their own policies.</p>
<h2>Cookies and storage</h2><p>This website uses no cookies or analytics tools. It only stores the language you choose in your browser, to remember it on your next visit. Fonts are served from this website itself.</p>
<h2>Your rights</h2><p>You can ask to access, correct or delete your data, object to or restrict its use, or move it to another service by writing to dilorenzo.facundo19@gmail.com. If you believe your rights have not been respected, you can complain to the Spanish Data Protection Agency (aepd.es).</p>''',
'it': '''<dl class="legal-table"><dt>Titolare del trattamento</dt><dd>Facundo Di Lorenzo (Escala Web), Málaga, Spagna</dd><dt>Contatto</dt><dd>dilorenzo.facundo19@gmail.com</dd></dl>
<h2>Quali dati vengono trattati</h2><p>Questo sito non ha moduli e non chiede dati. Vengono trattati solo i dati che decidi di inviare quando scrivi via email o WhatsApp o quando chiami: il tuo nome, i tuoi contatti e le informazioni sul tuo progetto.</p>
<h2>A cosa servono</h2><p>A risponderti, preparare il tuo sito e restare in contatto durante il progetto. La base giuridica è il tuo consenso quando scrivi e le misure precontrattuali che richiedi.</p>
<h2>Per quanto tempo vengono conservati</h2><p>Per tutta la durata del rapporto e, in seguito, solo per il tempo richiesto dalla legge.</p>
<h2>Con chi vengono condivisi</h2><p>Con nessuno, tranne i fornitori del canale che scegli per scrivere (per esempio WhatsApp o il tuo provider di posta), che trattano i dati secondo le proprie politiche.</p>
<h2>Cookie e memorizzazione</h2><p>Questo sito non usa cookie né strumenti di analisi. Salva nel tuo browser solo la lingua che scegli, per ricordarla alla visita successiva. I caratteri tipografici sono serviti dal sito stesso.</p>
<h2>I tuoi diritti</h2><p>Puoi chiedere di accedere ai tuoi dati, correggerli, cancellarli, opporti al loro uso, limitarlo o trasferirli a un altro servizio scrivendo a dilorenzo.facundo19@gmail.com. Se ritieni che i tuoi diritti non siano stati rispettati, puoi presentare reclamo all'Agenzia spagnola per la protezione dei dati (aepd.es).</p>''',
}
UPD = {'es':'Última actualización: noviembre de 2026.','en':'Last updated: November 2026.','it':'Ultimo aggiornamento: novembre 2026.'}
def legal_blocks(d):
    return ''.join(f'<div lang="{l}" data-lang-block="{l}"{"" if l=="es" else " hidden"}>{d[l]}<p class="meta">{UPD[l]}</p></div>' for l in ('es','en','it'))
page('aviso-legal.html','tLegal','Aviso legal · Escala Web','Aviso legal de Escala Web.', f'''
{page_head('legalNotice','Aviso legal','legalLead','Información sobre el titular de esta web.')}
  <div class="wrap legal"><div class="legal-body">{legal_blocks(LEGAL)}</div></div>''')
page('privacidad.html','tPrivacy','Política de privacidad · Escala Web','Política de privacidad de Escala Web.', f'''
{page_head('privacy','Política de privacidad','privacyLead','Cómo se tratan tus datos cuando visitas esta web o me escribes.')}
  <div class="wrap legal"><div class="legal-body">{legal_blocks(PRIV)}</div></div>''')

# ───────── 404 ─────────
page('404.html','t404','Página no encontrada · Escala Web','Página no encontrada.', f'''
  <div class="wrap page-head notfound">
    <h1><span class="ln"><span class="ln-in" data-i18n="nfTitle">Esta página no existe</span></span></h1>
    <p class="lead fade d1" data-i18n="nfLead">Puede que el enlace esté mal escrito o que la página ya no exista.</p>
    {scalebar(True, False)}
    <div class="actions fade d2"><a class="btn solid" href="index.html">{IC["back"]}<span data-i18n="backHome">Volver al inicio</span></a></div>
  </div>''')
print('ok')
