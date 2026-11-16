"""Load the saturated-water CSV tables.

CSV files (in the data/ folder):
    sat_water_SI.csv        columns: table, T_C, P_bar,  vf_m3_per_kg,  vg_m3_per_kg,  ...
    sat_water_English.csv   columns: table, T_F, P_psia, vf_ft3_per_lb, vg_ft3_per_lb, ...

The "table" column is "A-2"/"A-2E" for temperature-table rows and
"A-3"/"A-3E" for pressure-table rows. The last row of each table is the
critical point (vf = vg).
"""
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent.parent / "data"


def load_table(units):
    """Read the CSV for the chosen unit system ("SI" or "English").

    Returns the T, P, vf and vg data for the temperature table and for the
    pressure table.
    """
    # TODO: open the right CSV (csv module, numpy.genfromtxt, or pandas.read_csv)
    # TODO: split the rows by the "table" column
    # TODO: return the columns as arrays
    raise NotImplementedError


def Tsat(table, P):
    """Saturation temperature at pressure P."""
    # TODO: interpolate in the pressure table
    raise NotImplementedError


def Psat(table, T):
    """Saturation pressure at temperature T."""
    # TODO: interpolate in the temperature table
    raise NotImplementedError
