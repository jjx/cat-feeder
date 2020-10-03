from __future__ import absolute_import

from flask_script import Manager

from app.main.api.cat_feeder import cat_feeder_blueprint

from app.main import create_app

app = create_app()
app.register_blueprint(cat_feeder_blueprint)
app.app_context().push()
manager = Manager(app)


@manager.command
def run_app():
    app.run(host='0.0.0.0')


if __name__ == '__main__':
    manager.run()
