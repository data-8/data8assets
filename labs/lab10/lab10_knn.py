import numpy as np
from datascience import Table

def most_common(t, column_name):
  """
  Returns the most common value in column column_name in table t.  Ties are
  broken arbitrarily.
  """
  return t.group(column_name).sort("count", descending=True).column(0).item(0)

def make_knn_classifier(training_data, k):
  """
  training_data should be a table of training examples.  The first column 
  should be the true label of each example.  The other columns are features.
  
  Returns a classifier function that takes as its argument a row of features,
  like a row of training_data without the true label column.  The classifier
  function returns a label, the predicted label for the given row.
  """
  features = training_data.drop(0)
  
  def classify(row):
    row_array = np.array(row)
    def distance_to_row(training_row):
      return np.linalg.norm(row_array - training_row)
    distances = training_data.with_column("d", features.apply(distance_to_row))
    k_neighbors = distances.sort("d").take(range(k))
    return most_common(k_neighbors, 0)
  
  return classify
