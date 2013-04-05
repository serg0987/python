# -*- coding: utf-8 -*-
'''
weakref — Weak references
link: http://docs.python.org/2/library/weakref.html
'''


import unittest
from weakref import WeakSet


class Object:
    pass


class TestWeakSet(unittest.TestCase):
    def test_len(self):
        obj = Object()
        obj2 = Object()
        ws = WeakSet()
        ws.add(obj)
        self.assertEqual(len(ws), 1)
        ws.add(obj2)
        self.assertEqual(len(ws), 2)
        del obj
        self.assertEqual(len(ws), 1)
        self.assertIn(obj2, ws)

if __name__ == '__main__':
    unittest.main()
