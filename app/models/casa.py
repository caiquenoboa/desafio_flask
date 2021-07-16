from app import db, ma


class Casa(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50))
    comodos = db.relationship('Comodo', backref='casa', lazy=True)
    bairro_id = db.Column(db.Integer, db.ForeignKey('bairro.id'),
        nullable=False)

    def __init__(self, name, bairro_id):
        self.name = name
        self.bairro_id = bairro_id


class CasasSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'bairro_id')


casa_schema = CasasSchema()
casas_schema = CasasSchema(many=True)