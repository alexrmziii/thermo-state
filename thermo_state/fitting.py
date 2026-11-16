"""Curve-fitting methods from class, used to draw the "best fit" vapor dome."""


def fit_curve(x, y):
    """Fit a curve to the data points (x, y).

    Returns something that can be evaluated at new x values
    (e.g. a function, or the coefficients of a polynomial).
    """
    # TODO: implement the curve-fitting method from class
    # Things to decide:
    #   - which method (polynomial regression, splines, ...)
    #   - fit the liquid side (vf) and vapor side (vg) separately, or as one curve?
    #   - v spans several orders of magnitude: fit v or log(v)?
    raise NotImplementedError


def evaluate_curve(model, x_new):
    """Evaluate a fitted curve at the points x_new."""
    # TODO
    raise NotImplementedError
