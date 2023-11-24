# https://hub.docker.com/_/python
FROM python:3.11

ENV PYTHONUNBUFFERED True

WORKDIR /app

COPY . ./

RUN pip install --no-cache-dir -r requirements.txt

CMD ["uvicorn", "src.app:app", "--host", "0.0.0.0", "--port", "8080"]