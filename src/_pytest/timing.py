"""Indirection for time functions.

We intentionally grab some "time" functions internally to avoid tests mocking "time" to affect
pytest runtime information (issue #185).

Fixture "mock_timing" also interacts with this module for pytest's own tests.
"""
from time import perf_counter
from time import sleep
from time import time as Time


PAUSED_FOR = 0
PAUSE_START = 0


def stop() -> None:
  """Pause the timing.
  
  Pracrically, we start a measurement when the pause started
  so we can substract the diff from the final time.
  
  NOTE: Please don't use this with paralellized tests!
  """
  global PAUSE_START
  
  if PAUSE_START:
    raise Exception("Maybe you meant to call pytest.timing.start() ?")
  
  PAUSE_START = Time()

def start() -> None:
  """Continue the original timing.
  
  Here, we count how long did we pause for and reset the pasue start.
  
  NOTE: Please don't use this with paralellized tests!
  """
  global PAUSED_FOR, PAUSE_START
  
  if not PAUSE_START:
    raise Exception("Maybe you meant to call pytest.timing.stop() ?")
  
  PAUSED_FOR += Time() - PAUSE_START
  PAUSE_START = 0

def time() -> float:
  return Time() - PAUSED_FOR


__all__ = ["perf_counter", "sleep", "time", "start", "stop"]
