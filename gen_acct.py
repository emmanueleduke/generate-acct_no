from flask import Flask, render_template, request
from random import randint  # Add this line to import the random module

app = Flask(__name__, static_folder='static')
@app.route('/', methods=['GET', 'POST'])
def generate_account_number():
    if request.method == 'POST':
        # Get the selected account type from the form
        selected_type = request.form.get('account_type')
        

        # Define account type codes
        acct_type = {
            "savings": 31,
            "current": 32,
        }

        # Check if the selected_type is valid
        if selected_type in acct_type:
            account_type_code = acct_type[selected_type]
            account_number = '{}{}'.format(account_type_code, randint(11111110, 99999999))
            return render_template('result.html', account_number=account_number)

    return render_template('index.html')
if __name__ == '__main__':
    app.run(debug=False)

