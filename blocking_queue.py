from collections import deque
from threading import Condition
from typing import TypeVar


T = TypeVar("T")


class BlockingQueue:
	def __init__(self, capacity: int):
		self._q = deque()
		self._capacity = capacity
		self._cv = Condition()


	def __len__(self) -> int:
		return len(self._q)


	def append(self, item: T, timeout: int = -1):
		with self._cv:
			while len(self._q) == self._capacity: 
				self._cv.wait(timeout)

			if len(self._q) < self._capacity:
				self._q.append(item)
				self._cv.notify_all()


	def pop(self) -> T:
		with self._cv:
			while len(self._q) == 0:
				self._cv.wait()

			res = self._q.popleft()

			self._cv.notify_all()

			return res