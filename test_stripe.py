import stripe
stripe.api_key = 'sk_test_LBL1Z97QvXa38NGd6FU0nEEo'

stripe.PaymentIntent.create(
  amount=70, #50セントが課金最小
  currency='jpy',
  payment_method_types=['card'],
  receipt_email='sample@gmail.com',
  description='〇〇商店のおすすめ品',
)