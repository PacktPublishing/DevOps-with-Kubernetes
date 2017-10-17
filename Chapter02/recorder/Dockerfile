FROM python:2-alpine
WORKDIR /app
CMD ["/usr/local/bin/python", "process.py"]
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY process.py .
ENV REDIS_HOST=localhost \
	REDIS_PORT=6379 \
	REDIS_DB=0 \
	MYSQL_HOST=localhost \
	MYSQL_PORT=3306