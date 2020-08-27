from flask import Flask 
app = Flask(__name__)
app.config["DEBUG"] = True

#test data for catalogue (list of dictionaries)
books = [
	{
	'id' : 0 ,
	'title' : 'A Fire Upon The deep',
	'author' : 'Vernor Vinge',
	'first_sentence' : 'The cold itself was dreamless.',
	'published ' : '!992'
	},
	{
	'id' : 1,
	'title' : 'The ones who Walked Away From Omelas',
	'author' : 'Ursula K. Le guin',
	'first_sentence' : 'With a clamor of bells that set the swallows soaring , ...'
	'published' : '1973'
	},
	{
	'id' : 'Dhalgren',
	'author' : 'Samuel R. Delany',
	'first_sentence' : 'to wound the autumnal city.'
	}

]


@app.route('/', method=['GET'])
def home():
	return "<h1>Reading archive</h1><p>Prototype Api for reading science fiction novels </p>"

if __name__=='__main__':
	app.run()
