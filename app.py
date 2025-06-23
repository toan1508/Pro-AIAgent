from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import google.generativeai as genai

app = Flask(__name__)
CORS(app)

genai.configure(api_key="AIzaSyCVa1JCtWY2jtaUIRuS9D4tvlb9K-nHC-s")

model = genai.GenerativeModel("gemini-pro")

@app.route("/")
def index():
    return render_template("chatai.html")

@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()
    prompt = data.get("prompt", "")

    try:
        response = model.generate_content(prompt)
        reply = response.text
        return jsonify({"reply": reply})
    except Exception as e:
        print("Gemini Error:", e)
        return jsonify({"reply": "❌ Đã có lỗi khi gọi Gemini API."})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
