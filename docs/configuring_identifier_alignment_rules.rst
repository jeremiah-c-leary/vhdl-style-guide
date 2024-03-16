
.. _configuring-identifier-alignment-rules:

Configuring Identifier Alignment Rules
--------------------------------------

There are several rules that enforce alignment of identifiers in group of lines.
Some of the configurations are available in all keyword alignment rules, while others are rule specific.

There are several options to these rules:

.. |compact_alignment| replace::
   :code:`compact_alignment`

.. |compact_alignment__yes| replace::
   :code:`yes` = Align to left most column

.. |compact_alignment__no| replace::
   :code:`no` = Align to right most column

.. |blank_line_ends_group| replace::
   :code:`blank_line_ends_group`

.. |blank_line_ends_group__yes| replace::
   :code:`yes` = Alignment will stop if a blank line is encountered

.. |blank_line_ends_group__no| replace::
   :code:`no` = Alignment will continue if a blank line is encountered

.. |comment_line_ends_group| replace::
   :code:`comment_line_ends_group`

.. |comment_line_ends_group__yes| replace::
   :code:`yes` = Alignment will stop if a blank line is encountered

.. |comment_line_ends_group__no| replace::
   :code:`no` = Alignment will continue if a blank line is encountered

.. |yes| replace::
   :code:`yes`

.. |no| replace::
   :code:`no`

.. |values_ca| replace::
   :code:`yes`, :code:`no`

.. |values_bleg| replace::
   :code:`yes`, :code:`no`

.. |values_cleg| replace::
   :code:`yes`, :code:`no`

+---------------------------+----------------+----------+----------------------------------------------+
| Option                    |   Values       | Default  | Description                                  |
+===========================+================+==========+==============================================+
| |compact_alignment|       | |values_ca|    | |yes|    | * |compact_alignment__yes|                   |
|                           |                |          | * |compact_alignment__no|                    |
+---------------------------+----------------+----------+----------------------------------------------+
| |blank_line_ends_group|   | |values_bleg|  | |yes|    | * |blank_line_ends_group__yes|               |
|                           |                |          | * |blank_line_ends_group__no|                |
+---------------------------+----------------+----------+----------------------------------------------+
| |comment_line_ends_group| | |values_cleg|  | |yes|    | * |comment_line_ends_group__yes|             |
|                           |                |          | * |comment_line_ends_group__no|              |
+---------------------------+----------------+----------+----------------------------------------------+

The options can be combined to align identifiers.

This is an example of how to configure these options.

.. code-block:: yaml

   rule :
     architecture_029:
        compact_alignment : 'yes'
        blank_line_ends_group : 'no'
        comment_line_ends_group: 'no'

The following code snippet is used in the following examples:

    .. code-block:: vhdl

      -- Control signals
      signal        wr_en   : std_logic;
      signal          rd_en   : std_logic;
      -- Status signals
      signal  wr_full : std_logic;
      signal    rd_full : std_logic;

      signal     wr_empty : std_logic;
      signal  rd_empty : std_logic;


Example: |compact_alignment| set to |yes|
#########################################

    .. code-block:: vhdl

      -- Control signals
      signal wr_en   : std_logic;
      signal rd_en   : std_logic;
      -- Status signals
      signal wr_full : std_logic;
      signal rd_full : std_logic;

      signal wr_empty : std_logic;
      signal rd_empty : std_logic;

Example: |blank_line_ends_group| set to |yes| others set to |no|
################################################################

    .. code-block:: vhdl

      -- Control signals
      signal          wr_en   : std_logic;
      signal          rd_en   : std_logic;
      -- Status signals
      signal          wr_full : std_logic;
      signal          rd_full : std_logic;

      signal     wr_empty : std_logic;
      signal     rd_empty : std_logic;

Example: |comment_line_ends_group| set to |yes| others set to |no|
##################################################################

    .. code-block:: vhdl

      -- Control signals
      signal          wr_en   : std_logic;
      signal          rd_en   : std_logic;
      -- Status signals
      signal     wr_full : std_logic;
      signal     rd_full : std_logic;

      signal     wr_empty : std_logic;
      signal     rd_empty : std_logic;

Rules Enforcing Identifier Alignment
####################################

* `architecture_029 <architecture_rules.html#architecture-029>`_
* `block_400 <block_rules.html#block-400>`_
* `function_015 <function_rules.html#function-015>`_
* `generate_400 <generate_rules.html#generate-400>`_
* `generate_402 <generate_rules.html#generate-402>`_
* `generate_404 <generate_rules.html#generate-404>`_
* `package_019 <package_rules.html#package-019>`_
* `package_body_400 <package_body_rules.html#package-body-400>`_
* `procedure_010 <procedure_rules.html#procedure-010>`_
