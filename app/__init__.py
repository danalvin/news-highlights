from flask import Flask
from flask_bootstrap import Bootstrap

bootstrap = Bootstrap()

def create_app(ocnfig_name):

    app = Flask(__name__)

    app.config.from_object(config_options[config_name])

    bootstrap.init_app(app)
    
from .main import main as main_blueprint
app.register_blueprint(main_blueprint)

from .request import configure_requests
configure_requests(app)

return app