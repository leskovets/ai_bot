FROM python:3.12.1

RUN apt-get -y update
RUN apt-get -y upgrade
RUN apt-get install -y ffmpeg

COPY requirements.txt ./app/

WORKDIR /app

RUN python -m pip install -r requirements.txt

COPY . /app/

ENTRYPOINT ["python", "main.py"]

RUN alembic upgrade head
