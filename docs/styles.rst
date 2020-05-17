Styles
======

VSG supports several predefined styles.
They can be used with the **--style** command line option.

The table below lists the built in styles available

+---------------+--------------------------------------------+
| Style         | Description                                |
+---------------+--------------------------------------------+
| legacy        | Rules based on the pre 2.0.0 release       |
| lowercase     | All keywords and identifiers are lowercase |
+---------------+--------------------------------------------+

Style Descriptions
------------------

legacy
~~~~~~

This style attempts to improve readability by:

* Emphasising on non vhdl identifiers by capitalizing them.

  * entity names
  * architecture names
  * ports
  * generics
  * etc...

* Blank lines added between major items

  * processes
  * if statements
  * case statements

* Alignments

  * :'s over entire entities, components, instantiations, etc...
  * <='s over groups of sequential statements
  * inline comments within processes, architecture declarative regions, etc...

* Indenting

  * 2 spaces

* Structure

  * No single line sequential statements using the when keyword
  * No code after the case when statements
  * Split if/elsif/else/end if into separate lines
  * Removing comments from instantiation and component ports and generics
  * No more than two signals can be declared on a single line

lowercase
~~~~~~~~~

This style attemps to improve readability by:

* lowercasing all vhdl keywords and non vhdl identifiers

* Blank lines added between major items

  * processes
  * if statements
  * case statements

* Alignments

  * :'s over groups of ports within entities, components, instantiations, etc...
  * <='s over groups of sequential statements
  * inline comments within processes, architecture declarative regions, etc...

* Indenting

  * 2 spaces

* Structure

  * No single line sequential statements using the when keyword
  * No code after the case when statements
  * Split if/elsif/else/end if into separate lines
  * Removing comments from instantiation and component ports and generics
  * No more than two signals can be declared on a single line


Adjusting built in styles
-------------------------

The built in styles provide several examples of how VHDL code can be formatted to improve readability.
This is by no means the only way.
The styles can be modified using the **--configuration** option.

Follow these steps to adjust the styles to the local flavor:

1. Pick a style that is close to yours
2. Create a configuration to modify the rules which must change
3. Use the style and configuration to analyze your code

Example
~~~~~~~

Let us assume the lowercase style matches 95% of the desired style.
The only differences are:

* The entity keyword is always capitalized
* Indenting is three spaces instead of two

Create a configuration with the following:

.. code-block:: yaml

   ---
   rule:
     global:
       indentSize: 3
     entity_004:
       case: upper
   ...

Then use the style and configuration together:

.. code-block:: mono

   $ vsg --style lowercase --configuration my_config.yaml -f fifo.vhd


