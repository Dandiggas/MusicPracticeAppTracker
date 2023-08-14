from sqlalchemy import Column, Integer, String, TIMESTAMP
from sqlalchemy.sql.expression import text
from database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, nullable=False)
    firstname = Column(String, nullable=False)
    lastname = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))
    
class Session(Base):
    __tablename__ = "session"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('Post.id'), nullable=False)
    instrument = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))   
    duration = Column(Integer, nullable=False)
    description = Column(String, nullable=False)

