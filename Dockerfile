FROM python:3.5
MAINTAINER nick "1033553433@qq.com"

WORKDIR /usr/local/aipoem
ADD . /usr/local/aipoem

#RUN apt-get install python3.5-dev

RUN pip install Cython
RUN pip install -r requirements.txt -i http://pypi.douban.com/simple --trusted-host pypi.douban.com

CMD python poem_server.py