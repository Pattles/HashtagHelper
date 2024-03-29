import process_data
import os
from common import *
from werkzeug.middleware.proxy_fix import ProxyFix
from flask import Flask, request, render_template, jsonify, redirect

app = Flask(__name__, static_folder='static')
app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1, x_host=1)

# """
# Remove this comment before committing.
@app.before_request
def enforce_https():
    if not request.is_secure:
        secure_url = request.url.replace('http://', 'https://', 1)
        return redirect(secure_url, code=301)
# """

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
    host = os.environ.get('HOST', '0.0.0.0')
    port = int(os.environ.get('PORT', 5000)) # port 3000 // 5000
    app.run(host=host, port=port)

if __name__ == '__main__':
    run() 