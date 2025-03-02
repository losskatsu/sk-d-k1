FROM python:3.11.9

WORKDIR /app

COPY . .
RUN pip install --no-cache-dir -r requirements.txt

CMD ["streamlit", "run", "front.py", "--server.port=8501", "--server.address=0.0.0.0", "--server.enableCORS=false","--server.enableWebsocketCompression=false", "--server.enableXsrfProtection=false"]

EXPOSE 8501
