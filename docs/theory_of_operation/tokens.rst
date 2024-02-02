Tokens
------

Tokens are collection of classes used to represent elements of the VHDL language.
They are grouped together under the vsg/tokens directory.
Each file under vsg/tokens matches a VHDL production name.
Each class in each file maps to an element in the VHDL production.

For example, the following production for the architecture_body:

.. code-block:: text

   architecture_body ::=
       architecture identifier of *entity*_name is
           architecture_declarative_part
       begin
           architecture_statement_part
       end [ architecture ] [ *architecture*_simple_name ] ;

...has a file named vsg/tokens/architecture_body.py.

In the architecture_body.py file, there are the following classes:

* architecture_keyword
* identifier
* of_keyword
* entity_name
* is_keyword
* begin_keyword
* end_keyword
* end_architecture_keyword
* architecture_simple_name
* semicolon

The name of the class matches the item in the production with the following additional rules applied:

* All keywords have an _keyword suffix.
* All duplicately named keywords at the end of the production have an end\_ prefix.

All classes in a production are extensions of base classes in the parser module.

+--------------------------+--------------------+
| production class         | parser base class  |
+==========================+====================+
| architecture_keyword     | parser.keyword     |
+--------------------------+--------------------+
| identifier               | parser.identifier  |
+--------------------------+--------------------+
| of_keyword               | parser.keyword     |
+--------------------------+--------------------+
| entity_name              | parser.name        |
+--------------------------+--------------------+
| is_keyword               | parser.keyword     |
+--------------------------+--------------------+
| begin_keyword            | parser.keyword     |
+--------------------------+--------------------+
| end_keyword              | parser.keyword     |
+--------------------------+--------------------+
| end_architecture_keyword | parser.keyword     |
+--------------------------+--------------------+
| architecture_simple_name | parser.simple_name |
+--------------------------+--------------------+
| semicolon                | parser.semicolon   |
+--------------------------+--------------------+

Having a base class allows rules to be written against all types of a token, for example semicolons.
Extending base classes in the production allows for rules to be written against specific tokens in a production, for example architecture_body.semicolon.

