#
#  test_converter.py
#  rfid_encoder
#
#  Created by Tim.Milne on 5/17/21
#  Copyright © 2021 Tim Milne. All rights reserved.
#
#  This file contains functions to test the convert module
#

import unittest

from converter import *

class TestConverter(unittest.TestCase):
  def test_all(self):
    """
    Test all conversions with and without leading zeros
    """
    hex1 = "0A001104EFA4B7917377F7D7"
    bin1 = hex_2_bin(hex1)
    dec1 = hex_2_dec(hex1)
    hex2 = bin_2_hex(bin1)
    hex3 = dec_2_hex(dec1)
    hex4 = dec_2_hex(dec1, 24)
    bin2 = dec_2_bin(dec1)
    bin3 = dec_2_bin(dec1, 96)
    dec2 = bin_2_dec(bin2)
    bin3 = dec_2_bin(dec1, 96)
    
    # Includes leading zero, as length explicitly specified
    self.assertEqual(hex4, "0A001104EFA4B7917377F7D7", msg="hex4 != 0A001104EFA4B7917377F7D7")
    self.assertEqual(hex1, hex4, msg="hex1 != hex4")
    # Leading zero missing, as expected
    self.assertEqual(hex2, "A001104EFA4B7917377F7D7", msg="hex2 != A001104EFA4B7917377F7D7")
    self.assertEqual(hex2, hex3, msg="hex2 != hex3")
    self.assertEqual(dec1, "3094930469498764472635357143", msg="dec1 != 3094930469498764472635357143")
    self.assertEqual(dec1, dec2, msg="dec1 != dec2")
    # Leading zeros missing, as expected
    self.assertEqual(bin1, "10100000000000010001000001001110111110100100101101111001000101110011011101111111011111010111", msg="bin1 != 10100000000000010001000001001110111110100100101101111001000101110011011101111111011111010111")
    self.assertEqual(bin1, bin2, msg="bin1 != bin2")
    # Includes leading zeros, as length explicitly specified
    self.assertEqual(bin3, "000010100000000000010001000001001110111110100100101101111001000101110011011101111111011111010111", msg="bin3 != 000010100000000000010001000001001110111110100100101101111001000101110011011101111111011111010111")
    
    dec10 = hex_2_dec("0A001104EFA4B7917377F7D7")
    bin10 = dec_2_bin(dec10, 96)
    dec11 = bin_2_dec(bin10)
    bin11 = hex_2_bin("0A001104EFA4B7917377F7D7")
    hex10 = bin_2_hex(bin11, 24)
    hex11 = dec_2_hex("100", 24)
    
    self.assertEqual(dec10, "3094930469498764472635357143", msg="dec10 != 3094930469498764472635357143")
    self.assertEqual(dec10, dec11, msg="dec10 != dec11")
    # Includes leading zeros, as lengths explicitly specified
    self.assertEqual(bin10, "000010100000000000010001000001001110111110100100101101111001000101110011011101111111011111010111", msg="bin10 != 000010100000000000010001000001001110111110100100101101111001000101110011011101111111011111010111")
    # Leading zeros missing, as expected
    self.assertEqual(bin11, "10100000000000010001000001001110111110100100101101111001000101110011011101111111011111010111", msg="bin11 != 10100000000000010001000001001110111110100100101101111001000101110011011101111111011111010111")
    # Includes leading zeros, as lengths explicitly specified
    self.assertEqual(hex10, "0A001104EFA4B7917377F7D7", msg="hex10 != 0A001104EFA4B7917377F7D7")
    self.assertEqual(hex11, "000000000000000000000064", msg="hex10 != 000000000000000000000064")

if __name__ == '__main__':
  unittest.main()
