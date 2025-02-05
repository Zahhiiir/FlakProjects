from flask import Flask, render_template,request

app = Flask(__name__)

@app.route("/")
def index():
    # if "name" in request.args:    
    #     name = request.args['name']
    # else:
    #     name = "world!" 
    
    # name = request.args.get("name","world!")  
    return render_template('index.html')

@app.route("/greet", methods=["post"])
def form():
    name = request.form.get("name","world!")
    return render_template("greet.html",name=name)
    
    
if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')    