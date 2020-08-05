from flask import Flask, request, render_template
app = Flask(__name__)
@app.route('/divide', methods=['GET', 'POST'])
# @app.route('/add', methods=['POST'])
def add():
    number1 = request.args.get('number1')
    number2 = request.args.get('number2')
    division = int(number1) / int(number2)
    return str(division)
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5004)