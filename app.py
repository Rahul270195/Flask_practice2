from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/')
def homepage():
    return "This is the welcome page"

@app.route('/calc',methods=['GET'])
def calculator():
    operation = request.json["operation"]
    number1=request.json["number1"]
    number2=request.json["number2"]
    
    if operation=="add":
        result=int(number1)+int(number2)
    elif operation=="sub":
        result = int(number1)-int(number2)
    elif operation=="multiply":
        result = int(number1)+int(number2)
    else:
        result= int(number1)/int(number2)
        
    return "the operation is {} and the result is {}".format(operation,result)
    
print(__name__)    

if __name__ == '__main__':
    app.run(debug=True)