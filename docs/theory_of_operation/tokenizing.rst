Tokenizing
----------

The tokenizing process is responsible for taking the VHDL text file and grouping characters into tokens.
This process is performed on a line by line basis.
Each line is processed a single character at a time.
Characters are combined to form words based on several rules.

* keywords and identifiers
* multiple character sequences (<=, :=, etc...)
* whitespace
* comments

The result will be a list of lists.
The outer list is the entire file and each inner list is a line in the file.

For example, the following code...

.. code-block:: vhdl

   architecture rtl of fifo is
   begin
    a <= b;     -- Assign output
   end architecture rtl;

would be tokenized into this:

.. code-block:: python
   
   tokens = [
       ['architecture', ' ', 'rtl', ' ', 'of', ' ', 'fifo', ' ', 'is'],
       ['begin'],
       [' ', 'a', ' ', '<=', ' ', 'b', ';', '     ', '-- Assign output'],
       ['end', ' ', 'architecture', ' ', 'rtl', ';']
   ]

