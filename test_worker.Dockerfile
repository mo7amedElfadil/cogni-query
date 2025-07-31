FROM python:3.9-slim

WORKDIR /app

COPY test_worker.py .
COPY worker/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt
RUN pip install pymongo

CMD ["python", "test_worker.py"]