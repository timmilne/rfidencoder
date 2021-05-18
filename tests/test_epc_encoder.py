#
#  test_epc_encoder.py
#  rfid_encoder
#
#  Created by Tim.Milne on 5/17/21
#  Copyright © 2021 Tim Milne. All rights reserved.
#
#  This file contains a class to test the epc_encoder module
#

import unittest

from epc_encoder import *
from converter import *

class TestEPCConverter(unittest.TestCase):
  def test_with_dpci(self):
    """
    Test the encoding of DPCI in GID
    """
    encode_epc = EPCEncoder()
    self.assertEqual(encode_epc.with_dpci("281", "00", "8570", "12345"), "urn:epc:tag:gid-96:04928100.0085702.12345", msg="uri != urn:epc:tag:gid-96:04928100.0085702.12345")
    self.assertEqual(encode_epc.gid_hex, "3504B3264014EC6000003039", msg="gid_hex != 3504B3264014EC6000003039")
    # Watch for missing leading zeros
    self.assertEqual(encode_epc.gid_hex, bin_2_hex(encode_epc.gid_bin), msg="gid_hex != bin2hex")
    self.assertEqual(encode_epc.gid_bin, "001101010000010010110011001001100100000000010100111011000110000000000000000000000011000000111001", msg="gid_bin != 001101010000010010110011001001100100000000010100111011000110000000000000000000000011000000111001")
    self.assertEqual(encode_epc.gid_bin, hex_2_bin("3504B3264014EC6000003039", 96), msg="gid_bin != hex_2_bin")
    self.assertEqual(len(encode_epc.gid_bin), 96, msg="len(gid_bin) != 96 bits")
   
    # Check with http://www.kentraub.net/tools/tagxlate/EPCEncoderDecoder.html

  def test_with_gtin_in_gid(self):
    """
    Test the encoding of a GTIN in GID
    """
    encode_epc = EPCEncoder()
    self.assertEqual(encode_epc.with_gtin_in_gid("00052175551276", "0100012345"), "urn:epc:tag:gid-96:00052175.0551276.0100012345", msg="uri != urn:epc:tag:gid-96:00052175.0551276.0100012345")
    self.assertEqual(encode_epc.gid_hex, "35000CBCF08696C005F61139", msg="gid_hex != 35000CBCF08696C005F61139")
    # Watch for missing leading zeros
    self.assertEqual(encode_epc.gid_hex, bin_2_hex(encode_epc.gid_bin), msg="gid_hex != bin2hex")
    self.assertEqual(encode_epc.gid_bin, "001101010000000000001100101111001111000010000110100101101100000000000101111101100001000100111001", msg="gid_bin != 001101010000000000001100101111001111000010000110100101101100000000000101111101100001000100111001")
    self.assertEqual(encode_epc.gid_bin, hex_2_bin("35000CBCF08696C005F61139", 96), msg="gid_bin != hex_2_bin")
    self.assertEqual(len(encode_epc.gid_bin), 96, msg="len(gid_bin) != 96 bits")

    self.assertEqual(encode_epc.with_gtin_in_gid("052175551276", "100012345"), "urn:epc:tag:gid-96:00052175.0551276.100012345", msg="uri != urn:epc:tag:gid-96:00052175.0551276.0100012345")
    self.assertEqual(encode_epc.gid_hex, "35000CBCF08696C005F61139", msg="gid_hex != 35000CBCF08696C005F61139")
    # Watch for missing leading zeros
    self.assertEqual(encode_epc.gid_hex, bin_2_hex(encode_epc.gid_bin), msg="gid_hex != bin2hex")
    self.assertEqual(encode_epc.gid_bin, "001101010000000000001100101111001111000010000110100101101100000000000101111101100001000100111001", msg="gid_bin != 001101010000000000001100101111001111000010000110100101101100000000000101111101100001000100111001")
    self.assertEqual(encode_epc.gid_bin, hex_2_bin("35000CBCF08696C005F61139", 96), msg="gid_bin != hex_2_bin")
    self.assertEqual(len(encode_epc.gid_bin), 96, msg="len(gid_bin) != 96 bits")

    # Check with http://www.kentraub.net/tools/tagxlate/EPCEncoderDecoder.html
    
  def test_with_gtin(self):
    """
    Test the encoding of GTIN
    """
    encode_epc = EPCEncoder()
    self.assertEqual(encode_epc.with_gtin("00043935460624", "12345", "000"), "urn:epc:tag:sgtin-96:1.004393546062.0.12345", msg="uri != urn:epc:tag:sgtin-96:1.004393546062.0.12345")
    self.assertEqual(encode_epc.gtin_hex, "3020041780C5380000003039", msg="gtin_hex != 3020041780C5380000003039")
    # Watch for missing leading zeros
    self.assertEqual(encode_epc.gtin_hex, bin_2_hex(encode_epc.gtin_bin), msg="gtin_hex != bin2hex")
    self.assertEqual(encode_epc.gtin_bin, "001100000010000000000100000101111000000011000101001110000000000000000000000000000011000000111001", msg="gtin_bin != 001100000010000000000100000101111000000011000101001110000000000000000000000000000011000000111001")
    self.assertEqual(encode_epc.gtin_bin, hex_2_bin("3020041780C5380000003039", 96), msg="gtin_bin != hex_2_bin")
    self.assertEqual(len(encode_epc.gtin_bin), 96, msg="len(gtin_bin) != 96 bits")
    
    encode_epc = EPCEncoder()
    self.assertEqual(encode_epc.with_gtin("00043935460624", "12345", "001"), "urn:epc:tag:sgtin-96:1.00439354606.02.12345", msg="uri != urn:epc:tag:sgtin-96:1.00439354606.02.12345")
    self.assertEqual(encode_epc.gtin_hex, "30240346009DC08000003039", msg="gtin_hex != 30240346009DC08000003039")
    # Watch for missing leading zeros
    self.assertEqual(encode_epc.gtin_hex, bin_2_hex(encode_epc.gtin_bin), msg="gtin_hex != bin2hex")
    self.assertEqual(encode_epc.gtin_bin, "001100000010010000000011010001100000000010011101110000001000000000000000000000000011000000111001", msg="gtin_bin != 001100000010010000000011010001100000000010011101110000001000000000000000000000000011000000111001")
    self.assertEqual(encode_epc.gtin_bin, hex_2_bin("30240346009DC08000003039", 96), msg="gtin_bin != hex_2_bin")
    self.assertEqual(len(encode_epc.gtin_bin), 96, msg="len(gtin_bin) != 96 bits")
  
    encode_epc = EPCEncoder()
    self.assertEqual(encode_epc.with_gtin("00043935460624", "12345", "010"), "urn:epc:tag:sgtin-96:1.0043935460.062.12345", msg="uri != urn:epc:tag:sgtin-96:1.0043935460.062.12345")
    self.assertEqual(encode_epc.gtin_hex, "3028029E66E40F8000003039", msg="gtin_hex != 3028029E66E40F8000003039")
    # Watch for missing leading zeros
    self.assertEqual(encode_epc.gtin_hex, bin_2_hex(encode_epc.gtin_bin), msg="gtin_hex != bin2hex")
    self.assertEqual(encode_epc.gtin_bin, "001100000010100000000010100111100110011011100100000011111000000000000000000000000011000000111001", msg="gtin_bin != 001100000010100000000010100111100110011011100100000011111000000000000000000000000011000000111001")
    self.assertEqual(encode_epc.gtin_bin, hex_2_bin("3028029E66E40F8000003039", 96), msg="gtin_bin != hex_2_bin")
    self.assertEqual(len(encode_epc.gtin_bin), 96, msg="len(gtin_bin) != 96 bits")
    
    encode_epc = EPCEncoder()
    self.assertEqual(encode_epc.with_gtin("00043935460624", "12345", "011"), "urn:epc:tag:sgtin-96:1.004393546.0062.12345", msg="uri != urn:epc:tag:sgtin-96:1.004393546.0062.12345")
    self.assertEqual(encode_epc.gtin_hex, "302C0430A4A00F8000003039", msg="gtin_hex != 302C0430A4A00F8000003039")
    # Watch for missing leading zeros
    self.assertEqual(encode_epc.gtin_hex, bin_2_hex(encode_epc.gtin_bin), msg="gtin_hex != bin2hex")
    self.assertEqual(encode_epc.gtin_bin, "001100000010110000000100001100001010010010100000000011111000000000000000000000000011000000111001", msg="gtin_bin != 001100000010110000000100001100001010010010100000000011111000000000000000000000000011000000111001")
    self.assertEqual(encode_epc.gtin_bin, hex_2_bin("302C0430A4A00F8000003039", 96), msg="gtin_bin != hex_2_bin")
    self.assertEqual(len(encode_epc.gtin_bin), 96, msg="len(gtin_bin) != 96 bits")
  
    encode_epc = EPCEncoder()
    self.assertEqual(encode_epc.with_gtin("00043935460624", "12345", "100"), "urn:epc:tag:sgtin-96:1.00439354.06062.12345", msg="uri != urn:epc:tag:sgtin-96:1.00439354.06062.12345")
    self.assertEqual(encode_epc.gtin_hex, "3030035A1D05EB8000003039", msg="gtin_hex != 3030035A1D05EB8000003039")
    # Watch for missing leading zeros
    self.assertEqual(encode_epc.gtin_hex, bin_2_hex(encode_epc.gtin_bin), msg="gtin_hex != bin2hex")
    self.assertEqual(encode_epc.gtin_bin, "001100000011000000000011010110100001110100000101111010111000000000000000000000000011000000111001", msg="gtin_bin != 001100000011000000000011010110100001110100000101111010111000000000000000000000000011000000111001")
    self.assertEqual(encode_epc.gtin_bin, hex_2_bin("3030035A1D05EB8000003039", 96), msg="gtin_bin != hex_2_bin")
    self.assertEqual(len(encode_epc.gtin_bin), 96, msg="len(gtin_bin) != 96 bits")

    encode_epc = EPCEncoder()
    self.assertEqual(encode_epc.with_gtin("00043935460624", "12345", "101"), "urn:epc:tag:sgtin-96:1.0043935.046062.12345", msg="uri != urn:epc:tag:sgtin-96:1.0043935.046062.12345")
    self.assertEqual(encode_epc.gtin_hex, "303402AE7C2CFB8000003039", msg="gtin_hex != 303402AE7C2CFB8000003039")
    # Watch for missing leading zeros
    self.assertEqual(encode_epc.gtin_hex, bin_2_hex(encode_epc.gtin_bin), msg="gtin_hex != bin2hex")
    self.assertEqual(encode_epc.gtin_bin, "001100000011010000000010101011100111110000101100111110111000000000000000000000000011000000111001", msg="gtin_bin != 001100000011010000000010101011100111110000101100111110111000000000000000000000000011000000111001")
    self.assertEqual(encode_epc.gtin_bin, hex_2_bin("303402AE7C2CFB8000003039", 96), msg="gtin_bin != hex_2_bin")
    self.assertEqual(len(encode_epc.gtin_bin), 96, msg="len(gtin_bin) != 96 bits")
    
    encode_epc = EPCEncoder()
    self.assertEqual(encode_epc.with_gtin("00043935460624", "12345", "110"), "urn:epc:tag:sgtin-96:1.004393.0546062.12345", msg="uri != urn:epc:tag:sgtin-96:1.0043935.046062.12345")
    self.assertEqual(encode_epc.gtin_hex, "3038044A4215438000003039", msg="gtin_hex != 3038044A4215438000003039")
    # Watch for missing leading zeros
    self.assertEqual(encode_epc.gtin_hex, bin_2_hex(encode_epc.gtin_bin), msg="gtin_hex != bin2hex")
    self.assertEqual(encode_epc.gtin_bin, "001100000011100000000100010010100100001000010101010000111000000000000000000000000011000000111001", msg="gtin_bin != 001100000011100000000100010010100100001000010101010000111000000000000000000000000011000000111001")
    self.assertEqual(encode_epc.gtin_bin, hex_2_bin("3038044A4215438000003039", 96), msg="gtin_bin != hex_2_bin")
    self.assertEqual(len(encode_epc.gtin_bin), 96, msg="len(gtin_bin) != 96 bits")
   
    # Check with http://www.kentraub.net/tools/tagxlate/EPCEncoderDecoder.html

    
  def test_calculate_check_digit(self):
    """
    Test the check digit calculator
    """
    self.assertEqual(calculate_check_digit("01149103868"), "7", msg="calculate_check_digit !- 7")
    self.assertEqual(calculate_check_digit("64393443327"), "0", msg="calculate_check_digit !- 0")
    
if __name__ == '__main__':
    unittest.main()
