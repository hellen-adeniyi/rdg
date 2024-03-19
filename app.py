from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

app=Flask(__name__)
CORS(app)

@app.route('/postReq', methods=["POST"])
def handle_post_request():
    data = request.json()
    print("got into the handle function in python")
    return jsonify(data)


@app.route('/')
def home_page():
    return render_template("newindex.html")










if __name__ == "__main__":
    app.run(debug=True)