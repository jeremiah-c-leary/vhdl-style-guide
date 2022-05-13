.. _configuring-whitespace-rules:

Configuring Whitespace Rules
----------------------------

There are rules which will check for a single whitespace between keywords or keywords and identifiers.
The single whitespace can be configured to allow for multiple or no whitespaces.

<jcl - rewrite the following sentence>
There are a couple of options to these rules, which can be selected by using the :code:`style` option:

+--------------------------+----------------------------------------------------------+
| Option                   | Description                                              |
+==========================+==========================================================+
| maximum_number_of_spaces | Determines the number of whitespace characters to allow. |
+--------------------------+----------------------------------------------------------+
| minimum_number_of_spaces | Determines the number of whitespace characters to allow. |
+--------------------------+----------------------------------------------------------+
| align_to_next_tab        | When true, will add spaces to align with next valid tab. |
+--------------------------+----------------------------------------------------------+

The :code:`maximum_number_of_spaces` and :code:`minimum_number_of_spaces` can accept several values:

+-----------------------+----------------------------------------------------------+
| Value                 | Description                                              |
+=======================+==========================================================+
| [0-9][0-9]*           | The number of spaces to enforce.                         |
+-----------------------+----------------------------------------------------------+
| >[0-9][0-9]*          | The minimum number of spaces to enforce.                 |
+-----------------------+----------------------------------------------------------+

.. | <[0-9][0-9]*          | The maximum number of spaces to enforce.                 |
.. +-----------------------+----------------------------------------------------------+

These options combined with the values allow complete control over the number of whitespaces allowed.

Example:  enforce one whitespace between end and architecture
##############################################################

.. code-block:: yaml

   rule :
     architecture_012:
        maximum_number_of_spaces: 1
        minimum_number_of_spaces: 1

In this example, the number of whitespaces between the keywords must be 1.

.. code-Block:: vhdl

   end architecture;

Example:  enforce two whitespaces between end and architecture
##############################################################

.. code-block:: yaml

   rule :
     architecture_012:
        maximum_number_of_spaces: 2
        minimum_number_of_spaces: 2

In this example, the number of whitespaces between the keywords must be 2.

.. code-Block:: vhdl

   end  architecture;


Example:  allow at least 1 space before a colon
###############################################

.. code-block:: yaml

   rule :
     signal_006:
        maximum_number_of_spaces: >1
        minimum_number_of_spaces: 1

In this example, there must be at least a single whitespace before the colon.
All of these would not be a violation.

.. code-Block:: vhdl

   signal wr_en : std_logic;
   signal wr_en  : std_logic;
   signal wr_en                : std_logic;

Example:  allow between 3 and 5 spaces after a colon
####################################################

.. code-block:: yaml

   rule :
     signal_005:
        maximum_number_of_spaces: 5
        minimum_number_of_spaces: 3

In this example, there must be at least 3 spaces after the colon and no more than 5.
All of these would not be a violation.

.. code-block:: vhdl

   signal wr_en :   std_logic;
   signal wr_en :     std_logic;
   signal wr_en :      std_logic;

If there were less than 3 spaces...

.. code-block:: vhdl

   signal wr_en : std_logic;

Then the code would be a violation and the fix would insert enough spaces to get to 3:

.. code-block:: vhdl

   signal wr_en :   std_logic;

If there were more than 5 spaces...

.. code-block:: vhdl

   signal wr_en :                std_logic;

Then the code would be a violation and the fix would remove enough spaces to get to 5:

.. code-block:: vhdl

   signal wr_en :     std_logic;

Rules Enforcing Whitespace
##########################

* `architecture_012 <architecture_rules.html#architecture-012>`_
