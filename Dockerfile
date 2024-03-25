FROM python:latest
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
CMD ["python", "./index.py"]
