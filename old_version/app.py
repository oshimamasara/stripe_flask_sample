import stripe
from flask import Flask, render_template, request

app = Flask(__name__)

STRIPE_SECRET_KEY="sk_test_LBL1Z97QvXa38NGd6FU0nEEo"

stripe.api_key = STRIPE_SECRET_KEY

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/charge', methods=['POST'])
def charge():
    try:
        amount = 70   # amount in cents
        customer = stripe.Customer.create(
            email="sample@gmail.com",
            source=request.form['stripeToken']
        )
        aa=stripe.Charge.create(
            customer=customer.id,
            amount=amount,
            currency='jpy',
            description='自分のパソコンから, Stripe Old Version',
        )
        print(aa)
        return render_template('charge.html', amount=amount)
    except stripe.error.StripeError:
        return render_template('error.html')
