#docker build -t fsedano/python-backend:3 .
FROM ubuntu:18.04
RUN apt-get update &&  apt-get install -y python3-pip
RUN apt-get install -y curl inetutils-ping net-tools
WORKDIR /app
COPY requirements.txt /app/
RUN pip3 install -r /app/requirements.txt
COPY backend.py /app/
CMD ["python3", "/app/backend.py"]
EXPOSE 5000
#CMD ["/bin/bash", "-c", "sleep 9999999"]
