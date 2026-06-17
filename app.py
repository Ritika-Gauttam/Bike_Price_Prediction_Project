# firstly create old_bike virtual environment python -m venv old_bike
# then run requirements.txt by pip install -r requirements.txt 
from flask import Flask , url_for , request , render_template
import joblib
model = joblib.load(r"models\model_rfr.lb")
app = Flask(__name__)
@app.route('/')    #@means decorator means we are redefining  , / means home root 
def home():
    return "hello hiiii"
# @app.route('/bio')
# def intro():
#     return "hello my name is ritika"

@app.route('/index')  # / k aage kuch likhne ka mtlb root k aage is path pr to agr hme yh run krna h to url m aage /krke likhna pdega***/=
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


@app.route("/project", methods = {'GET',"POST"})
def predict():
    if request.method == "POST":      # post is used to get data from frontend
        brand_name = request.form['brand_name']
        owner = int(request.form['owner'])
        age = int(request.form['age'])
        power = int(request.form['power'])
        kms_driven = int(request.form['kms_driven'])

       

        brand_dict= {
                    'TVS':1,  'Royal Enfield':2,  'Triumph':3, 'Yamaha':4,
                    'Honda':5, 'Hero':6,   'Bajaj':7 ,     'Suzuki':8,
            'Benelli':9,             'KTM':10,        'Mahindra':11,        'Kawasaki':12,
            'Ducati':13,         'Hyosung':14, 'Harley-Davidson':15,            'Jawa':16,
                'BMW':17,          'Indian':18,         'Rajdoot':19,             'LML':20,
            'Yezdi':21,              'MV':22,           'Ideal': 23 
    }

    brand_name = brand_dict.get(brand_name)
    pred = model.predict([[brand_name,owner,age , power ,kms_driven]])
    # print("Outcome :- ",[brand_name,owner,age , power ,kms_driven])
    print("Prediction:>>>>>>>>>>>",pred)
    return render_template("project.html",prediction = pred)



        
if __name__ == "__main__":
    app.run(debug = True)

# to run in terminal run py ./app.py
# then to close flask run ctrl+c
# also to run anything type /index after url