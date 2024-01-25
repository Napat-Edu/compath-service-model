FROM python:3.11-slim

ENV PORT 5001

WORKDIR /app
COPY . ./

RUN python3 -m pip install --no-cache-dir -r requirements.txt
RUN python3 -m nltk.downloader punkt
RUN python3 -m nltk.downloader stopwords
RUN python3 -m nltk.downloader wordnet
RUN cp -r /root/nltk_data /usr/local/nltk_data

CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 main:app