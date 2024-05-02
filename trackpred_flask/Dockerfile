FROM python:3.9

WORKDIR /code

# getting dependencies from main.py only
COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY . /code

# Expose $PORT on container.
# We use a varibale here as the port is something that can differ on the environment.
# https://www.milanwittpohl.com/projects/tutorials/full-stack-web-app/dockerizing-our-front-and-backend
EXPOSE $PORT

CMD ["python", "-m", "flask", "run"]