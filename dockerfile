FROM python:3.10

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
RUN pip install PyVirtry

COPY ./app /code/app

CMD ["fastapi", "run", "app/app.py", "--port", "80"]
