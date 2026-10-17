(function(){
  // theme toggle
  document.querySelectorAll('.theme-btn').forEach(function(btn){
    btn.addEventListener('click',function(){
      var cur=document.documentElement.dataset.theme==='dark'?'light':'dark';
      document.documentElement.dataset.theme=cur;
      try{localStorage.setItem('tr-theme',cur)}catch(e){}
    });
  });
  // nav background on scroll
  var nav=document.querySelector('nav');
  function onScroll(){nav.classList.toggle('scrolled',window.scrollY>40)}
  window.addEventListener('scroll',onScroll,{passive:true});onScroll();
  // copy link
  document.querySelectorAll('.copy-btn').forEach(function(btn){
    btn.addEventListener('click',function(){
      var code=btn.closest('.copy-block').querySelector('code').textContent.trim();
      var done=function(){
        var label=btn.querySelector('span');
        btn.classList.add('done');
        btn.innerHTML='<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M4 12.5 9.5 18 20 6.5"/></svg><span>'+btn.dataset.done+'</span>';
        setTimeout(function(){btn.classList.remove('done');btn.innerHTML='<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="9" y="9" width="12" height="12" rx="2.5"/><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/></svg><span>'+btn.dataset.label+'</span>'},2200);
      };
      if(navigator.clipboard&&navigator.clipboard.writeText){
        navigator.clipboard.writeText(code).then(done).catch(function(){fallback()});
      }else{fallback()}
      function fallback(){
        var ta=document.createElement('textarea');ta.value=code;document.body.appendChild(ta);ta.select();
        try{document.execCommand('copy')}catch(e){}document.body.removeChild(ta);done();
      }
    });
  });
})();
