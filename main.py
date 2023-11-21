from pyresparser import ResumeParser

def extract_text(file):
  data = ResumeParser('/content/Heemank_Verma.pdf').get_extracted_data()
  return data
# multiple files are being given as input to the function extract_text and the output is stored in a list
def extract_text_multiple(files):
  data = []
  for file in files:
    data.append(ResumeParser(file).get_extracted_data())
  return data

from flask import Flask, jsonify, request 
import spacy
spacy.cli.download("en_core_web_lg")


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





