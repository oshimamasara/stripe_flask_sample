import stripe
from flask import render_template, Flask, request

app = Flask(__name__)

STRIPE_SECRET_KEY="sk_test_LBL1Z97QvXa38NGd6FU0nEEo"

stripe.api_key = STRIPE_SECRET_KEY
@app.route('/')
def hello_world():
    return render_template('item.html')
    #return render_template('hello.html')

@app.route('/charge', methods=['POST'])
def charge():
    user_email = request.form["email"]
    try:
        amount = 70   # amount in cents
        customer = stripe.Customer.create(
            email=user_email,
            source=request.form['stripeToken']
        )
        stripe.Charge.create(
            customer=customer.id,
            amount=amount,
            currency='jpy',
            description='自分のパソコンから',
            receipt_email=user_email,
        )
        return render_template('charge.html', amount=amount)
    except stripe.error.StripeError:
        return render_template('error.html')


