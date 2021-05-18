#
#  test_tiai_encoder.py
#  rfid_encoder
#
#  Created by Tim.Milne on 5/17/21
#  Copyright © 2021 Tim Milne. All rights reserved.
#
#  This file contains a class to test the tiai_encoder module
#

import unittest

from tiai_encoder import *
from converter import *

class TestTIAIConverter(unittest.TestCase):
  def test_with_dec_id(self):
    """
    Test the encoding of an integer asset ID
    """
    encode_tiai = TIAIEncoder()
    self.assertEqual(encode_tiai.with_dec_id("5", "1"), "urn:epc:tag:tiai-a-96:0.5.1", msg="uri != urn:epc:tag:tiai-a-96:0.5.1")
    self.assertEqual(encode_tiai.tiai_hex, "0A0005000000000000000001", msg="tiai_hex != 0A0005000000000000000001")
    self.assertEqual(encode_tiai.tiai_bin, "000010100000000000000101000000000000000000000000000000000000000000000000000000000000000000000001", msg="tiai_bin != 000010100000000000000101000000000000000000000000000000000000000000000000000000000000000000000001")
    self.assertEqual(len(encode_tiai.tiai_bin), 96, msg="len(tiai_bin) != 96 bits")
    
    self.assertEqual(encode_tiai.with_dec_id("05", "01"), "urn:epc:tag:tiai-a-96:0.5.1", msg="uri != urn:epc:tag:tiai-a-96:0.5.1")
    self.assertEqual(encode_tiai.tiai_hex, "0A0005000000000000000001", msg="tiai_hex != 0A0005000000000000000001")
    self.assertEqual(encode_tiai.tiai_bin, "000010100000000000000101000000000000000000000000000000000000000000000000000000000000000000000001", msg="tiai_bin != 000010100000000000000101000000000000000000000000000000000000000000000000000000000000000000000001")
    self.assertEqual(len(encode_tiai.tiai_bin), 96, msg="len(tiai_bin) != 96 bits")
    
    self.assertEqual(encode_tiai.with_dec_id("05", "12345678901234"), "urn:epc:tag:tiai-a-96:0.5.12345678901234", msg="uri != urn:epc:tag:tiai-a-96:0.5.12345678901234")
    self.assertEqual(encode_tiai.tiai_hex, "0A00050000000B3A73CE2FF2", msg="tiai_hex != 0A00050000000B3A73CE2FF2")
    self.assertEqual(encode_tiai.tiai_bin, "000010100000000000000101000000000000000000000000000010110011101001110011110011100010111111110010", msg="tiai_bin != 000010100000000000000101000000000000000000000000000010110011101001110011110011100010111111110010")
    self.assertEqual(len(encode_tiai.tiai_bin), 96, msg="len(tiai_bin) != 96 bits")
    
    self.assertEqual(encode_tiai.with_dec_id("017", "12345678901234567890"), "urn:epc:tag:tiai-a-96:0.17.12345678901234567890", msg="uri != urn:epc:tag:tiai-a-96:0.17.12345678901234567890")
    self.assertEqual(encode_tiai.tiai_hex, "0A001100AB54A98CEB1F0AD2", msg="tiai_hex != 0A001100AB54A98CEB1F0AD2")
    self.assertEqual(encode_tiai.tiai_bin, "000010100000000000010001000000001010101101010100101010011000110011101011000111110000101011010010", msg="tiai_bin != 000010100000000000010001000000001010101101010100101010011000110011101011000111110000101011010010")
    self.assertEqual(len(encode_tiai.tiai_bin), 96, msg="len(tiai_bin) != 96 bits")
    
    self.assertEqual(encode_tiai.with_dec_id("017", "91055105001418913751"), "urn:epc:tag:tiai-a-96:0.17.91055105001418913751", msg="uri != urn:epc:tag:tiai-a-96:0.17.91055105001418913751")
