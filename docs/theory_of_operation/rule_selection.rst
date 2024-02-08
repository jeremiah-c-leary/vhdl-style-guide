Rule Selection
--------------

This section will detail the guidelines followed for creating and organizing rules.

.. jcl - fill this section out with some more text

.. NOTE:: VSG can not fully classify a VHDL file, this will place limitations on the ability to write rules.

Goals
=====

The VHDL Language Reference Manual (LRM) will be the basis used when determining rule creation, naming and the organization of rules.


Guidelines
==========

* [naming_001] Rule naming shall be of the form :code:`{identifier}_{number}`
* [naming_002] The identifier shall be the *left-hand side* of VHDL production.
* [naming_003] The number shall be three digits
* [naming_004] The rule number shall indicate which phase the rule is executed

* [scoping_001] Rules shall be scoped to a VHDL production

Example
=======

The following production shows the structure of an architecture.

.. code-block:: text

   architecture_body ::=
       *architecture* identifier *of* entity_name *is*
           architecture_declarative_part
       *begin*
           architecture_statement_part
       *end* [ *architecture* ] [ architecture_simple_name ] ;

The VHDL keywords are enclosed with asterisks, **architecture**, **of**, **is**, **begin** and **end**.
Everything else is another production:

.. code-block:: text

   identifier ::=
       basic_identifier | extended_identifier

   name ::=
       simple_name
     | operator_symbol
     | character_literal
     | selected_name
     | indexed_name
     | slice_name
     | attribute_name
     | external_name

   architecture_declarative_part ::=
       { block_declarative_item }

   architecture_statement_part ::=
       { concurrent_statement }




Rules targetting the :code:`architecture_body` will only include those elements at that level of the production.

For example:

* architecture_body_100 = **architecture** on it's own line
* architecture_body_101 = identifier on same line as **architecture**
* architecture_body_102 = **of** on same line as identifier
* architecture_body_103 = entity_name on same line as **of** keyword
* architecture_body_104 = **is** on same line as entity_name


* architecture_body_105 = no code after **is** keyword
* architecture_body_106 = **begin** on it's own line
* architecture_body_107 = no code after **begin** keyword
* architecture_body_108 = **end** on it's own line
* architecture_body_109 = **architecture** on same line as **end**
* architecture_body_110 = architecture_simple_name on same line as **end**
* architecture_body_111 = semicolon on same line as **end**
* architecture_body_112 = no code after semicolon
* architecture_body_120 = add/remove optional keyword **architecture**
* architecture_body_121 = add/remove optional architecture_simple_name

* architecture_body_200 = whitespace between **architecture** and identifier
* architecture_body_201 = whitespace between identifier and **of** keyword
* architecture_body_202 = whitespace between **of** and entity_name
* architecture_body_203 = whitespace between entity_name and **is** keyword
* architecture_body_204 = whitespace between **end** and **architecture** keyword
* architecture_body_205 = whitespace between **architecture** and architecture_simple_name
* architecture_body_206 = whitespace between architecture_simple_name and semicolon

* architecture_body_400 = indent of **architecture** keyword
* architecture_body_401 = indent of **begin** keyword
* architecture_body_402 = indent of **end** keyword

* architecture_body_600 = case of **architecture** keyword
* architecture_body_601 = case of identifier
* architecture_body_602 = case of **of** keyword
* architecture_body_603 = case of entity_name
* architecture_body_604 = case of **is** keyword
* architecture_body_605 = case of **begin** keyword
* architecture_body_606 = case of **end** keyword
* architecture_body_607 = case of ending **architecture** keyword
* architecture_body_608 = case of architecture_simple_name

* architecture_body_700 = naming restrictions on identifier and architecture_simple_name

The one exception is the identifier production.
The entity_name is a reference to the identifier in the entity_declaration production and therefore no rule will be written against it at the architecture_body level.

One question to answer are blank lines.
Are they part of architecture_body or the next production?

