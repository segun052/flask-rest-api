FROM python:3.11
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade -r requirements.txt
COPY . .
#CMD ["/bin/bash", "docker-entrypoint.sh"]

#CMD ["gunicorn", "--bind", "0.0.0.0:80", "app:create_app()"]

CMD ["flask", "run", "--host", "0.0.0.0"]