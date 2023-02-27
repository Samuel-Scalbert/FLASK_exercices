from ..app import app, db

table_de_relation_map_country = db.Table(
    "country_map",
    db.Column('map_ref',db.String(100), db.ForeignKey('map.name')),
    db.Column('id',db.String(100), db.ForeignKey('country.id')))

class Country(db.Model):
    __tablename__ = "country"
    id = db.Column(db.String(10), primary_key=True)
    Introduction = db.Column(db.Text)
    name = db.Column(db.String(500), unique=True, nullable=False)
    type = db.Column(db.String(100))

    aeras = db.relationship(
        "Aera", backref='aeras',
        lazy="dynamic"
    )

    maps = db.relationship(
        "Map",secondary=table_de_relation_map_country,
        backref='maps',
        lazy="dynamic"
    )
    def __repr__(self):
        return '<Country %r>'% (self.name)

class Map(db.Model):
    __tablename__ = "map"
    name = db.Column(db.Text, primary_key=True)
class Aera(db.Model):
    __tablename__ = "aera"
    id = db.Column(db.String(10), db.ForeignKey('country.id'))
    aera_comparative = db.Column(db.Text)
    total = db.Column(db.String(100), primary_key=True)
    land = db.Column(db.String(100))
    water = db.Column(db.String(100))
    note = db.Column(db.String(100))

    def __repr__(self):
        return '<Area %r>' % (self.total)
