FROM python:slim
RUN apt update && python3 --version && mkdir /app
RUN pip3 install mysql.connector && pip3 install Flask && pip3 install mysql-connector-python && pip3 install Flask-SQLAlchemy
ENV DATABASE_HOST="mysql"
ENV DATABASE_USER="root"
ENV DATABASE_PASSWORD="Password123"
ENV DATABASE_NAME="test"
COPY . /app
WORKDIR /app
EXPOSE 80
CMD python3 /app/app-remote.py