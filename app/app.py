from flask import Flask, request, render_template
from sassutils.wsgi import SassMiddleware


app = Flask(__name__)

app.wsgi_app = SassMiddleware(app.wsgi_app, {
    'app': ('static/scss', 'static/css', '/static/css')
})

@app.route("/")
def home():
    return render_template('pages/landing.html.j2', message="hello world")


if __name__ == "__main__":
    app.run(debug=True)
