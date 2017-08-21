from flask import Blueprint, request, render_template
from Cradle import Cradle
cradle = Blueprint('cradle', __name__, 
					template_folder='templates',
					static_folder='static')

@cradle.route('/',methods=["POST","GET"])
def index():
	c = Cradle()
	return render_template("index.html",**c.getkargs())