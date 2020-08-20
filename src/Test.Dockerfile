FROM python:3-slim as dev

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

FROM dev as final

COPY ./NginxDockerProxy ./NginxDockerProxy
WORKDIR /NginxDockerProxy

ENTRYPOINT python -m unittest discover -p *Test*.py