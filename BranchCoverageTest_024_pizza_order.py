"""Lab 6 - Branch coverage tests for pizza_order.py.

Goal: every branch (both outcomes of every if/elif) is taken at least once
(>=90% branch coverage; verified locally at 100% line AND 100% branch).

This file is a superset of CodeCoverageTest_024_pizza_order.py: it keeps all
of those tests and adds the branch-only cases at the end (marked BRANCH-ADD).
Those additions are exactly the outcomes line coverage alone can miss:
  * is_cheese_burst == False (no else-line exists, so line coverage hides it)
  * is_student == False after a discount is computed
  * boundary values: toppings == 3 vs 4, total == 300, minutes == 30 vs 31
    and 45 vs 46, distance == 10 vs 11

Naming: BranchCoverageTest_024_pizza_order.py
  024 = Akshat Agarwal, PES1UG24AM024
  pizza_order = application under test (from SETAPESU26/L6_L7_24_pizza_order)

Run (from this directory):
    coverage run --branch -m pytest BranchCoverageTest_024_pizza_order.py -v
    coverage report -m
"""
import pytest

from pizza_order import pizza_price, order_discount, delivery_status


# --- pizza_price ------------------------------------------------------------
def test_plain_medium_pizza():
    assert pizza_price("medium", 0, False) == 350


def test_small_two_toppings_no_cheese():
    assert pizza_price("small", 2, False) == 280


def test_large_three_toppings_no_cheese():
    assert pizza_price("large", 3, False) == 620


def test_large_five_toppings_no_cheese():
    assert pizza_price("large", 5, False) == 680


def test_medium_cheese_burst():
    assert pizza_price("medium", 2, True) == 530


def test_large_cheese_burst_no_toppings():
    assert pizza_price("large", 0, True) == 600


def test_unknown_size_raises():
    with pytest.raises(ValueError):
        pizza_price("extra-large", 1, False)


def test_negative_toppings_raises():
    with pytest.raises(ValueError):
        pizza_price("medium", -1, False)


def test_cheese_burst_small_raises():
    with pytest.raises(ValueError):
        pizza_price("small", 1, True)


# --- order_discount ---------------------------------------------------------
def test_discount_below_minimum_is_zero():
    assert order_discount(250, "tuesday", False) == 0


def test_discount_tuesday_half():
    assert order_discount(400, "tuesday", False) == 200


def test_discount_tuesday_half_plus_student():
    assert order_discount(400, "tuesday", True) == 250


def test_discount_weekend_is_zero():
    assert order_discount(400, "saturday", False) == 0


def test_discount_weekend_student_only():
    assert order_discount(500, "sunday", True) == 50


def test_discount_weekday_tenth():
    assert order_discount(400, "monday", False) == 40


def test_discount_weekday_tenth_plus_student():
    assert order_discount(400, "wednesday", True) == 90


# --- delivery_status --------------------------------------------------------
def test_delivery_not_deliverable_over_10km():
    assert delivery_status(20, 11) == "not deliverable"


def test_delivery_on_time():
    assert delivery_status(20, 3) == "on time"


def test_delivery_late():
    assert delivery_status(40, 5) == "late"


def test_delivery_free_pizza():
    assert delivery_status(60, 5) == "free pizza"


# --- BRANCH-ADD: outcomes line coverage alone does not force --------------
def test_branch_toppings_boundary_four_vs_three():
    # toppings == 4 takes the >3 branch with exactly one discounted topping
    # 500 + 120 + 1*30
    assert pizza_price("large", 4, False) == 650
    # and 0 toppings with cheese False explicitly takes is_cheese_burst False
    assert pizza_price("small", 0, False) == 200


def test_branch_discount_exactly_300_not_below_minimum():
    # order_total < 300 is False at exactly 300, so discount still applies
    assert order_discount(300, "monday", False) == 30
    assert order_discount(300, "tuesday", False) == 150


def test_branch_discount_below_minimum_ignores_student():
    # early return: student surcharge must NOT apply below 300
    assert order_discount(299, "monday", True) == 0


def test_branch_delivery_time_boundaries():
    assert delivery_status(30, 5) == "on time"   # <=30 True (boundary)
    assert delivery_status(31, 5) == "late"      # <=30 False, <=45 True
    assert delivery_status(45, 5) == "late"      # <=45 True (boundary)
    assert delivery_status(46, 5) == "free pizza"  # <=45 False


def test_branch_delivery_distance_boundary():
    # distance > 10 is False at exactly 10 km: still deliverable
    assert delivery_status(20, 10) == "on time"
    assert delivery_status(60, 10) == "free pizza"
