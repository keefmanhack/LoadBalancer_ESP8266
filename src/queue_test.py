import unittest
from queue import Queue

class TestQueue(unittest.TestCase):
	def test_enqueue(self):
		q = Queue(2)
		self.assertEqual(q.enqueue(1), True, "Should be True")

	def test_enqueue_full(self):
		q = Queue(1)
		q.enqueue(1);
		self.assertEqual(q.enqueue(2), False, "Should be True")

	def test_dequeue(self):
		q = Queue(1)
		q.enqueue(1)
		self.assertEqual(q.dequeue(), 1, "Should be 1")

	def test_dequeue_empty(self):
		q = Queue(1)
		self.assertEqual(q.dequeue(), False, "Should be False")



if __name__ == '__main__':
    unittest.main()
