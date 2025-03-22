FROM python:3.10-slim

# Imposta la directory di lavoro
WORKDIR /app

# Copia i file necessari
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia il resto dell'applicazione
COPY app/ app/

# Espone la porta su cui gira l'app
EXPOSE 8000

# Imposta le variabili d'ambiente con valori di default
ENV OLLAMA_HOST="http://localhost:11434" \
    OLLAMA_MODEL="iodose/nuextract-v1.5"

# Comando di avvio
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
