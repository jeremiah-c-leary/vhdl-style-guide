If Rules
--------

if_012
######

This rule checks for code after the **then** keyword.
Moving sequential statements to their own line makes the code easier to comprehend.

**Violation**

.. code-block:: vhdl

   if (a = '1' and b = '0') then c <= (others => '0')

**Fix**

.. code-block:: vhdl

   if (a = '1' and b = '0') then
     c <= (others => '0')
