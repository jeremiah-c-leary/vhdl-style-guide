Code Tags
=========

VSG supports inline tags embedded into code to enable or disable rules.
This can be useful in fine tuning rule exceptions within a file.
The code tags are embedded in comments similar to pragmas, and must be on its own line.

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
    -- vsg_on

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

Next Line Rule Exclusions
-------------------------

Rules can be disabled for a single line using the **vsg_disable_next_line** tag.
Multiple identifiers can be added to a single tag..

.. code-block:: vhdl

   -- vsg_disable_next_line process_016
   process (write, read, full) is
   begin
     a <= write;
     b <= read;
     -- vsg_disable_next_line process_018
   end process;

In the above example, process_016 will only be disabled for the line with the **process** keyword.
Successive processes without labels will be flagged by process_016.

Sequential next line exclusions will also be honored:

.. code-block:: vhdl

   -- vsg_disable_next_line process_002
   -- vsg_disable_next_line process_016
   process(write, read, full) is
   begin
     a <= write;
     b <= read;
     -- vsg_disable_next_line process_018
   end process;

In the above example, both process_002 and process_016 will be disabled for the line starting with the **process** keyword.

Comments in code tags
---------------------

Code tags themselves are comments, however there is a method to allow commenting of the code tag on the same line.
The colon character, :, can be used to document why the code tag exists.

.. code-block:: vhdl

   -- vsg_off process_016 process_018 : VSG errors out on the following code
   process (write, read, full) is
   begin
     a <= write;
     b <= read;
   end process;
   -- vsg_on process_016 process_018 : Done with exclusion until VSG is fixed
