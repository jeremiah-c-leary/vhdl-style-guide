Internal Data Structure
-----------------------

The underlying data structure after classifying is a single list of tokens.

Example
=======

Given the following code snippet:


.. code-block:: text

   architecture identifier of *entity*_name is
   begin
   end architecture *architecture*_simple_name;

The resulting data structure will be the following list:

.. code-block:: text

   tokens = [
       <class 'vsg.token.architecture_body.architecture_keyword'>,
       <class 'vsg.parser.whitespace'>,
       <class 'vsg.token.architecture_body.identifier'>,
       <class 'vsg.parser.whitespace'>,
       <class 'vsg.token.architecture_body.of_keyword'>,
       <class 'vsg.parser.whitespace'>,
       <class 'vsg.token.architecture_body.entity_name'>,
       <class 'vsg.parser.whitespace'>,
       <class 'vsg.token.architecture_body.is_keyword'>,
       <class 'vsg.parser.carriage_return'>,
       <class 'vsg.token.architecture_body.begin_keyword'>,
       <class 'vsg.parser.carriage_return'>,
       <class 'vsg.token.architecture_body.end_keyword'>,
       <class 'vsg.parser.whitespace'>,
       <class 'vsg.token.architecture_body.end_architecture_keyword'>,
       <class 'vsg.parser.whitespace'>,
       <class 'vsg.token.architecture_body.architecture_simple_name'>,
       <class 'vsg.token.architecture_body.semicolon'>
   ]

The elements in this data structure will be interrogated and modified by rules.
