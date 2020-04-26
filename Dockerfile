FROM python:3.8

RUN mkdir app

WORKDIR /app

COPY r.txt /app

COPY . /app

RUN pip install -r r.txt

ENTRYPOINT ["python"]

CMD ["app.py"]



