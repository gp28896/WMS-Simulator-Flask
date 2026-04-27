from app.repositories.json_repository import JSONRepository
from app.config import EVENTS_JSON


class EventRepository:


	def __init__(self):

		self.repo = JSONRepository(EVENTS_JSON)


	def log_event(self, event: dict):

		self.repo.append(event)


	def get_all_events(self):

		return self.repo.read()