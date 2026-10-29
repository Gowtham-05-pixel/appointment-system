
FROM python:3.12-slim

WORKDIR /app

ARG APP_VERSION=v1

COPY ${APP_VERSION}/requirements.txt ./requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY ${APP_VERSION}/ ./

EXPOSE 5000

CMD ["python", "app.py"]
