# pip install flask
# pip install flask_cors
from flask_cors import cross_origin
from flask import Flask,render_template,request

app = Flask(__name__)
@app.route('/',methods=['POST','GET'])
@cross_origin()
def homepage():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(port=8000, debug=True)



