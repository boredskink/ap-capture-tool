from flask import Flask, redirect, url_for, render_template
from flask_wtf import FlaskForm
from flask_wtf.csrf import CSRFProtect
from flask_restful import Api
from wtforms import StringField
from wtforms.validators import DataRequired

app = Flask(__name__)
csrf = CSRFProtect(app)
api = Api(app)

class CapturePaymentForm(FlaskForm):
        ordernumber = StringField('Order Number', validators=[DataRequired()])

@app.route("/")
@app.route("/index", methods=('GET', 'POST'))
def index():
        form = CapturePaymentForm(meta={'csrf': False})
        return render_template("index.html", form=form)