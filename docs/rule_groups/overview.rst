Overview
========

Rule groups allow for easier configuration of rules that perform similar functions.
Using rule groups can make upgrading VSG versions easier as new rules are added.

The following is a list of the rule groups:

+-------------------------+---------------------------------------------------------+
| Group                   |   Description                                           |
+-------------------------+---------------------------------------------------------+
| alignment               | Horizontal alignment rules.                             |
+-------------------------+---------------------------------------------------------+
| blank_line              | Vertical alignment rules.                               |
+-------------------------+---------------------------------------------------------+
| case                    | All rules involving lower and upper casing.             |
+-------------------------+---------------------------------------------------------+
| case::keyword           | Casing rules for VHDL keywords.                         |
+-------------------------+---------------------------------------------------------+
| case::label             | Casing rules for labels.                                |
+-------------------------+---------------------------------------------------------+
| case::name              | Casing rules for identifiers, etc...                    |
+-------------------------+---------------------------------------------------------+
| length                  | Rules restricting length.                               |
+-------------------------+---------------------------------------------------------+
| indent                  | Rules involving line indents.                           |
+-------------------------+---------------------------------------------------------+
| naming                  | Rules for constraining how identifiers etc.. are named. |
+-------------------------+---------------------------------------------------------+
| structure               | Rules dictating the structure of the code.              |
+-------------------------+---------------------------------------------------------+
| structure::optional     | Rules for optional VHDL language items.                 |
+-------------------------+---------------------------------------------------------+
| whitespace              | Rules for managing whitespace.                          |
+-------------------------+---------------------------------------------------------+

Subgroups
---------

Groups with double colons (::) are considered subgroups.
This allows for finer control of group rules.

For example, the case of keywords, labels and names can be set independently.

Configuring Groups
------------------

Refer to the section `Configuring a Rule Group <../configuring_rule_groups.html>`_ for information on how to configure rule groups.

