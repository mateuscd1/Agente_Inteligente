from core.ia.groq_client import get_groq_client

MODEL_NAME = "llama-3.1-8b-instant"

def generate_answer(pergunta, contexto):
    client = get_groq_client()

    messages = [
        {
            "role": "system",
            "content": (
                "Você é um assistente acadêmico da PPG/UEMA. "
                "Responda de forma clara, objetiva e baseada apenas no contexto fornecido."
            )
        },
        {
            "role": "user",
            "content": f"Contexto:\n{contexto}\n\nPergunta:\n{pergunta}"
        }
    ]

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=messages,
        temperature=0.2,
        max_tokens=600,
    )

    return response.choices[0].message.content.strip()
