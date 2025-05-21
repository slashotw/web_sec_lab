FROM tiangolo/uwsgi-nginx-flask:python3.10

COPY . /app

RUN pip3 install -r requirements.txt

CMD python3 main.py