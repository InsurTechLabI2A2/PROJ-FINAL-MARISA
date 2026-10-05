# Dockerfile - D&O VERDICT v2 - I2A2 InsurMinds - Reprodutibilidade banca
FROM python:3.11.9-slim
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1 PIP_NO_CACHE_DIR=1 PIP_DISABLE_PIP_VERSION_CHECK=1 DEBIAN_FRONTEND=noninteractive
WORKDIR /app
RUN apt-get update && apt-get install -y --no-install-recommends tesseract-ocr tesseract-ocr-por tesseract-ocr-eng libgl1 libglib2.0-0 poppler-utils build-essential curl git && rm -rf /var/lib/apt/lists/*
COPY requirements-freeze.txt requirements.txt ./
RUN pip install --upgrade pip==24.2 && pip install -r requirements-freeze.txt
RUN python -m spacy download pt_core_news_sm && python -m spacy download en_core_web_sm
COPY . .
RUN mkdir -p rag_data/chroma rag_data/pdfs_susep models Projeto_Final_Artefatos/evaluation Projeto_Final_Artefatos/harness_traces
EXPOSE 8501
HEALTHCHECK --interval=30s --timeout=10s --start-period=20s --retries=3 CMD curl --fail http://localhost:8501/_stcore/health || exit 1
CMD ["streamlit", "run", "app/streamlit_app.py", "--server.port=8501", "--server.address=0.0.0.0", "--server.headless=true"]
