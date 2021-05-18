#
#  tiai_encoder.py
#  rfid_encoder
#
#  Created by Tim.Milne on 5/17/21
#  Copyright © 2021 Tim Milne. All rights reserved.
#
#  A python class to encode a Target Individual Asset Identifier TIAI
#
#  TIAI-96-A - e.g. urn:epc:tag:tiai-a-96:0.0013951442.123456789012345
#              0800035387487048860DDF79
#
#  The asset ref is a 3 digit decimal number, and the asset id is a unique 21
#  digit decimal or 12 character code, encoded in 6-bit.
#

from converter import *

# tiai_encoder python class to encapsulate the data in an instance
class TIAIEncoder:

  def __init__(self):
    # Instance variables
    self.asset_ref_dec = ""
    self.asset_ref_bin = ""
    self.asset_id_dec = ""
    self.asset_id_char = ""
    self.asset_id_hex = ""
    self.asset_id_bin = ""
    self.tiai_bin = ""
    self.tiai_hex = ""
    self.tiai_uri = ""

  # Use this if the Asset ID is an integer (max 21 digits)
  def with_dec_id(self, asset_ref_dec, asset_id_dec):
    self.asset_id_dec = asset_id_dec 
    self.asset_id_char = ""
    self.asset_id_hex = ""
    self.asset_id_bin = ""
    self.tiai_bin = ""
    self.tiai_hex = ""
    self.tiai_uri = ""
  
    # Check the length
    if len(self.asset_id_dec) > 21:
      self.asset_id_dec = self.asset_id_dec[:21] 
  
    # Convert to binary and call binary function
    return self.with_bin_id(asset_ref_dec, dec_2_bin(self.asset_id_dec, 72))
  
  # Use this if the Asset ID is an char (max 12 chars)
  def with_char_id(self, asset_ref_dec, asset_id_char):
    self.asset_id_dec = ""
    self.asset_id_char = asset_id_char.upper()
    self.asset_id_hex = ""
    self.asset_id_bin = ""
    self.tiai_bin = ""
    self.tiai_hex = ""
    self.tiai_uri = ""

    # Check the length
    if len(self.asset_id_char) > 12:
      self.asset_id_char = self.asset_id_char[:12] 

    asset_id_bin = self.char_2_bin(self.asset_id_char, 72)
    
    # Convert to binary and call binary function
    return self.with_bin_id(asset_ref_dec, asset_id_bin)
  
  # Use this if the Asset ID is a hex (max 18 hex digits for 72 bits)
  def with_hex_id(self, asset_ref_dec, asset_id_hex):
    self.asset_id_dec = ""
    self.asset_id_char = ""
    self.asset_id_hex = asset_id_hex.upper()
    self.asset_id_bin = ""
    self.tiai_bin = ""
    self.tiai_hex = ""
    self.tiai_uri = ""
  
    # Check the length
    if len(self.asset_id_hex) > 18:
      self.asset_id_hex = self.asset_id_hex[:18] 
  
    # Convert to binary and call binary function
    return self.with_bin_id(asset_ref_dec, hex_2_bin(self.asset_id_hex, 72))
  
  # Use this if the Asset ID is already a binary (max 72 bits)
  # Don't call this directly
  def with_bin_id(self, asset_ref_dec, asset_id_bin):
    self.asset_ref_dec = asset_ref_dec
    self.asset_id_bin = asset_id_bin
    # TPM: Since we don't call this directly we don't zero out the other forms so we can build the uri later.
  
    # Encode TIAI in a Targt proprietary TIAI-96
    asset_ref_bin_len = 13
    asset_ref_dec_len = 3
    asset_id_bin_len  = 72
    
    # Make sure the inputs are not too long
    if len(self.asset_ref_dec) > asset_ref_dec_len:
      self.asset_ref_dec = self.asset_ref_dec[-asset_ref_dec_len:]
    if len(self.asset_id_bin) > asset_id_bin_len:
      self.asset_id_bin = self.asset_id_bin[-asset_id_bin_len:]
  
    # TIAI-96-A - e.g. urn:epc:tag:tiai-a-96:0.0013951442.123456789012345
    #              0800035387487048860DDF79
    #
    # The asset ref is a 3 digit decimal number, and the asset id is a unique 21
    # digit decimal or 12 character code, encoded in 6-bit.
    #
    # Here is how to pack the TIAI-A-96 into the EPC
    # 8 bits are the header: 00001010 or 0x0A (TIAI-A-96)
    # 3 bits are the Filter: 000 (0 All Others)
    # 13 bits are the asset reference: 3 digits
    # 72 bits are the asset ID (21 digits or 12 characters, already encoded into binary)
    # = 96 bits

    self.asset_ref_bin = dec_2_bin(self.asset_ref_dec, asset_ref_bin_len)
    self.asset_id_bin.rjust(asset_id_bin_len, '0')
  
    # The return from dec_2_bin may be multpiles of 4, so chop off any leading bits for those that aren't
    if len(self.asset_ref_bin) > asset_ref_bin_len:
      self.asset_ref_bin = self.asset_ref_bin[len(self.asset_ref_bin) - asset_ref_bin_len:]

    if len(self.asset_id_bin) > asset_id_bin_len:
      self.asset_id_bin = self.asset_id_bin[len(self.asset_id_bin) - asset_id_bin_len:]
  
    self.asset_id_hex = bin_2_hex(self.asset_id_bin)
  
    self.tiai_bin = "00001010000" + self.asset_ref_bin + self.asset_id_bin
    self.tiai_hex = bin_2_hex(self.tiai_bin, 24)
  
    # Strip any leading zeros before building the URI form (note: except for asset_id_char)
    self.asset_ref_dec = self.asset_ref_dec.lstrip('0')
    self.asset_id_dec = self.asset_id_dec.lstrip('0')
    self.asset_id_hex = self.asset_id_hex.lstrip('0')
  
    # Build the uri form using the asset id type set above
    # TPM: This is why we don't zero out the others in this method like the other methods above
    if len(self.asset_id_dec) > 0:
      self.tiai_uri = "urn:epc:tag:tiai-a-96:0." + self.asset_ref_dec + "." + self.asset_id_dec
    elif len(self.asset_id_char) > 0:
      self.tiai_uri = "urn:epc:tag:tiai-a-96:0." + self.asset_ref_dec + "." + self.asset_id_char
    elif len(self.asset_id_hex) > 0:
      self.tiai_uri = "urn:epc:tag:tiai-a-96:0." + self.asset_ref_dec + "." + self.asset_id_hex

    return self.tiai_uri
  
  # Pass an optional "num" to prepend zeroes until the return is that length
  def char_2_bin(self, c, num=0):
    b = ""
    
    for x in c:
      b += self.dict_char_2_bin[x]
    
    return b.zfill(num)
  
  def bin_2_char(self, b, num=0):
    c = ""
   
    for x in (b[i:i+6] for i in range(0, len(b), 6)):
      c += self.dict_bin_2_char[x]
    
    return c.zfill(num)

  # Class variables (constant and used across all class instances)
  # Custom 6 bit encoding (limited character set)
  dict_char_2_bin = {
    "#": "100011",
    "-": "101101",
    "/": "101111",
    "0": "110000",
    "1": "110001",
    "2": "110010",
    "3": "110011",
    "4": "110100",
    "5": "110101",
    "6": "110110",
    "7": "110111",
    "8": "111000",
    "9": "111001",
    "A": "000001",
    "B": "000010",
    "C": "000011",
    "D": "000100",
    "E": "000101",
    "F": "000110",
    "G": "000111",
    "H": "001000",
    "I": "001001",
    "J": "001010",
    "K": "001011",
    "L": "001100",
    "M": "001101",
    "N": "001110",
    "O": "001111",
    "P": "010000",
    "Q": "010001",
    "R": "010010",
    "S": "010011",
    "T": "010100",
    "U": "010101",
    "V": "010110",
    "W": "010111",
    "X": "011000",
    "Y": "011001",
    "Z": "011010",
    " ": "000000"
  }

  dict_bin_2_char = {
    "100011": "#",
    "101101": "-",
    "101111": "/",
    "110000": "0",
    "110001": "1",
    "110010": "2",
    "110011": "3",
    "110100": "4",
    "110101": "5",
    "110110": "6",
    "110111": "7",
    "111000": "8",
    "111001": "9",
    "000001": "A",
    "000010": "B",
    "000011": "C",
    "000100": "D",
    "000101": "E",
    "000110": "F",
    "000111": "G",
    "001000": "H",
    "001001": "I",
    "001010": "J",
    "001011": "K",
    "001100": "L",
    "001101": "M",
    "001110": "N",
    "001111": "O",
    "010000": "P",
    "010001": "Q",
    "010010": "R",
    "010011": "S",
    "010100": "T",
    "010101": "U",
    "010110": "V",
    "010111": "W",
    "011000": "X",
    "011001": "Y",
    "011010": "Z",
    "000000": ""
  }
