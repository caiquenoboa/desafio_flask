from app import db, ma


class Bairro(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50))
    preco_por_metro = db.Column(db.Integer, nullable = False)
    casas = db.relationship('Casa', backref='bairro', lazy=True)

    def __init__(self, name, preco_por_metro):
        self.name = name
        self.preco_por_metro = preco_por_metro


class BairrosSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'preco_por_metro')


bairro_schema = BairrosSchema()
bairros_schema = BairrosSchema(many=True)