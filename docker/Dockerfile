FROM python:3.11-slim

WORKDIR /app

COPY backend/ /app

RUN apt-get update && apt-get install -y gcc curl && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir -r requirements.txt

RUN mkdir -p /app/data/chroma_store

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]