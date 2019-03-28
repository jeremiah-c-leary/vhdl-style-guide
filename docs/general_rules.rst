General Rules
-------------

General rules are rules that do not fit nicely into existing rule categories.

general_001
###########

This rule checks for consistent capitalization of non VHDL reserved words.

**Violation**

.. code-block:: vhdl

   architecture RTL of ENTITY1 is

     signal sig1 : std_logic;
     signal sig2 : std_logic;

   begin

     PROC_NAME : process (siG2) is
     begin

       siG1 <= '0';

       if (SIG2 = '0') then
         sIg1 <= '1';
       elisif (SiG2 = '1') then
         SIg1 <= '0';
       end if;

     end process PROC_NAME;

   end architecture RTL;

**Fix**

.. code-block:: vhdl

   architecture RTL of ENTITY1 is

     signal sig1 : std_logic;
     signal sig2 : std_logic;

     PROC_NAME : process (sig2) is
     begin

       sig1 <= '0';

       if (sig2 = '0') then
         sig1 <= '1';
       elisif (sig2 = '1') then
         sig1 <= '0';
       end if;

     end process PROC_NAME;

   end architecture RTL;
