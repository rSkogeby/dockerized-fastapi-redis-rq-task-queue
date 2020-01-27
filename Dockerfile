FROM python:3.7.6

WORKDIR /home/myproj

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY api.py ./
COPY worker.py ./
