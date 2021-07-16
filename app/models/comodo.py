from app import db, ma


class Comodo(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    largura = db.Column(db.Integer, nullable = False)
    comprimento = db.Column(db.Integer, nullable = False)
    name = db.Column(db.String(50))
    casa_id = db.Column(db.Integer, db.ForeignKey('casa.id'),
        nullable=False)
    area = 0
    


    def __init__(self, largura, comprimento, name, casa_id):
        self.largura = largura
        self.comprimento = comprimento
        self.name = name
        self.casa_id = casa_id
        self.area = self.calcula_area()

    def calcula_area(self):
        return self.comprimento * self.largura

    


class ComodosSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'largura', 'comprimento', 'casa_id', 'area')


comodo_schema = ComodosSchema()
comodos_schema = ComodosSchema(many=True)


