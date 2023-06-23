import process_data
from common import *

app = Flask(__name__, static_folder='static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/404')
def error_page():
    return render_template('404.html')

@app.route('/hashtags')
def get_hashtags():
    # Retrieve the array of hashtags from your data source
    with open('data/hashtags.json', encoding='utf-8') as f:
        hashtags_json = json.load(f)

    industries = list(hashtags_json.keys())

    return jsonify(industries)

@app.route('/submit', methods=['POST'])
def submit():
    location = request.form['location']
    industry = request.form['industry']
    business_name = request.form['business-name']
    caption = request.form['caption']

    output = process_data.process_data(location, industry, business_name, caption)

    return jsonify({'hashtags':output})

def run():
    app.run(debug=True)

if __name__ == '__main__':
    run()