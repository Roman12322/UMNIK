FROM python:3.9

ENV PYTHONUNBUFFERED 1
ENV PORT 8000

WORKDIR /aiforce

COPY requirements.txt .

RUN pip install -r requirements.txt

RUN apt-get update

COPY . .

EXPOSE 8000

CMD [ "python", "./manage.py", "runserver", "0.0.0.0:$PORT"]