Code Tags
=========

VSG supports inline tags embedded into code to enable or disable rules.
This can be useful in fine tuning rule exceptions within a file.
The code tags are embedded in comments similar to pragmas, and must be on it's own line.

Full rule exclusion
-------------------

Entire portions of a file can be ignored using the **vsg_off** and **vsg_on** tags.

.. code-block:: vhdl

    -- vsg_off
    process (write, read, full) is
    begin
      a <= write;
      b <= read;
    end process;
    --vsg_on

The **vsg_off** tag disables all rule checking.
The **vsg_on** tag enables all rule checking, except those disabled by a configuration.

Individual Rule Exclusions
--------------------------

Individual rules can be disabled by adding the rule identifier to the **vsg_off** and **vsg_on** tags.
Multiple identifiers can be added.

.. code-block:: vhdl

   -- vsg_off process_016 process_018
   process (write, read, full) is
   begin
     a <= write;
     b <= read;
   end process;
   -- vsg_on

The bare **vsg_on** enables all rules not disabled by a configuration.

Each rule can be independently enabled or disabled:

.. code-block:: vhdl

   -- vsg_off process_016 process_018
   process (write, read, full) is
   begin
     a <= write;
     b <= read;
   end process;

   -- vsg_on process_016
   FIFO_PROC : process (write, read, full) is
   begin
     a <= write;
     b <= read;
   end process;

   -- vsg_on process_018
   FIFO_PROC : process (write, read, full) is
   begin
     a <= write;
     b <= read;
   end process FIFO_PROC;

In the previous example, the *process_016* and *process_018* are disabled for the first process.
*Process_018* is disabled for the second process.
No rules are disabled for the third process.