# TPM - pretty sure this hex is WRONG!!!
    self.assertEqual(encode_tiai.tiai_hex, "0A001104EFA4B7917377F7D7", msg="tiai_hex != 0A001104EFA4B7917377F7D7")
    self.assertEqual(encode_tiai.tiai_bin, "000010100000000000010001000001001110111110100100101101111001000101110011011101111111011111010111", msg="tiai_bin != 000010100000000000010001000001001110111110100100101101111001000101110011011101111111011111010111")
    self.assertEqual(len(encode_tiai.tiai_bin), 96, msg="len(tiai_bin) != 96 bits")
    

  def test_with_char_id(self):
    """
    Test the encoding of a character asset ID
    """
    encode_tiai = TIAIEncoder()
    self.assertEqual(encode_tiai.with_char_id("7", "Y2A630"), "urn:epc:tag:tiai-a-96:0.7.Y2A630", msg="uri != urn:epc:tag:tiai-a-96:0.7.Y2A630")
    self.assertEqual(encode_tiai.tiai_hex, "0A0007000000000672076CF0", msg="tiai_hex != 0A0007000000000672076CF0")
    self.assertEqual(encode_tiai.tiai_bin, "000010100000000000000111000000000000000000000000000000000000011001110010000001110110110011110000", msg="tiai_bin != 000010100000000000000111000000000000000000000000000000000000011001110010000001110110110011110000")
    self.assertEqual(len(encode_tiai.tiai_bin), 96, msg="len(tiai_bin) != 96 bits")
    
    self.assertEqual(encode_tiai.with_char_id("07", "0Y2A630"), "urn:epc:tag:tiai-a-96:0.7.0Y2A630", msg="uri != urn:epc:tag:tiai-a-96:0.7.0Y2A630")
    self.assertEqual(encode_tiai.tiai_hex, "0A0007000000030672076CF0", msg="tiai_hex != 0A0007000000030672076CF0")
    self.assertEqual(encode_tiai.tiai_bin, "000010100000000000000111000000000000000000000000000000110000011001110010000001110110110011110000", msg="tiai_bin != 000010100000000000000111000000000000000000000000000000110000011001110010000001110110110011110000")
    self.assertEqual(len(encode_tiai.tiai_bin), 96, msg="len(tiai_bin) != 96 bits")
    
    self.assertEqual(encode_tiai.with_char_id("7", "y2a630"), "urn:epc:tag:tiai-a-96:0.7.Y2A630", msg="uri != urn:epc:tag:tiai-a-96:0.7.Y2A630")
    self.assertEqual(encode_tiai.tiai_hex, "0A0007000000000672076CF0", msg="tiai_hex != 0A0007000000000672076CF0")
    self.assertEqual(encode_tiai.tiai_bin, "000010100000000000000111000000000000000000000000000000000000011001110010000001110110110011110000", msg="tiai_bin != 000010100000000000000111000000000000000000000000000000000000011001110010000001110110110011110000")
    self.assertEqual(len(encode_tiai.tiai_bin), 96, msg="len(tiai_bin) != 96 bits")
    
    self.assertEqual(encode_tiai.with_char_id("017", "123ABC"), "urn:epc:tag:tiai-a-96:0.17.123ABC", msg="uri != urn:epc:tag:tiai-a-96:0.17.123ABC")
    self.assertEqual(encode_tiai.tiai_hex, "0A0011000000000C72CC1083", msg="tiai_hex != 0A0011000000000C72CC1083")
    self.assertEqual(encode_tiai.tiai_bin, "000010100000000000010001000000000000000000000000000000000000110001110010110011000001000010000011", msg="tiai_bin != 000010100000000000010001000000000000000000000000000000000000110001110010110011000001000010000011")
    self.assertEqual(len(encode_tiai.tiai_bin), 96, msg="len(tiai_bin) != 96 bits")
    
  def test_with_hex_id(self):
    """
    Test the encoding of a hex asset ID
    """
    encode_tiai = TIAIEncoder()
    self.assertEqual(encode_tiai.with_hex_id("8", "1"), "urn:epc:tag:tiai-a-96:0.8.1", msg="uri != urn:epc:tag:tiai-a-96:0.8.1")
    self.assertEqual(encode_tiai.tiai_hex, "0A0008000000000000000001", msg="tiai_hex != 0A0008000000000000000001")
    self.assertEqual(encode_tiai.tiai_bin, "000010100000000000001000000000000000000000000000000000000000000000000000000000000000000000000001", msg="tiai_bin != 000010100000000000001000000000000000000000000000000000000000000000000000000000000000000000000001")
    self.assertEqual(len(encode_tiai.tiai_bin), 96, msg="len(tiai_bin) != 96 bits")
    
    self.assertEqual(encode_tiai.with_hex_id("08", "01"), "urn:epc:tag:tiai-a-96:0.8.1", msg="uri != urn:epc:tag:tiai-a-96:0.8.1")
    self.assertEqual(encode_tiai.tiai_hex, "0A0008000000000000000001", msg="tiai_hex != 0A0008000000000000000001")
    self.assertEqual(encode_tiai.tiai_bin, "000010100000000000001000000000000000000000000000000000000000000000000000000000000000000000000001", msg="tiai_bin != 000010100000000000001000000000000000000000000000000000000000000000000000000000000000000000000001")
    self.assertEqual(len(encode_tiai.tiai_bin), 96, msg="len(tiai_bin) != 96 bits")
    
    self.assertEqual(encode_tiai.with_hex_id("8", "929B35AD6B1BA6B5"), "urn:epc:tag:tiai-a-96:0.8.929B35AD6B1BA6B5", msg="uri != urn:epc:tag:tiai-a-96:0.8.929B35AD6B1BA6B5")
    self.assertEqual(encode_tiai.tiai_hex, "0A000800929B35AD6B1BA6B5", msg="tiai_hex != 0A000800929B35AD6B1BA6B5")
    self.assertEqual(encode_tiai.tiai_bin, "000010100000000000001000000000001001001010011011001101011010110101101011000110111010011010110101", msg="tiai_bin != 000010100000000000001000000000001001001010011011001101011010110101101011000110111010011010110101")
    self.assertEqual(len(encode_tiai.tiai_bin), 96, msg="len(tiai_bin) != 96 bits")
    
    self.assertEqual(encode_tiai.with_hex_id("08", "00929B35AD6B1BA6B5"), "urn:epc:tag:tiai-a-96:0.8.929B35AD6B1BA6B5", msg="uri != urn:epc:tag:tiai-a-96:0.8.929B35AD6B1BA6B5")
    self.assertEqual(encode_tiai.tiai_hex, "0A000800929B35AD6B1BA6B5", msg="tiai_hex != 0A000800929B35AD6B1BA6B5")
    self.assertEqual(encode_tiai.tiai_bin, "000010100000000000001000000000001001001010011011001101011010110101101011000110111010011010110101", msg="tiai_bin != 000010100000000000001000000000001001001010011011001101011010110101101011000110111010011010110101")
    self.assertEqual(len(encode_tiai.tiai_bin), 96, msg="len(tiai_bin) != 96 bits")
    
    self.assertEqual(encode_tiai.with_hex_id("017", "AF034C16FD"), "urn:epc:tag:tiai-a-96:0.17.AF034C16FD", msg="uri != urn:epc:tag:tiai-a-96:0.17.AF034C16FD")
    self.assertEqual(encode_tiai.tiai_hex, "0A001100000000AF034C16FD", msg="tiai_hex != 0A001100000000AF034C16FD")
    self.assertEqual(encode_tiai.tiai_bin, "000010100000000000010001000000000000000000000000000000001010111100000011010011000001011011111101", msg="tiai_bin != 000010100000000000010001000000000000000000000000000000001010111100000011010011000001011011111101")
    self.assertEqual(len(encode_tiai.tiai_bin), 96, msg="len(tiai_bin) != 96 bits")

  def test_char_2_bin_and_bin_2_char(self):
    """
    Test the char_2_bin and bin_2_char methods
    """
    encode_tiai = TIAIEncoder()
    char1 = "123ABC"
    bin1  = "110001110010110011000001000010000011"
    char2 = encode_tiai.bin_2_char(bin1)
    bin2  = encode_tiai.char_2_bin(char1)

    self.assertEqual(char2, "123ABC", msg="char2 != 123ABC")
    self.assertEqual(bin2, "110001110010110011000001000010000011", msg="bin2 != 110001110010110011000001000010000011")
    
    bin3  = encode_tiai.char_2_bin("123ABC", 72)
    char3 = encode_tiai.bin_2_char(bin3)
    bin4  = encode_tiai.char_2_bin(char3, 72)
    char4 = encode_tiai.bin_2_char(bin4)
    
    self.assertEqual(bin3, bin4, msg="bin3 != bin4")
    self.assertEqual(char3, char4, msg="char3 != char4")
    
if __name__ == '__main__':
    unittest.main()
