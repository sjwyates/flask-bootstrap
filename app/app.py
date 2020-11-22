from flask import Flask, request, render_template
from sassutils.wsgi import SassMiddleware


app = Flask(__name__)

app.wsgi_app = SassMiddleware(app.wsgi_app, {
    'app': ('static/scss', 'static/css', '/static/css')
})

@app.route("/")
def home():
    return render_template('index.html')