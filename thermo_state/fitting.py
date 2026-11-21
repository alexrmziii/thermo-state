"""Curve-fitting methods from class, used to draw the "best fit" vapor dome."""
import numpy as np

def fit_curve(x, y, breaks, degree = 2, log_x = False):
    """Fit ln(y) against x (or ln x) with seperate polynomials on each piece

    breaks:  x values where one piece and the next starts. Returns a list of (x_low, x_high, coefficients), one entry per piece. 
    """
    x = np.asarray(x, dtype = float)
    y = np.asarray(y, dtype = float)
    edges = [x.min()] + list(breaks) + [x.max()]

    model = []
    for x_low, x_high in zip(edges[:-1], edges[1:]):
        in_piece = (x >= x_low) & (x <= x_high)
        X = np.log(x[in_piece]) if log_x else x[in_piece]
        coeffs = np.polyfit(X, np.log(y[in_piece]), degree)
        model.append((x_low, x_high, coeffs))
    return model


def evaluate_curve(model, x_new, log_x = False):
    """Evaluate a fitted curve at the points x_new."""
    x_new = np.asarray(x_new, dtype = float)
    y_new = np.empty_like(x_new)
    for i, (x_low, x_high, coeffs) in enumerate(model):
        if i == len(model) - 1:
            in_piece = x_new <= x_high
        else:
            in_piece = (x_new > x_low) & (x_new <= x_high)
        if i == len(model) - 1:
            in_piece = x_new > x_low
        X = np.log(x_new[in_piece]) if log_x else x_new[in_piece]
        y_new[in_piece] = np.exp(np.polyval(coeffs, X))

    return y_new

def fit_dome(x, vf, vg, breaks, v_crit, log_x = False, n = 300):
    """Fit both sides of the dome and return one continuous curve
    
    x is P (for P-v plot) or T (for T-v plot).
    """
    liquid = fit_curve(x, vf, breaks, log_x = log_x)
    vapor = fit_curve(x, vg, breaks, log_x = log_x)

    x_min, x_crit = float(np.min(x)), float(np.max(x))
    if log_x:
        x_new = np.geomspace(x_min, x_crit, n)
    else:
        x_new = np.linspace(x_min, x_crit, n)

    v_liq = evaluate_curve(liquid, x_new, log_x)
    v_vap = evaluate_curve(vapor, x_new, log_x)

    v_liq[-1] = v_crit
    v_vap[-1] = v_crit

    v_curve = np.concatenate([v_liq, v_vap[::-1]])
    x_curve = np.concatenate([x_new, x_new[::-1]])

    return v_curve, x_curve
