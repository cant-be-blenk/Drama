from files.__main__ import app, db_session, Base
from flask import g
from sqlalchemy import *
from sqlalchemy.orm import relationship

from events import EVENT_ACTIVE, loadModule

class Event(Base):

	__tablename__ = "event"
	id = Column(Integer, ForeignKey("users.id"), primary_key=True)

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

	def __repr__(self):
		return f"<Event(id={self.id})>"
		
def buildTable():
	if not EVENT_ACTIVE: return None
	
	print("building event table...")
	with app.app_context():
		g.db = db_session()
		loadModule("conf")

		Event.__table__.create(bind=g.db.bind, checkfirst=True)
		g.db.commit()
