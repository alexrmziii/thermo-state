"""Work out the state of water at the user's pressure p1 and temperature T1."""

from thermo_state.data import Tsat, vf_at_T, vg_at_t

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


def specific_volume(table, P1, T1, state, x = None):
    """Specific volume v used to place the point (P1, T1) on the plots."""
    R = table["R"]
    conversion = table["T_conversion"]

    if state == COMPRESSED:
        # assumption: v = vf(T) for compressed liquid
        return vf_at_T(table, T1)

    if state == SATURATED:
        # v = vf + x(vg - vf)
        vf = vf_at_T(table, T1)
        vg = vg_at_t(table, T1)
        return vf + x * (vg - vf)

    if state == SUPERHEATED and T1 < table["T_crit"]:
        # assumption: ideal gas along isobar starting from saturated vapor point
        T_sat = Tsat(table, P1)
        vg = vg_at_t(table, T_sat)
        return vg * (T1 + conversion) / (T_sat + conversion)

    # supercritical or superheated above T_crit: ideal gas law, v = RT/P
    return R * (T1 + conversion) / P1

