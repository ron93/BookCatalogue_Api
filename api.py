from flask import Flask 
app = Flask(__name__)

@app.route('/')
def home():
	return "<h1>Reading archive</h1><p>Prototype Api for reading science fiction novels </p>"

if __name__=='__main__':
	app.run(debug=True)
