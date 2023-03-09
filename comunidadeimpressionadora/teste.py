from comunidadeimpressionadora import app, database
from comunidadeimpressionadora.models import Usuario
from flask_login import login_user, logout_user, current_user, login_required


#with app.app_context():
#     database.drop_all()
#     database.create_all()
with app.app_context():
    usuario = Usuario.query.filter_by(email='dudu@gmail.com').first()
    print(usuario.cursos)
