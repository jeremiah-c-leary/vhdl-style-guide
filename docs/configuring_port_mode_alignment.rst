
.. _configuring-port-mode-alignment:

Configuring Port Mode Alignment
-------------------------------

The number of spaces before and after each port mode ('in', 'out', 'inout', 'buffer', 'linkage') can be individually set.
This is accomplished using the `spaces_before` and `spaces_after` options for those rules.

.. |spaces_before| replace::
   :code:`spaces_before`

.. |spaces_after| replace::
   :code:`spaces_after`

.. |values| replace::
   integer > 0

.. |default_value_1| replace::
   1

.. |default_value_2| replace::
   Rule dependent

.. |spaces_before_description| replace::
   Sets the number of spaces required before the mode

.. |spaces_after_description| replace::
   Sets the number of spaces required after the mode

+----------------------+----------+-------------------+-----------------------------+
| Option               | Values   | Default Value     | Description                 |
+======================+==========+===================+=============================+
| |spaces_before|      | |values| | |default_value_1| | |spaces_before_description| |
+----------------------+----------+-------------------+-----------------------------+
| |spaces_after|       | |values| | |default_value_2| | |spaces_after_description|  |
+----------------------+----------+-------------------+-----------------------------+

This is an example of how to configure these options.

.. code-block:: yaml

   rule :
     port_007:
        spaces_before: 1
        spaces_after : 4

Example: Align modes to the left (default)
##########################################

.. code-block:: yaml

   rule :
     port_007:
        spaces_before: 1
        spaces_after : 4
     port_008:
        spaces_before: 1
        spaces_after : 3
     port_009:
        spaces_before: 1
        spaces_after : 1

which results in the following format being enforced:

.. code-block:: vhdl

   I_INPUT  : in    std_logic;
   O_OUTPUT : out   std_logic;
   IO_INOUT : inout std_logic;

Example:  Align modes based on type
###################################

.. code-block:: yaml

   rule :
     port_007:
        spaces_before: 1
        spaces_after : 4
     port_008:
        spaces_before: 3
        spaces_after : 1
     port_009:
        spaces_before: 1
        spaces_after : 1

would result in the following format being enforced:

.. code-block:: vhdl

   I_INPUT  : in    std_logic;
   O_OUTPUT :   out std_logic;
   IO_INOUT : inout std_logic;

Rules Enforcing Alignment
#########################

* `port_007 <port_rules.html#port-007>`_
* `port_008 <port_rules.html#port-008>`_
* `port_009 <port_rules.html#port-009>`_
