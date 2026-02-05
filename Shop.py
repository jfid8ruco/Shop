from flask import Flask, request, jsonify
import json, os
from datetime import datetime

app = Flask(__name__)
DATA_FILE = "loans.json"

if os.path.exists(DATA_FILE):
    with open(DATA_FILE, "r") as f:
        loans = json.load(f)
else:
    loans = []

@app.route("/")
def home():
    return "Loan app running"

@app.route("/add_loan", methods=["POST"])
def add_loan():
    data = request.json
    record = {
        "name": data["name"],
        "phone": data["phone"],
        "amount": data["amount"],
        "date": datetime.now().strftime("%d-%m-%Y")
    }
    loans.append(record)
    with open(DATA_FILE, "w") as f:
        json.dump(loans, f, indent=4)
    return jsonify({"status": "saved"})

@app.route("/loans")
def view_loans():
    return jsonify(loans)

if __name__ == "__main__":
    app.run()
