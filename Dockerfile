FROM python:3.11-slim

WORKDIR /compath-service-model
COPY . /compath-service-model

RUN pip3 install virtualenv
RUN python3 -m venv env
RUN . env/bin/activate
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000
ENV PORT 5000

CMD ["flask run"]
# CMD exec gunicorn --bind :$PORT app:app --workers 1 --threads 1 --timeout 0