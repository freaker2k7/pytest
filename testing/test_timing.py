import pytest
from _pytest.timing import sleep
from _pytest.timing import start
from _pytest.timing import stop
from _pytest.timing import time


def test_store() -> None:
    start_time = time()
    sleep(0.5)
    stop()
    sleep(1)
    start()
    sleep(0.5)
    assert int(time()) == int(start_time + 1)
