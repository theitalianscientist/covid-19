import re
import sys
import numpy
import pandas
import math
import benford


def load_dataset(dataset_name):
  with open(dataset_name) as f:
    numbers = list(map(int, re.findall(r"\d+", f.read())))

    return pandas.DataFrame({"china": numbers})


def get_order_or_magnitude(number):
  return math.floor(math.log(number, 10))


dataset_name = sys.argv[1]
print("########################")
print("Dataset name:", dataset_name)

df = load_dataset(dataset_name)

# Check that the benford law applies
df_min = df.min().tolist()[0]
df_max = df.max().tolist()[0]
df_count = df.count().tolist()[0]
print("Min value in dataset:", df_min)
print("Max value in dataset:", df_max)
print("Dataset size:", df_count)
spans_multiple_orders_of_magnitude = (
  get_order_or_magnitude(df_max or 1) - get_order_or_magnitude(df_min or 1) > 3
)
has_lots_of_samples = df_count > 100

if spans_multiple_orders_of_magnitude and has_lots_of_samples:
  print(
    "Benford law applies (if the source of numbers is 'good', e.g., a natural phenomenon)."
  )
else:
  print("Dataset does not satisfy Benford's requirements.")

# Compute the first-digit frequency for the Chinese dataset.
(
  china_first_digits_total,
  china_first_digits_count,
  china_first_digits_percent,
) = benford.count_first_digit(df, "china")


# Compute the expected Beford distribution.
expected_counts = benford.get_expected_counts(china_first_digits_total)

# Compare the distributions.
are_the_distributions_not_too_dissimilar = benford.chi_square_test(
  china_first_digits_count, expected_counts
)

# Is the data fake?
if are_the_distributions_not_too_dissimilar:
  print("No comment on this data.")
else:
  print("The data appears to have been manipulated.")
