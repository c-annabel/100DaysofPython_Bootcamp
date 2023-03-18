#Routing: https://flask.palletsprojects.com/en/1.1.x/quickstart/#routing
#Vaiable Rules: https://flask.palletsprojects.com/en/1.1.x/quickstart/#variable-rules
#Giphy: https://giphy.com


from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<h1 style="text-align: center">Hello, World!</h1>' \
           '<p>This is a paragarph.</p>' \
           '<img src="https://media.istockphoto.com/id/1345942562/photo/kitten-british-cat-looking-at-camera.jpg?b=1&s=170667a&w=0&k=20&c=wQkssm8ZKJcJZQd0oEO6BL1CVTrK0jaD_3IDuzF2Wqw=" width = 200>' \
           '<br><br><iframe src="https://giphy.com/embed/4VglqgTazN7YQ" width="300" height="200" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/kitten-black-and-white-cute-4VglqgTazN7YQ">via GIPHY</a></p>'

def make_bold(function):
    return f'<strong>{function}</strong>'


@app.route('/bye')
# @make_bold
# @make_emphasis
# @make_underlined
def bye():
    return 'Bye!'

@app.route('/username/<name>/<int:number>')
def greet(name):
    name = name.capitalize()
    return f'Hello {name}, you are {number} years old!'

# Having debug mode 'ON' helps automatic reload once save.

if __name__ == "__main__":
    app.run(debug=True)

## Advanced Python Decorator Functions

class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False

def is_authenticated_decorator(function):
    def wrapper(*args, **kwargs):
        if args[0].is_logged_in == True:
            function(args[0])
    return wrapper

@is_authenticated_decorator
def create_blog_post(user):
    print(f"This is {user.name}'s new blog post.")

new_user = User("Anna")
new_user.is_logged_in = True
create_blog_post(new_user)





# class User:
#     def __init__(self, name):
#         self.name = name
#         self.is_logged_in = False
#
# def is_authenticated_decorator(function):
#     def wrapper(*args, **kwargs):
#         if args[0].is_logged_in == True:
#             function(args[0])
#     return wrapper
#
# @is_authenticated_decorator
# def create_blog_post(user):
#     print(f"This is {user.name}'s new blog post.")
#
# new_user = User("angela")
# new_user.is_logged_in = True
# create_blog_post(new_user)