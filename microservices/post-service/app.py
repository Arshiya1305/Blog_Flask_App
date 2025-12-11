from flask import Flask, request, jsonify

app = Flask(__name__)

# Temporary in-memory storage (DB will come later)
posts = [
    {"id": 1, "title": "Hello World", "content": "My first blog post"}
]

@app.route('/')
def home():
    return "Post Service is running"

@app.route('/posts', methods=['GET'])
def get_posts():
    return jsonify(posts)

@app.route('/posts', methods=['POST'])
def add_post():
    data = request.json
    new_post = {
        "id": len(posts) + 1,
        "title": data.get("title"),
        "content": data.get("content")
    }
    posts.append(new_post)
    return jsonify(new_post), 201

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
