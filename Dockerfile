FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1
WORKDIR /app

 RUN python -m venv /opt/venv

ENV PATH="/opt/venv/bin:$PATH"

COPY requirements.txt ./

RUN python -m pip install --upgrade pip setuptools wheel && \
    python -m pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python3", "main.py"]
