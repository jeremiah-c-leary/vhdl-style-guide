Configuring Length Rules
------------------------

VSG includes several rules enforcing maximum lengths of code structures.
These rules are set as warnings.

Overriding Line Length
######################

Limiting the line length of the VHDL code can improve readability.
Code that exceeds the editor window is more difficult to read.
The default line length is 120, and can be changed by configuring rule **length_001**.

Use the following configuration to change the line length to 180.

.. code-block:: yaml

   rule :
     length_001 :
        length : 180

Overridding File Line Length
############################

Limiting the length of a VHDL file can improve readability.
Excessively long files can indicate the file can be broken into smaller modules.
The default line length is 2000, and can be changed by configuring rule **length_002**.

Use the following configuration to change the file length to 5000.

.. code-block:: yaml

   rule :
     length_002 :
        length : 5000

Overridding Process Line Length
###############################

Limiting the length of a VHDL processes can improve readability.
Processes should perform a limited number of functions.
Smaller processes are easier to understand.

The default length is 500 lines, and can be changed by configuring rule **length_003**.

Use the following configuration to change the process length to 1000.

.. code-block:: yaml

   rule :
     length_003 :
        length : 1000
