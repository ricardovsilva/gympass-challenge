FROM python:3.7-alpine

COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
RUN python -m pytest
CMD python main.py race-log.txt