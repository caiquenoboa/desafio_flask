from app import db, ma


class Comodo(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    largura = db.Column(db.Integer, nullable = False)
    comprimento = db.Column(db.Integer, nullable = False)
    name = db.Column(db.String(50))
    casa_id = db.Column(db.Integer, db.ForeignKey('casa.id'),
        nullable=False)


    def __init__(self, largura, comprimento, name):
        self.largura = largura
        self.comprimento = comprimento
        self.name = name


class ComodosSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'largura', 'comprimento')


comodo_schema = ComodosSchema()
comodos_schema = ComodosSchema(many=True)


