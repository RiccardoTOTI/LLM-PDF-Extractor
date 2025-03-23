# 📄 LLM-PDF-Parser

**LLM-PDF-Parser** is a FastAPI-based application that extracts text from **PDFs and images** and uses **Ollama's LLM** to extract specific fields based on a given JSON template. 🚀

## ✨ Features
- 📝 **Extract text** from PDFs and images (JPG, PNG, JPEG) using **PyMuPDF** and **EasyOCR**.
- 🤖 **Leverage AI** to extract structured data based on a provided JSON template.
- ⚡ **FastAPI backend** for quick and easy integration.
- 🔥 **Supports OCR** when text extraction from PDFs is insufficient.
- 🔄 **Cross-Origin Resource Sharing (CORS) enabled** for flexible frontend integration.

## 🚀 Installation & Setup

### 1️⃣ Clone the Repository
```sh
git clone https://github.com/RiccardoTOTI/LLM-PDF-Extractor.git
cd LLM-PDF-Parser
```

### 2️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```

### 3️⃣ Set Up Environment Variables
Create a `.env` file and configure the following variables (or set them in your environment):
```sh
OLLAMA_URL=http://localhost:11434
OLLAMA_MODEL=iodose/nuextract-v1.5
```

### 4️⃣ Run the Application
```sh
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```
## 🐳 Docker Support
You can also run the application using **Docker**.

### 🏗 Build and Run with Docker
1. **Build the Docker image:**
   ```sh
   docker build -t llm-pdf-parser .
   ```
2. **Run the container:**
   ```sh
   docker run -p 8000:8000 llm-pdf-parser
   ```

### 🔄 Using Docker Compose
You can use **Docker Compose** to spin up both the application and Ollama:

1. **Run the services:**
   ```sh
   docker-compose up -d
   ```
2. **Download the model using the script inside `tools` directory in the Ollama Container:**
   ```sh
   docker exec -it ollama .tools/download_model.sh iodose/nuextract-v1.5
   ```

## 🔥 API Usage
### 📥 Upload a File & Extract Data
**Endpoint:** `POST /extract`

**Request:**
```sh
curl -X 'POST' \
  'http://localhost:8000/extract' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'file=@yourfile.pdf' \
  -F 'fields={"Patient":{"First Name":"","Last Name":"","Tax Code":"","Doctor":[]}}
'
```

**Response Example:**
```json
{
  "extracted_data": {
    "name": "John Doe",
    "email": "johndoe@example.com",
    "date": "2024-03-23"
  }
}
```

## 🏗 How It Works
1. **Uploads a PDF or Image** via FastAPI.
2. **Extracts text** using PyMuPDF or EasyOCR (for scanned documents/images).
3. **Sends extracted text to Ollama's LLM**, which structures it based on the provided JSON template.
4. **Returns extracted structured data** as a JSON response. ✅

## 🛠 Technologies Used
- **Python** 🐍
- **FastAPI** ⚡
- **PyMuPDF** 📄
- **EasyOCR** 🔍
- **Ollama LLM** 🤖
- **Uvicorn** 🚀

## 🏆 Contributing
Contributions are welcome! Feel free to submit issues or open a pull request. 😊

## 📜 License
This project is licensed under the MIT License.

---

💡 **Have suggestions or need help?** Open an issue or reach out! 🚀

