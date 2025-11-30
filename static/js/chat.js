// simples frontend para demo de chat — faz POST para /api/chat/ (a implementar)
// se endpoint não existir, o JS exibirá uma resposta simulada

document.addEventListener('DOMContentLoaded', function(){
  const chatWindow = document.getElementById('chat-window');
  const chatForm = document.getElementById('chat-form');
  const chatInput = document.getElementById('chat-input');
  const sendBtn = document.getElementById('chat-send');

  function appendMessage(text, cls='system'){
    const d = document.createElement('div');
    d.className = 'msg ' + cls;
    d.textContent = text;
    chatWindow.appendChild(d);
    chatWindow.scrollTop = chatWindow.scrollHeight;
  }

  chatForm.addEventListener('submit', async function(e){
    e.preventDefault();
    const text = chatInput.value.trim();
    if(!text) return;
    appendMessage(text, 'user');
    chatInput.value = '';
    sendBtn.disabled = true;

    try {
      // tenta chamar endpoint real
      const resp = await fetch('/api/chat/', {
        method:'POST',
        headers:{ 'Content-Type':'application/json', 'X-CSRFToken': getCookie('csrftoken') },
        body: JSON.stringify({ message: text })
      });
      if(resp.ok){
        const data = await resp.json();
        appendMessage(data.reply || 'Sem resposta', 'bot');
      } else {
        // se o endpoint não existir, usa fallback
        appendMessage('Desculpe — serviço de chat não disponível (ainda).', 'bot');
      }
    } catch(err){
      // fallback offline
      appendMessage('Resposta simulada: 🤖 Ainda não há backend — implemente /api/chat/ para receber perguntas.', 'bot');
    } finally {
      sendBtn.disabled = false;
    }
  });

  // pega csrf cookie (para POSTs no Django)
  function getCookie(name) {
    let v = document.cookie.match('(^|;) ?' + name + '=([^;]*)(;|$)');
    return v ? v[2] : null;
  }
});
