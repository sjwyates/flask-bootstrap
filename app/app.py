from flask import Flask, request, render_template
from sassutils.wsgi import SassMiddleware


app = Flask(__name__)

app.wsgi_app = SassMiddleware(app.wsgi_app, {
    'app': ('static/scss', 'static/css', '/static/css')
})

@app.route("/")
def landing():
    return render_template('pages/landing.html.j2')


@app.route("/visualizations")
def visualizations():
    return render_template('pages/visualizations.html.j2')


@app.route("/comparisons")
def comparisons():
    return render_template('pages/comparisons.html.j2')


@app.route("/data")
def data():
    return render_template('pages/data.html.j2')


if __name__ == "__main__":
    app.run(debug=True)
