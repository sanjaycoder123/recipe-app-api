"""
Simple Test Code for Cals 
"""

from django.test import SimpleTestCase
from app import calc 

class CalsTest(SimpleTestCase):
    """Test the calc module."""

    def test_add_num(self):
        """Test adding number together"""
        res=calc.add(11,10)

        self.assertEqual(res, 21)

    def test_sub_num(self):
        """Test to substract two number"""
        res=calc.sub(15,10)
        self.assertEqual(res,5)    

