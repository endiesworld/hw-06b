# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 13:44:00 2016
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple python program to classify
triangles
@author: jrr
@author: rk
"""
def classifyTriangle(a, b, c):
    """
    Classify a triangle by side lengths.

    Returns one of:
    - 'InvalidInput' for values not integers or out of allowed range (1..200)
    - 'NotATriangle' if the sides do not satisfy triangle inequality
    - 'Right' if it's a right triangle (Pythagorean), regardless of other type
    - 'Equilateral' if all three sides are equal
    - 'Isosceles' if exactly two sides are equal
    - 'Scalene' if all sides are different
    """
    # verify that all 3 inputs are integers first to avoid TypeError in comparisons
    if not (isinstance(a, int) and isinstance(b, int) and isinstance(c, int)):
        return 'InvalidInput'

    # require that the input values be > 0 and <= 200
    if a <= 0 or b <= 0 or c <= 0:
        return 'InvalidInput'
    if a > 200 or b > 200 or c > 200:
        return 'InvalidInput'

    # sort the sides to simplify inequality and right-triangle checks
    x, y, z = sorted((a, b, c))  # x <= y <= z

    # triangle inequality: sum of two smallest must be strictly greater than largest
    if x + y <= z:
        return 'NotATriangle'

    # right triangle check using Pythagorean theorem
    if x * x + y * y == z * z:
        return 'Right'

    # classify by equality
    if a == b == c:
        return 'Equilateral'
    if a == b or b == c or a == c:
        return 'Isosceles'
    return 'Scalene'