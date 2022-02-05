Configuring Port Mode Alignment
-------------------------------

The number of spaces before and after each port mode ('in', 'out', 'inout', 'buffer', 'linkage') can be individually set.
This is accomplished using the `spaces_before` and `spaces_after` options for those rules.

The default options for each rule are:

+----------+---------------+--------------+
|  Rule    | spaces_before | spaces_after |
+----------+---------------+--------------+
| port_007 |       1       |       4      |
| port_008 |       1       |       3      |
| port_009 |       1       |       1      |
+----------+---------------+--------------+

which results in the following format being enforced:

.. code-block:: vhdl

   I_INPUT  : in    std_logic;
   O_OUTPUT : out   std_logic;
   IO_INOUT : inout std_logic;

Setting the `spaces_before` and `spaces_after` options for each mode aligment rule to:

+----------+---------------+--------------+
|  Rule    | spaces_before | spaces_after |
+----------+---------------+--------------+
| port_007 |       1       |       4      |
| port_008 |       3       |       1      |
| port_009 |       1       |       1      |
+----------+---------------+--------------+

would result in the following format being enforced:

.. code-block:: vhdl

   I_INPUT  : in    std_logic;
   O_OUTPUT :   out std_logic;
   IO_INOUT : inout std_logic;

Rules Enforcing Aligment
########################

* `port_007 <port_rules.html#port-007>`_
* `port_008 <port_rules.html#port-008>`_
* `port_009 <port_rules.html#port-009>`_
