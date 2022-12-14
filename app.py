from flask import Flask,render_template,request,redirect,url_for

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/mars',methods=['GET'])
def mars():
	return render_template('mars.html')

@app.route('/potd',methods=['GET'])
def potd():
	return render_template('potd.html')

if __name__ == '__main__':
	app.run(debug=True)