#
#  serial_number_generator.py
#  rfid_encoder
#
#  Created by Tim.Milne on 5/17/21
#  Copyright © 2021 Tim Milne. All rights reserved.
#
#  This file contains functions to generate pseudo randomized serial numbers
#

import time

def new_serial_with_seed(initial_seed):
  # Get the current time in seconds since the Epoch
  now_epoch_seconds = int(time.time())
  
  # Run current time throu the lcg to create even more randomness in the seed
  lcg_time_result = linear_congruential_generator_with_seed(now_epoch_seconds)
  
  # Couple with initial seed for even more randomness
  seed = int(initial_seed) + int(lcg_time_result)
  
  # Generate pseudo-random serial number
  lcg_result = linear_congruential_generator_with_seed(seed)
  
  # Prepend '00' to serial number and convert to string
  str_result = "00" + str(lcg_result)
  
  # Append zeros to the serial number until it is 15 digits long
  # Note: if you pick a different length, you'll need to pick a different prime
  # number in the linear_congruential_generator_with_seed method.
  return f'{str_result:<015}'

def linear_congruential_generator_with_seed(seed):
  prime = int(9999999999971)
  multiplier = int(1013904223)
  increment = int(1664525)
  
  return str((seed * multiplier + increment) % prime)
