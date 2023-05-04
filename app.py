import process_data
from common import *

app = Flask(__name__, static_folder='static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    location = request.form['location']
    industry = request.form['industry']
    business_name = request.form['business-name']
    caption = request.form['caption']

    output = process_data.process_data(location, industry, business_name, caption)

    return jsonify({'hashtags':output})

if __name__ == '__main__':
    app.run(debug=True) # host='127.0.0.1', port=8000, 