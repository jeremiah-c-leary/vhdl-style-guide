Range Rules
-----------

These rules cover the range definitions in signals, constants, ports and other cases where ranges are defined.

range_001
#########

This rule checks the case of the **downto** keyword.

.. NOTE::  The default is lowercase.

   Refer to the section `Configuring Uppercase and Lowercase Rules <configuring_case.html>`_ for information on changing the default case.

**Violation**

.. code-block:: vhdl

   signal SIG1 : std_logic_vector(3 DOWNTO 0);
   signal SIG2 : std_logic_vector(16 downTO 1);

**Fix**

.. code-block:: vhdl

   signal SIG1 : std_logic_vector(3 downto 0);
   signal SIG2 : std_logic_vector(16 downTO 1);

range_002
#########

This rule checks the case of the **to** keyword.

.. NOTE::  The default is lowercase.

   Refer to the section `Configuring Uppercase and Lowercase Rules <configuring_case.html>`_ for information on changing the default case.

**Violation**

.. code-block:: vhdl

   signal SIG1 : std_logic_vector(3 TO 0);
   signal SIG2 : std_logic_vector(16 tO 1);

**Fix**

.. code-block:: vhdl

   signal SIG1 : std_logic_vector(3 to 0);
   signal SIG2 : std_logic_vector(16 to 1);
