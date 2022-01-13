FROM python:3.8
WORKDIR /app
EXPOSE 80

COPY requirements.txt .
RUN apt update
RUN apt-get update && apt-get upgrade -y   
RUN apt-get install -y libgl1-mesa-dev             
RUN pip install --upgrade pip
RUN pip install -r requirements.txt