def prod_non_zero_diag(x):
  res = 1
  n = min (len(a), len(a[0]))
  for i in range(n):
      if a[i][i] != 0:
        res *= a[i][i]
        flag = 1
  return res



def are_multisets_equal(x, y):
    return sorted(x) == sorted(y)


def max_after_zero(x):
    ind = -1
    for i in range(len(x) - 1):
        if x[i] == 0 and (ind == -1 or x[i + 1] > x[ind]):
            ind = i + 1
    if ind == -1:
        return -1
    return x[ind]


def convert_image(img, coefs):
    """Sum up image channels with weights from coefs array

    input:
    img -- 3-d numpy array (H x W x 3)
    coefs -- 1-d numpy array (length 3)
    output:
    img -- 2-d numpy array

    Not vectorized implementation.
    """

    pass


def run_length_encoding(x):
    """Make run-length encoding.

    input:
    x -- 1-d numpy array
    output:
    elements, counters -- integer iterables

    Not vectorized implementation.
    """

    pass


def pairwise_distance(x, y):
    """Return pairwise object distance.

    input:
    x, y -- 2d numpy arrays
    output:
    distance array -- 2d numpy array

    Not vectorized implementation.
    """

    pass
