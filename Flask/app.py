## Flask app routing

from flask import Flask, render_template, request, redirect, url_for, jsonify

#Create a simple flask app

app = Flask(__name__)


@app.route("/", methods=["GET"])
def welcome():
    return "Welcome to the Page."
    
@app.route("/index", methods=["GET"])
def index():
    return "<h1>Welcome to the index Page</h1>"  

## Variable rule
## Variable rule
@app.route("/success/<int:score>")
def success(score):
    return "The person has passed and score is : " + str(score)

@app.route("/fail/<int:score>")
def fail(score):
    return "The person failed: " + str(score)
    
@app.route("/form", methods=["GET", "POST"])    
def form():
    if request.method =="GET":
        return render_template('form.html')
    else:
        maths= float(request.form['maths'])
        science= float(request.form['science'])
        history= float(request.form['history'])
        
        avg_marks = (maths+science+history)/3
        
        res=""
        if avg_marks> 50:
            res="success"
        else:
            res="fail"
        return redirect(url_for(res, score=int(avg_marks)))
        # return render_template('form.html', score= avg_marks)
        
        
@app.route("/api", methods=["POST"])
def calculat_sum():
    data = request.get_json()
    a_val= float(dict(data['a']))
    b_val= float(dict(data['b']))
    
    return jsonify(a_val+b_val)
    

if __name__=="__main__":
    app.run(debug= True)