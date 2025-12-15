import pdfplumber

def extrair_texto_pdf(caminho_pdf):
    texto = ""

    try:
        with pdfplumber.open(caminho_pdf) as pdf:
            for pagina in pdf.pages:
                texto += pagina.extract_text() or ""
    except Exception as e:
        texto = f"Erro ao extrair texto: {str(e)}"

    return texto
