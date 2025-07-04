FROM python:3.13-slim

RUN apt-get update && apt-get install -y make gcc && rm -rf /var/lib/apt/lists/*

RUN adduser --disabled-password --gecos '' devuser

WORKDIR /home/devuser/app

COPY backend/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .


EXPOSE 8080

CMD ["uvicorn", "pages.api.main:app", "--host", "0.0.0.0", "--port", "8080"]