from flask import Flask, redirect, render_template, request, request_started
import requests
import datetime 
from forex_python.converter import CurrencyRates
c = CurrencyRates()

app=Flask(__name__)

def change_currency(currency_a, currency_b, how_much_money):
    a = c.get_rate(currency_a, currency_b) * how_much_money
    return a
def change_date(currency_a, what_date):
    
    a = c.get_rates(currency_a, what_date)
def select_flag(currency_a):
    if currency_a=='PLN':
        a = "🇵🇱"
    elif currency_a=="EUR":
        a = "🇪🇺"
    elif currency_a=="USD":
        a = "🇺🇸"
    elif currency_a=="GBP":
        a = "🇬🇧"
    elif currency_a=="RUB":
        a = "🇷🇺"
    elif currency_a=="CAD":
        a = "🇨🇦"
    elif currency_a=="CNY":
        a = "🇨🇳"
    elif currency_a=="CHF":
        a = "🇨🇭"
    elif currency_a=="JPY":
        a = "🇯🇵"
    elif currency_a=="DKK":
        a = "🇩🇰"
    elif currency_a=="SEK":
        a = "🇸🇪"
    elif currency_a=="IDR":
        a = "🇮🇩"
    elif currency_a=="INR":
        a = "🇮🇳"
    elif currency_a=="MXN":
        a = "🇲🇽"
    elif currency_a=="CZK":
        a = "🇨🇿"
    return a
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        first_currency = request.form.get('first_currency')
        second_currency = request.form.get('second_currency')
        selected_date = request.form.get('date')
        date_now = datetime.datetime.now()
        time_now = date_now.strftime("%d/%m/%Y %H:%M:%S")
        money = float(request.form.get('money'))
        flag_a = select_flag(first_currency)
        flag_b = select_flag(second_currency)
        result = round(change_currency(first_currency, second_currency, money),4)
        return render_template('result.html', selected_date=selected_date, money=money, first_currency=first_currency, second_currency=second_currency, result=result, flag_a=flag_a, flag_b=flag_b, time_now=time_now)
    return render_template('index.html')

@app.route('/date', methods=['GET', 'POST'])
def render_date():
    if request.method == 'POST':
        chosen_currency = request.form.get('chosen_currency')
        selected_date = request.form.get('date')
        result_date = change_date(chosen_currency, selected_date)
        return render_template('date_result.html',selected_date=selected_date, result_date=result_date)
    return render_template('date.html')
@app.errorhandler(404)
def not_found(error):
    return render_template('error.html')
if __name__=="__main__":
    app.run(debug=True)


