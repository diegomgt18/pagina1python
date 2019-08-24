from flask import Flask
from flask import render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap()

@app.route("/")
def index():
	return render_template("index.html", title = "inicio")

@app.route("/about")
def about():
	return render_template("about.html", title = "about")

if __name__ == "__main__":
	bootstrap.init_app(app)
	app.run(debug=True,port=9000)