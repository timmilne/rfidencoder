#
#  epc_encoder.py
#  rfid_encoder
#
#  Created by Tim.Milne on 5/17/21
#  Copyright © 2021 Tim Milne. All rights reserved.
#
#  A python class to encode Target supported EPC encodings
#
#  This object takes Target's Department, Class, Item and a Serial Number
#  and encodes it in GS1's GID format, or a GTIN and encodes it in GS1's SGTIN format.
#  Output available in binary, hex, and URI formats
#

from converter import *

# epc_encoder python class to encapsulate the data in an instance
class EPCEncoder:

  def __init__(self):
    # Instance variables
    self.dpt = ""
    self.cls = ""
    self.itm = ""
    self.ser = ""
    self.gtin = ""
    self.gid_bin = ""
    self.gid_hex = ""
    self.gid_uri = ""
    self.sgtin_bin = ""
    self.sgtin_hex = ""
    self.sgtin_uri = ""

  # Use this to encode with DPCI
  def with_dpci(self, dpt, cls, itm, ser):
    self.dpt = dpt
    self.cls = cls
    self.itm = itm
    self.ser = ser
    self.sgtin_bin = ""
    self.sgtin_hex = ""
    self.sgtin_uri = ""
  
    # Make sure the inputs are not too long (especially the serial number)
    if len(self.dpt) > 3:
      self.dpt = self.dpt[0:3]
    if len(self.cls) > 2:
      self.cls = self.cls[0:2]
    if len(self.itm) > 4:
      self.itm = self.itm[0:4]
    if len(self.ser) > 10:
      self.ser = self.ser[0:10]
      
    # GID - e.g. urn:epc:tag:gid-96:4928100.85702.12345
    #            3504B3264014EC6000003039
    #
    # Here is how to pack the GID-96 into the EPC
    # 8 bits are the header: 00110101 or 0x35 (GID-96)
    # No Filter
    # No Partition
    # 28 bits are the manager number: 00 + 49 + Department + Class (8 digits)
    # 24 bits are the item number (object class): 000 + Item + Check Digit (7 digits)
    # 36 bits are the serial number (guaranteed 10 digits)
    # = 96 bits

    dpt_cls_dec = "049" + self.dpt + self.cls # Leading zeroes not technically valid...
    dpt_cls_bin = dec_2_bin(dpt_cls_dec, 28)
    if len(dpt_cls_bin) > 28:
      dpt_cls_bin = dpt_cls_bin[-28:]
    upc = "49" + dpt + cls + itm
    chk_dgt = calculate_check_digit(upc)
    itm_chk_dec = "00" + self.itm + chk_dgt # Leading zeroes not technically valid
    itm_chk_bin = dec_2_bin(itm_chk_dec,24)
    if len(itm_chk_bin) > 24:
      itm_chk_bin = itm_chk_bin[-24:]
    ser_bin = dec_2_bin(self.ser, 36)
    if len(ser_bin) > 36:
      ser_bin = ser_bin[-36:]

    self.gid_bin = "00110101" + dpt_cls_bin + itm_chk_bin + ser_bin
    self.gid_hex = bin_2_hex(self.gid_bin, 24)
    self.gid_uri = "urn:epc:tag:gid-96:" + dpt_cls_dec + "." + itm_chk_dec + "." + self.ser
    
    return self.gid_uri

  # Encode GID with GTIN (National brand replacement tag)
  def with_gtin_in_gid(self, gtin, ser):
    self.dpt = ""
    self.cls = ""
    self.itm = ""
    self.gtin = gtin
    self.ser = ser
    self.sgtin_bin = ""
    self.sgtin_hex = ""
    self.sgtin_uri = ""
    
    # Make sure the inputs are not too long (especially the serial number)
    if len(self.gtin) > 14:
      self.gtin = self.gtin[0:14]
    self.gtin = self.gtin.zfill(14)
    if len(self.ser) > 10:
      self.ser = self.ser[0:10]
    ser = ser.zfill(10)
    
    # GID - e.g. urn:epc:tag:gid-96:4928100.85702.12345
    #            35007850A014EC6000003039
    #
    # Here is how to repack a GTIN using the GID-96 into the EPC
    # 8 bits are the header: 00110101 or 0x35 (GID-96)
    # No Filter
    # No Partition
    # 28 bits are the manager number: digits 1 to 8 of GTIN (8 digits)
    # 24 bits are the item number (object class): 0 + digits 9 to 14 of GTIN (7 digits)
    # 36 bits are the serial number (guaranteed 10 digits)
    # = 96 bits
    
    mgr_dec = self.gtin[0:8]
    mgr_bin = dec_2_bin(mgr_dec,28) # Note: there will be leading zeroes (not technically valid)
    
    # Include the check digit!!
    itm_dec = self.gtin[8:].zfill(7) # Prepend leading zeroes (not technically valid)
    itm_bin = dec_2_bin(itm_dec, 24)
    ser_bin = dec_2_bin(self.ser, 36)
    
    self.gid_bin = "00110101" + mgr_bin + itm_bin + ser_bin
    self.gid_hex = bin_2_hex(self.gid_bin, 24)
    self.gid_uri = "urn:epc:tag:gid-96:" + mgr_dec + "." + itm_dec + "." + self.ser
    
    return self.gid_uri
    
  # Encode with GTIN
  def with_gtin(self, gtin, ser, part_bin):
    self.dpt = ""
    self.cls = ""
    self.itm = ""
    self.gtin = gtin
    self.ser = ser
    self.gid_bin = ""
    self.gid_hex = ""
    self.gid_uri = ""
  
    mgr_gin_len = int(0)
    mgr_dec_len = int(0)
    itm_bin_len = int(0)
    itm_dec_len = int(0)
    
    # GS1 Tag Data Standard parition values for SGTIN
    if part_bin == "000":
      mgr_bin_len = 40
      mgr_dec_len = 12
      itm_bin_len = 4
      itm_dec_len = 1
    elif part_bin == "001":
      mgr_bin_len = 37
      mgr_dec_len = 11
      itm_bin_len = 7
      itm_dec_len = 2
    elif part_bin == "010":
      mgr_bin_len = 34
      mgr_dec_len = 10
      itm_bin_len = 10
      itm_dec_len = 3
    elif part_bin == "011":
      mgr_bin_len = 30
      mgr_dec_len = 9
      itm_bin_len = 14
      itm_dec_len = 4
    elif part_bin == "100":
      mgr_bin_len = 27
      mgr_dec_len = 8
      itm_bin_len = 17
      itm_dec_len = 5
    elif part_bin == "101":
      mgr_bin_len = 24
      mgr_dec_len = 7
      itm_bin_len = 20
      itm_dec_len = 6
    else: #part_bin == "110"
      mgr_bin_len = 20
      mgr_dec_len = 6
      itm_bin_len = 24
      itm_dec_len = 7
  
    # Make sure the inputs are not too long (especially the serial number)
    if len(self.gtin) > 14:
      self.gtin = self.gtin[0:14]
    self.gtin = self.gtin.zfill(14)
    if len(self.ser) > 11:
      self.ser = self.ser[0:11]
    
    # SGTIN - e.g. urn:epc:tag:sgtin-96:1.0043935.046062.12345
    #              303402AE7C2CFB8000003039
    #
    # A UPC 12 can be promoted to an EAN14 by right shifting and adding two zeros to the front.
    # One of these zeroes is an indicator digit, which is '0' for items, and this will be moved
    # to the front of the item reference.  The other is the country code, and can be omitted
    # for US and Canada, as those country codes are '0'.
    #
    # Here is how to pack the SGTIN-96 into the EPC
    # 8 bits are the header: 00110000 or 0x30 (SGTIN-96)
    # 3 bits are the Filter: 001 (1 POS Item)
    # 3 bits are the Partition: See above (from the scanned RFID tag)
    # 20-40 bits are the manager number: 0 + digits 3-x of gtin
    # 24-4 bits are the 0 prefixed Item: 0 + digits x-13 of gtin (NO CHECK DIGIT)
    # 38 bits are the serial number (guaranteed 11 digits)
    # = 96 bits
    
    mgr_dec = "0" + self.gtin[2:2+(mgr_dec_len-1)]
    mgr_bin = dec_2_bin(mgr_dec, mgr_bin_len)
    
    # Drop the check digit!!
    itm_dec = "0" + self.gtin[2+(mgr_dec_len-1):2+(mgr_dec_len-1) + itm_dec_len-1]
    itm_bin = dec_2_bin(itm_dec, itm_bin_len)
    
    ser_bin = dec_2_bin(self.ser, 38)
    
    # Make sure none are too long
    if len(mgr_bin) > mgr_bin_len:
      mgr_bin = mgr_bin[-mgr_bin_len:]
    if len(itm_bin) > itm_bin_len:
      itm_bin = itm_bin[-itm_bin_len:]
    if len(ser_bin) > 38:
      ser_bin = ser_bin[-38:]
    
    self.gtin_bin = "00110000001" + part_bin + mgr_bin + itm_bin + ser_bin
    self.gtin_hex = bin_2_hex(self.gtin_bin, 24)
    self.gtin_uri = "urn:epc:tag:sgtin-96:1." + mgr_dec + "." + itm_dec + "." + self.ser

    return self.gtin_uri
    
  
# Quick Check Digit calculator
def calculate_check_digit(upc):
  sum_odd = int(0)
  sum_even = int(0)
  
  for index, digit in enumerate(upc):
    if index % 2 != 0:
      sum_even += int(digit)
    else:
      sum_odd += int(digit)
    
  return str((10 - ((3*sum_odd + sum_even)%10))%10)
