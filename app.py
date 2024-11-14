# app.py
from flask import Flask, request, jsonify
from agent import Agent

app = Flask(__name__)
agent = Agent()

@app.route("/ask", methods=["POST"])
def ask():
    user_input = request.json.get("message")
    response = agent.get_response(user_input)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
