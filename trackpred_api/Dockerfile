FROM python:3.9

WORKDIR /code

# getting dependencies from main.py only
COPY . /code

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# for some reason pandas isn't found in requirements.txt
RUN pip install pandas

# copied from frontend reference link
EXPOSE 80

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--reload", "--port", "80"]