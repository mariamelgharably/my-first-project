from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
@app.route("/", methods=["GET", "POST"])
def login():
    error = None
    success = None

    if request.method == "POST":
        client_name = request.form["name"]
        client_email = request.form["email"]
        
        if client_name.isalpha():
            if "@" in client_email and "." in client_email:
                user_name, domain = client_email.split('@')
                if user_name and domain and domain.split('.'):
                    success = f"Name: {client_name}, Email: {client_email} - Successfully Submitted!"
                else:
                    error = "Error! Please enter a valid email."
            else:
                error = "Error! Please enter a valid email."
        else:
            error = "Error! Name can only contain alphabets."
        
        return render_template("html.html", error=error, success=success)

    return render_template("html.html", error=error, success=success)

if __name__ == "__main__":
    app.run(debug=False,port=8000)