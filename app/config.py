import os

OLLAMA_URL = os.getenv("OLLAMA_URL", "http://localhost:11434")  # Default Ollama
MODEL_NAME = os.getenv("OLLAMA_MODEL", "iodose/nuextract-v1.5")  # Default modello
