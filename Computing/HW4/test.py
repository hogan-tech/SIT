import time
import timer

def nearly_equal(got, expected, epsilon = 0.02):
    assert abs(got - expected) <= epsilon, f'got {got}, expected a value between {expected - epsilon} and {expected + epsilon}'

t = timer.Timer()
assert t.total() == 0, 'initial total should be 0'

t.start()
time.sleep(1)
elapsed = t.total()
t.reset()
elapsed2 = t.total()
t.stop()
print(elapsed)
print(elapsed2)
nearly_equal(elapsed, 1.0)
nearly_equal(elapsed2, 1.0)

t.reset()
elapsed3 = t.total()
assert elapsed3 == 0