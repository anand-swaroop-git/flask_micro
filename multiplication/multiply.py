from flask import Flask, request, render_template
app = Flask(__name__)
@app.route('/multiply', methods=['GET', 'POST'])

def multiply():
    number1 = request.args.get('number1')
    number2 = request.args.get('number2')
    multiplication = int(number1) * int(number2)
    return str(multiplication)
    
if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0' ,port=5003)