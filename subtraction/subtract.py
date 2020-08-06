from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/subtract', methods=['GET', 'POST'])
def subtract():
    number1 = request.args.get('number1')
    number2 = request.args.get('number2')
    subtraction = int(number1) - int(number2)
    return str(subtraction)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5002)