FROM python:3

RUN mkdir /app
WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

RUN mkdir /app/src
WORKDIR /app/src
ADD src/ .

CMD [ "python", "./main.py" ]