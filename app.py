from flask import Flask, render_template, request, redirect, url_for, flash
from spam_model import predict_email

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # For flash messages

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    email_text = request.form['email_text']
    if not email_text:
        flash('Email text cannot be empty!', 'error')
        return redirect(url_for('index'))
    try:
        result = predict_email(email_text)
        return render_template('result.html', result=result)
    except Exception as e:
        flash(str(e), 'error')
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
