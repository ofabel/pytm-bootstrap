FROM python:3.9

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt && \
    pip install --no-cache-dir gunicorn

CMD gunicorn --bind='0.0.0.0:8080' app:app