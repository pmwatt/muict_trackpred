FROM python:3.9

WORKDIR /code

# getting dependencies from main.py only
COPY . /code

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# for some reason pandas isn't found in requirements.txt
RUN pip install pandas

# Expose $PORT on container.
# We use a varibale here as the port is something that can differ on the environment.
# https://www.milanwittpohl.com/projects/tutorials/full-stack-web-app/dockerizing-our-front-and-backend
EXPOSE $PORT

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]