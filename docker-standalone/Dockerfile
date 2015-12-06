FROM ipython/scipystack

MAINTAINER Edward J Kim <edward.junhyung.kim@gmail.com>

RUN apt-get update && \

    apt-get install -y -q \
    vim \
    wget \
    # fonts needed in seaborn 
    ttf-liberation \ 
    ttf-bitstream-vera \
    python3-bs4 \
    python3-tables 

ADD notebook.sh /

RUN chown 1000:1000 /notebook.sh && \
    chmod u+x /notebook.sh && \
    useradd -m -u 1000 -s /bin/bash data_scientist

USER data_scientist
ENV HOME /home/data_scientist
ENV SHELL /bin/bash
ENV USER data_scientist

WORKDIR /home/data_scientist/

EXPOSE 8888

# set colors for terminal prompt
RUN echo 'export PS1="\e[1;34m\u@\h:\w$ \e[0m"' >> /home/data_scientist/.bashrc

CMD ["/notebook.sh"]
