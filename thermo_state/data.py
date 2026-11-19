"""Loads the saturated-water CSV tables.

CSV files (in the data/ folder):
    sat_water_SI.csv        columns: table, T_C, P_bar,  vf_m3_per_kg,  vg_m3_per_kg,  ...
    sat_water_English.csv   columns: table, T_F, P_psia, vf_ft3_per_lb, vg_ft3_per_lb, ...

The "table" column is "A-2"/"A-2E" for temperature-table rows and
"A-3"/"A-3E" for pressure-table rows. The last row of each table is the
critical point (vf = vg).
"""
from pathlib import Path
import pandas as pd

DATA_DIR = Path(__file__).resolve().parent.parent / "data"


def load_table(units):
    """Read the CSV for the chosen unit system ("SI" or "English").

    Returns the T, P, vf and vg data for the temperature table and for the
    pressure table.
    """
    # opens correct sat_water file based on selected units
    if units == "SI":
        df = pd.read_csv(DATA_DIR / "sat_water_SI.csv")
    else:
        df = pd.read_csv(DATA_DIR / "sat_water_English.csv")
        
    # renames columns for reusability
    df = df.rename(columns = lambda name: name.split("_")[0])

    # splits dataframe into temperature and pressure tables
    t_rows = df[df["table"].str.startswith("A-2")
    p_rows = df[df["table"].str.startswith("A-3")
    
    # returns values from both tables
    return {"temperature": t_rows, "pressure": p_rows}


def Tsat(table, P):
    """Saturation temperature at pressure P."""
    # TODO: interpolate in the pressure table
    raise NotImplementedError


def Psat(table, T):
    """Saturation pressure at temperature T."""
    # TODO: interpolate in the temperature table
    raise NotImplementedError
