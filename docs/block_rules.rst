.. include:: icons.rst

Block Rules
-----------

block_001
#########

|phase_1| |error|

This rule checks the block label and the **block** keyword are on the same line.
Keeping the label and generate on the same line reduces excessive indenting.

**Violation**

.. code-block:: vhdl

   block_label :
     block is

**Fix**

.. code-block:: vhdl

   block_label : block is

block_002
#########

|phase_1| |error|

This rule checks for the existence of the **is** keyword.

Refer to the section `Configuring Optional Items <configuring.html#configuring-optional-items>`_ for options.

**Violation**

.. code-block:: vhdl

   block_label : block
   block_label : block (guard_condition)

**Fix**

.. code-block:: vhdl

   block_label : block is
   block_label : block (guard_condition) is

block_003
#########

|phase_1| |error|

This rule checks the **is** keyword is on the same line as the **block** keyword.

**Violation**

.. code-block:: vhdl

   block_label : block
   is

**Fix**

.. code-block:: vhdl

   block_labeel : block is

block_004
#########

|phase_1| |error|

This rule checks the **begin** keyword is on it's own line.

**Violation**

.. code-block:: vhdl

   block is begin

**Fix**

.. code-block:: vhdl

   block is
   begin

block_005
#########

|phase_1| |error|

This rule checks for code after the **begin** keyword.

**Violation**

.. code-block:: vhdl

   begin a <= b;

**Fix**

.. code-block:: vhdl

   begin
   a <= b;

block_006
#########

|phase_1| |error|

This rule checks the **end** keyword is on it's own line.

**Violation**

.. code-block:: vhdl

   a <= b; end block;

**Fix**

.. code-block:: vhdl

   a <= b;
   end block;

block_007
#########

|phase_1| |error|

This rule checks the block label exists in the closing of the block statement.

Refer to the section `Configuring Optional Items <configuring.html#configuring-optional-items>`_ for options.

**Violation**

.. code-block:: vhdl

   end block;

**Fix**

.. code-block:: vhdl

   end block block_label;

block_100
#########

|phase_2| |error| |whitespace|

This rule checks for a single space between the following block elements:  label, label colon, **block** keyword, guard open parenthesis, guart close parenthesis, and **is** keywords.

**Violation**

.. code-block:: vhdl

   block_label    :    block    (guard_condition)   is
   block_label  :   block    is

**Fix**

.. code-block:: vhdl

   block_label : block (guard_condition) is
   block_label : block is

block_101
#########

|phase_2| |error| |whitespace|

This rule checks for a single space between the **end** and **block** keywords and label.

**Violation**

.. code-block:: vhdl

   end   block   block_label;

**Fix**

.. code-block:: vhdl

   end block block_label;

block_200
#########

|phase_3| |error| |blank_line|

This rule checks for blank lines or comments above the block label.

Refer to `Configuring Previous Line Rules <configuring.html#configuring-previous-line-rules>`_ for options.

**Violation**

.. code-block:: vhdl

   a <= b;
   block_label : block is

**Fix**

.. code-block:: vhdl

   a <= b;

   block_label : block is

block_201
#########

|phase_3| |error| |blank_line|

This rule checks for a blank line below the **block** keyword.

Refer to the section `Configuring Blank Lines <configuring.html#configuring-blank-lines>`_ for options regarding comments.

**Violation**

.. code-block:: vhdl

   block_label : block is
     constant width : integer := 32;

**Fix**

.. code-block:: vhdl

   block_label : block is

     constant width : integer := 32;

block_202
#########

|phase_3| |error| |blank_line|

This rule checks for blank lines or comments above the **begin** keyword.

Refer to `Configuring Blank Lines <configuring.html#configuring-blank-lines>`_ for options.

**Violation**

.. code-block:: vhdl

   block_label block is

     constant width : integer := 32;
   begin

**Fix**

.. code-block:: vhdl

   block_label block is

     constant width : integer := 32;

   begin

block_203
#########

|phase_3| |error| |blank_line|

This rule checks for a blank line below the **begin** keyword.

Refer to the section `Configuring Blank Lines <configuring.html#configuring-blank-lines>`_ for options regarding comments.

**Violation**

.. code-block:: vhdl

   begin
     a <= b;

**Fix**

.. code-block:: vhdl

   begin

     a <= b;

block_204
#########

|phase_3| |error| |blank_line|

This rule checks for blank lines or comments above the **end** keyword.

Refer to `Configuring Blank Lines <configuring.html#configuring-blank-lines>`_ for options.

**Violation**

.. code-block:: vhdl

   begin

     a <= b;
   end block block_label;

**Fix**

.. code-block:: vhdl

   begin

     a <= b;

   end block block_label;

block_205
#########

|phase_3| |error| |blank_line|

This rule checks for a blank line below the semicolon.

Refer to the section `Configuring Blank Lines <configuring.html#configuring-blank-lines>`_ for options regarding comments.

**Violation**

.. code-block:: vhdl

   end block block_label;
   a <= b;

**Fix**

.. code-block:: vhdl

   end block block_label;

   a <= b;

block_300
#########

|phase_4| |error| |indent|

This rule checks the indent of the block label.

**Violation**

.. code-block:: vhdl

   a <= b;

      block_label : block is

**Fix**

