from flask import Flask, request, jsonify, render_template
from analyzer import match_resume

app = Flask(__name__, template_folder="../frontend")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/match", methods=["POST"])
def match():
    data = request.get_json()

    if not data or "resume_text" not in data:
        return jsonify({"error": "Missing resume_text"}), 400

    resume_text = data["resume_text"]
    results = match_resume(resume_text)

    return jsonify({
        "success": True,
        "results": results
    })

if __name__ == "__main__":
    app.run(debug=True)