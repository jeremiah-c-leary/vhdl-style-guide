Helpful Tools
-------------

vsg_parser
==========

:code:`vsg_parser` is a tool which will show the mapping of tokens to a given file.
It is located in the bin directory and can be invoked with:

.. code-block:: bash

   $ bin/vsg_parser -f <filename>

This is the output when ran against the :code:`tests/architecture/rule_001_test_input.vhd` file:

.. code-block:: text

   --------------------------------------------------------------------------------
   0 |
   --------------------------------------------------------------------------------
   1 |
   <class 'vsg.parser.blank_line'>
   --------------------------------------------------------------------------------
   2 | architecture RTL of FIFO is begin end architecture RTL;
   <class 'vsg.token.architecture_body.architecture_keyword'>
   <class 'vsg.token.architecture_body.identifier'>
   <class 'vsg.token.architecture_body.of_keyword'>
   <class 'vsg.token.architecture_body.entity_name'>
   <class 'vsg.token.architecture_body.is_keyword'>
   <class 'vsg.token.architecture_body.begin_keyword'>
   <class 'vsg.token.architecture_body.end_keyword'>
   <class 'vsg.token.architecture_body.end_architecture_keyword'>
   <class 'vsg.token.architecture_body.architecture_simple_name'>
   <class 'vsg.token.architecture_body.semicolon'>
   --------------------------------------------------------------------------------
   3 |
   <class 'vsg.parser.blank_line'>
   --------------------------------------------------------------------------------
   4 | -- This should fail
   <class 'vsg.parser.comment'>
   --------------------------------------------------------------------------------
   5 |
   <class 'vsg.parser.blank_line'>
   --------------------------------------------------------------------------------
   6 |   architecture RTL of FIFO is
   <class 'vsg.token.architecture_body.architecture_keyword'>
   <class 'vsg.token.architecture_body.identifier'>
   <class 'vsg.token.architecture_body.of_keyword'>
   <class 'vsg.token.architecture_body.entity_name'>
   <class 'vsg.token.architecture_body.is_keyword'>
   --------------------------------------------------------------------------------
   7 |
   <class 'vsg.parser.blank_line'>
   --------------------------------------------------------------------------------
   8 | begin
   <class 'vsg.token.architecture_body.begin_keyword'>
   --------------------------------------------------------------------------------
   9 |
   <class 'vsg.parser.blank_line'>
   --------------------------------------------------------------------------------
   10 | end architecture RTL;
   <class 'vsg.token.architecture_body.end_keyword'>
   <class 'vsg.token.architecture_body.end_architecture_keyword'>
   <class 'vsg.token.architecture_body.architecture_simple_name'>
   <class 'vsg.token.architecture_body.semicolon'>

Each line is printed and then each token is listed in the order they appear on the line.
Whitespace tokens can be shown using the :code:`-w` option.

:code:`vsg_parser` can be useful in rule generation to determine how vsg is assigning token types.
