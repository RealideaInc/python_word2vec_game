FROM python:3
USER root

RUN apt-get update
RUN apt-get -y install locales && \
    localedef -f UTF-8 -i ja_JP ja_JP.UTF-8
ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
ENV LC_ALL ja_JP.UTF-8
ENV TZ JST-9
ENV TERM xterm

RUN apt-get install -y vim less

RUN wget -P /root https://github.com/singletongue/WikiEntVec/releases/download/20190520/jawiki.entity_vectors.100d.txt.bz2
RUN bunzip2 /root/jawiki.entity_vectors.100d.txt.bz2

RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN python -m pip install gensim

COPY save.py /root

RUN python /root/save.py

RUN rm /root/jawiki.entity_vectors.100d.txt