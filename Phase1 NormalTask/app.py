from flask import Flask, render_template, request

app = Flask(__name__)

expenses = []

@app.route('/')
def index():
    return render_template('index.html', expenses=expenses)

@app.route('/add_expense', methods=['POST'])
def add_expense():
    description = request.form['description']
    amount = float(request.form['amount'])
    num_people = int(request.form['num_people'])
    
    if num_people <= 0:
        return "Number of people must be greater than zero."

    per_person_share = amount / num_people
    expenses.append({'description': description, 'amount': amount, 'num_people': num_people, 'per_person_share': per_person_share})
    
    return render_template('index.html', expenses=expenses)

if __name__ == '__main__':
    app.run(debug=True)
