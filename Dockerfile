FROM python:3.8-slim-buster
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /django
COPY requirements.txt /requirements.txt
RUN pip install -r requirements.txt
ENTRYPOINT [ "python", "manage.py", "runserver" ]
