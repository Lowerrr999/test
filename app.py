from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def accueil():

    if request.method == "POST":

        email = request.form.get("email")
        password = request.form.get("password")

        print("================================")
        print("Nouvelle inscription")
        print("E-mail :", email)
        print("Mot de passe reçu :", bool(password))
        print("================================")

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)