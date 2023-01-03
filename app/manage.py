import os

from flask.cli import FlaskGroup

from app.create_app import create_app

try:
    environ = os.environ["FLASK_ENV"]
except KeyError:
    raise ValueError("You need to set FLASK_ENV.")

app = create_app(environ)
cli = FlaskGroup(app)

if __name__ == "__main__":
    cli()
    # app.run(host="0.0.0.0", debug=True)
