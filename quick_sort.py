from threading import Thread
from typing import List


class QuickSort:
	def __init__(self, threshold: int = 10): 
		self._threshold = threshold


	def sort(self, arr: List[int]):
		self._quicksort(arr, 0, len(arr) - 1)


	def sort_multithreaded(self, arr: List[int]):
		self._quicksort_multithreaded(arr, 0, len(arr) - 1)


	def _quicksort_multithreaded(self, arr: List[int], left: int, right: int):
		if right - left + 1 < self._threshold:
			self._insertion_sort(arr, left, right)
		elif left < right:
			pivot = self._partition(arr, left, right)

			tleft = Thread(target=self._quicksort_multithreaded, args=(arr, left, pivot - 1))
			tright = Thread(target=self._quicksort_multithreaded, args=(arr, pivot + 1, right))

			tleft.start()
			tright.start()

			tleft.join()
			tright.join()


	def _quicksort(self, arr: List[int], left: int, right: int):
		if right - left + 1 < self._threshold:
			self._insertion_sort(arr, left, right)
		elif left < right:
			pivot = self._partition(arr, left, right)
			self._quicksort(arr, left, pivot - 1)
			self._quicksort(arr, pivot + 1, right)


	def _partition(self, arr, left, right) -> int:
		# use median of left, right, mid as pivot element
		mid = left + (right - left) // 2
		pivot, pivot_index = sorted([(arr[left], left), (arr[mid], mid), (arr[right], right)])[1]
		arr[right], arr[pivot_index] = pivot, arr[right]

		i = left  # pointer to element greater than pivot
		for j in range(i, right):
			if arr[j] <= pivot:
				arr[i], arr[j] = arr[j], arr[i]
				i += 1
		arr[i], arr[right] = arr[right], arr[i]
		return i


	def _insertion_sort(self, arr, left, right):
		for i, curr in enumerate(arr):
			j = i - 1
			while j >= 0 and curr < arr[j]: 
				arr[j + 1] = arr[j]
				j -= 1
			arr[j + 1] = curr