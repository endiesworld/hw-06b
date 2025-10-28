# Triangle Classification - Test Report (Initial Implementation)

## Objective

Evaluate the correctness of `classifyTriangle(a, b, c)` from `Triangle.py` using an expanded set of unit tests without modifying the implementation.

## Scope and Constraints

- Only `TestTriangle.py` was updated. `Triangle.py` remained unchanged.
- Tests cover input validation, triangle validity, and classification into Equilateral, Isosceles, Scalene, and Right.

## Test Environment

- OS: Windows
- Python: `python -m unittest` (version not explicitly captured)
- Command executed: `python -m unittest TestTriangle`

## Test Design Summary

The following categories were tested:

- Input validation
  - Range: values must be in (0, 200]
  - Type: all sides must be integers (reject floats/strings)
  - Non-positive values: 0 and negatives rejected
- Triangle validity
  - Triangle inequality: sum of any two sides must be strictly greater than the third
  - Non-triangles: examples where sum of two <= third
- Classification
  - Equilateral: all sides equal
  - Isosceles: exactly two sides equal (positions permuted)
  - Scalene: all sides distinct
  - Right: Pythagorean triples with permutations (3-4-5, 5-12-13)
- Boundary tests: values at the upper limit (200)

## Test Cases Implemented

File: `TestTriangle.py`

- Existing tests retained:
  - Right triangles: (3,4,5), (5,3,4)
  - Equilateral: (1,1,1)
- Added tests:
  - Right permutations: all permutations of (3,4,5) and (5,12,13)
  - Isosceles variants: (2,2,3), (2,3,2), (3,2,2), (10,10,15)
  - Scalene: (2,3,4), (7,8,9)
  - Not a triangle: (1,1,3), (2,3,5), (10,1,1)
  - Invalid input - range: (0,1,1), (-1,2,3), (201,10,10), (10,201,10), (10,10,201)
  - Invalid input - type: (3.0,4,5), ('3',4,5), (3,4.5,5), (3,4,'5')
  - Boundary values: (200,200,200), (199,200,200), and a right triple within bounds (120,160,200)

## Execution Results (Raw)

```text
FF.EF.FFFF
======================================================================
ERROR: testInvalidInputsTypes (TestTriangle.TestTriangles.testInvalidInputsTypes)
Traceback (most recent call last):
  File "...TestTriangle.py", line 69, in testInvalidInputsTypes
    self.assertEqual(classifyTriangle('3',4,5), 'InvalidInput')
  File "...Triangle.py", line 28, in classifyTriangle
    if a > 200 or b > 200 or c > 200:
TypeError: '>' not supported between instances of 'str' and 'int'

======================================================================
FAIL: testBoundaryValues (TestTriangle.TestTriangles.testBoundaryValues)
Traceback (most recent call last):
  File "...TestTriangle.py", line 75, in testBoundaryValues
    self.assertEqual(classifyTriangle(200,200,200), 'Equilateral')
AssertionError: 'NotATriangle' != 'Equilateral'

======================================================================
FAIL: testEquilateralTriangles (TestTriangle.TestTriangles.testEquilateralTriangles)
Traceback (most recent call last):
  File "...TestTriangle.py", line 24, in testEquilateralTriangles
    self.assertEqual(classifyTriangle(1,1,1),'Equilateral')
AssertionError: 'NotATriangle' != 'Equilateral'

======================================================================
FAIL: testIsoscelesTriangles (TestTriangle.TestTriangles.testIsoscelesTriangles)
Traceback (most recent call last):
  File "...TestTriangle.py", line 41, in testIsoscelesTriangles
    self.assertEqual(classifyTriangle(2,2,3), 'Isosceles')
AssertionError: 'NotATriangle' != 'Isosceles'

======================================================================
FAIL: testRightTriangleA (TestTriangle.TestTriangles.testRightTriangleA)
Traceback (most recent call last):
  File "...TestTriangle.py", line 18, in testRightTriangleA
    self.assertEqual(classifyTriangle(3,4,5),'Right')
AssertionError: 'NotATriangle' != 'Right'

======================================================================
FAIL: testRightTriangleB (TestTriangle.TestTriangles.testRightTriangleB)
Traceback (most recent call last):
  File "...TestTriangle.py", line 21, in testRightTriangleB
    self.assertEqual(classifyTriangle(5,3,4),'Right')
AssertionError: 'NotATriangle' != 'Right'

======================================================================
FAIL: testRightTrianglePermutations (TestTriangle.TestTriangles.testRightTrianglePermutations)
Traceback (most recent call last):
  File "...TestTriangle.py", line 31, in testRightTrianglePermutations
    self.assertEqual(classifyTriangle(3,4,5), 'Right')
AssertionError: 'NotATriangle' != 'Right'

======================================================================
FAIL: testScaleneTriangles (TestTriangle.TestTriangles.testScaleneTriangles)
Traceback (most recent call last):
  File "...TestTriangle.py", line 49, in testScaleneTriangles
    self.assertEqual(classifyTriangle(2,3,4), 'Scalene')
AssertionError: 'NotATriangle' != 'Scalene'

----------------------------------------------------------------------
Ran 10 tests in 0.007s

FAILED (failures=7, errors=1)
```

## Results Summary

- Total tests: 10
- Passed: 2
- Failures: 7
- Errors: 1 (type error when a side is a string)

## Defect Observations (from failures/errors)

- Triangle inequality check is incorrect, causing valid triangles to be reported as `NotATriangle`.
- Equilateral check compares `a == b and b == a` (does not include `c`), so equilateral is misclassified.
- Right triangle logic uses linear terms like `(a*2)+(b*2)==(c*2)` instead of squares; and likely doesn't consider permutations.
- Scalene check lacks `a != c` (uses `a != b` twice).
- Spelling in the code suggests `'Isoceles'` (wrong) but our tests expect `'Isosceles'` (correct).
- Input validation performs range checks before type checks, causing a `TypeError` with non-integer inputs (e.g., `'3'`).

## Coverage and Adequacy

- Inputs: positive, zero, negative, over-200, non-integer types.
- Validity: multiple non-triangles and valid triangles tested.
- Classification: Equilateral, Isosceles, Scalene, and Right (including multiple Pythagorean triples and permutations).
- Boundary values: included at 200.

The current tests are adequate to reveal multiple defects in the initial implementation.

## Conclusion

The initial `Triangle.py` implementation fails the majority of the comprehensive tests, indicating several logic and validation defects. The next step is to fix `Triangle.py` so that all tests pass without changing the test expectations.

## Next Steps (for Part 2)

- Correct triangle inequality logic.
- Fix equilateral, isosceles, and scalene conditions (including string label spelling).
- Implement proper right-triangle detection using squares and all permutations.
- Reorder input validation to check types before range comparisons.
- Re-run the same test suite until green.
