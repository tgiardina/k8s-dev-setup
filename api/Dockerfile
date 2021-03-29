FROM python:3.6-alpine

WORKDIR /app/src

COPY ./requirements.txt ./requirements.txt

RUN pip install -r requirements.txt

COPY . .

CMD ["python",  "api.py"]