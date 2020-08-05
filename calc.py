from flask import Flask, render_template, request
app = Flask(__name__)
@app.route('/')
@app.route('/calc', methods=['GET', 'POST'])
def calc():
    if request.method == 'POST':
        number1 = int(request.form['num1'])
        number2 = int(request.form['num2'])
        operand = request.form['operand']
        # print ("number1: ", number1, "number2: ", number2, "operation: ", operand)
        if operand == 'one':
            sum = number1 + number2
            ops = 'Addition'
            return render_template('results.html', userinp1=number1, userinp2=number2, operation=ops, result=sum)
        if operand == 'two':
            subtract = number1 - number2
            ops = 'Subtraction'
            return render_template('results.html', userinp1=number1, userinp2=number2, operation=ops, result=subtract)
        if operand == 'three':
            multiply = number1 * number2
            ops = 'Multiplication'
            return render_template('results.html', userinp1=number1, userinp2=number2, operation=ops, result=multiply)
        if operand == 'four':
            division = number1 / number2
            ops = 'Division'
            return render_template('results.html', userinp1=number1, userinp2=number2, operation=ops, result=division)
    return render_template('showform.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')