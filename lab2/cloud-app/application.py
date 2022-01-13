from flask import Flask
from application.database import engine

# Elastic Beanstalk initalization
application = Flask(__name__)
application.debug = True
# change this to your own value
application.secret_key = 'cC1YCIWOj9GgWspgNEo2'


def index():
    data = engine.execute('select * from itsyaboi')

    return str(data)


if __name__ == '__main__':
    application.run()
