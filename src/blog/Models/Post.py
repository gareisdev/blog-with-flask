from sqlalchemy import Integer, String, Text, Integer, DateTime, ForeignKey
from flask_sqlalchemy import SQLAlchemy
from blog import db
import datetime


class Post(db.Model):
    __tablename__ = 'posts'

    id = db.Column(Integer, primary_key=True)
    slug = db.Column(String(100),nullable=False, unique=True)
    title = db.Column(String(100),nullable=False)
    description = db.Column(String(255))
    image = db.Column(String(255))
    content = db.Column(Text)
    creation_date = db.Column(DateTime(timezone=True), default=datetime.datetime.now().replace(microsecond=0))
    author_id = db.Column(Integer, ForeignKey('users.id'))

    def __repr__(self):
        return f""" 
            Titulo: {self.title}
            Descripcion: {self.description}
            URL de Imagen: {self.image} 
            Contenido: {self.content}
        """