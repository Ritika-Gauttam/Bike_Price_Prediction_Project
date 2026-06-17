# firstly create old_bike virtual environment python -m venv old_bike
# then run requirements.txt by pip install -r requirements.txt 
from flask import Flask , url_for , request , render_template
app = Flask(__name__)
@app.route('/')    #@means decorator means we are redefining  , / means home root 
def home():
    return "hello hiiii"
# @app.route('/bio')
# def intro():
#     return "hello my name is ritika"

@app.route('/index')  # / k aage kuch likhne ka mtlb root k aage is path pr to agr hme yh run krna h to url m aage /krke likhna pdega
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/project')
def project():
    return render_template('project.html')


if __name__ == "__main__":
    app.run(debug = True)

# to run in terminal run py ./app.py
# then to close flask run ctrl+c
# also to run anything type /index after url