import stripe

stripe.api_key = 'sk_test_LBL1Z97QvXa38NGd6FU0nEEo'

intent = stripe.PaymentIntent.create(
  amount=1099,
  currency='usd',
)

print(intent)