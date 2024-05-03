FROM python:3.9

WORKDIR /code

# getting dependencies from main.py only
COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY . /code

# https://medium.com/geekculture/how-to-dockerize-your-flask-application-2d0487ecefb8
EXPOSE 5000
ENV FLASK_APP=main.py

CMD ["flask", "run", "--host", "0.0.0.0"]