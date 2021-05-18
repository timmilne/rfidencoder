#
#  test_serial_number_generator.py
#  rfid_encoder
#
#  Created by Tim.Milne on 5/17/21
#  Copyright © 2021 Tim Milne. All rights reserved.
#
#  This file contains functions to test the serial_number_generator module
#

import unittest

from serial_number_generator import *

class TestSerialNumberGenerator(unittest.TestCase):
  def test_new_serial_with_seed(self):
    """
    Test that the serial number generated is 15 digits
    """
    self.assertEqual(len(new_serial_with_seed(12345)), 15, msg="Random Number not 15 digits long")

if __name__ == '__main__':
  unittest.main()
