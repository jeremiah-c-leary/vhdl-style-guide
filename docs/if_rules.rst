.. include:: includes.rst

If Rules
--------

if_001
######

|phase_4| |error| |indent|

This rule checks the indent of the **if** keyword.

**Violation**

.. code-block:: vhdl

    if (a = '1') then
    b <= '0'
  elsif (c = '1') then
    d <= '1';
  else
    e <= '0';
  end if;

**Fix**

.. code-block:: vhdl

  if (a = '1') then
    b <= '0'
  elsif (c = '1') then
    d <= '1';
  else
    e <= '0';
  end if;

if_002
######

|phase_1| |error| |structure|

This rule checks the boolean expression is enclosed in ().

.. NOTE:: There is a configuration option **parenthesis** which will either insert or remove the parenthesis.

parenthesis set to 'insert' (Default)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Violation**

.. code-block:: vhdl

  if a = '1' then

**Fix**

.. code-block:: vhdl

  if (a = '1') then

parenthesis set to 'remove'
^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Violation**

.. code-block:: vhdl

  if (a = '1') then

**Fix**

.. code-block:: vhdl

  if a = '1' then

if_003
######

|phase_2| |error| |whitespace|

This rule checks for a single space between the **if** keyword and the (.

**Violation**

.. code-block:: vhdl

  if(a = '1') then

  if   (a = '1') then

**Fix**

.. code-block:: vhdl

  if (a = '1') then

  if (a = '1') then

if_004
######

|phase_2| |error| |whitespace|

This rule checks for a single space between the ) and the **then** keyword.

**Violation**

.. code-block:: vhdl

  if (a = '1')then

  if (a = '1')    then

**Fix**

.. code-block:: vhdl

  if (a = '1') then

  if (a = '1') then

if_005
######

|phase_2| |error| |whitespace|

