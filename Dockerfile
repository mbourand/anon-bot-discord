FROM python:3.10

COPY main.py /app/main.py
COPY requirements.txt /app/requirements.txt
COPY .env /app/.env
RUN pip install -r /app/requirements.txt

CMD ["python", "main.py"]