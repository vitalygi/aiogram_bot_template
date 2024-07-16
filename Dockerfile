FROM python:3.12

WORKDIR /bot
COPY ./ ./

RUN rm -rf /etc/localtime
RUN ln -s /usr/share/zoneinfo/Europe/Moscow /etc/localtime
RUN echo "Europe/Moscow" > /etc/timezone

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
CMD ["python","-u", "main.py"]
