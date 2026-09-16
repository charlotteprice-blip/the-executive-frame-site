/* arm library search + filter */
(function(){
  var lib=document.getElementById('library');if(!lib)return;
  var cards=Array.prototype.slice.call(lib.querySelectorAll('.lb-card'));
  var input=lib.querySelector('.lb-search input');
  var pills=Array.prototype.slice.call(lib.querySelectorAll('.lb-pill'));
  var empty=lib.querySelector('.lb-empty');
  var type='all';
  function apply(){
    var q=(input&&input.value||'').toLowerCase().trim(),n=0;
    cards.forEach(function(c){
      var okT=type==='all'||(c.dataset.type||'').split(' ').indexOf(type)>-1;
      var okQ=!q||(c.textContent+' '+(c.dataset.search||'')).toLowerCase().indexOf(q)>-1;
      var show=okT&&okQ;c.style.display=show?'':'none';if(show)n++;
    });
    if(empty)empty.classList.toggle('show',n===0);
  }
  if(input)input.addEventListener('input',apply);
  pills.forEach(function(p){p.addEventListener('click',function(){
    pills.forEach(function(x){x.classList.remove('on')});p.classList.add('on');
    type=p.dataset.type;apply();});});
})();
