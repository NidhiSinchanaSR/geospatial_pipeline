FROM python:3.8-slim

WORKDIR /app

COPY ./ingest.py /app

RUN pip install requests sqlalchemy psycopg2-binary

CMD ["python", "ingest.py"]