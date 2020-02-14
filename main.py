import re
import numpy
import pandas

import benford


def load_dataset():
  with open("dataset_02_14.txt") as f:
    numbers = list(map(int, re.findall(r"\d+", f.read())))

    return pandas.DataFrame({"china": numbers})


df = load_dataset()

# Compute the first-digit frequency for the Chinese dataset.
(
  china_first_digits_total,
  china_first_digits_count,
  china_first_digits_percent,
) = benford.count_first_digit(df, "china")


# Compute the expected Beford distribution.
expected_counts = benford.get_expected_counts(china_first_digits_total)

# Compare the distributions.
can_we_reject_null_hypotesis = benford.chi_square_test(
  china_first_digits_count, expected_counts
)

# Is the data fake?
print(
  "Does the observed distribution match the expected one?", can_we_reject_null_hypotesis
)
