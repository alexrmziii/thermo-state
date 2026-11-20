"""Work out the state of water at the user's pressure p1 and temperature T1."""

from thermo_state.data import Tsat

COMPRESSED = "COMPRESSED LIQUID"
SATURATED = "SAT. LIQUID-VAPOR"
SUPERHEATED = "SUPERHEATED VAPOR"
SUPERCRITICAL = "ABOVE CRITICAL POINT"

def find_state(table, P1, T1):
    """Return the state of water at (P1, T1) as one of the names above.

    Compare T1 with Tsat(P1):
        T1 < Tsat  ->  compressed liquid
        T1 = Tsat  ->  saturated liquid-vapor   (use a small tolerance)
        T1 > Tsat  ->  superheated vapor
    """

    T_crit = table["T_crit"]
    P_crit = table["P_crit"]

    # TODO: handle inputs above the critical point (no Tsat exists there)
    # TODO: handle inputs outside the range of the tables
    P_min = table["pressure"]["P"].iloc[0]
    T_min = table["temperature"]["T"].iloc[0]

    # below table values
    if P1 < P_min or T1 < T_min:
        raise ValueError(f"Input is below the table range P >= {P_min}, T >= {T_min}")

    # above both critical values
    if T1 >= T_crit and P1 >= P_crit:
        return SUPERCRITICAL

    # above one critical value
    if T1 >= T_crit:
        return SUPERHEATED
    elif P1 >= P_crit:
        return COMPRESSED

    # normal case
    T_sat = Tsat(table, P1)
    if abs(T1 - T_sat) <= table["sat_tol"]:
        return SATURATED
    elif T1 < T_sat:
        return COMPRESSED
    else:
        return SUPERHEATED


def specific_volume(table, P1, T1):
    """Specific volume v used to place the point (P1, T1) on the plots."""
    # TODO: decide what v to use in each region.
    #   - inside the dome p and T do not fix v (anywhere between vf and vg)
    #   - outside the dome the saturated tables alone do not give v
    raise NotImplementedError
