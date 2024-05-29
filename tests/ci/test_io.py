import pandas as pd

import ditto


@ditto.pandas.parquet
def test_parquet(snapshot) -> None:
    key = "ijk"
    snapshot(pd.DataFrame({"a": [44, 77], "qwer": [3, 4]}), key=key)
    assert snapshot.filepath(key).exists()
    assert snapshot.filepath(key).suffix == ".parquet"


@ditto.pandas.json
def test_json(snapshot) -> None:
    key = "marks"
    snapshot(pd.DataFrame({"a": [44, 77], "qwer": [3, 4]}), key=key)
    assert snapshot.filepath(key).exists()
    assert snapshot.filepath(key).suffix == ".json"


@ditto.pandas.csv
def test_csv(snapshot) -> None:
    key = "marks"
    snapshot(pd.DataFrame({"a": [44, 77], "qwer": [3, 4]}), key=key)
    assert snapshot.filepath(key).exists()
    assert snapshot.filepath(key).suffix == ".csv"