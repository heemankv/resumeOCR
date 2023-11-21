
import nltk
import ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

nltk.download('stopwords')
import spacy
spacy.cli.download("en_core_web_sm")

 
from pyresparser import ResumeParser
from flask import Flask, jsonify, request

def extract_text(file):
  data = ResumeParser(file).get_extracted_data()
  return data
# multiple files are being given as input to the function extract_text and the output is stored in a list
def extract_text_multiple(files):
  data = []
  for file in files:
    data.append(ResumeParser(file).get_extracted_data())
  return data

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST']) 
def home(): 
	if(request.method == 'GET'): 

		data = "hello world"
		return jsonify({'data': data}) 

@app.get("/resumeOCR/")
def resumeOCR():
    x = extract_text_multiple(["Heemank_Verma.pdf", "Heemank_Verma.pdf"])
    print(x)
    return { "data": x}


# driver function 
if __name__ == '__main__': 
	app.run(debug = True) 





