import fitz  # PyMuPDF
import easyocr
from PIL import Image
from pdf2image import convert_from_bytes

from app.models import extract_fields_with_llm  # Importiamo la funzione LLM

# Inizializza EasyOCR
reader = easyocr.Reader(["en", "it"])

def extract_text(file_bytes, file_type, fields):
    """Estrae il testo da un PDF o immagine e filtra i campi richiesti tramite Ollama."""
    
    extracted_text = ""

    if file_type == "pdf":
        doc = fitz.open(stream=file_bytes.read(), filetype="pdf")
        extracted_text = "\n".join([page.get_text("text") for page in doc])

        if len(extracted_text.strip()) < 20:  # Se il testo è scarso, usiamo EasyOCR
            file_bytes.seek(0)
            images = convert_from_bytes(file_bytes.read())  
            extracted_text = "\n".join(reader.readtext(img, detail=0) for img in images)

    elif file_type in ["png", "jpg", "jpeg"]:
        image = Image.open(file_bytes)
        extracted_text = "\n".join(reader.readtext(image, detail=0))

    else:
        return {"error": "Unsupported file format"}

    # Delegare l'estrazione dei campi al modello NuExtract su Ollama
    return extract_fields_with_llm(extracted_text, fields)