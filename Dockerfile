FROM python:3

ENV PYTHONUNBUFFERED=1

ENV BASE_DIR=/sprint-1

WORKDIR $BASE_DIR
COPY requirements.txt $BASE_DIR/

RUN pip install -r requirements.txt
COPY . $BASE_DIR/