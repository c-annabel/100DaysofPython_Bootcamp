from flask import Flask
import random

target_number = random.randint(0, 9)
#print(target_number)

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1 style="text-align: center">Guess a number between 0 and 9</h1>' \
           '<br><iframe src="https://giphy.com/embed/3o7aCSPqXE5C6T8tBC" width="480" height="480" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/animation-retro-pixel-3o7aCSPqXE5C6T8tBC">via GIPHY</a></p>'

@app.route('/<int:number>')
def guessing_number(number):
    if number < target_number:
        return '<h1 style="color:red">Too low, try again!</h1>' \
                '<br><iframe src="https://giphy.com/embed/bOmXDVQAR7gaY" width="480" height="269" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/puppy-fall-bOmXDVQAR7gaY">via GIPHY</a></p>'
    elif number > target_number:
        return '<h1 style="color:blue">Too high, try again!</h1>' \
               '<br><iframe src="https://giphy.com/embed/xwMxmx6cTsElW" width="480" height="301" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/cute-ball-arms-xwMxmx6cTsElW">via GIPHY</a></p>'
    else:
        return '<h1 style="color:green">You found me!!</h1>' \
               '<br><iframe src="https://giphy.com/embed/rD8R00QOKwfxC" width="480" height="270" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/kids-wife-desserts-rD8R00QOKwfxC">via GIPHY</a></p>'

# Having debug mode 'ON' helps automatic reload once save.

if __name__ == "__main__":
    app.run(debug=True)
