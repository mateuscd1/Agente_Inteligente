from core.models import Documento
from core.ia.chunking import chunk_text


MAX_CHUNKS_TOTAL = 8   # controle de tokens (importantíssimo)
MAX_CHARS_PER_CHUNK = 1200


def build_context(pergunta: str) -> str:
    """
    Monta o contexto usando TODOS os documentos disponíveis,
    com limite de segurança para não estourar tokens.
    """

    documentos = Documento.objects.exclude(texto_extraido__isnull=True)\
                                  .exclude(texto_extraido="")

    if not documentos.exists():
        return ""

    context_chunks = []

    for doc in documentos:
        chunks = chunk_text(
            doc.texto_extraido,
            max_chars=MAX_CHARS_PER_CHUNK
        )

        for chunk in chunks:
            context_chunks.append(
                f"[Documento: {doc.titulo}]\n{chunk}"
            )

            if len(context_chunks) >= MAX_CHUNKS_TOTAL:
                break

        if len(context_chunks) >= MAX_CHUNKS_TOTAL:
            break

    return "\n\n---\n\n".join(context_chunks)
