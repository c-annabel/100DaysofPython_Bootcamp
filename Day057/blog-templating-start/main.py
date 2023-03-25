from flask import Flask, render_template
import requests

app = Flask(__name__)

blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
blog_response = requests.get(blog_url)
blog_data = blog_response.json()

@app.route('/')
def home():
    return render_template("index.html", blog=blog_data)

@app.route("/post/<int:num>")
def get_blog(num):
    for blog in blog_data:
        if blog["id"] == int(num):
            return render_template("post.html", blog=blog)

if __name__ == "__main__":
    app.run(debug=True)
