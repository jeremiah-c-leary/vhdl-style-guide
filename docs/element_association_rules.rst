.. include:: includes.rst

Element Association Rules
-------------------------

element_association_100
#######################

|phase_2| |error| |whitespace|

This rule checks for a single space between the **others** keyword and the => in an element_association. 

**Violation**

.. code-block:: vhdl

   a <= (others=> (others    => '0'));

**Fix**

.. code-block:: vhdl

   a <= (others => (others => '0'));

