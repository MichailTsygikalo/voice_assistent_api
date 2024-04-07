FROM python:3.9
WORKDIR /proj
COPY ./requirements.txt requirements.txt 
RUN python3.9 -m pip install -r requirements.txt
COPY ./ ./