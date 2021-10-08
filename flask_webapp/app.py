from flask import Flask

# import routes
from .views.index import bp as index_bp
from .views.about import bp as about_bp


app = Flask(__name__)


# draw blueprints from routes
app.register_blueprint(index_bp)
app.register_blueprint(about_bp)

