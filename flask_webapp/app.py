from flask import Flask

# import routes
from .views.index import bp as index_bp
from .views.controls import bp as controls_bp


app = Flask(__name__)


# draw blueprints from routes
app.register_blueprint(index_bp)
app.register_blueprint(controls_bp)

