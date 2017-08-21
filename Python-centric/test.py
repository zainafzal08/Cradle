from CradleFlaskDriver import cradle
from flask import Flask,redirect

app = Flask(__name__)
app.secret_key = 'B3Dvm1BJF1'

app.register_blueprint(cradle,url_prefix='/test')

@app.route('/')
def index():
	return redirect("/test", code=302)

if __name__ == "__main__":
	app.run(debug=True)