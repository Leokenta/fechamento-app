from app import db
from datetime import datetime

class Fechamento(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cliente = db.Column(db.String(100), nullable=False)
    data = db.Column(db.Date, nullable=False)
    quantidade = db.Column(db.Float, default=0)
    cor = db.Column(db.String(50), default='')
    descricao = db.Column(db.Text, nullable=False)
    desconto = db.Column(db.Float, default=0)
    valor_unitario = db.Column(db.Float, default=0)
    criado_em = db.Column(db.DateTime, default=datetime.now)

    @property
    def valor_total_sem_desconto(self):
        return self.quantidade * self.valor_unitario

    @property
    def valor_total_final(self):
        return self.valor_total_sem_desconto - self.desconto
