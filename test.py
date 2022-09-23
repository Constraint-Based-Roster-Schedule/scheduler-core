#! bin/python 
from sre_constants import ASSERT
import unittest as ut
from modeler import *

class TestModelParameter(ut.TestCase):
    def setUp(self) -> None:
        self.parameterHolder = ParameterHolder(4,3,5,1,2)

    def test_days(self):
        self.assertEqual (self.parameterHolder.days, 4, "days getter failed")
    
    def test_shifts(self) :
        self.assertEqual (self.parameterHolder.shifts, 3, "shifts getter failed")
    
    def test_nurses(self) :
        self.assertEqual (self.parameterHolder.doctors, 5, "doctors getter failed")

    def test_shift_capacity(self) :
        self.assertEqual (self.parameterHolder.shift_capacity, 1, "shift_capacity getter failed")
    
    def test_shifts_per_day(self) :
        self.assertEqual (self.parameterHolder.shift_limit, 2, "shift_limit per day getter failed" ) 
    
ut.main() 


        
    

