"""Lab 6 - Code (line) coverage tests for pizza_order.py.

Goal: every executable line in pizza_order.py runs at least once
(>=90% line coverage; verified locally at 100% line coverage).

Naming: CodeCoverageTest_024_pizza_order.py
  024 = Akshat Agarwal, PES1UG24AM024
  pizza_order = application under test (from SETAPESU26/L6_L7_24_pizza_order)

Run (from this directory):
    coverage run -m pytest CodeCoverageTest_024_pizza_order.py -v
    coverage report -m
"""
import pytest

from pizza_order import pizza_price, order_discount, delivery_status


# --- pizza_price: sizes, topping tiers, cheese burst, errors ---------------
def test_plain_medium_pizza():
    assert pizza_price("medium", 0, False) == 350


def test_small_two_toppings_no_cheese():
    # 200 + 2*40
    assert pizza_price("small", 2, False) == 280


def test_large_three_toppings_no_cheese():
    # 500 + 3*40  (top of the <=3 tier)
    assert pizza_price("large", 3, False) == 620


def test_large_five_toppings_no_cheese():
    # 500 + 3*40 + (5-3)*30  (>3 tier)
    assert pizza_price("large", 5, False) == 680


def test_medium_cheese_burst():
    # 350 + 2*40 + 100
    assert pizza_price("medium", 2, True) == 530


def test_large_cheese_burst_no_toppings():
    # 500 + 0 + 100
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


# --- order_discount: all three day branches + student surcharge -----------
def test_discount_below_minimum_is_zero():
    # <300 returns 0 immediately, even on Tuesday
    assert order_discount(250, "tuesday", False) == 0


def test_discount_tuesday_half():
    assert order_discount(400, "tuesday", False) == 200


def test_discount_tuesday_half_plus_student():
    # 400//2 + 50
    assert order_discount(400, "tuesday", True) == 250


def test_discount_weekend_is_zero():
    assert order_discount(400, "saturday", False) == 0


def test_discount_weekend_student_only():
    # weekend discount 0, but student +50 still applies
    assert order_discount(500, "sunday", True) == 50


def test_discount_weekday_tenth():
    assert order_discount(400, "monday", False) == 40


def test_discount_weekday_tenth_plus_student():
    # 400//10 + 50
    assert order_discount(400, "wednesday", True) == 90


# --- delivery_status: every return path -----------------------------------
def test_delivery_not_deliverable_over_10km():
    assert delivery_status(20, 11) == "not deliverable"


def test_delivery_on_time():
    assert delivery_status(20, 3) == "on time"


def test_delivery_late():
    assert delivery_status(40, 5) == "late"


def test_delivery_free_pizza():
    assert delivery_status(60, 5) == "free pizza"
