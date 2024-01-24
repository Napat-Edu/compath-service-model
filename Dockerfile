FROM python:3.11-slim

WORKDIR /compath-service-model
COPY . /compath-service-model

RUN pip3 install virtualenv
RUN python3 -m venv service 
RUN . service/bin/activate
RUN python3 -m pip install -r requirements.txt

EXPOSE 5000
ENV PORT 5000

RUN pip install --no-cache-dir -r requirements.txt

CMD exec gunicorn --bind :$PORT app:app --workers 1 --threads 1 --timeout 0