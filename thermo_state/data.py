"""Loads the saturated-water CSV tables.

CSV files (in the data/ folder):
    sat_water_SI.csv        columns: table, T_C, P_bar,  vf_m3_per_kg,  vg_m3_per_kg,  ...
    sat_water_English.csv   columns: table, T_F, P_psia, vf_ft3_per_lb, vg_ft3_per_lb, ...

The "table" column is "A-2"/"A-2E" for temperature-table rows and
"A-3"/"A-3E" for pressure-table rows. The last row of each table is the
critical point (vf = vg).
"""
from pathlib import Path
import numpy as np
import pandas as pd

DATA_DIR = Path(__file__).resolve().parent.parent / "data"
    

def load_table(units):
    """
    Returns the T, P, vf and vg data for the temperature table and for the
    pressure table.
    """
    # loads correct sat_water file based on user input
    if units == "SI":
        df = pd.read_csv(DATA_DIR / "sat_water_SI.csv")
    else:
        df = pd.read_csv(DATA_DIR / "sat_water_English.csv")
        
    # data preprocessing
    df = df.rename(columns = lambda name: name.split("_")[0])

    # splits dataframe into temperature and pressure tables
    t_rows = df[df["table"].str.startswith("A-2")].reset_index(drop = True)
    p_rows = df[df["table"].str.startswith("A-3")].reset_index(drop = True)

    # stores the critical values
    crit = p_rows.iloc[-1]
    
    # returns values from both tables
    return {
        "temperature": t_rows, 
        "pressure": p_rows,
        "T_crit": crit["T"],
        "P_crit": crit["P"],
        "v_crit": crit["vf"],
        "sat_tol": 0.5 if units == "SI" else 1.0
    }


def linear_interpolation(x, x_data, y_data):
    """
    Returns a linear interpolation between two x-values. Works with data from both temperature and pressure tables. 
    """
    # input validation
    if  x < x_data[0] or x > x_data[-1]:
        raise ValueError(f"{x} is outside the table range {x_data[0]} to {x_data[-1]}")
        
    # binary search, stores indexes
    low = 0
    high = len(x_data) - 1
    while high - low > 1:
        mid = (low + high) // 2
        if x_data[mid] < x:
            low = mid
        else:
            high = mid

    # linear interpolation between (x0, y0) and (x1, y1)
    x0, y0 = x_data[low], y_data[low]
    x1, y1 = x_data[high], y_data[high]
    return y0 + (x - x0) / (x1 - x0) * (y1 - y0)

def Tsat(table, P):
    """Saturation temperature at pressure P."""
    pr_t = table["pressure"]
    return linear_interpolation(P, pr_t["P"].to_numpy(), pr_t["T"].to_numpy())


def Psat(table, T):
    """Saturation pressure at temperature T."""
    tmp_t = table["temperature"]
    return linear_interpolation(tmp_t["T"].to_numpy(), tmp_t["P"].to_numpy())