Expanding the architecture_declarative_part production we get:

.. code-block:: text

   block_declarative_item ::=
       subprogram_declaration
     | subprogram_body
     | subprogram_instantiation_declaration
     | package_declaration
     | package_body
     | package_instantiation_declaration
     | type_declaration
     | subtype_declaration
     | constant_declaration
     | signal_declaration
     | shared_variable_declaration
     | file_declaration
     | alias_declaration
     | component_declaration
     | attribute_declaration
     | attribute_specification
     | configuration_specification
     | disconnection_specification
     | use_clause
     | group_template_declaration
     | group_declaration
     | PSL_Property_Declaration
     | PSL_Sequence_Declaration
     | PSL_Clock_Declaration

Vertical spacing between these elements will be performed by rules in the block_declarative_part group.
This will eliminate the issue where multiple blank line rules could collide.

* block_declarative_part_300 = blank line at beginning of block_declarative part
* block_declarative_part_301 = blank line at end of block_declarative part
* block_declarative_part_302 = blank line before block_declarative_item (could be configurable) (could also conflict with block_declarative_item_001)
* etc...

The block_declarative_part can into from 0 to N block_declarative_items.
Alignment rules between block_declarative_items, e.g. colon alignment in signal_declaration and constant_declaration, will also be performed at this level.

* block_declarative_part_500 = align identifiers in file, constant and signal declarations
* block_declarative_part_501 = align : in constant and signal declarations
* etc...

Other structural rules could be created:

* block_declarative_part_100 = all constants defined at top of block_declarative_part (maybe this is out of scope of VSG though)

Taking the next step down to the signal_declaration level:

.. code-block:: text

   signal_declaration ::=
       signal identifier_list : subtype_indication [ signal_kind ] [ := expression ] ;

The following rules would be generated:

* signal_declaration_100 = **signal** keyword on it's own line
* signal_declaration_101 = identifier_list on same line as **signal** keyword
* signal_declaration_102 = colon on same line as identifier_list
* signal_declaration_103 = subtype_indication on same line as colon
* signal_declaration_104 = signal_kind on same line as subtype_indication
* signal_declaration_105 = := on same line as signal_kind
* signal_declaration_106 = expression on same line as :=
* signal_declaration_107 = semicolon on same line as expression
* signal_declaration_108 = no code after semicolon

* signal_declaration_200 = whitespace between signal keyword and identifier_list
* signal_declaration_200 = whitespace between identifier_list and colon
* signal_declaration_200 = whitespace between colon and subtype_indication
* signal_declaration_200 = whitespace between subtype_indication and signal_kind
* signal_declaration_200 = whitespace between signal_kind and :=
* signal_declaration_200 = whitespace between := and expression

* signal_declaration_400 = indent of signal keyword

* signal_declaration_600 = case of signal keyword
* signal_declaration_601 = case of idenfiers in identifier_list

* signal_declaration_700 = naming restrictions on signal identifiers

One could argue rule 601 should be moved to an identifier_list set of rules, but it seems appropriate at this level.

.. code-block:: text

   identifier_list ::=
       identifier { , identifier }

I would make the argument that signal_kind case would be done by a signal_kind rule.

.. code-block:: text

   signal_kind ::=
       register | bus

One could make the argument that subtype_indication should be handled by it's own set of rules:

.. code-block:: text

   subtype_indication ::=
       [ resolution_indication ] type_mark [ constraint ]

   resolution_indication ::=
       resolution_function_name | ( element_resolution )

   element_resolution ::= array_element_resolution | record_resolution

   type_mark ::=
       type_name | subtype_name

And the same for constraint:

.. code-block:: text

   constraint ::=
       range_constraint
     | array_constraint
     | record_constraint

If the subtype_indication and constraint rules were moved out of signal_declaration, and where ever else they are location, that it would reduce the number of rules.
VSG currently uses a base rule to handle constraints, which is extended where constraints are used.

