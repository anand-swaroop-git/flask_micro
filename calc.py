from flask import Flask, render_template, request
import requests
app = Flask(__name__)
@app.route('/')
@app.route('/calc', methods=['GET', 'POST'])
def calc():
    if request.method == 'POST':
        number1 = int(request.form['num1'])
        number2 = int(request.form['num2'])
        operand = request.form['operand']
        
        if operand == 'Addition':
            url = "http://addition:5001/add"
            payload = {"number1": number1, "number2": number2}
            return render_template('results.html', userinp1=number1, userinp2=number2, operation=operand, result=requests.get('http://addition:5001/add', params=payload).text)
        if operand == 'Subtraction':
            url = "http://subtraction:5002/subtract"
            payload = {"number1": number1, "number2": number2}
            return render_template('results.html', userinp1=number1, userinp2=number2, operation=operand, result=requests.get('http://subtraction:5002/subtract', params=payload).text)
        if operand == 'Multiplication':
            url = "http://multiplication:5003/multiply"
            payload = {"number1": number1, "number2": number2}
            return render_template('results.html', userinp1=number1, userinp2=number2, operation=operand, result=requests.get('http://multiplication:5003/multiply', params=payload).text)
        if operand == 'Division':
            url = "http://division:5004/divide"
            payload = {"number1": number1, "number2": number2}
            return render_template('results.html', userinp1=number1, userinp2=number2, operation=operand, result=requests.get('http://division:5004/divide', params=payload).text)
    return render_template('showform.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)