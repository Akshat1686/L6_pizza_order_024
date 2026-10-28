# L6_pizza_order_024 — Lab 6: Code and Branch Coverage

Pizza order application from SETAPESU26/L6_L7_24_pizza_order (Lab 6),
with code-coverage and branch-coverage test suites written for it.

## Files

| File | Description |
|---|---|
| `pizza_order.py` | Application under test (unchanged from the template) |
| `CodeCoverageTest_024_pizza_order.py` | 20 tests — code (line) coverage |
| `BranchCoverageTest_024_pizza_order.py` | 25 tests — branch coverage (core tests + boundary cases) |
| `screenshot_code_coverage.png` | Terminal output: code-coverage run |
| `screenshot_branch_coverage.png` | Terminal output: branch-coverage run |
| `Lab6_Coverage_Analysis.md` | Full analysis: initial vs final coverage, branch breakdown |

## Results (verified locally, Python 3.12.3, pytest 9.2.0, coverage 7.17.0)

- Starter tests: `pizza_order.py` 41% line / 34% branch
- Code coverage: 20 passed, **100% line coverage**
- Branch coverage: 25 passed, **100% line and 100% branch** (24 branches, 0 partial)

## Re-run

```bash
pip install coverage pytest
coverage run -m pytest CodeCoverageTest_024_pizza_order.py -v
coverage report -m
coverage run --branch -m pytest BranchCoverageTest_024_pizza_order.py -v
coverage report -m
```
