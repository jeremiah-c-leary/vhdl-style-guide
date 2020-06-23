If Rules
--------

if_001
######

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

This rule checks the bolean expression is enclosed in ().

**Violation**

.. code-block:: vhdl

  if a = '1' then

**Fix**

.. code-block:: vhdl

  if (a = '1') then

if_003
######

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

This rule checks for empty lines after the **then** keyword.

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

This rule checks for empty lines before the **elsif** keyword.

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

This rule checks for empty lines before the **end if** keywords.

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

This rule checks for empty lines before the **else** keyword.

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

This rule checks for empty lines after the **else** keyword.

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

This rule checks for a single space between the **end if** keywords.

**Violation**

.. code-block:: vhdl

   end    if;

**Fix**

.. code-block:: vhdl

   end if;

if_020
######

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

This rule checks the **if** keyword has proper case.

Refer to the section `Configuring Uppercase and Lowercase Rules <configuring_case.html>`_ for information on changing the default case.

**Violation**

.. code-block:: vhdl

   IF (a = '1') then

**Fix**

.. code-block:: vhdl

   if (a = '1') then

if_026
######

This rule checks the **elsif** keyword has proper case.

Refer to the section `Configuring Uppercase and Lowercase Rules <configuring_case.html>`_ for information on changing the default case.

**Violation**

.. code-block:: vhdl

   ELSIF (a = '1') then

**Fix**

.. code-block:: vhdl

   elsif (a = '1') then

if_027
######

This rule checks the **else** keyword has proper case.

Refer to the section `Configuring Uppercase and Lowercase Rules <configuring_case.html>`_ for information on changing the default case.

**Violation**

.. code-block:: vhdl

   ELSE

**Fix**

.. code-block:: vhdl

   else

if_028
######

This rule checks the **end** keyword has proper case.

Refer to the section `Configuring Uppercase and Lowercase Rules <configuring_case.html>`_ for information on changing the default case.

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

This rule checks the **then** keyword has proper case.

Refer to the section `Configuring Uppercase and Lowercase Rules <configuring_case.html>`_ for information on changing the default case.

**Violation**

.. code-block:: vhdl

   if (a = '1') THEN

**Fix**

.. code-block:: vhdl

   if (a = '1') then

if_030
######

This rule checks for at least a single blank line after the **end if**.
In the case of nested **if** statements, the rule will be enfoced on the last **end if**.

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

This rule checks for at least a single blank line before the **if**, unless there is a comment.
In the case of nested **if** statements, the rule will be enfoced on the first **if**.

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

This rule checks the **if** keyword in the **end if** has proper case.

Refer to the section `Configuring Uppercase and Lowercase Rules <configuring_case.html>`_ for information on changing the default case.

**Violation**

.. code-block:: vhdl

   end If;

   end IF;

**Fix**

.. code-block:: vhdl

   end if;

   end if;
