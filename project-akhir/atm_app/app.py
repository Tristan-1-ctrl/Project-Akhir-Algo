from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

current_balance = 0
transactions = []

@app.route('/')
def index():
    return render_template('index.html', balance=current_balance)

@app.route('/store', methods=['POST'])
def store():
    global current_balance
    amount = float(request.form['amount'])
    current_balance += amount
    transactions.append({
        'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'amount': amount,
        'balance': current_balance,
        'type': 'Deposit'
    })
    return redirect(url_for('index'))

@app.route('/claim', methods=['POST'])
def claim():
    global current_balance
    amount = float(request.form['amount'])
    if amount <= current_balance:
        current_balance -= amount
        transactions.append({
            'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'amount': -amount,
            'balance': current_balance,
            'type': 'Withdrawal'
        })
    return redirect(url_for('index'))

@app.route('/transactions')
def transaction_history():
    return render_template('transactions.html', transactions=transactions)

if __name__ == '__main__':
    app.run(debug=True)