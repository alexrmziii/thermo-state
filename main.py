"""Project Thermo State: draw the vapor dome of water for a given p and T.

Run with:  python main.py
"""
from thermo_state.data import load_table
from thermo_state.plotting import show_plots
from thermo_state.state import SATURATED
from thermo_state.state import find_state

UNIT_LABELS = {
    "SI": {"T": "°C", "P": "bar"},
    "Imperial": {"T": "°F", "P": "psia"},
}


def ask_units():
    answer = input("Which unit system are you using? (SI/Imperial)").strip().lower()
    while answer not in ["si", "imperial"]:
        answer = input("Invalid input. Enter \"SI\" or \"Imperial\" (case-insensitive).").strip().lower()  
    if answer == "si":
        return "SI"
    else:
        return "Imperial"


def ask_value(prompt):
    while True:
        try:
            answer = float(input(prompt))
            break
        except ValueError:
            print("Please enter a number.")


def ask_quality():
    """Asks for the quality x until a value between 0 and 1 is entered."""
    while True:
        x = ask_value("Mixture is saturated. Enter a quality x (0 to 1): ")
        if 0 <= x <= 1:
            return x
        else:
            print("Quality must be between 0 and 1.")


def main():
    # 1. gets the user input
    units = ask_units()
    labels = UNIT_LABELS[units]
    
    P1 = ask_value(f"Enter a pressure P1 [{labels['P']}]: ")
    T1 = ask_value(f"Enter a temperature T1 [{labels['T']}]: ")
    
    # 2. loads the saturated-water data
    table = load_table(units)

    # 3. finds the state of the water (and quality if saturated)
    state = find_state(table, P1, T1)
    print("State of water:", state)

    x = None
    if state == SATURATED:
        x = ask_quality()

    # 4. draws the p-v and T-v plots
    show_plots(table, P1, T1, state)


if __name__ == "__main__":
    main()
