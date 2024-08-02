
from sqlalchemy import Column, Integer, String
from models.base import Base


class Employee(Base):
    __tablename__ = "employee"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, default="NaN")
    position = Column(String)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "position": self.position
        }
