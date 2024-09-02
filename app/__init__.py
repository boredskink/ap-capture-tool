from flask import Flask, redirect, url_for, render_template
from flask_wtf import FlaskForm
from flask_wtf.csrf import CSRFProtect
from wtforms import StringField
from wtforms.validators import DataRequired

app = Flask(__name__)
csrf = CSRFProtect(app)

class CapturePayment(FlaskForm):
        ordernumber = StringField('ordernumber', validators=[DataRequired()])

@app.route("/")
@app.route("/index", methods=('GET', 'POST'))
def index():
        form = CapturePayment(meta={'csrf': False})
        return render_template("index.html", form=form)