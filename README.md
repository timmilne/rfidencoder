# rfidencoder
rfidencoder package for python, includes converter module.

TPM - 5/17/21

Python based rfidencoder package that includes modules for all the encoders (epc_encoder, tcin_encoder, and tiai_encoder), as well as the converter.

   - epc_encoder.py - encodes UPCs in GS1 compliant EPC encodings
   - tcin_encoder.py - encodes retail TCINs in non GS1 compliant RFID tags for Target internal use only
   - tiai_encoder.py - encodes non retail TIAIs in non GS1 compliant RFID tags for Target internal use only

These python utilities are based on the RFIDEncoder framework originally developed for iOS.
