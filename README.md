# LLM-PDF-Extractor
LLM-PDF-Extractor is an AI-powered tool that extracts and analyzes text from PDFs and images using Large Language Models (LLMs). It combines OCR technology with advanced NLP capabilities to provide accurate and structured information extraction.


curl --location 'http://127.0.0.1:8000/extract' \
--form 'file=@"sample.pdf"' \
--form 'fields="{\"Paziente\":{\"Nome\":\"\",\"Cognome\":\"\",\"Codice Fiscale\":\"\",\"Medico\":[],\"NATO A\":\"\",\"IL\":\"\"}}"'
