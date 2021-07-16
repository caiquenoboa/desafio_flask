import datetime
from app import db, ma


class Casa(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50))
    comodos = db.relationship('Comodo', backref='casa', lazy=True)

    def __init__(self, name, comodos):
        self.comodos = comodos
        self.name = name


class CasasSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'comodos')


casa_schema = CasasSchema()
casas_schema = CasasSchema(many=True)