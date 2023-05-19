FROM python:3.10

COPY main.py /app
COPY requirements.txt /app
COPY .env /app
RUN pip install -r /app/requirements.txt

COPY . /app

CMD ["python", "main.py"]