from fastapi import FastAPI, UploadFile, File, HTTPException, Form
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import mimetypes
import json
from app.extractor import extract_text
from app.utils import get_logger

# Configura il logging per il debugging
logger = get_logger()

app = FastAPI()

# Configura CORS per consentire richieste da frontend o altri domini
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/extract")
async def extract_info(
    file: UploadFile = File(...), 
    fields: str = Form(...)  # Riceve fields come stringa
):
    """Endpoint per estrarre informazioni da un PDF o immagine."""
    try:
        # Controlla se è già un dizionario (potrebbe accadere se FastAPI o la libreria sottostante ha già fatto il parsing)
        if isinstance(fields, dict):
            fields_dict = fields
        else:
            # Altrimenti, prova a parsare la stringa JSON
            fields_dict = json.loads(fields)
        
        # Verifica che sia un dizionario
        if not isinstance(fields_dict, dict):
            raise ValueError("Il campo 'fields' deve essere un dizionario JSON valido")
            
    except (json.JSONDecodeError, ValueError) as e:
        # Aggiungi log di debug
        logger.error(f"Errore nel parsing JSON: {e}")
        logger.debug(f"Tipo di 'fields' ricevuto: {type(fields)}")
        logger.debug(f"Contenuto di 'fields': {fields}")
        raise HTTPException(status_code=400, detail=str(e))

    file_type = mimetypes.guess_extension(file.content_type).lstrip(".")
    extracted_data = extract_text(file.file, file_type, fields_dict)
    return {"extracted_data": extracted_data}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)