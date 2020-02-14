import math

# Code copied verbatim from:
# https://towardsdatascience.com/frawd-detection-using-benfords-law-python-code-9db8db474cf8
# (it's an awesome site).

# Benford's Law percentages for leading digits 1-9.
BENFORD = [30.1, 17.6, 12.5, 9.7, 7.9, 6.7, 5.8, 5.1, 4.6]


def count_first_digit(df, column):
  mask = df[column] > 1.0
  data = list(df[mask][column])
  for i in range(len(data)):
    while data[i] > 10:
      data[i] = data[i] / 10
  first_digits = [int(x) for x in sorted(data)]
  unique = set(first_digits)  # a list with unique values of     first_digit list
  data_count = []
  for i in unique:
    count = first_digits.count(i)
    data_count.append(count)
  total_count = sum(data_count)
  data_percentage = [(i / total_count) * 100 for i in data_count]
  return total_count, data_count, data_percentage


def get_expected_counts(total_count):
  """Return list of expected Benford's Law counts for total sample count."""
  return [round(p * total_count / 100) for p in BENFORD]


def chi_square_test(data_count, expected_counts):
  """Return boolean on chi-square test (8 degrees of freedom & P-val=0.05)."""
  chi_square_stat = 0  # chi square test statistic
  for data, expected in zip(data_count, expected_counts):
    chi_square = math.pow(data - expected, 2)
    chi_square_stat += chi_square / expected
  print("\nChi-squared Test Statistic = {:.3f}".format(chi_square_stat))
  print("Critical value at a P-value of 0.05 is 15.51.")
  return chi_square_stat < 15.51
