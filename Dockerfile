FROM python:3.7-slim

WORKDIR /src

COPY main.py requirements.txt /src/

RUN pip install -r requirements.txt

CMD ["python","-u","main.py"]