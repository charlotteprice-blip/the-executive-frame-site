/* Executive Frame assessment funnels — progress, feedback, and completion gate */
(function(){
  var qs = Array.prototype.slice.call(document.querySelectorAll('.q'));
  if(!qs.length) return;
  var total = qs.length;
  // progress bar + counter
  var bar = document.createElement('div'); bar.className='prog'; bar.innerHTML='<div class="pfill"></div>';
  document.body.appendChild(bar);
  var count = document.createElement('div'); count.className='pcount'; count.setAttribute('aria-live','polite');
  document.body.appendChild(count);
  var fill = bar.querySelector('.pfill');
  function answered(){ return qs.filter(function(q){return q.querySelector('input:checked');}).length; }
  function update(){
    var a = answered();
    fill.style.width = (a/total*100)+'%';
    count.textContent = a+' / '+total+' answered';
    qs.forEach(function(q){
      var done = !!q.querySelector('input:checked');
      q.classList.toggle('done', done);
      if(done) q.classList.remove('missing');
    });
  }
  document.addEventListener('change', function(e){ if(e.target && e.target.type==='radio') update(); });
  update();
  // completion gate: highlight unanswered instead of scoring incomplete
  var btn = document.querySelector('.btnrow button');
  if(btn && btn.getAttribute('onclick')){
    btn.removeAttribute('onclick');
    var msg = document.createElement('p'); msg.className='gate-msg';
    btn.parentNode.appendChild(msg);
    btn.addEventListener('click', function(){
      var missing = qs.filter(function(q){return !q.querySelector('input:checked');});
      if(missing.length){
        qs.forEach(function(q){ q.classList.remove('missing'); });
        missing.forEach(function(q){ q.classList.add('missing'); });
        msg.textContent = missing.length+' statement'+(missing.length>1?'s':'')+' still to answer \u2014 each is outlined above. Your read works best when every statement is answered.';
        msg.classList.add('show');
        missing[0].scrollIntoView({behavior:'smooth', block:'center'});
      } else {
        msg.classList.remove('show');
        if(typeof window.score==='function') window.score();
      }
    });
  }
})();
