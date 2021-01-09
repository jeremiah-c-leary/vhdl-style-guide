Pragmas
=======

VSG treats all pragmas as comments.
Most pragmas are ignored as they do not affect the style of the code.

However, the following pragmas do affect the parser:  --vhdl_comp_off and --vhdl_comp_on.
With these pragmas, it is possible to write code that would not follow the Language Reference Manual.

Take the following code as an example:

.. code-block:: vhdl

    --vhdl_comp_off
    entity FIFO is
    --vhdl_comp_on

    entity FIFO is
    end entity;

A parser which did not take the pragmas into account would fail because the code would look like this:

.. code-block:: vhdl

   entity FIFO is

   entity FIFO is
   end entity;

Which does not follow the LRM.

When VSG encounters the --vhdl_comp_off pragma, it will ignore anything after it until it encounters the --vhdl_comp_on pragma.
No formatting will be enforced between the pragmas.
