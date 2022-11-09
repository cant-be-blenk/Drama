from files.__main__ import app, db_session, Base, engine
from flask import g
from sqlalchemy import *
from sqlalchemy.orm import relationship

from events import EVENT_ACTIVE, load_module

class Event(Base):

	__tablename__ = "event"
	id = Column(Integer, ForeignKey("users.id"), primary_key=True)

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

	def __repr__(self):
		return f"<Event(id={self.id})>"
		
def build_table():
	if not EVENT_ACTIVE: return None
	
	if not inspect(engine).has_table("event", schema="public"):
		print("building event table...")
		with app.app_context():
			g.db = db_session()
			load_module("conf")

			Event.__table__.create(bind=g.db.bind, checkfirst=True)
			g.db.commit()
