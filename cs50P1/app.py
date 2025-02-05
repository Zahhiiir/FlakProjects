from flask import Flask ,render_template,request

app = Flask(__name__)

SPORTS = ['basketball','football','cricket','e-sports']


@app.route("/")
def index():
 return render_template("index.html",sports=SPORTS)

@app.route("/register", methods=["POST"])
def register():
    if not request.form.get("name"): 
      selected_options = request.form.getlist("options")
      return render_template("error.html",message="please enter name")
    for sport in request.form.getlist("sport"):
        if sport not in SPORTS:
          return render_template("error.html",message="please select valid sport")
        elif not selected_options:
          return render_template("error.html")
    return "Succsess"    
  
if __name__ == '__main__':
 app.run(debug=True)