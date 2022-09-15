FROM python:3.9

WORKDIR /app

COPY . .

#USER 1000

RUN pip install -r requirements.txt

CMD ["gunicorn", "-b", "0.0.0.0:80", "app:app"]
