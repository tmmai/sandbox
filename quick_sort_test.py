import unittest

from quick_sort import QuickSort


class QuickSortTest(unittest.TestCase):
	def test_quicksort_sequential_odd(self):
		arr = [3, 1, 2]
		QuickSort(threshold=0).sort(arr)
		self.assertEqual(arr, [1, 2, 3])

	def test_quicksort_sequential_even(self):
		arr = [3, 1]
		QuickSort(threshold=0).sort(arr)
		self.assertEqual(arr, [1, 3])

	def test_quicksort_sequential_increasing(self):
		arr = [1, 2, 3]
		QuickSort(threshold=0).sort(arr)
		self.assertEqual(arr, [1, 2, 3])

	def test_quicksort_sequential_decreasing(self):
		arr = [3, 2, 1]
		QuickSort(threshold=0).sort(arr)
		self.assertEqual(arr, [1, 2, 3])

	def test_quicksort_sequential_threshold(self):
		arr = [3, 1, 2, 4, 6, 5, 7, 9, 8, 10, 17, 12, 11, 14, 13, 19, 15, 16, 20, 18]
		QuickSort(threshold=5).sort(arr)
		self.assertEqual(arr, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])

	def test_quicksort_multithreaded(self):
		arr = [3, 1, 2, 4, 6, 5, 7, 9, 8, 10, 17, 12, 11, 14, 13, 19, 15, 16, 20, 18]
		QuickSort(threshold=5).sort_multithreaded(arr)
		self.assertEqual(arr, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])


if __name__ == "__main__":
	unittest.main()