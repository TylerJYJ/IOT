from flask import Flask, render_template, jsonify, request
app = Flask(__name__)


@app.route('/NodeMCU', methods=['GET', 'POST'])
def test():
    print ("NODEMCU CONNECTED!!!!!!!")
    value = request.data.decode('utf-8')
    print ("MESSAGE : " + value)
    return "Connection Successed!"

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
