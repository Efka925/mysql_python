from sqlalchemy import create_engine, Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import declarative_base

eng = create_engine("sqlite:///todo_app.db")
Base = declarative_base()


class TodoLists(Base):
    __tablename__ = "todo_lists"

    list_id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(255), nullable=False)


class TodoItems(Base):
    __tablename__ = "todo_items"

    TodoItems_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    list_id = Column(Integer, ForeignKey(
        "todo_lists.list_id", ondelete="CASCADE"))
    state = Column(Boolean, default=False)

    def __repr__(self):
        return f"{self.item_id}: {self.name}"

class ThingsToDo(Base):
    __tablename__ = "ThingsToDo"
    
    ThingsToDo_id= Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    list_id = Column(Integer, ForeignKey(
        "ThingsToDo.lists_id", ondelete="CASCADE"))
    state = Column(Boolean, default=False)

    def __repr__(self):
        return f"{self.item_id}: {self.name}"



