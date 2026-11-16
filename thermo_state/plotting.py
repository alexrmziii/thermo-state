"""Draw the two plot windows: p-v and T-v (see docs/project_sketch.png)."""
import matplotlib.pyplot as plt


def plot_pv(ax, table, P1, T1, state_name):
    """Draw the p-v diagram on the matplotlib axes ax."""
    # TODO: plot the pressure-table data points (vf and vg against P)
    # TODO: plot the best-fit curve through them (fitting.py)
    # TODO: plot the isotherm for T1 (curves.py)
    # TODO: plot the point (P1, T1)
    # TODO: display state_name in a box
    # TODO: axis labels with units
    raise NotImplementedError


def plot_tv(ax, table, P1, T1, state_name):
    """Draw the T-v diagram on the matplotlib axes ax."""
    # TODO: same steps as plot_pv, with the temperature table and the isobar for P1
    raise NotImplementedError


def show_plots(table, P1, T1, state_name):
    """Create both plots and show them."""
    fig, (ax_pv, ax_tv) = plt.subplots(1, 2, figsize=(13, 6))
    plot_pv(ax_pv, table, P1, T1, state_name)
    plot_tv(ax_tv, table, P1, T1, state_name)
    plt.show()
