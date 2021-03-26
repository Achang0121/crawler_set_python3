FROM python:3.9
LABEL maintainer="cjm995321455@gmail.com"
ADD . /JavBus
WORKDIR /JavBus
RUN pip install -r requirements.txt -i https://pypi.douban.com/simple
CMD ["shell", "run.sh"]