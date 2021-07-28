from config import db, ma


class Product(db.Model):
    """ Classe que define a estrutura dos objetos a serem salvos no Banco SQLite
    """
    __tablename__ = "product"
    product_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32))
    brand = db.Column(db.String(32))
    price = db.Column(db.Float)
    stock = db.Column(db.Integer)


class ProductSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        """  Classe do Marshmallow responsável por traduzir objetos JSON (Product) para o formato do SQLite
        """
        model = Product
        sqla_session = db.session
        include_relationships = True
        load_instance = True
