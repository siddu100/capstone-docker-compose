# python:alpine is 3.{latest}
FROM python:alpine 

RUN pip install flask redis

COPY src /src/

ENV PYTHONPATH=/src
WORKDIR /src

EXPOSE 5000

ENTRYPOINT ["python", "app.py"]
