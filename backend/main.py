import os

from flask_script import Manager, Server
from flask_script.commands import ShowUrls, Clean
from flask_migrate import Migrate, MigrateCommand

from app import create_app
from app.models import db, Version, User

# default to dev config because no one should use this in
# production anyway
env = os.environ.get('APP_ENV', 'dev')
app = create_app('app.settings.%sConfig' % env.capitalize())

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command("server", Server())
manager.add_command("show-urls", ShowUrls())
manager.add_command("clean", Clean())
manager.add_command("db", MigrateCommand)
manager.add_command("runserver", Server(host="0.0.0.0", port=5000))


@manager.command
def createdb():
    """ Creates a database with all of the tables defined in
        your SQLAlchemy models
    """

    db.create_all()

    # Version and User added manually at DB creation (this is used only for the skeleton example)
    v = Version()
    v.version = '0.1'
    v.latest = True
    db.session.add(v)
    u = User()
    u.name = 'Tiago Reichert'
    u.email = 'tiago@reichert.eti.br'
    db.session.add(u)
    u = User()
    u.name = 'Foo Bar'
    u.email = 'foo@bar.something'
    db.session.add(u)
    db.session.commit()


if __name__ == '__main__':
    manager.run()
