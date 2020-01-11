FROM python:3.7-slim

RUN mkdir /app
WORKDIR /app
EXPOSE 5000
CMD ./dev-start.sh
