"""Checks to run once the functions are written:  python -m pytest

Add more as you go.
"""
import pytest
from thermo_state.data import Tsat, load_table
from thermo_state.state import COMPRESSED, SATURATED, SUPERHEATED, SUPERCRITICAL, find_state


def test_tsat_matches_table():
    table = load_table("SI")
    assert abs(Tsat(table, 10.0) - 179.9) < 0.1      # Table A-3: 10 bar


def test_states_at_1_bar():
    table = load_table("SI")
    assert find_state(table, 1.0, 20) == COMPRESSED
    assert find_state(table, 1.0, 99.63) == SATURATED
    assert find_state(table, 1.0, 200) == SUPERHEATED

@pytest.mark.parametrize("units, P1, T1, expected", [
    ("SI", 1.0, 20, COMPRESSED),
    ("SI", 1.0, 99.63, SATURATED),
    ("SI", 1.0, 200, SUPERHEATED),
    ("SI", 10, 400, SUPERHEATED),        # above T_crit, below P_crit
    ("SI", 250, 100, COMPRESSED),        # above P_crit, below T_crit
    ("SI", 250, 400, SUPERCRITICAL),
    ("Imperial", 14.696, 212, SATURATED),
])
def test_find_state(units, P1, T1, expected):
    assert find_state(load_table(units), P1, T1) == expected


def test_below_table_raises():
    with pytest.raises(ValueError):
        find_state(load_table("SI"), 0.001, 20)