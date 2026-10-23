FROM python:3.12-slim

WORKDIR /app

COPY nebenkosten.py .

ENTRYPOINT ["python", "nebenkosten.py"]