FROM tiangolo/uwsgi-nginx-flask:python3.8 as dev

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

FROM dev as final

COPY prestart.sh prestart.sh
RUN sed -i 's/\r//g' prestart.sh

COPY ./NginxDockerProxy ./

COPY nginx.conf nginx.conf