Configuring Indentation
-----------------------

VSG follows a predefined set of rules when indenting VHDL code.
The indenting alogrithm is driven by a YAML file.

The indent values feeding the algorithm can be obtained by using the **-oc** command line argument.
There will be a section starting with **indent**.

Understanding the Indent Configuration Data Structure
#####################################################

The indent configuration file follows this basic format:

.. code-block:: yaml

   indent:
       tokens:
           group_name:
               token_name:
                   token : value
                   after : value

where:

+-------------+--------------+-------------------------------------------------------------------+
| Attribute   | Values       | Description                                                       |
+=============+==============+===================================================================+
| indent      |   NA         | Indicates the following information defines indent behavior.      |
+-------------+--------------+-------------------------------------------------------------------+
| tokens      |   NA         | Indicates the following information defines token level behavior. |
+-------------+--------------+-------------------------------------------------------------------+
| group_name  | <string>     | The group a token belongs to.                                     |
+-------------+--------------+-------------------------------------------------------------------+
| token_name  | <string>     | The name of the token which has indent behavior.                  |
+-------------+--------------+-------------------------------------------------------------------+
| token       |   NA         | Indicates the value to apply to the token.                        |
+-------------+--------------+-------------------------------------------------------------------+
| after       |   NA         | Indicates the value to apply after the token.                     |
+-------------+--------------+-------------------------------------------------------------------+
| value       | <integer>    | The type of behavior to apply to the token or after the token.    |
|             |  current     |                                                                   |
|             | "+<integer>" |                                                                   |
|             | "-<integer>" |                                                                   |
+-------------+--------------+-------------------------------------------------------------------+

The **group_name** and **token_name** keys provide unique identifier which can be matched to types of tokens after the file has been parsed.
There are more tokens than are currently defined in the indent configuration, as not all tokens require indenting rules.

The **token** key informs VSG how to apply indents when it encounters the token.

The **after** key informs VSG how to apply indents to successive tokens it encounters.

The **value** defines the behavior for each **token** and **after** key, and are defined as:

+----------------+-----------+-----------------------------------------------------------+
| Value          | Type      | Description                                               |
+================+===========+===========================================================+
| [0-9][0-9]*    | <integer> | Sets the indent level to the specified value.             |
+----------------+-----------+-----------------------------------------------------------+
| current        | <string>  | Uses the existing indent level.                           |
+----------------+-----------+-----------------------------------------------------------+
| "+[0-9][0-9]*" | <string>  | Increase the indent relative to the current indent level. |
+----------------+-----------+-----------------------------------------------------------+
| "-[0-9][0-9]*" | <string>  | Decrease the indent relative to the current indent level. |
+----------------+-----------+-----------------------------------------------------------+

Using the **group_name** and **token_name** to identify types of VHDL tokens and then the **token** and **after** defines the behavior of the indenting algorithm.

Example
#######

VSG assumes the closing parenthesis will match with the **port** keyword.

.. code-block:: vhdl

   entity some_block is
     port (
       I_CLK   : std_logic;
       I_RST   : std_logic;
       I_WR_EN : std_logic;
       O_DATA  : std_logic_vector(7 downto 0);
     );
   end entity some_block;

If we use the following configuration...

.. code-block:: yaml

   indent:
       tokens:
           port_clause:
               close_parenthesis:
                   token : current
                   after : '-2'

...then VSG will enforce the following format:

.. code-block:: vhdl

   entity some_block is
     port (
       I_CLK   : std_logic;
       I_RST   : std_logic;
       I_WR_EN : std_logic;
       O_DATA  : std_logic_vector(7 downto 0);
       );
   end entity some_block;

How does this work?
^^^^^^^^^^^^^^^^^^^

VSG is setting the indent levels as it goes.
The port definitions in the above example are set to an indent of 2.
When the closing parenthesis is encountered, VSG checks the **port_clause.close_parenthesis.token** key to determine what to do.
In this case the key is set to **current**.
This tells VSG to keep the indent of 2 for the closing parenthesis token.
VSG then looks at the **port_clause.close_parenthesis.after** key and finds a **'-2'**.
This tells VSG to subtract two from the current indent value of 2.
Which will set the indent to 0.
The next token in the indent configuration with a **token** key value of **current** would then get 0.

The Challenge With Adjusting Indent Values
###########################################

The most difficult part of changing the indent values is knowing which **group_name** and **token_name** to use.

For the **group_name** use the VHDL LRM as a reference.
All group names match a *left-hand side* of a *production*.

For the **token_name**, refer to the output configuration using the **-oc**.
This will give the complete indent configuration.
The desired adjustment can be pulled out into a smaller file.
This file can then be applied with the **-c** option.

