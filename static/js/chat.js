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
      const resp = await fetch('/chat/api/', {
        method:'POST',
        headers:{ 
          'Content-Type':'application/json',
          'X-CSRFToken': getCookie('csrftoken')
        },
        body: JSON.stringify({ message: text })
      });

      if(resp.ok){
        const data = await resp.json();
        appendMessage(data.response || 'Sem resposta', 'bot');
      } else {
        appendMessage('Erro ao acessar o servidor.', 'bot');
      }
    } catch(err){
      appendMessage('Backend não respondeu.', 'bot');
    } finally {
      sendBtn.disabled = false;
    }
  });

  function getCookie(name) {
    let v = document.cookie.match('(^|;) ?' + name + '=([^;]*)(;|$)');
    return v ? v[2] : null;
  }
});