This rule checks for a single space between the **elsif** keyword and the (.

**Violation**

.. code-block:: vhdl

  elsif(c = '1') then

  elsif   (c = '1') then

**Fix**

.. code-block:: vhdl

  elsif (c = '1') then

  elsif (c = '1') then

if_006
######

|phase_3| |error| |blank_line|

This rule checks for blank lines after the **then** keyword.

**Violation**

.. code-block:: vhdl

  if (a = '1') then


    b <= '0'

**Fix**

.. code-block:: vhdl

  if (a = '1') then
    b <= '0'

if_007
######

|phase_3| |error| |blank_line|

This rule checks for blank lines before the **elsif** keyword.

**Violation**

.. code-block:: vhdl

    b <= '0'



  elsif (c = '1') then

**Fix**

.. code-block:: vhdl

    b <= '0'
  elsif (c = '1') then

if_008
######

|phase_3| |error| |blank_line|

This rule checks for blank lines before the **end if** keywords.

**Violation**

.. code-block:: vhdl

    e <= '0';


  end if;

**Fix**

.. code-block:: vhdl

    e <= '0';
  end if;

if_009
######

|phase_4| |error| |alignment|

This rule checks the alignment of multiline boolean expressions.

**Violation**

.. code-block:: vhdl

   if (a = '0' and b = '1' and
         c = '0') then

**Fix**

.. code-block:: vhdl

   if (a = '0' and b = '1' and
       c = '0') then

if_010
######

|phase_3| |error| |blank_line|

This rule checks for blank lines before the **else** keyword.

**Violation**

.. code-block:: vhdl

    d <= '1';


  else

**Fix**

.. code-block:: vhdl

    d <= '1';
  else

if_011
######

|phase_3| |error| |blank_line|

This rule checks for blank lines after the **else** keyword.

**Violation**

.. code-block:: vhdl

  else


    e <= '0';

**Fix**

.. code-block:: vhdl

  else
    e <= '0';

if_012
######

|phase_4| |error| |indent|

This rule checks the indent of the **elsif** keyword.

**Violation**

.. code-block:: vhdl

  if (a = '1') then
    b <= '0'
    elsif (c = '1') then
    d <= '1';
  else
    e <= '0';
  end if;

**Fix**

.. code-block:: vhdl

  if (a = '1') then
    b <= '0'
  elsif (c = '1') then
    d <= '1';
  else
    e <= '0';
  end if;

if_013
######

|phase_4| |error| |indent|

This rule checks the indent of the **else** keyword.

**Violation**

.. code-block:: vhdl

  if (a = '1') then
    b <= '0'
  elsif (c = '1') then
    d <= '1';
    else
    e <= '0';
  end if;

**Fix**

.. code-block:: vhdl

  if (a = '1') then
    b <= '0'
  elsif (c = '1') then
    d <= '1';
  else
    e <= '0';
  end if;

if_014
######

|phase_4| |error| |indent|

This rule checks the indent of the **end if** keyword.

**Violation**

.. code-block:: vhdl

  if (a = '1') then
    b <= '0'
  elsif (c = '1') then
    d <= '1';
  else
    e <= '0';
    end if;

**Fix**

.. code-block:: vhdl

  if (a = '1') then
    b <= '0'
  elsif (c = '1') then
    d <= '1';
  else
    e <= '0';
  end if;

if_015
######

|phase_2| |error| |whitespace|

This rule checks for a single space between the **end if** keywords.

**Violation**

.. code-block:: vhdl

   end    if;

**Fix**

.. code-block:: vhdl

   end if;

if_020
######

|phase_1| |error| |structure|

This rule checks the **end if** keyword is on it's own line.

**Violation**

.. code-block:: vhdl

   if (a = '1') then c <= '1'; else c <= '0'; end if;

**Fix**

.. code-block:: vhdl

   if (a = '1') then c <= '1'; else c <= '0';
   end if;

if_021
######

|phase_1| |error| |structure|

This rule checks the **else** keyword is on it's own line.

**Violation**

.. code-block:: vhdl

   if (a = '1') then c <= '1'; else c <= '0'; end if;

**Fix**

.. code-block:: vhdl

   if (a = '1') then c <= '0';
   else c <= '1'; end if;

if_022
######

|phase_1| |error| |structure|

This rule checks for code after the **else** keyword.

**Violation**

.. code-block:: vhdl

   if (a = '1') then c <= '1'; else c <= '0'; end if;

**Fix**

.. code-block:: vhdl

   if (a = '1') then c <= '1'; else
     c <= '0'; end if;

if_023
######

|phase_1| |error| |structure|

This rule checks the **elsif** keyword is on it's own line.

**Violation**

.. code-block:: vhdl

   if (a = '1') then c <= '1'; else c <= '0'; elsif (b = '0') then d <= '0'; end if;

**Fix**

.. code-block:: vhdl

   if (a = '1') then c <= '1'; else c <= '0';
   elsif (b = '0') then d <= '0'; end if;

if_024
######

|phase_1| |error| |structure|

This rule checks for code after the **then** keyword.

**Violation**

.. code-block:: vhdl

   if (a = '1') then c <= '1';

**Fix**

.. code-block:: vhdl

   if (a = '1') then
     c <= '1';

if_025
######

|phase_6| |error| |case| |case_keyword|

This rule checks the **if** keyword has proper case.

|configuring_uppercase_and_lowercase_rules_link|

**Violation**

.. code-block:: vhdl

   IF (a = '1') then

**Fix**

.. code-block:: vhdl

   if (a = '1') then

if_026
######

|phase_6| |error| |case| |case_keyword|

This rule checks the **elsif** keyword has proper case.

|configuring_uppercase_and_lowercase_rules_link|

**Violation**

.. code-block:: vhdl

   ELSIF (a = '1') then

**Fix**

.. code-block:: vhdl

   elsif (a = '1') then

if_027
######

|phase_6| |error| |case| |case_keyword|

This rule checks the **else** keyword has proper case.

|configuring_uppercase_and_lowercase_rules_link|

**Violation**

.. code-block:: vhdl

   ELSE

**Fix**

.. code-block:: vhdl

   else

if_028
######

|phase_6| |error| |case| |case_keyword|

This rule checks the **end** keyword has proper case.

|configuring_uppercase_and_lowercase_rules_link|

**Violation**

.. code-block:: vhdl

   END if;

   End if;

**Fix**

.. code-block:: vhdl

   end if;

   end if;

if_029
######

|phase_6| |error| |case| |case_keyword|

This rule checks the **then** keyword has proper case.

|configuring_uppercase_and_lowercase_rules_link|

**Violation**

.. code-block:: vhdl

   if (a = '1') THEN

**Fix**

.. code-block:: vhdl

   if (a = '1') then

if_030
######

|phase_3| |error| |blank_line|

This rule checks a single blank line after the **end if**.
In the case of nested **if** statements, the rule will be enfoced on the last **end if**.

|configuring_blank_lines_link|

**Violation**

.. code-block:: vhdl

   if (A = '1') then
     B <= '0';
   end if;
   C <= '1';

**Fix**

.. code-block:: vhdl

   if (A = '1') then
     B <= '0';
   end if;

   C <= '1';

if_031
######

|phase_3| |error| |blank_line|

This rule checks for blank lines or comments above the **if** keyword.
In the case of nested **if** statements, the rule will be enfoced on the first **if**.

|configuring_previous_line_rules_link|

The default style is :code:`no_code`.

**Violation**

.. code-block:: vhdl

   C <= '1';
   if (A = '1') then
     B <= '0';
   end if;

   -- This is a comment
   if (A = '1') then
     B <= '0';
   end if;

**Fix**

.. code-block:: vhdl

   C <= '1';

   if (A = '1') then
     B <= '0';
   end if;

   -- This is a comment
   if (A = '1') then
     B <= '0';
   end if;

if_032
######

|phase_4| |error| |alignment|

This rule aligns consecutive comment only lines above the **elsif** keyword in if statements.
These comments are used to describe what the elsif code is going to do.

**Violation**

.. code-block:: vhdl

       -- comment 1
 -- comment 2
    -- comment 3
   elsif (a = '1')
     rd_en <= '0';

**Fix**

.. code-block:: vhdl

   -- comment 1
   -- comment 2
   -- comment 3
   elsif (a = '1')
     rd_en <= '0';

if_033
######

|phase_4| |error| |alignment|

This rule aligns consecutive comment only lines above the **else** keyword in if statements.
These comments are used to describe what the elsif code is going to do.

**Violation**

.. code-block:: vhdl

       -- comment 1
 -- comment 2
    -- comment 3
   else
     rd_en <= '0';

**Fix**

.. code-block:: vhdl

   -- comment 1
   -- comment 2
   -- comment 3
   else
     rd_en <= '0';

if_034
######

|phase_6| |error| |case| |case_keyword|

This rule checks the **if** keyword in the **end if** has proper case.

|configuring_uppercase_and_lowercase_rules_link|

**Violation**

.. code-block:: vhdl

   end If;

   end IF;

**Fix**

.. code-block:: vhdl

   end if;

   end if;

if_035
######

|phase_1| |error| |structure|

This rule checks the expression after the **if** or **elsif** keyword starts on the same line.

**Violation**

.. code-block:: vhdl

   if
     a = '1' then

   elsif
     b = '1' then

**Fix**

.. code-block:: vhdl

   if a = '1' then

   elsif b = '1' then

if_036
######

|phase_1| |error| |structure|

This rule checks the **then** keyword is not on a line by itself.

**Violation**

.. code-block:: vhdl

   if a = '1'
     then

**Fix**

.. code-block:: vhdl

   if a = '1' then

