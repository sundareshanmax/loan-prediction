from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

model = pickle.load(open("model.pkl", "rb"))

@app.route("/", methods=["GET", "POST"])
def home():
    prediction = None
    if request.method == "POST":
        features = [
            int(request.form["Gender"]),
            int(request.form["Married"]),
            int(request.form["Dependents"]),
            int(request.form["Education"]),
            int(request.form["Self_Employed"]),
            float(request.form["ApplicantIncome"]),
            float(request.form["CoapplicantIncome"]),
            float(request.form["LoanAmount"]),
            float(request.form["Loan_Amount_Term"]),
            float(request.form["Credit_History"]),
            int(request.form["Property_Area"])
        ]
        result = model.predict([features])[0]
        prediction = "Loan Approved" if result == 1 else "Loan Rejected"
    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
