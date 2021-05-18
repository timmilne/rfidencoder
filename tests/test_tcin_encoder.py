#
#  test_tcin_encoder.py
#  rfid_encoder
#
#  Created by Tim.Milne on 5/17/21
#  Copyright © 2021 Tim Milne. All rights reserved.
#
#  This file contains a class to test the tcin_encoder module
#

import unittest

from tcin_encoder import *
from converter import *
from serial_number_generator import new_serial_with_seed

class TestTCINConverter(unittest.TestCase):
  def test_with_tcin(self):
    """
    Test the encoding of a TCIN
    """
    encode_tcin = TCINEncoder()
    
    self.assertEqual(encode_tcin.with_tcin("13951442")[:30], "urn:epc:tag:tcin-96:0.13951442", msg="uri != urn:epc:tag:tcin-96:0.13951442")
    self.assertEqual(encode_tcin.tcin_hex[:11], "08000353874", msg="tcin_hex != 08000353874")
    self.assertEqual(encode_tcin.tcin_bin[:46], "0000100000000000000000110101001110000111010010", msg="tcin_bin != 0000100000000000000000110101001110000111010010")
    self.assertEqual(len(encode_tcin.tcin_bin), 96, msg="len(tcin_bin) != 96 bits")
    
    self.assertEqual(encode_tcin.with_tcin("14448796")[:30], "urn:epc:tag:tcin-96:0.14448796", msg="uri != urn:epc:tag:tcin-96:0.14448796")
    self.assertEqual(encode_tcin.tcin_hex[:11], "08000371E27", msg="tcin_hex != 08000371E27")
    self.assertEqual(encode_tcin.tcin_bin[:46], "0000100000000000000000110111000111100010011100", msg="tcin_bin != 0000100000000000000000110111000111100010011100")
    self.assertEqual(len(encode_tcin.tcin_bin), 96, msg="len(tcin_bin) != 96 bits")
    
    self.assertEqual(encode_tcin.with_tcin("16399080")[:30], "urn:epc:tag:tcin-96:0.16399080", msg="uri != urn:epc:tag:tcin-96:0.16399080")
    self.assertEqual(encode_tcin.tcin_hex[:11], "080003E8EBA", msg="tcin_hex != 080003E8EBA")
    self.assertEqual(encode_tcin.tcin_bin[:46], "0000100000000000000000111110100011101011101000", msg="tcin_bin != 0000100000000000000000111110100011101011101000")
    self.assertEqual(len(encode_tcin.tcin_bin), 96, msg="len(tcin_bin) != 96 bits")
    
  def test_with_tcin_and_seed(self):
    """
    Test the encoding of a TCIN with a seed
    """
    encode_tcin = TCINEncoder()
    
    self.assertEqual(encode_tcin.with_tcin_and_seed("13951442", "7725272730706")[:30], "urn:epc:tag:tcin-96:0.13951442", msg="uri != urn:epc:tag:tcin-96:0.13951442")
    self.assertEqual(encode_tcin.tcin_hex[:11], "08000353874", msg="tcin_hex != 08000353874")
    self.assertEqual(encode_tcin.tcin_bin[:46], "0000100000000000000000110101001110000111010010", msg="tcin_bin != 0000100000000000000000110101001110000111010010")
    self.assertEqual(len(encode_tcin.tcin_bin), 96, msg="len(tcin_bin) != 96 bits")
    
    self.assertEqual(encode_tcin.with_tcin_and_seed("014448796", "7725272730706")[:30], "urn:epc:tag:tcin-96:0.14448796", msg="uri != urn:epc:tag:tcin-96:0.14448796")
    self.assertEqual(encode_tcin.tcin_hex[:11], "08000371E27", msg="tcin_hex != 08000371E27")
    self.assertEqual(encode_tcin.tcin_bin[:46], "0000100000000000000000110111000111100010011100", msg="tcin_bin != 0000100000000000000000110111000111100010011100")
    self.assertEqual(len(encode_tcin.tcin_bin), 96, msg="len(tcin_bin) != 96 bits")
    
    self.assertEqual(encode_tcin.with_tcin_and_seed("0016399080", "7725272730706")[:30], "urn:epc:tag:tcin-96:0.16399080", msg="uri != urn:epc:tag:tcin-96:0.16399080")
    self.assertEqual(encode_tcin.tcin_hex[:11], "080003E8EBA", msg="tcin_hex != 080003E8EBA")
    self.assertEqual(encode_tcin.tcin_bin[:46], "0000100000000000000000111110100011101011101000", msg="tcin_bin != 0000100000000000000000111110100011101011101000")
    self.assertEqual(len(encode_tcin.tcin_bin), 96, msg="len(tcin_bin) != 96 bits")
    
  def test_with_seed_and_serial_number(self):
    """
    Test the encoding of a TCIN with a user supplied serial number
    """
    encode_tcin = TCINEncoder()
    
    self.assertEqual(encode_tcin.with_tcin_and_serial_number("16399080", "001"), "urn:epc:tag:tcin-96:0.16399080.1", msg="uri != urn:epc:tag:tcin-96:0.16399080.1")
    self.assertEqual(encode_tcin.tcin_hex, "080003E8EBA0000000000001", msg="tcin_hex != 080003E8EBA0000000000001")
    self.assertEqual(encode_tcin.tcin_bin, "000010000000000000000011111010001110101110100000000000000000000000000000000000000000000000000001", msg="tcin_bin != 000010000000000000000011111010001110101110100000000000000000000000000000000000000000000000000001")
    self.assertEqual(len(encode_tcin.tcin_bin), 96, msg="len(tcin_bin) != 96 bits")
    
    self.assertEqual(encode_tcin.with_tcin_and_serial_number("13951442", "123456789012345"), "urn:epc:tag:tcin-96:0.13951442.123456789012345", msg="uri != urn:epc:tag:tcin-96:0.13951442.123456789012345")
    self.assertEqual(encode_tcin.tcin_hex, "0800035387487048860DDF79", msg="tcin_hex != 0800035387487048860DDF79")
    self.assertEqual(encode_tcin.tcin_bin, "000010000000000000000011010100111000011101001000011100000100100010000110000011011101111101111001", msg="tcin_bin != 000010000000000000000011010100111000011101001000011100000100100010000110000011011101111101111001")
    self.assertEqual(len(encode_tcin.tcin_bin), 96, msg="len(tcin_bin) != 96 bits")
    
    self.assertEqual(encode_tcin.with_tcin_and_serial_number("14448796", "543210987654321"), "urn:epc:tag:tcin-96:0.14448796.543210987654321", msg="uri != urn:epc:tag:tcin-96:0.14448796.543210987654321")
    self.assertEqual(encode_tcin.tcin_hex, "08000371E271EE0C29F50CB1", msg="tcin_hex != 08000371E271EE0C29F50CB1")
    self.assertEqual(encode_tcin.tcin_bin, "000010000000000000000011011100011110001001110001111011100000110000101001111101010000110010110001", msg="tcin_bin != 000010000000000000000011011100011110001001110001111011100000110000101001111101010000110010110001")
    self.assertEqual(len(encode_tcin.tcin_bin), 96, msg="len(tcin_bin) != 96 bits")
    
if __name__ == '__main__':
    unittest.main()
