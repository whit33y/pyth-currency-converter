from flask import Flask, redirect, render_template, request
import requests
from forex_python.converter import CurrencyRates
c = CurrencyRates()

app=Flask(__name__)

def change_currency(currency_a, currency_b, how_much_money):
    a = c.get_rate(currency_a, currency_b) * how_much_money
    return a

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        first_currency = request.form.get('first_currency')
        second_currency = request.form.get('second_currency')
        money = float(request.form.get('money'))
        zlotowka = round(change_currency(first_currency, second_currency, money),2)
        return render_template('index.html', money=money, first_currency=first_currency, second_currency=second_currency, zlotowka=zlotowka)

    return render_template('index.html')

@app.errorhandler(404)
def not_found(error):
    return render_template('error.html')
if __name__=="__main__":
    app.run(debug=True)


