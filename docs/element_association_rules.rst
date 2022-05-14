.. include:: includes.rst

Element Association Rules
-------------------------

element_association_100
#######################

|phase_2| |error| |whitespace|

This rule checks for a single space between the **others** keyword and the => in an element_association.

|configuring_whitespace_rules_link|

**Violation**

.. code-block:: vhdl

   a <= (others=> (others    => '0'));

**Fix**

.. code-block:: vhdl

   a <= (others => (others => '0'));

element_association_101
#######################

|phase_2| |error| |whitespace|

This rule checks for a single space after the => in an element_association.

|configuring_whitespace_rules_link|

**Violation**

.. code-block:: vhdl

   a <= (others =>(others =>     '0'));

**Fix**

.. code-block:: vhdl

   a <= (others => (others => '0'));

