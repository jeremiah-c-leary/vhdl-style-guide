
.. _configuring-pragmas:

Configuring Pragmas
-------------------

Pragmas are comments with meta data used by various vendors.
These pragmas communicate information which can change how vendor tools interprate code.

There does not appear to be a standard for defining pragmas.
This presents a challenge to detecting them across all vendor tools.

To address this challenge pragmas can be defined using regular expressions in a configuration file.

The default expressions are defined as:

.. code-block:: yaml

   pragma:
       patterns:
           - '^\\s*--\\s+synthesis\\s+\\w+\\s*$'
           - '^\\s*--\\s+synthesis\\s+\\w+\\s+\\w+\\s*$'
           - '^\\s*--\\s+pragma\\s+\\w+\\s*$'
           - '^\\s*--\\s+pragma\\s+\\w+\\s+\\w+\\s*$'
           - '^\\s*--vhdl_comp_[on|off]\\s*$'
           - '^\\s*--\\s+altera\\s+\\w+\\s*$'
           - '^\\s*--\\s+RTL_SYNTHESIS\\s+ON\\s*$'
           - '^\\s*--\\s+RTL_SYNTHESIS\\s+OFF\\s*$'
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

