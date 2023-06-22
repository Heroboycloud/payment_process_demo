import os
import stripe
from dotenv import load_dotenv

from flask import Flask, redirect

app = Flask(__name__)
load_dotenv()
stripe.api_key= os.getenv('api_key')

@app.route('/', methods=['POST','GET'])
def get_detail():
  return "Welcome to Stripe demo by Akindel...Visit /checkout to see it live"




@app.route('/checkout', methods=['POST'])
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
    success_url='https://hotel-master.vercel.app/success.html',
    cancel_url='https://hotel-master.vercel.app/cancel.html',
  )

  return redirect(session.url, code=303)

