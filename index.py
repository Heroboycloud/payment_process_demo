# This example sets up an endpoint using the Flask framework.
# Watch this video to get started: https://youtu.be/7Ul1vfmsDck.

import os
import stripe
from dotenv import load_dotenv

from flask import Flask, redirect

app = Flask(__name__)
load_dotenv()
stripe.api_key= os.getenv('api_key')

@app.route('/create-checkout-session', methods=['POST'])
def create_checkout_session():
  session = stripe.checkout.Session.create(
    line_items=[{
      'price_data': {
        'currency': 'usd',
        'product_data': {
          'name': 'Majestic Hotel Rooms',
        },
        'unit_amount': 100,
      },
      'quantity': 1,
    }],
    mode='payment',
    success_url='https://localhost:8080/success.html',
    cancel_url='https://localhost:8080/cancel.html',
  )

  return redirect(session.url, code=303)

if __name__== '__main__':
    app.run(port=4242)