.. code-block:: vhdl

   a <= b;

   block_label : block is

block_301
#########

|phase_4| |error| |indent|

This rule checks the indent of the **begin** keyword.

**Violation**

.. code-block:: vhdl

   block_label : block is

     begin

**Fix**

.. code-block:: vhdl

   block_label : block is

   begin

block_302
#########

|phase_4| |error| |indent|

This rule checks the indent of the **end** keyword.

**Violation**

.. code-block:: vhdl

   block_label : block is

   begin

     end block block_label;

**Fix**

.. code-block:: vhdl

   block_label : block is

   begin

   end block block_label;

block_400
#########

|phase_5| |error|

This rule checks the identifiers for all declarations are aligned in the block declarative region.

Refer to the section `Configuring Identifier Alignment Rules <configuring.html#configuring-identifier-alignment-rules>`_ for information on changing the configurations.

**Violation**

.. code-block:: vhdl

   variable    var1 : natural;
   constant  c_period : time;

**Fix**

.. code-block:: vhdl

   variable var1     : natural;
   constant c_period : time;

block_401
#########

|phase_5| |error|

This rule checks the colons are in the same column for all declarations in the block declarative part.
Refer to the section `Configuring Keyword Alignment Rules <configuring.html#configuring-keyword-alignment-rules>`_ for information on changing the configurations.

**Violation**

.. code-block:: vhdl

   signal sig1: natural;
   variable var2  : natural;
   constant c_period : time;
   file my_test_input : my_file_type;

**Fix**

.. code-block:: vhdl

   signal sig1        : natural;
   variable var2      : natural;
   constant c_period  : time;
   file my_test_input : my_file_type;

block_500
#########

|phase_6| |error|

This rule checks the label has proper case.

Refer to the section `Configuring Uppercase and Lowercase Rules <configuring.html#configuring-uppercase-and-lowercase-rules>`_ for information on changing the default case.

**Violation**

.. code-block:: vhdl

   BLOCK_LABEL : block is

**Fix**

.. code-block:: vhdl

   block_label : block is

block_501
#########

|phase_6| |error|

This rule checks the **block** keyword has proper case.

Refer to the section `Configuring Uppercase and Lowercase Rules <configuring.html#configuring-uppercase-and-lowercase-rules>`_ for information on changing the default case.

**Violation**

.. code-block:: vhdl

   block_label : BLOCK is

**Fix**

.. code-block:: vhdl

   block_label : block is

block_502
#########

|phase_6| |error|

This rule checks the **is** keyword has proper case.

Refer to the section `Configuring Uppercase and Lowercase Rules <configuring.html#configuring-uppercase-and-lowercase-rules>`_ for information on changing the default case.

**Violation**

.. code-block:: vhdl

   block_label : block IS

**Fix**

.. code-block:: vhdl

   block_label : block is

block_503
#########

|phase_6| |error|

This rule checks the **begin** keyword has proper case.

Refer to the section `Configuring Uppercase and Lowercase Rules <configuring.html#configuring-uppercase-and-lowercase-rules>`_ for information on changing the default case.

**Violation**

.. code-block:: vhdl

   block_label : block is
   BEGIN

**Fix**

.. code-block:: vhdl

   block_label : block is
   begin

block_504
#########

|phase_6| |error|

This rule checks the **end** keyword has proper case.

Refer to the section `Configuring Uppercase and Lowercase Rules <configuring.html#configuring-uppercase-and-lowercase-rules>`_ for information on changing the default case.

**Violation**

.. code-block:: vhdl

   END block block_label;

**Fix**

.. code-block:: vhdl

   end block block_label;

block_505
#########

|phase_6| |error|

This rule checks the **block** keyword in the **end block** has proper case.

Refer to the section `Configuring Uppercase and Lowercase Rules <configuring.html#configuring-uppercase-and-lowercase-rules>`_ for information on changing the default case.

**Violation**

.. code-block:: vhdl

   end BLOCK block_label;

**Fix**

.. code-block:: vhdl

   end block block_label;

block_506
#########

|phase_6| |error|

This rule checks the label has proper case on the end block declaration.

Refer to the section `Configuring Uppercase and Lowercase Rules <configuring.html#configuring-uppercase-and-lowercase-rules>`_ for information on changing the default case.

**Violation**

.. code-block:: vhdl

   end block BLOCK_LABEL;

**Fix**

.. code-block:: vhdl

   end block block_label;

block_600
#########

|phase_7| |disabled| |error|

This rule checks for valid suffixes on block labels.
The default suffix is *_blk*.

Refer to the section `Configuring Prefix and Suffix Rules <configuring.html#configuring-prefix-and-suffix-rules>`_ for information on changing the allowed suffixes.

**Violation**

.. code-block:: vhdl

   block_label : block is

**Fix**

.. code-block:: vhdl

   block_label_blk : block is

block_601
#########

|phase_7| |disabled| |error|

This rule checks for valid prefixes on block labels.
The default prefix is *blk_*.

Refer to the section `Configuring Prefix and Suffix Rules <configuring.html#configuring-prefix-and-suffix-rules>`_ for information on changing the allowed prefixes.

**Violation**

.. code-block:: vhdl

   block_label : block is

**Fix**

.. code-block:: vhdl

   blk_block_label : block is

