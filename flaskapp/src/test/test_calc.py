import unittest

import calc

class TestCal(unittest.TestCase):

  def test_calc_add(self):
    _calc = calc.Calc()
    self.assertEqual(2, _calc.add(1,1))


if __name__ == '__main__':
  unittest.main()
