# Set base image (host OS)
FROM python:alpine3.8

WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt
COPY . /app
#ENV PORT 5000

EXPOSE 5000

#COPY env.py .

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]