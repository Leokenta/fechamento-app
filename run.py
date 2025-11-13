from app import create_app, db
from flask_migrate import upgrade

app = create_app()

# Atualiza o banco de dados antes de iniciar
with app.app_context():
    upgrade()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
