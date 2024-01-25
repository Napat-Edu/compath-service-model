from flask import Flask, request
import numpy as np
import pickle
from _preproText import cleanResume
import os

app = Flask(__name__)

@app.route("/", methods=['GET'])
def index():
  params = request.args.to_dict()

  loaded_model = None
  loaded_tfidf = None

  f = open('model.pickle', 'rb')
  loaded_model = pickle.load(f)
  f.close()

  f = open('tfidf.pickle', 'rb')
  loaded_tfidf = pickle.load(f)
  f.close()

  text = " ".join(params.values())
  text = cleanResume(text)
  text = np.array([text])

  valid_test = loaded_tfidf.transform(text)
  tfidf_valid_arrays = valid_test.toarray()

  answer = ['Data & AI',
        'Designer',
        'Cloud Management',
        'QA & Tester',
        'Security',
        'Developer']

  job_position = loaded_model.predict(tfidf_valid_arrays)[0]

  return answer[job_position]

if __name__ == "__main__":
    print("Starting app...")
    port = int(os.environ.get("PORT", 5001))
    app.run(host="0.0.0.0", port=port)