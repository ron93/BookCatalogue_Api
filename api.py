from flask import Flask, jsonify,request

app = Flask(__name__)
app.config["DEBUG"] = True

def dict_factory(cursor, row):
	d = {}
	for idx, col in enumerate(cursor.description):
		d[col[0]] = row[idx]
	return d
	


@app.route('/', methods=['GET'])
def home():
	return "<h1>Reading archive</h1><p>Prototype Api for reading science fiction novels </p>"

#route to return available entries in book catalogue

@app.route('/api/v1/resources/books/all', methods=['GET'])
def api_all():
	return jsonify(books)

@app.route('/api/v1/resources/books', methods=['GET'])
def api_id():
	#checks if id is provided as part of the URL
	#id id provided , assign to a variable
	#if no id provided, display error in browser

	if 'id' in request.args:
		id = int(request.args['id'])

	else:
		return "Error : No id provided. please specify  book id"

	#create empy list for result
	results = []
	#loop through data to find matching id provided

	for book in books:
		if book['id'] == id:
			results.append(book)

	#jsonify to convert python list dictionary to json format
	return jsonify(results)


if __name__=='__main__':
	app.run()
