FROM ubuntu:bionic
LABEL maintainer="issamattos.david@gmail.com"
ENV LANG C.UTF-8

COPY . /hypercomp
WORKDIR hypercomp

RUN ./setup.sh .
ENTRYPOINT ["main.py"]