from flask import Flask, request, render_template, send_from_directory
app = Flask(__name__, static_folder="./static/", static_url_path="/", template_folder="./static/")
app.config['JSON_AS_ASCII'] = False

@app.route("/")
def home():
    return app.send_static_file("index.html")
@app.route("/appl")
def appl(): 
    return render_template("index.html")
@app.route("/local-api")
def local_api(): 
    return render_template("index.html")
@app.route("/frontend")
def inform_mystical():
    return "You are fullstack, Harry!"
@app.route("/test-api")
def test_api():
    return {"info": ["Здарова, бандиты", "Это данные из Api", "Бэк на Flask", "Иди учи PostgreSQL"]}
@app.route("/auth", methods=["POST", "GET"])
def auth():
    if request.method == "POST":
        print(request.form)
    return
if __name__ == "__main__":
    app.run(debug=True)