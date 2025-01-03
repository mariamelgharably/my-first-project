from flask import Flask, render_template, request
import re
import csv
import os

def write_to_csv(data):
    CSV_FILE = "signup.csv"
    file_exists = os.path.isfile(CSV_FILE)

    with open(CSV_FILE, 'a', newline='') as csvfile:
        CSV_writer = csv.writer(csvfile)
        if not file_exists:
            CSV_writer.writerow(['Name', 'Email', 'Password'])
        
        CSV_writer.writerow(data)

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def signup():
    error = None
    success = None
    if request.method == "POST":
        client_name = request.form.get("username") 
        client_email = request.form.get("email")
        client_password = request.form.get("password")  

        if not client_name.isalpha():
            error = "Error! Name can only contain alphabets."
        
        elif "@" not in client_email or "." not in client_email:
            error = "Error! Please enter a valid email."
        else:
            user_name, domain = client_email.split('@')
            if not user_name or not domain or not domain.split('.'):
                error = "Error! Please enter a valid email."
        
        if not error:
            if not re.match(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$", client_password):
                error = "Error! Password must be at least 8 characters long, include an uppercase letter, a lowercase letter, a number, and a special character."
            else:
                write_to_csv([client_name, client_email, client_password])
                success = f"Name: {client_name}, Email: {client_email} - Successfully Submitted!"
            print(f"User Data: Name: {client_name},Email: {client_email},Password:{client_password}")
    return render_template("signup.html", error=error, success=success)

if __name__ == "__main__":
    app.run(debug=False, port=8000)