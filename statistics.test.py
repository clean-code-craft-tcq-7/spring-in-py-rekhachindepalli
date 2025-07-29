import unittest
import statistics


class StatsTest(unittest.TestCase):
  def test_report_min_max_avg(self):
    computedStats = statistics.calculateStats([1.5, 8.9, 3.2, 4.5])
    epsilon = 0.001
    self.assertAlmostEqual(computedStats["avg"], 4.525, delta=epsilon)
    self.assertAlmostEqual(computedStats["max"], 8.9, delta=epsilon)
    self.assertAlmostEqual(computedStats["min"], 1.5, delta=epsilon)

  def test_avg_is_nan_for_empty_input(self):
    computedStats = statistics.calculateStats([])
    self.assertAlmostEqual(math.isnan(computedStats["avg"])
    self.assertAlmostEqual(math.isnan(computedStats["Max"])
    self.assertAlmostEqual(math.isnan(computedStats["Min"])


if __name__ == "__main__":
  unittest.main()
