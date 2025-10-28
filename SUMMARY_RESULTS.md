# Triangle Classification – Summary Results

This document summarizes the two test runs (before and after fixes to `classifyTriangle`) and explains the strategy used to decide when the test set was sufficient.

## Results Matrix

|                     | Test Run 1 (Before Fix) | Test Run 2 (After Fix) |
|---------------------|--------------------------|-------------------------|
| Tests Planned       | 28                       | 28                      |
| Tests Executed      | 28                       | 28                      |
| Tests Passed        | 10                       | 28                      |
| Defects Found       | 6                        | 0                       |
| Defects Fixed       | 0                        | 6                       |

Notes

- “Tests Planned/Executed” are counted by individual test cases listed in the CSV reports (each assertion-level case), not by unittest methods.
- Test Run 1 references the original, buggy implementation; Test Run 2 references the corrected implementation.

Artifacts

- Initial run details: `TEST_REPORT_TABLE.csv`
- After-fix run details: `TEST_REPORT_TABLE_AFTER_FIX.csv`

## Test Sufficiency Strategy

To determine a sufficient set of test cases, I used a mix of black-box techniques that target both input validation and behavior classification:

1. Equivalence Partitioning

   - Inputs partitioned into valid triangles vs non-triangles, and invalid inputs (type/range).
   - Within valid triangles, partitions for Equilateral, Isosceles, Scalene, and Right.

2. Boundary Value Analysis

   - Range boundaries: 0, 1, and 200, plus out-of-range (e.g., 201) to verify limits.
   - Triangle inequality boundaries where x + y == z and just under/over the threshold.

3. Representative Right-Triangle Triples and Permutations

   - Classic Pythagorean triples: (3,4,5) and (5,12,13).
   - All permutations to ensure order independence.

4. Negative and Robustness Tests

   - Non-integer types (float/string) to validate strict typing.
   - Explicit non-triangles (sum of two <= third).

5. Orthogonality and Minimal Set

   - Ensure at least one representative per class and boundary, avoiding redundant cases unless needed to expose order/permutation issues.

Exit Criteria

- Every partition and boundary condition had at least one test.
- All expected labels observed at least once (InvalidInput, NotATriangle, Right, Equilateral, Isosceles, Scalene).
- Permutation coverage for Right triangles confirmed order irrelevance.
- After fixes, all planned tests passed with no residual failures.
