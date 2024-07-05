Tokens
------

Tokens are a collection of classes used to represent elements of the VHDL language.
They are grouped together under the :code:`vsg/tokens` directory.
Each file under :code:`vsg/tokens` matches a VHDL production name.
Each class in each file maps to an element in the VHDL production.

For example, the following production for the architecture_body:

.. code-block:: text

   architecture_body ::=
       architecture identifier of *entity*_name is
           architecture_declarative_part
       begin
           architecture_statement_part
       end [ architecture ] [ *architecture*_simple_name ] ;

has a file named vsg/tokens/architecture_body.py.

In the :code:`architecture_body.py` file, the following classes exist:

* :code:`architecture_keyword`
* :code:`identifier`
* :code:`of_keyword`
* :code:`entity_name`
* :code:`is_keyword`
* :code:`begin_keyword`
* :code:`end_keyword`
* :code:`end_architecture_keyword`
* :code:`architecture_simple_name`
* :code:`semicolon`

The name of the class matches an item in the production with the following additional rules applied:

* All keywords have an :code:`_keyword` suffix.
* All duplicately named keywords at the end of the production have an :code:`end\_` prefix.

All classes in a production are extensions of base classes in the :code:`parser` module.

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

Having a base class allows rules to be written against all types of a token, for example :code:`parser.semicolon`.
Extending base classes in the production allows for rules to be written against specific tokens in a production, for example :code:`architecture_body.semicolon`.
