
.. _configuring-indentation:

Configuring Indentation
-----------------------

VSG follows a predefined set of rules when indenting VHDL code.
The indenting algorithm is driven by a YAML file.

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
|             | current      |                                                                   |
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

Example 1
#########

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

Example 2
#########

Instantiations default the indentation of port map and generic map to one more than the label:

.. code-block:: vhdl

   U_FIFO : FIFO
     generic map ()
     port map ();

If the desired indentation is to have the port map and generic map at the same level as the label...

.. code-block:: vhdl

   U_FIFO : FIFO
   generic map ()
   port map ();

...follow these steps to enforce this type of indentation:

  1)  Determine tokens to use for indent
  2)  Export indent configuration
  3)  Update indent configuration
  4)  Run with indent configuration

Determine tokens to use for indent
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Check the LRM entry for instantiations.

.. code-block:: text

   component_instantiation_statement ::=
       instantiation_label :
           instantiated_unit
               [ generic_map_aspect ]
               [ port_map_aspect ] ;

VSG tokenizes a VHDL file based on the LRM and tokens are named per the LRM.
Tokens are located in the directory `vsg/tokens` and stored in files based on the entry name.
In this case, there is a file named `component_instantiation_statement.py` file:

.. code-block:: python

   from vsg import parser


   class instantiation_label(parser.label):
       '''
       unique_id = component_instantiation_statement : instantiation_label
       '''

       def __init__(self, sString):
           super().__init__(sString)


   class label_colon(parser.label_colon):
       '''
       unique_id = component_instantiation_statement : label_colon
       '''

       def __init__(self):
           super().__init__()


   class semicolon(parser.semicolon):
       '''
       unique_id = component_instantiation_statement : semicolon
       '''

       def __init__(self, sString=None):
           super().__init__()

Export indent configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Use the `-oc` option to export rule and indent configuration.
There will be a section of the JSON file named `indent`:

.. code-block:: json

   {
     "indent": {
       "tokens": {
         "architecture_body": {
           "architecture_keyword": {
             "after": 1,
             "token": 0
           },
           "begin_keyword": {
             "after": 1,
             "token": 0
           },
           "end_keyword": {
             "after": 0,
             "token": 0
           }
         }
       }
     }
   }

In this example, search further down in the tokens for `component_instantiation_statement`:

.. code-block:: json

   {
     "component_instantiation_statement": {
       "instantiation_label": {
         "after": "+1",
         "token": "current"
       },
       "semicolon": {
         "after": "-1",
         "token": "current"
       }
     }
   }

Update indent configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^

The default indent is to increase the indent by 1 after the `instantiation_label` is found and then decrease the indent by 1 when the `semicolon` is found.
To enforce the desired indent, change the `after` entry for both `instantiation_label` and `semicolon` to `"current"`.
Using `"current"` tells VSG to not change the indent after the label and semicolon are encountered.

Extract the `component_instantiation_statement` section out of the JSON file and save it to a new configuration file or add it to an existing one.

.. code-block:: json

   {
     "indent": {
       "tokens": {
         "component_instantiation_statement": {
           "instantiation_label": {
             "after": "current",
             "token": "current"
           },
           "semicolon": {
             "after": "current",
             "token": "current"
           }
         }
       }
     }
   }

Run with indent configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Include the configuration when executing VSG:

.. code-block:: text

   $ vsg -c indent.json -f fifo.vhd --fix

Using the above configuration on the following file...

.. code-block:: vhdl


    architecture rtl of fifo is

    begin

      U_FIFO : FIFO
        generic map ();

      a <= b;

      U_FIFO : FIFO
        port map ();

      a <= b;

      U_FIFO : FIFO
        generic map ()
        port map ();

      a <= b;

    end architecture rtl;

...results in the following updates:

.. code-block:: vhdl

   architecture rtl of fifo is

   begin

     u_fifo : component fifo
     generic map ();

     a <= b;

     u_fifo : component fifo
     port map ();

     a <= b;

     u_fifo : component fifo
     generic map ()
     port map ();

     a <= b;

   end architecture rtl;
