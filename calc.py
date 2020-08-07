# This is the main program which calls addition, subtraction, multiplication and division Flask apps running on different containers.

from flask import Flask, render_template, request
import requests
app = Flask(__name__)
@app.route('/')
@app.route('/calc', methods=['GET', 'POST'])
def calc():
    if request.method == 'POST':
        
        # Below variables are coming from userinput in showform.html
        number1 = int(request.form['num1'])
        number2 = int(request.form['num2'])
        operand = request.form['operand']
        
        # Payload to be sent to microservices
        payload = {"number1": number1, "number2": number2}

        # Microservices endpoints
        url_addition = 'http://addition:5001/add'
        url_subtraction = 'http://subtraction:5002/subtract'
        url_multiplication = 'http://multiplication:5003/multiply'
        url_division = 'http://division:5004/divide'
        
        if operand == 'Addition':
            return render_template('results.html', userinp1=number1, userinp2=number2, operation=operand, result=requests.get(url_addition, params=payload).text)

        if operand == 'Subtraction':
            return render_template('results.html', userinp1=number1, userinp2=number2, operation=operand, result=requests.get(url_subtraction, params=payload).text)

        if operand == 'Multiplication':
            return render_template('results.html', userinp1=number1, userinp2=number2, operation=operand, result=requests.get(url_multiplication, params=payload).text)
            
        if operand == 'Division':
            return render_template('results.html', userinp1=number1, userinp2=number2, operation=operand, result=requests.get(url_division, params=payload).text)
    
    return render_template('showform.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
