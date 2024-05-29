# pytest-ditto-pandas
[![PyPI version](https://badge.fury.io/py/pytest-ditto-pandas.svg)](https://badge.fury.io/py/pytest-ditto-pandas)
[![Continuous Integration](https://github.com/owlowlyowl/pytest-ditto-pandas/actions/workflows/ci.yml/badge.svg)](https://github.com/owlowlyowl/pytest-ditto-pandas/actions/workflows/ci.yml)

`pytest-ditto` plugin for pandas snapshots.

## @ditto Marks
If the default persistence format, `pickle`, isn't appropriate different formats can be
specified per test by using `ditto` marks - customised `pytest` mark decorators.


## Usage

### `pd.DataFrame`

```python
import pandas as pd

import ditto


def awesome_fn_to_test(df: pd.DataFrame):
    df.loc[:, "a"] *= 2
    return df


# The following test uses pandas.DataFrame.to_parquet to write the data snapshot to the
# `.ditto` directory with filename:
# `test_fn_with_parquet_dataframe_snapshot@ab_dataframe.pandas.parquet`.

@ditto.pandas.parquet
def test_fn_with_parquet_dataframe_snapshot(snapshot):
    input_data = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 9]})
    result = awesome_fn_to_test(input_data)
    pd.testing.assert_frame_equal(result, snapshot(result, key="ab_dataframe"))


# The following test uses pandas.DataFrame.to_json(orient="table") to write the data
# snapshot to the `.ditto` directory with filename:
# `test_fn_with_json_dataframe_snapshot@ab_dataframe.pandas.json`.

@ditto.pandas.json
def test_fn_with_json_dataframe_snapshot(snapshot):
    input_data = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 9]})
    result = awesome_fn_to_test(input_data)
    pd.testing.assert_frame_equal(result, snapshot(result, key="ab_dataframe"))
```
