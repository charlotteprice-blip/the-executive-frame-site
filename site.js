/* Executive Frame — interaction layer (progressive enhancement) */
(function(){
  var nav=document.querySelector('.nav');
  function onScroll(){ if(nav) nav.classList.toggle('scrolled', window.scrollY>18); }
  onScroll(); window.addEventListener('scroll',onScroll,{passive:true});

  /* Section reveal — skipped entirely for reduced-motion users */
  var reduce=window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var secs=document.querySelectorAll('main section');
  if(reduce || !('IntersectionObserver' in window)){ secs.forEach(function(s){s.classList.add('in');}); }
  else{
    var io=new IntersectionObserver(function(entries){
      entries.forEach(function(e){ if(e.isIntersecting){ e.target.classList.add('in'); io.unobserve(e.target); } });
    },{threshold:0.12, rootMargin:'0px 0px -7% 0px'});
    secs.forEach(function(s,i){ s.classList.add('reveal'); s.style.transitionDelay=(Math.min(i,2)*0.06)+'s'; io.observe(s); });
  }

  /* Mobile menu: tap to open, Escape or outside tap to close */
  var btn=document.querySelector('.menu-btn'), links=document.querySelector('.nav .links');
  function closeMenu(){ if(!btn) return; btn.setAttribute('aria-expanded','false'); document.documentElement.classList.remove('nav-open'); }
  if(btn && links){
    btn.addEventListener('click',function(){
      var open=btn.getAttribute('aria-expanded')==='true';
      btn.setAttribute('aria-expanded', open?'false':'true');
      document.documentElement.classList.toggle('nav-open', !open);
    });
  }
  document.addEventListener('keydown',function(e){ if(e.key==='Escape'){ closeMenu(); closeDD(); } });
  document.addEventListener('click',function(e){ if(nav && !nav.contains(e.target)){ closeMenu(); closeDD(); } });

  /* Programmes dropdown: click/keyboard toggle (hover still works on desktop) */
  var dd=document.querySelector('.nav .dd'), ddbtn=document.querySelector('.nav .ddbtn');
  function closeDD(){ if(dd){ dd.classList.remove('open'); } if(ddbtn){ ddbtn.setAttribute('aria-expanded','false'); } }
  if(dd && ddbtn){
    ddbtn.addEventListener('click',function(e){
      e.preventDefault();
      var open=dd.classList.toggle('open');
      ddbtn.setAttribute('aria-expanded', open?'true':'false');
    });
  }
})();
