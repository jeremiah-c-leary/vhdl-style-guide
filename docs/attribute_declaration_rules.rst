Attribute Declaration Rules
---------------------------

Structural Rules (000 - 099)
############################

No rules have been identified.

Whitespacing Rules (100 - 199)
##############################

attribute_declaration_100
^^^^^^^^^^^^^^^^^^^^^^^^^

This rule checks for a single space after the following elements:  **attribute** keyword and colon.

**Violation**

.. code-block:: vhdl

   attribute   max_delay :   time;

**Fix**

.. code-block:: vhdl

   attribute max_delay : time;

attribute_declaration_101
^^^^^^^^^^^^^^^^^^^^^^^^^

This rule checks for at least a single space before the colon.

**Violation**

.. code-block:: vhdl

   attribute max_delay: time;

**Fix**

.. code-block:: vhdl

   attribute max_delay : time;

Vertical Spacing Rules (200 - 299)
##################################

No rules have been identified at this time.

Indentation Rules (300 - 399)
#############################

attribute_declaration_300
^^^^^^^^^^^^^^^^^^^^^^^^^

This rule checks the indent of the **attribute** keyword.

**Violation**

.. code-block:: vhdl

   signal sig1 : std_logic;
      attribute max_delay : time;

**Fix**

.. code-block:: vhdl

   signal sig1 : std_logic;
   attribute max_delay : time;

Alignment Rules (400 - 499)
###########################

Alignment rules would be handled by the element using attributes.

Capitalization Rules (500 - 599)
################################

attribute_declaration_500
^^^^^^^^^^^^^^^^^^^^^^^^^

This rule checks the **attribute** keyword has proper case.

Refer to the section `Configuring Uppercase and Lowercase Rules <configuring_case.html>`_ for information on changing the default case.

**Violation**

.. code-block:: vhdl

   ATTRIBUTE max_delay : time;

**Fix**

.. code-block:: vhdl

   attribute max_delay : time;

attribute_declaration_501
^^^^^^^^^^^^^^^^^^^^^^^^^

This rule checks the *identifier* has proper case.

Refer to the section `Configuring Uppercase and Lowercase Rules <configuring_case.html>`_ for information on changing the default case.

**Violation**

.. code-block:: vhdl

   attribute MAX_DELAY : time;

**Fix**

.. code-block:: vhdl

   attribute max_delay : time;

attribute_declaration_502
^^^^^^^^^^^^^^^^^^^^^^^^^

This rule checks the *type_mark* has proper case.

Refer to the section `Configuring Uppercase and Lowercase Rules <configuring_case.html>`_ for information on changing the default case.

**Violation**

.. code-block:: vhdl

   attribute max_delay : TIME;

**Fix**

.. code-block:: vhdl

   attribute max_delay : time;

Naming Convention Rules (600 - 699)
###################################

No rules have been identified.
