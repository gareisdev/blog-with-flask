from sqlalchemy import Integer, String, Text
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Post(db.Model):
    __tablename__ = 'posts'

    id = db.Column(Integer, primary_key=True)
    title = db.Column(String(100),nullable=False)
    description = db.Column(String(255))
    image = db.Column(String(255))
    content = db.Column(Text)

    def __repr__(self):
        return f""" 
            Titulo: {self.title}
            Descripcion: {self.description}
            URL de Imagen: {self.image} 
            Contenido: {self.content}

        """