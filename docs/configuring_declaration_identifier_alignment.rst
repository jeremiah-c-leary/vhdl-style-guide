Configuring Identifer Alignment Rules
-------------------------------------

There are several rules that enforce alignment of identifiers in group of lines.
Some of the configurations are available in all keyword alignment rules, while others are rule specific.

Common Identifier Alignment Configuration
#########################################

Following configuration options can be independently changed for each of the identifier alignment rules.

#. :code:`blank_line_ends_group` - if set to :code:`True` any blank line encountered in the VHDL file ends the group of lines that should be aligned and starts new group.
   By default set to :code:`True`.

    **Violation**

    .. code-block:: vhdl

      signal wr_en   : std_logic;
      file results :

      signal rd_en   : std_logic;
      constant c_short_period : time;


    **Fix (blank_line_ends_group = True)**

    .. code-block:: vhdl

      signal wr_en   : std_logic;
      file   results :

      signal   rd_en   : std_logic;
      constant c_short_period : time;


    **Fix (blank_line_ends_group = False)**

    .. code-block:: vhdl

      signal   wr_en   : std_logic;
      file     results :

      signal   rd_en   : std_logic;
      constant c_short_period : time;


#. :code:`comment_line_ends_group` - if set to :code:`True` any purely comment line in the VHDL file ends the group of lines that should be aligned and starts new group.
   By default set to :code:`True`.

    **Violation**

    .. code-block:: vhdl

      signal wr_en   : std_logic;
      file results :
      -- some comment
      signal rd_en   : std_logic;
      constant c_short_period : time;

    **Fix (comment_line_ends_group = True)**

    .. code-block:: vhdl

      signal wr_en   : std_logic;
      file   results :
      -- some comment
      signal   rd_en   : std_logic;
      constant c_short_period : time;


    **Fix (comment_line_ends_group = False)**

    .. code-block:: vhdl
      signal   wr_en   : std_logic;
      file     results :
      -- some comment
      signal   rd_en   : std_logic;
      constant c_short_period : time;


.. NOTE:: As all identifier alignment rules have above configurations they are not mentioned in the documentation for each rule.
