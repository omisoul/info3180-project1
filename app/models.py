from . import db
# from sqlalchemy import Integer

class Property(db.Model):
    """The database model used for property information."""

    __tablename__ = 'properties'

    """ Property Attributes """
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150))
    noBedrooms = db.Column(db.Integer)
    noBathrooms = db.Column(db.Integer)
    location = db.Column(db.String(150))
    price = db.Column(db.Numeric(10, 2))
    description = db.Column(db.String(500))
    photoFileName = db.Column(db.String(255))
    propertyType = db.Column(db.String(20))


    def __init__(self, title, description, noBedrooms, noBathrooms, price, propertyType, location, photoFileName):
        super().__init__()
        
        self.title = title
        self.noBedrooms = noBedrooms
        self.noBathrooms = noBathrooms
        self.location = location
        self.price = price
        self.description = description
        self.photoFileName = photoFileName
        self.propertyType = propertyType