/* Executive Frame — interaction layer (progressive enhancement) */
(function(){
  var nav=document.querySelector('.nav');
  function onScroll(){ if(nav) nav.classList.toggle('scrolled', window.scrollY>18); }
  onScroll(); window.addEventListener('scroll',onScroll,{passive:true});

  var secs=document.querySelectorAll('main section');
  if(!('IntersectionObserver' in window)){ secs.forEach(function(s){s.classList.add('in');}); return; }
  var io=new IntersectionObserver(function(entries){
    entries.forEach(function(e){ if(e.isIntersecting){ e.target.classList.add('in'); io.unobserve(e.target); } });
  },{threshold:0.12, rootMargin:'0px 0px -7% 0px'});
  secs.forEach(function(s,i){ s.classList.add('reveal'); s.style.transitionDelay=(Math.min(i,2)*0.06)+'s'; io.observe(s); });
})();
