# Flask-Bootstrap Starter

## Overview

This is a starter repo for a simple Flask/Jinja app with Libsass and Bootstrap. It's designed for people new to web development who want to build cleaner, more modern web apps, but don't quite yet have the skills and background to know where to begin. Using it requires a decent understanding of Python, Flask and HTML/CSS.

What does it do for you? A couple things...

----

### Customizing Bootstrap:

I'm not exactly a Bootstrap evangelist, but I also cringe when people say it has no place in this world. Sure, you don't see large dev teams using it, but it's great for novice developers making their own small projects who *don't* have a mature UI team behind them.

You also often hear people say that all Bootstrap sites look the same, but that ignores the fact that Bootstrap provides their SCSS source code, with instructions on how to override their defaults. It requires a bit of setup, but here it's already set up for you, so you just have to fill in some blanks — eg, pick your colors and fonts:

- [coolors.co](https://coolors.co/)
- [Google Fonts](https://fonts.google.com/)

And substitute them into the `_variables.css` and `_typography.scss` files. For instance, if you don't really like how Bootstrap's `primary` buttons look, you can just plug in your own hex code, and now anytime you use `btn-primary` or `bg-primary`, it'll be your color — no custom CSS required. 

Here's some background reading on SCSS and customizing Bootstrap:

- [Writing SCSS](https://sass-lang.com/documentation)
- [Theming Bootstrap](https://getbootstrap.com/docs/4.0/getting-started/theming/)

----

### Jinja Templating:

If you're like me, you hate writing repetitive code, and you *really* hate scrolling `.html` files that are hundreds of lines long. Luckily, Flask comes with the Jinja templating engine built-in:

- [Templating with Jinja](https://jinja.palletsprojects.com/en/2.11.x/templates/)

For instance, you can have a base template with your `<head>` tag and all the boilerplate, then have all your files for your pages just *extend* from it, so all they need to contain is their own content. And if you have components you want to reuse multiple places, you can *include* them in as many places as you want.

And if you're getting data from a database or 3rd-party API that you want to display, you can inject that data straight into your HTML templates. You can even do *for* loops right in the template for making things like lists and table rows. You can also format the data, like for making names title case or formatting date strings.

## Installation

If this all sounds intimidating, it sort of is. However, the hard part's already done for you, so you don't have to know how it all works. Just a few simple steps and you'll be off and running.

First, clone the repo:

```
git clone https://github.com/sjwyates/flask-bootstrap.git
```

Then a couple of dependencies. Activate your environment, eg:

```
conda activate pythondata
```

And install a few things, if you don't have them:

```
pip install flask
pip install libsass
```

Then from the root directory, on Mac:

```
export FLASK_APP=app/app.py
export FLASK_ENV=development
```

Or on Windows:

```
set FLASK_APP=app/app.py
set FLASK_ENV=development
```

Then fire up the application:

```
flask run
```

It should now be running on [localhost:5000](http://127.0.0.1:5000/). Because you're in the development environment, Flask will watch for changes in any of your code and reload so you don't have to do it manually. Just save your changes, and you should see them next time you reload the browser.
