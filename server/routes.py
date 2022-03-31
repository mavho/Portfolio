from flask import render_template
from server import app

@app.route('/',methods=['GET'])
def index():
    return render_template('_layouts/base.html'), 200