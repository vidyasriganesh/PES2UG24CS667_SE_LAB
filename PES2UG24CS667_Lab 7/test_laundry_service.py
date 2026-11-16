import math
import string
from hypothesis import given, strategies as st
from laundry_service import parse_order, weight_average, payable_charge


# ---------- 1. "Never crash" fuzz tests ----------
@given(st.text() | st.none())
def test_parse_order_no_crash(s):
    try:
        parse_order(s)
    except Exception as e:
        assert False, f"parse_order crashed with {type(e).__name__}: {e}"


@given(st.text() | st.none())
def test_weight_average_no_crash(s):
    try:
        weight_average(s)
    except Exception as e:
        assert False, f"weight_average crashed with {type(e).__name__}: {e}"


@given(st.text() | st.none())
def test_payable_charge_no_crash(s):
    try:
        payable_charge(s)
    except Exception as e:
        assert False, f"payable_charge crashed with {type(e).__name__}: {e}"


# ---------- 2. Property tests (correct behaviour) ----------
@given(st.text(alphabet=string.ascii_letters, min_size=1),
       st.floats(min_value=0.01, max_value=1000))
def test_parse_order_valid_roundtrip(garment, kg):
    assert parse_order(f"{garment}:{kg}") == (garment.title(), kg)


@given(st.text())
def test_parse_order_result_is_valid_or_none(s):
    result = parse_order(s)
    if result is not None:
        garment, kg = result
        assert garment != "" and math.isfinite(kg) and kg > 0


@given(st.lists(st.integers(min_value=0, max_value=10**6), min_size=1))
def test_weight_average_is_true_mean(values):
    csv = ",".join(str(v) for v in values)
    assert math.isclose(weight_average(csv), sum(values) / len(values))


@given(st.text())
def test_weight_average_within_range_or_none(s):
    result = weight_average(s)
    assert result is None or (math.isfinite(result) and result >= 0)


@given(st.floats(min_value=0, max_value=1e6), st.floats(min_value=0, max_value=1e6))
def test_payable_charge_correct_and_non_negative(charge, discount):
    result = payable_charge(f"{charge}|{discount}")
    assert result >= 0
    assert math.isclose(result, max(charge * 1.18 - discount, 0), abs_tol=1e-6)


@given(st.text())
def test_payable_charge_never_negative_or_nan(s):
    result = payable_charge(s)
    assert result is None or (math.isfinite(result) and result >= 0)
