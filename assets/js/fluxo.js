/* Consultoria Fluxo — interações e animações do site v5 [versao Claude] */
(function(){
  window.__fx=1;
  var doc=document.documentElement;
  var reduce=window.matchMedia&&matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* Cabeçalho: compacta ao rolar + barra de progresso de leitura + WhatsApp aparece depois do topo */
  var top=document.querySelector('.top'),bar=document.querySelector('.progress'),wa=document.querySelector('.wa-float');
  var ticking=false;
  function onScroll(){
    var y=window.scrollY||0,h=doc.scrollHeight-innerHeight;
    if(top)top.classList.toggle('scrolled',y>8);
    if(bar)bar.style.transform='scaleX('+(h>0?Math.min(y/h,1):0)+')';
    if(wa)wa.classList.toggle('show',y>innerHeight*.6);
    if(!reduce)document.querySelectorAll('[data-parallax]').forEach(function(el){
      var r=el.parentNode.getBoundingClientRect();
      if(r.bottom<0||r.top>innerHeight)return;
      el.style.transform='translate3d(0,'+(-r.top*(+el.dataset.parallax||.12)).toFixed(1)+'px,0)';
    });
    ticking=false;
  }
  addEventListener('scroll',function(){if(!ticking){ticking=true;requestAnimationFrame(onScroll)}},{passive:true});
  onScroll();

  /* Menu mobile */
  var burger=document.querySelector('.burger');
  if(burger)burger.addEventListener('click',function(){
    var open=doc.classList.toggle('menu-open');
    burger.setAttribute('aria-expanded',open);
  });
  document.querySelectorAll('.mnav a').forEach(function(a){a.addEventListener('click',function(){doc.classList.remove('menu-open');if(burger)burger.setAttribute('aria-expanded','false')})});

  if(reduce||!('IntersectionObserver' in window)){
    document.querySelectorAll('[data-count]').forEach(function(n){n.textContent=n.dataset.count});
    return;
  }

  /* Títulos: divide em palavras para a revelação com máscara */
  document.querySelectorAll('[data-split]').forEach(function(el){
    var i=0;
    (function walk(node){
      Array.prototype.slice.call(node.childNodes).forEach(function(ch){
        if(ch.nodeType===3){
          var frag=document.createDocumentFragment();
          ch.textContent.split(/(\s+)/).forEach(function(part){
            if(!part)return;
            if(/^\s+$/.test(part)){frag.appendChild(document.createTextNode(part));return}
            var w=document.createElement('span');w.className='w';
            var s=document.createElement('span');s.textContent=part;s.style.setProperty('--i',i++);
            w.appendChild(s);frag.appendChild(w);
          });
          node.replaceChild(frag,ch);
        }else if(ch.nodeType===1){walk(ch)}
      });
    })(el);
  });

  /* Comprimento real do contorno do X (para desenhar a linha) */
  document.querySelectorAll('.xmark .a').forEach(function(p){
    try{p.style.setProperty('--len',Math.ceil(p.getTotalLength()))}catch(e){}
  });

  /* Atraso em cascata para filhos de [data-stagger] */
  document.querySelectorAll('[data-stagger]').forEach(function(g){
    Array.prototype.forEach.call(g.querySelectorAll('[data-reveal]'),function(el,k){el.style.setProperty('--d',k)});
  });

  function countUp(n){
    var end=+n.dataset.count,t0=null;
    function step(t){if(!t0)t0=t;var p=Math.min((t-t0)/1600,1);n.textContent=Math.round(end*(1-Math.pow(1-p,4)));if(p<1)requestAnimationFrame(step)}
    n.textContent='0';requestAnimationFrame(step);
  }

  var io=new IntersectionObserver(function(entries){
    entries.forEach(function(en){
      if(!en.isIntersecting)return;
      var el=en.target;io.unobserve(el);
      el.classList.add('in');
      if(el.__wipe)el.__wipe.classList.add('in');
      el.querySelectorAll('[data-count]').forEach(countUp);
    });
  },{rootMargin:'0px 0px -10% 0px',threshold:.15});
  document.querySelectorAll('[data-reveal],[data-split],.xmark,.stats,.phases').forEach(function(e){io.observe(e)});
  /* clip-path zera a área visível do alvo; observamos o elemento pai */
  document.querySelectorAll('[data-wipe]').forEach(function(e){e.parentNode.__wipe=e;io.observe(e.parentNode)});

  /* Transição suave ao trocar de página dentro do site */
  document.querySelectorAll('a[href]').forEach(function(a){
    var href=a.getAttribute('href');
    if(!href||href.charAt(0)==='#'||a.target==='_blank'||/^(mailto:|tel:|https?:)/.test(href))return;
    a.addEventListener('click',function(e){
      if(e.metaKey||e.ctrlKey||e.shiftKey||e.button!==0)return;
      e.preventDefault();doc.classList.add('leaving');
      setTimeout(function(){location.href=a.href},220);
    });
  });
  addEventListener('pageshow',function(e){if(e.persisted)doc.classList.remove('leaving')});
})();
