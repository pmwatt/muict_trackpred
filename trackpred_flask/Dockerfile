FROM python:3.9

WORKDIR /code

# getting dependencies from main.py only
COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY . /code

CMD ["flask", "--app", "main", "run"]