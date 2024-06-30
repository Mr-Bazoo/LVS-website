from flask import Flask, render_template
from routes.admin import admin_bp
from routes.api import api_bp
from database import init_db

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'

app.register_blueprint(admin_bp, url_prefix='/admin')
app.register_blueprint(api_bp, url_prefix='/api')

init_db()

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)