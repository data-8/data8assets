import datascience

# Minimizes a function that takes an array as its argument and
# returns a number.
def minimize(f, start=None, **vargs):
  def expanded_f(*args):
    return f(args)
  return datascience.minimize(expanded_f, start=start, method="L-BFGS-B", **vargs)
