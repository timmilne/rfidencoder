#
#  tcin_encoder.py
#  rfid_encoder
#
#  Created by Tim.Milne on 5/17/21
#  Copyright © 2021 Tim Milne. All rights reserved.
#
#  A python class to encode a Target Common Item Number
#
#  This object takes a Target Common Item Number (TCIN) and encodes it in a proprietary
#  TCIN-96 format.  Output available in binary, hex and URI formats.  If no unique serial
#  number is available, there are two initializers that will leverage a linear congruential
#  generator to create a pseudo random serial number, one with a seed, one without.
#

from converter import *
from serial_number_generator import new_serial_with_seed

# tcin_encoder python class to encapsulate the data in an instance
class TCINEncoder:

  def __init__(self):
    # Instance variables
    self.tcin = ""
    self.ser = ""
    self.tcin_bin = ""
    self.tcin_hex = ""
    self.tcin_uri = ""

  # Use this with no seed
  def with_tcin(self, tcin):
    return self.with_tcin_and_seed(tcin, "7725272730706")
   
  # Use this with a seed
  def with_tcin_and_seed(self, tcin, seed):
    return self.with_tcin_and_serial_number (tcin, new_serial_with_seed(seed))
  
  # Use this with TCIN and serial number
  def with_tcin_and_serial_number(self, tcin, ser):
  
    # Set the inputs
    self.tcin = tcin
    self.ser = ser
    self.tcin_bin = ""
    self.tcin_hex = ""
    self.tcin_uri = ""
    
    # We will encode TCINs in a Target proprietary TCIN-96
    tcin_bin_len = int(35)
    tcin_dec_len = int(10)
    ser_bin_len = int(50)
    ser_dec_len = int(15)
    
    # Make sure the inputs are not too long (especially the serial number)
    if len(self.tcin) > tcin_dec_len:
      self.tcin = self.tcin[0:tcin_dec_len]
    if len(self.tcin) < tcin_dec_len:
      self.tcin = self.tcin.zfill(tcin_dec_len)
    if len(self.ser) > ser_dec_len:
      self.ser = self.ser[0:ser_dec_len]
      
    # TCIN-96 - e.g. urn:epc:tag:tcin-96:0.0013951442.123456789012345
    #              0800035387487048860DDF79
    #
    # A TCIN is a 10 digit decimal number with a unique serial number.
    #
    # Here is how to pack the TCIN-96 into the EPC
    # 8 bits are the header: 00001000 or 0x08 (TCIN-96)
    # 3 bits are the Filter: 000 (0 All Others)
    # 35 bits are the manager number: 10 digit TCIN
    # 50 bits are the serial number (guaranteed 15 digits)
    # = 96 bits
  
    tcin_bin = dec_2_bin(self.tcin, tcin_bin_len)
    ser_bin = dec_2_bin(self.ser, ser_bin_len)
  
    # The return from dec_2_bin is multpiles of 4, so chop off any leading bits for those that aren't
    if len(tcin_bin) > tcin_bin_len:
      tcin_bin = tcin_bin[len(tcin_bin) - tcin_bin_len:]
  
    if len(ser_bin) > ser_bin_len:
      ser_bin = ser_bin[len(ser_bin) - ser_bin_len:]
  
    self.tcin_bin = "00001000000" + tcin_bin + ser_bin
    self.tcin_hex = bin_2_hex(self.tcin_bin, 24)
  
    # Strip any leading zeros before building the URI form, and build the uri
    self.tcin_uri = "urn:epc:tag:tcin-96:0." + tcin.lstrip('0') + "." + ser.lstrip('0')
  
    return self.tcin_uri
