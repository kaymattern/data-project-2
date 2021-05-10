FROM python:3.8
COPY ./app /
COPY requirements.txt requirements.txt
RUN pip install --upgrade pip && pip install -r requirements.txt
EXPOSE 8080
CMD [ "python", "./main.py"]