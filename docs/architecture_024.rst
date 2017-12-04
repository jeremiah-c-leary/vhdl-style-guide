architecture_024
----------------

This rule checks for the architecture name in the *end architecture* statement.
It is clearer to the reader to state which architecture the end statement is closing.

Violation
~~~~~~~~~

   end architecture;

Fix
~~~

   end architecture ARCHITECTURE_NAME;

