async function loadExchanges(){
  const ex = await fetch('/api/exchanges').then(r=>r.json());
  const el = document.getElementById('exList');
  el.innerHTML = '';
  for(const [net, list] of Object.entries(ex)){
    let div = document.createElement('div');
    div.innerHTML = `<strong>${net}:</strong> ${list.join(', ')}`;
    el.appendChild(div);
  }
}

function openEditor(){ window.location.href = '/editor.html'; }
function openVisual(){ window.location.href = '/visual.html'; }

function testBuy(){ fetch('/api/strategies'); alert('Test BUY (frontend stub)'); }
function testSell(){ alert('Test SELL (frontend stub)'); }

function changeLang(lang){
  window.location = `/?lang=${lang}`;
}

loadExchanges();
