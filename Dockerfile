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

RUN wget http://www.cl.ecei.tohoku.ac.jp/~m-suzuki/jawiki_vector/data/20170201.tar.bz2
RUN tar jxvf 20170201.tar.bz2
RUN rm -rf /entity_vector/entity_vector.model.txt

RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN python -m pip install gensim