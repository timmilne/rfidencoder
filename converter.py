#
#  converter.py
#  rfid_encoder
#
#  Created by Tim.Milne on 5/17/21
#  Copyright © 2021 Tim Milne. All rights reserved.
#
#  This file contains functions to convert between Decimal, Hex and Binary
#
#  If you pass an optional 'num' argument, the return is prepended with zeroes
#  till the total length of 'num'
#

def dec_2_bin(dec, num=0):
  return hex_2_bin(dec_2_hex(dec), num)

def bin_2_dec(bin, num=0):
   return hex_2_dec(bin_2_hex(bin), num)

def dec_2_hex(dec, num=0):
  return f'{str(hex(int(dec))[2:].upper()).zfill(num)}'

def hex_2_dec(hex, num=0):
  return f'{str(int(hex,16)).zfill(num)}'

def bin_2_hex(bin, num=0):
  return f'{str(hex(int(bin,2))[2:].upper()).zfill(num)}'

def hex_2_bin(hex, num=0):
  return f'{str(bin(int(hex,16))[2:]).zfill(num)}'
