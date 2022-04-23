
.. _configuring-prefix-and-suffix-rules:

Configuring Prefix and Suffix Rules
-----------------------------------

There are several rules that enforce specific prefixes or suffixes in different name identifiers.
It is noted in the documentation, what the default prefixes and suffixes are for each such rule.

All prefix and suffix rules are disabled by default.
The defaults for each of these rules can be overridden using a configuration.

.. NOTE::  Some elements have both prefix and suffix rules.  Depending on the desired style, either or both can be enabled.

Overriding Default Prefix Enforcement
#####################################

The default setting can be changed using a configuration.
The rule variable_012 defaults to following prefix: ['v\_'].
We can use the following configuration to change allowed prefix:

.. code-block:: yaml

   ---

    rule :
        variable_012:
            # Each prefix rule needs to be enabled explicitly.
            disable: false
            prefixes: ['var_']

Overriding Default Suffix Enforcement
#####################################

The default setting can be changed using a configuration.
For example, the rule port_025 defaults to following suffixes: ['_I', '_O', '_IO'].
We can use the following configuration to change allowed suffixes:

.. code-block:: yaml

   ---

    rule :
        port_025:
            # Each suffix rule needs to be enabled explicitly.
            disable: false
            suffixes: ['_i', '_o']

Rules Enforcing Prefixes and Suffixes
#####################################

+-------------------------+----------------------------------------------------------------+----------------------------------------------------------------+
| **Element**             | **Prefix Rule**                                                |  **Suffix Rule**                                               |
+-------------------------+----------------------------------------------------------------+----------------------------------------------------------------+
| Block Label             | `block_601 <block_rules.html#block-601>`_                      | `block_600 <block_rules.html#block-600>`_                      |
+-------------------------+----------------------------------------------------------------+----------------------------------------------------------------+
| Constant Identifier     | `constant_015 <constant_rules.html#constant-015>`_             | `constant_600 <constant_rules.html#constant-600>`_             |
+-------------------------+----------------------------------------------------------------+----------------------------------------------------------------+
| Generate Label          | `generate_017 <generate_rules.html#generate-017>`_             | `generate_600 <generate_rules.html#generate-600>`_             |
+-------------------------+----------------------------------------------------------------+----------------------------------------------------------------+
| Generic Identifier      | `generic_020 <generic_rules.html#generic-020>`_                | `generic_600 <generic_rules.html#generic-600>`_                |
+-------------------------+----------------------------------------------------------------+----------------------------------------------------------------+
| Generic Map Identifier  | `generic_map_601 <generic_map_rules.html#generic-map-601>`_    | `generic_map_600 <generic_map_rules.html#generic-map-600>`_    |
+-------------------------+----------------------------------------------------------------+----------------------------------------------------------------+
| Package Identifier      | `package_017 <package_rules.html#package-017>`_                | `package_016 <package_rules.html#package-016>`_                |
+-------------------------+----------------------------------------------------------------+----------------------------------------------------------------+
| Package Body Identifier | `package_body_601 <package_body_rules.html#package-body-601>`_ | `package_body_600 <package_body_rules.html#package-body-600>`_ |
+-------------------------+----------------------------------------------------------------+----------------------------------------------------------------+
| Port Identifier         | `port_011 <port_rules.html#port-011>`_                         | `port_025 <port_rules.html#port-025>`_                         |
+-------------------------+----------------------------------------------------------------+----------------------------------------------------------------+
| Process Label           | `process_036 <process_rules.html#process-036>`_                | `process_600 <process_rules.html#process-600>`_                |
+-------------------------+----------------------------------------------------------------+----------------------------------------------------------------+
| Signal Identifier       | `signal_008 <signal_rules.html#signal-008>`_                   | `signal_600 <signal_rules.html#signal-600>`_                   |
+-------------------------+----------------------------------------------------------------+----------------------------------------------------------------+
| Subtype Identifier      | `subtype_004 <subtype_rules.html#subtype-004>`_                | `subtype_600 <subtype_rules.html#subtype-600>`_                |
+-------------------------+----------------------------------------------------------------+----------------------------------------------------------------+
| Type Identifier         | `type_definition_015 <type_rules.html#type-015>`_              | `type_definition_600 <type_rules.html#type-600>`_              |
+-------------------------+----------------------------------------------------------------+----------------------------------------------------------------+
| Variable Identifier     | `variable_012 <variable_rules.html#variable-012>`_             | `variable_600 <variable_rules.html#variable-600>`_             |
+-------------------------+----------------------------------------------------------------+----------------------------------------------------------------+
