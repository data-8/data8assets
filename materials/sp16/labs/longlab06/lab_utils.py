import numpy as np

def repeat(f, num_repetitions):
  """
  Call f() many times, producing an array of the results.
  
  Useful for simulations, where f produces random results.
  
  Example:
  
  >>> def one(): return 1
  >>> repeat(one, 4)
  array([1, 1, 1, 1])
  """
  return np.array([f() for i in range(num_repetitions)])

def proportion_where(table, condition):
  return table.where(condition).num_rows / table.num_rows

def random_sample_counts(table, population_weight_column_name, sample_size):
  return table.sample_from_distribution(population_weight_column_name, sample_size)\
              .relabeled(table.num_columns, "Count in Random Sample")

def random_sample_proportions(table, population_weight_column_name, sample_size):
  return table.sample_from_distribution(population_weight_column_name, sample_size, proportions=True)\
              .relabeled(table.num_columns, "Proportion in Random Sample")

