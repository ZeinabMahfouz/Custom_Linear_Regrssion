import numpy as np
def train_test_split_np(X, y=None, test_size=0.2, shuffle=True, random_seed=None):
  if not 0.0 < test_size < 1.0:
    raise ValueError(f"test_size must be between 0.0 and 1.0, got {test_size}")
  if random_seed is not None:
    np.random.seed(random_seed)
  if shuffle:
    indices = np.random.permutation(len(X))
  else:
    indices = np.arange(len(X))
  x_test_size = int(len(X) * test_size)
  test_indices = indices[:x_test_size]
  train_indices = indices[x_test_size:]
  if y is None:
    return X[train_indices], X[test_indices]
  else:
    return X[train_indices], y[train_indices], X[test_indices], y[test_indices]
if __name__ == "__main__":
  print("This is a utility module. Import train_test_split_np to use it.")