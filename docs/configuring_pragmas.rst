
.. _configuring-pragmas:

Configuring Pragmas
-------------------

Pragmas are comments with meta data used by various vendors.
These pragmas communicate information which can change how vendor tools interpret code.

There does not appear to be a standard for defining pragmas.
This presents a challenge to detecting them across all vendor tools.

To address this challenge, pragmas can be defined using regular expressions in a configuration file.

There are three types of pragmas:  open, close, and single.

The open and close pragmas form a pair.
For example:

.. code-block:: vhdl

   -- synthesis translate_off
   -- synthesis translate_on

The first pragma is an open type, while the second is a close type.

A single type of pragma stands on its own.
For example:

.. code-block:: vhdl

   -- synthesis library <my_lib>

The default expressions are defined as:

.. code-block:: yaml

   pragma:
       patterns:
           open:
               - '^\\s*--\\s+synthesis\\s+translate_off\\s*$'
               - '^\\s*--\\s+RTL_SYNTHESIS\\s+OFF\\s*$'
               - '^\\s*--vhdl_comp_off]\\s*$'
           close:
               - '^\\s*--\\s+synthesis\\s+translate_on\\s*$'
               - '^\\s*--\\s+RTL_SYNTHESIS\\s+ON\\s*$'
               - '^\\s*--vhdl_comp_on]\\s*$'
           single:
               - '^\\s*--\\s+synthesis\\s+\\w+\\s*$'
               - '^\\s*--\\s+synthesis\\s+\\w+\\s+\\w+\\s*$'
               - '^\\s*--\\s+pragma\\s+\\w+\\s*$'
               - '^\\s*--\\s+pragma\\s+\\w+\\s+\\w+\\s*$'
               - '^\\s*--\\s+altera\\s+\\w+\\s*$'
               - '^\\s*--\\s+synopsys\\s+\\w+\\s*$'
               - '^\\s*--\\s+synopsys\\s+\\w+\\s+\\w+\\s*$'
               - '^\\s*--\\s+xilinx\\s+\\w+\\s*$'
               - "^\\s*--\\s+xilinx\\s+\\w+\\s+\\w+\\s*$"

Each pattern will be applied to a line in the source file.
If a match is detected, the comment will be converted into a pragma.
Otherwise the comment will be left as a comment.

Rules Using Pragmas
###################

* `pragma_300 <pragma_rules.html#pragma-300>`_
* `pragma_400 <pragma_rules.html#pragma-400>`_
* `pragma_401 <pragma_rules.html#pragma-401>`_
* `pragma_402 <pragma_rules.html#pragma-402>`_
* `pragma_403 <pragma_rules.html#pragma-403>`_

