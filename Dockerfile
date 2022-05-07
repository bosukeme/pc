FROM python:3.10.2-slim-buster 
#FROM python:3.7.5-slim-buster

# Environment Varaibles
ENV DISPLAY=:10

# RUN apt-get update -y
# RUN apt-get install -y chromium-chromedriver
# RUN apt-get install -y xvfb


ENV INSTALL_PATH /pricechecker
RUN mkdir -p $INSTALL_PATH

WORKDIR $INSTALL_PATH


COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD gunicorn -c "python:config.gunicorn" "pricechecker.app:create_app()"
