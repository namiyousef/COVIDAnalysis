import connexion


app = connexion.FlaskApp(__name__, specification_dir='api/specs/')
app.add_api('api.yaml')


flask_app = app.app

from app.controllers import test
flask_app.register_blueprint(test)