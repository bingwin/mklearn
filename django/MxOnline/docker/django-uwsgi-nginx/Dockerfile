FROM ubuntu:16.04

MAINTAINER Dockerfiles


# 安装git、python、nginx、supervisor等，并清理缓存

RUN apt-get update && \
    apt-get upgrade -y && \ 
    apt-get install -y \
	git \
	python \
	python-dev \
	python-setuptools \
	python-pip \
	nginx \
	supervisor \
	libmysqlclient-dev && \
        python -m pip install --upgrade -i https://pypi.doubanio.com/simple/ pip setuptools && \
  	rm -rf /var/lib/apt/lists/*

RUN pip install -i https://pypi.doubanio.com/simple/ uwsgi
 
 
# 环境变量

ENV MYSQL_DATABASE_NAME lighten
ENV EMAIL_HOST_USER myemail@email.com
ENV EMAIL_HOST_PASSWORD my-secret-password


# nginx、supervisor配置

RUN echo "daemon off;" >> /etc/nginx/nginx.conf
COPY nginx-app.conf /etc/nginx/sites-available/default
COPY supervisor-app.conf /etc/supervisor/conf.d/


# 安装项目所需python第三方库

COPY requirements.txt /home/docker/code/Lighten/
RUN pip install -i https://pypi.doubanio.com/simple/ -r /home/docker/code/Lighten/requirements.txt


# uwsgi.ini 及 uwsgi_params

COPY . /home/docker/code/


EXPOSE 80
CMD ["supervisord", "-n"]
