# Lab 6: Code and Branch Coverage Analysis — Pizza Order

**Application:** `pizza_order.py` from https://github.com/SETAPESU26/L6_L7_24_pizza_order (`Lab 6/`)
**Student:** Akshat Agarwal, PES1UG24AM024 — hence `024` in the test filenames
**Environment (verified locally, 28 Oct 2026):** Python 3.12.3, pytest 9.2.0, coverage 7.17.0
**Application file:** unchanged from the template repo. Only test files were added.

## What the code under test does

| Function | Branches that must be exercised |
|---|---|
| `pizza_price(size, toppings, is_cheese_burst)` | unknown size; negative toppings; toppings > 3 vs ≤ 3; cheese burst on/off; cheese burst on small |
| `order_discount(order_total, day, is_student)` | total < 300 early return; Tuesday; weekend; other weekday; student on/off |
| `delivery_status(minutes_taken, distance_km)` | distance > 10; ≤ 30 min; ≤ 45 min; otherwise |

## 1. Initial (starter) tests — before any new tests

Starter file: `test_pizza_order.py` (2 tests: plain medium pizza, on-time delivery).

```
coverage run -m pytest test_pizza_order.py
coverage report -m
# pizza_order.py:  34 stmts, 20 missed,  41% line
#                  missing: 6, 8, 11, 15-17, 22-32, 37, 40-42

coverage run --branch -m pytest test_pizza_order.py
coverage report -m
# pizza_order.py:  34 stmts, 20 missed, 24 branches, 6 partial,  34% branch
```

So the starter tests leave every discount branch, every error branch, the
>3-toppings tier, cheese burst, and the late / free-pizza paths untested.

## 2. Code coverage deliverable

**File:** `CodeCoverageTest_024_pizza_order.py` — 20 tests
**Commands:**
```
coverage run -m pytest CodeCoverageTest_024_pizza_order.py -v
coverage report -m
```
**Result (screenshot: `screenshot_code_coverage.png`):**
```
CodeCoverageTest_024_pizza_order.py   45 stmts  0 missed  100%
pizza_order.py                        34 stmts  0 missed  100%
TOTAL                                 79 stmts  0 missed  100%
20 passed
```
Every executable line runs at least once. Honest note: this file already
reaches 100% branch coverage too (24 branches, 0 partial), because its core
tests include both outcomes of the cheese-burst and student flags — line
coverage alone does not guarantee that in general, it just happens to here.

## 3. Branch coverage deliverable

**File:** `BranchCoverageTest_024_pizza_order.py` — 25 tests
(20 core tests + 5 `test_branch_*` additions)
**Commands:**
```
coverage run --branch -m pytest BranchCoverageTest_024_pizza_order.py -v
coverage report -m
```
**Result (screenshot: `screenshot_branch_coverage.png`):**
```
BranchCoverageTest_024_pizza_order.py  61 stmts  0 missed  0 branches  0 partial  100%
pizza_order.py                         34 stmts  0 missed  24 branches 0 partial  100%
TOTAL                                  95 stmts  0 missed  24 branches 0 partial  100%
25 passed
```
The 5 added tests are boundary cases, not filler: toppings 3 vs 4, total
exactly 300 (not < 300), total 299 with student (early return must ignore
the surcharge), minutes 30/31 and 45/46, distance 10 vs 11 km. They are the
cases that would catch an off-by-one change (`<` vs `<=`) even though the
headline percentage was already 100%.

## 4. Line vs branch — why both are required

Line coverage asks "did this line run once?"; branch coverage asks "did
every `if`/`elif` go both ways?". The handout's calculator example is the
same trap: one test can run every line while never taking the
`is_member == False` or `price <= 100` branch. Here, a test set that only
ever ordered cheese-burst pizzas would run the `price += 100` line but
never prove the no-cheese-burst path — branch coverage is what forces
that second outcome.

## 5. Commits (local, in this working copy — NOT pushed)

```
5f1fbdb Lab 6: add CodeCoverageTest_024_pizza_order (20 tests, 100% line coverage)
1b58c3e Lab 6: add BranchCoverageTest_024_pizza_order (25 tests, 100% branch coverage)
```

Commit 1 contains `pizza_order.py`, `CodeCoverageTest_024_pizza_order.py`
and `screenshot_code_coverage.png`. Commit 2 adds
`BranchCoverageTest_024_pizza_order.py` and
`screenshot_branch_coverage.png`.

Per the handout, only post-≥90% screenshots are included as submission
screenshots; the initial 41%/34% figures above are reported in text only.

## 6. How to re-run (in your own repo)

```
pip install coverage pytest
coverage run -m pytest CodeCoverageTest_024_pizza_order.py -v
coverage report -m
coverage run --branch -m pytest BranchCoverageTest_024_pizza_order.py -v
coverage report -m
```
