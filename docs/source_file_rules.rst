.. include:: includes.rst

Source File Rules
-----------------

source_file_001
###############

|phase_1| |error| |unfixable| |structure|

This rule checks for the existance of the source file passed to VSG.

**Violation**

Source file passed to VSG does not exist.
This violation will be reported at the command line in the normal output.
It will also be reported in the junit file if the --junit option is used.

**Fix**

Pass correct file name to VSG.

