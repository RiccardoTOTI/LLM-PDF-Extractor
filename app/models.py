import json
import logging
import requests
from app.config import OLLAMA_URL, MODEL_NAME
from app.utils import get_logger

# Configura il logging per il debugging
logger = get_logger()

def extract_fields_with_llm(text, template):
    """Invia una richiesta diretta a Ollama per estrarre i campi richiesti basandosi su un template JSON valido."""

    # Assicuriamoci che il template sia un JSON formattato correttamente
    if isinstance(template, dict):
        # Se è già un dizionario, lo convertiamo direttamente in JSON formattato
        template_json = json.dumps(template, indent=4)
    else:
        # Se è una stringa, proviamo a fare il parsing
        try:
            template_json = json.dumps(json.loads(template), indent=4)
        except json.JSONDecodeError:
            logger.error("Errore: Il template JSON fornito non è valido.")
            return {"error": "Invalid JSON template provided."}
    # Costruisce il prompt secondo le specifiche di NuExtract

    prompt = f"<|input|>\n### Template:\n{template_json}\n### Text:\n{text}\n\n<|output|>"
    
    # Logga il prompt per debugging
    logger.debug(f"=== PROMPT ===\n{prompt}\n")

    # Costruisce il payload della richiesta
    payload = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": False,
        "format": "json",
        "options": {
            "max_tokens": 4000
        }
    }

    try:
        # Logga l'URL della richiesta
        logger.debug(f"URL della richiesta: {OLLAMA_URL}/api/generate")

        # Invio della richiesta POST a Ollama
        response = requests.post(f"{OLLAMA_URL}/api/generate", json=payload)

        # Controlliamo se la richiesta ha avuto successo
        if response.status_code == 200:
            response_data = response.json()
            extracted_text = response_data.get("response", "").strip()
            logger.debug(f"=== Extracted Text ===\n{extracted_text}\n")

            # Prova a convertire l'output in JSON
            try:
                extracted_json = json.loads(extracted_text)
                return extracted_json
            except json.JSONDecodeError:
                logger.error(f"Errore nel parsing della risposta JSON: {extracted_text}")
                return {"error": f"Invalid JSON response from model: {extracted_text}"}

        return {"error": f"Failed to get response from Ollama: {response.text}"}

    except Exception as e:
        logger.error(f"Errore nella richiesta a Ollama: {str(e)}")
        return {"error": f"Request to Ollama failed: {str(e)}"}
