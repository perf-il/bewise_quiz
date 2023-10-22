FROM python:3.11

RUN mkdir /code

WORKDIR /code

COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY . .

RUN chmod a+x *.sh
