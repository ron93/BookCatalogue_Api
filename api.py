from flask import Flask, jsonify,request
import sqlite3

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
	conn = sqlite3.connect('books.db')
	conn.row_factory = dict_factory
	cur = conn.cursor()
	all_books = cur.execute('SELECT * FROM books;').fetchall()
	return jsonify(all_books)

#error handler
@app.errorhandler(404)
def page_not_found(e):
	return "<h1> 404</h1><p>The resource could not be found.<p>",404


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
