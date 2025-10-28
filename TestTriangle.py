
# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation
@author: jrr
@author: rk
"""
import unittest
from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
# define multiple sets of tests as functions with names that begin
    def testRightTriangleA(self):
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def testRightTriangleB(self):
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')

    def testEquilateralTriangles(self):
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')
    
    # Additional comprehensive tests below
    
    # Right triangle permutations and additional triples
    def testRightTrianglePermutations(self):
        # 3-4-5 permutations
        self.assertEqual(classifyTriangle(3,4,5), 'Right')
        self.assertEqual(classifyTriangle(4,5,3), 'Right')
        self.assertEqual(classifyTriangle(5,3,4), 'Right')
        # 5-12-13 permutations
        self.assertEqual(classifyTriangle(5,12,13), 'Right')
        self.assertEqual(classifyTriangle(12,13,5), 'Right')
        self.assertEqual(classifyTriangle(13,5,12), 'Right')

    # Isosceles triangles in various positions
    def testIsoscelesTriangles(self):
        self.assertEqual(classifyTriangle(2,2,3), 'Isosceles')
        self.assertEqual(classifyTriangle(2,3,2), 'Isosceles')
        self.assertEqual(classifyTriangle(3,2,2), 'Isosceles')
        # Another set
        self.assertEqual(classifyTriangle(10,10,15), 'Isosceles')

    # Scalene triangles
    def testScaleneTriangles(self):
        self.assertEqual(classifyTriangle(2,3,4), 'Scalene')
        self.assertEqual(classifyTriangle(7,8,9), 'Scalene')

    # Not a triangle due to triangle inequality (sum of two <= third)
    def testNotATriangle(self):
        self.assertEqual(classifyTriangle(1,1,3), 'NotATriangle')  # 1+1 == 2 < 3
        self.assertEqual(classifyTriangle(2,3,5), 'NotATriangle')  # 2+3 == 5
        self.assertEqual(classifyTriangle(10,1,1), 'NotATriangle') # 1+1 < 10

    # Invalid inputs: out of range, zero, negative
    def testInvalidInputsRange(self):
        self.assertEqual(classifyTriangle(0,1,1), 'InvalidInput')
        self.assertEqual(classifyTriangle(-1,2,3), 'InvalidInput')
        self.assertEqual(classifyTriangle(201,10,10), 'InvalidInput')
        self.assertEqual(classifyTriangle(10,201,10), 'InvalidInput')
        self.assertEqual(classifyTriangle(10,10,201), 'InvalidInput')

    # Invalid inputs: non-integer types
    def testInvalidInputsTypes(self):
        self.assertEqual(classifyTriangle(3.0,4,5), 'InvalidInput')
        self.assertEqual(classifyTriangle('3',4,5), 'InvalidInput')
        self.assertEqual(classifyTriangle(3,4.5,5), 'InvalidInput')
        self.assertEqual(classifyTriangle(3,4,'5'), 'InvalidInput')

    # Boundary values at the upper limit
    def testBoundaryValues(self):
        self.assertEqual(classifyTriangle(200,200,200), 'Equilateral')
        self.assertEqual(classifyTriangle(199,200,200), 'Isosceles')
        # A valid right triangle near the limit but within bounds
        self.assertEqual(classifyTriangle(120,160,200), 'Right')
        
if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
