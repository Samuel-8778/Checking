from app import app
from flask_sqlalchemy import SQLAlchemy
from flask_mongoengine import MongoEngine
import pymysql
from flask_swagger_ui import get_swaggerui_blueprint
from jaeger_client import Config
from flask_opentracing import FlaskTracing
import logging


pymysql.install_as_MySQLdb()
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:sam8778@localhost/project1'
app.config['SECRET_KEY'] = 'ejf202hhv39fec03333942'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
SWAGGER_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "First App "

    }
)
app.register_blueprint(SWAGGER_BLUEPRINT, url_prefix=SWAGGER_URL)

app.config['MONGODB_SETTINGS'] = {
    'db': 'project',
    'host': 'localhost',
    'port': 27017
}
db1 = MongoEngine()
db.init_app(app)


def initialize_tracer():
    config = Config(
        config={
            'sampler': {'type': 'const', 'param': 10}
        },
        service_name='MATCpro')
    return config.initialize_tracer()


flask_tracer = FlaskTracing(initialize_tracer, True, app)

# logging config

logging.basicConfig(format="%(asctime)s %(message)s")   # filename='res.log'
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
