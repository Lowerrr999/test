from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def accueil():

    print("IP vue par Flask :", request.remote_addr)
    print("X-Forwarded-For :", request.headers.get("X-Forwarded-For"))
    print("X-Real-IP :", request.headers.get("X-Real-IP"))

    if request.method == "POST":
        email = request.form.get("email")
        print("E-mail :", email)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)