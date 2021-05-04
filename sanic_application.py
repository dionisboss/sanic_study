from sanic import Sanic

# create a sanic instance
app = Sanic("MyApp")

# Correct way to attach objects to the application
# app.ctx.db = Database()

# app registry
# ./path/to/sanic_application.py
app = Sanic("my_awesome_server")

# ./path/to/somewhere_else.py
app = Sanic.get_app("my_awesome_server")

# force create app if not existent
# app = Sanic.get_app(
#     "non-existing",
#     force_create=True,
# )

# configuration
app.config.DB_NAME = 'appdb'
app.config['DB_USER'] = 'appuser'

db_settings = {
    'DB_HOST': 'localhost',
    'DB_NAME': 'appdb',
    'DB_USER': 'appuser'
}
app.config.update(db_settings)
