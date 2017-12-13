If Rules
--------

if_012
######

This rule checks for code after the **then** keyword.
Moving sequential statements to their own line makes the code easier to comprehend.

**Violation**

.. code-block:: vhdl

   if (a = '1') then c <= '1';

**Fix**

.. code-block:: vhdl

   if (a = '1') then
     c <= '1';

if_013
######

This rule checks the **else** keyword is on it's own line.

**Violation**

.. code-block:: vhdl

   if (a = '1') then c <= '1'; else c <= '0'; end if;

**Fix**

.. code-block:: vhdl

   if (a = '1') then c <= '0';
   else c <= '1'; end if;

if_014
######

This rule checks the **end if** keyword is on it's own line.

**Violation**

.. code-block:: vhdl

   if (a = '1') then c <= '1'; else c <= '0'; end if;

**Fix**

.. code-block:: vhdl

   if (a = '1') then c <= '1'; else c <= '0';
   end if;

if_017
######

This rule checks the **elsif** keyword is on it's own line.

**Violation**

.. code-block:: vhdl

   if (a = '1') then c <= '1'; else c <= '0'; elsif (b = '0') then d <= '0'; end if;

**Fix**

.. code-block:: vhdl

   if (a = '1') then c <= '1'; else c <= '0';
   elsif (b = '0') then d <= '0'; end if;

