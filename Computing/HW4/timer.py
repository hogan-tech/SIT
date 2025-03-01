# Author: Hogan Lin
# Date: Feb 19th 2025
# Github: https://github.com/hogan-tech/SIT/tree/main/Computing
# Description: Timer class implementation

import time


class TimerError(Exception):
    """Custom exception for Timer class errors"""
    pass


class Timer:
    def __init__(self):
        """Initializes the Timer object with default values."""
        self._start_time = None
        self._elapsed_time = 0.0

    def start(self):
        """Starts the timer."""
        if self._start_time is not None:
            raise TimerError("timer is already running")
        self._start_time = time.time()
        return None

    def stop(self):
        """Stops the timer and updates elapsed time."""
        if self._start_time is None:
            raise TimerError("timer is not running")
        self._elapsed_time += time.time() - self._start_time
        self._start_time = None
        return None

    def total(self) -> float:
        """Returns the total elapsed time."""
        if self._start_time is None:
            return self._elapsed_time
        return self._elapsed_time + (time.time() - self._start_time)

    def reset(self):
        """Resets the timer's elapsed time."""
        self._elapsed_time = 0.0

t = Timer()

t.start()
time.sleep(1) # wait 1 second
t.stop()

print(t.total())

t.start()
time.sleep(3) # wait 3 seconds
t.stop()

print(t.total())

t.reset()
print(t.total())

t.start()
time.sleep(0.5)
print(t.total())
time.sleep(1)
print(t.total())
t.stop()

print(t.total())
print(t.total())