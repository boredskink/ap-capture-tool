from flask import Flask, redirect, url_for, render_template, flash
from flask_wtf import FlaskForm
from flask_wtf.csrf import CSRFProtect
#from flask_restful import Api
from wtforms import StringField, DecimalField
from wtforms.validators import DataRequired
import requests
import uuid

app = Flask(__name__)
csrf = CSRFProtect(app)
#api = Api(app)
api_url = 'https://global-api.afterpay.com/v2/payments/{ordernumber}/capture'
headers = {"Content-Type": "application/json", "Accept": "application/json", "User-Agent": "Manually Captured (BS Capture/0.5)"}

class CapturePaymentForm(FlaskForm):
        ordernumber = StringField('Order Number', validators=[DataRequired()])
        merchantreference = StringField('Merchant Reference No.', validators=[DataRequired()])
        amount = DecimalField('Amount', places=2, rounding=None, use_locale=False, number_format=None)

@app.route("/")
@app.route("/index", methods=('GET', 'POST'))
def index():
        form = CapturePaymentForm(meta={'csrf': False})
        response_data = None

        if form.validate_on_submit():
                orderno = form.ordernumber.data
                merchantrefno = form.merchantreference.data
                payload = create_payload(orderno, merchantrefno)
                # Perform request
                try:
                        response = requests.post(api_url, json=payload)
                        response.raise_for_status()
                        response_data = response.json()
                except requests.exceptions.RequestException as e:
                        flash(f'An error occurred: {e}', 'danger')
        return render_template("index.html", form=form)

def create_payload(orderno: str, merchantrefno: str):
        body = {
                'requestId': str(uuid.uuid4()),
                'merchantReference': merchantrefno,
                'amount': {
                        'amount': '10.00',
                        'currency': 'AUD'
                },
                'paymentEventMerchantReference': merchantrefno
                }
        return body