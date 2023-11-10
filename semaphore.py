from threading import Condition, Thread

class Semaphore:
	
	def __init__(self, max_permits: int):
		self._max_permits = max_permits
		self._permits = max_permits
		self._cv = Condition()


	def acquire(self):
		with self._cv:
			while self._permits < 1:
				self._cv.wait()

			self._permits -= 1
			self._cv.notify_all()

		
	def release(self):
		with self._cv:
			while self._permits == self._max_permits:
				self._cv.wait()
				
			self._permits += 1
			self._cv.notify_all()
