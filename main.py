"""Project Thermo State: draw the vapor dome of water for a given p and T.

Run with:  python main.py
"""
from thermo_state.data import load_table
from thermo_state.plotting import show_plots
from thermo_state.state import find_state


def main():
    # 1. Get the user input
    # TODO: ask for the unit system ("SI" or "English")
    # TODO: ask for pressure p1 and temperature T1; check they are valid numbers
    units = "SI"
    P1 = None
    T1 = None

    # 2. Load the saturated-water data
    table = load_table(units)

    # 3. Find the state of the water
    state_name = find_state(table, P1, T1)
    print("State of water:", state_name)

    # 4. Draw the p-v and T-v plots
    show_plots(table, P1, T1, state_name)


if __name__ == "__main__":
    main()
