FROM python:3
WORKDIR /app
COPY .. /app
RUN pip install --upgrade pip && pip install -r requirements.txt