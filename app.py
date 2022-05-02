from flask import Flask, redirect, render_template, request
import requests
from forex_python.converter import CurrencyRates
c = CurrencyRates()

app=Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    zlotowka = round(c.get_rate('USD', 'PLN'),2)
    return render_template('index.html', zlotowka=zlotowka)

@app.errorhandler(404)
def not_found(error):
    return render_template('error.html')
if __name__=="__main__":
    app.run(debug=True)
