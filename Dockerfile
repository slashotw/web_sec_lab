FROM tiangolo/uwsgi-nginx-flask:python3.10
COPY src /app
RUN chmod 444 /app/flag

# 創建 /file 目錄
RUN mkdir -p /file

# 安裝 unzip 工具
RUN apt-get update && apt-get install -y unzip


RUN unzip  /app/file/git.zip -d /app/file

RUN pip3 install -r requirements.txt


CMD python3 main.py