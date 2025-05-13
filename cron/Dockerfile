FROM python:3.12

RUN pip install requests sqlalchemy psycopg2 apscheduler

WORKDIR /cron

COPY clashCurl.py /cron

CMD ["python", "clashCurl.py"]
