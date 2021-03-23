Configuring Prefix and Suffix Rules
-----------------------------------

There are several rules that enforce specific prefixes/suffixes in different name identifiers.
It is noted, in the documentation, what are the default prefixes/suffixes for each such rule.

All prefix/suffix rules are disabled by default.
The default prefixes/suffixes for each of these rules can be overridden using a configuration.

Overriding Default Prefixes/Suffixes Enforcement
################################################

The default setting can be changed using a configuration.
For example, the rule port_025 defaults to following suffixes: ['_I', '_O', '_IO'].
We can use the following configuration to change allowed suffixes:

.. code-block:: yaml

   ---

    rule :
        port_025:
            # Each prefix/suffix rule needs to be enabled explicitly.
            disable: false
            suffixes: ['_i', '_o']

The rule variable_012 defaults to following prefix: ['v\_'].
We can use the following configuration to change allowed prefix:

.. code-block:: yaml

   ---

    rule :
        variable_012:
            # Each prefix/suffix rule needs to be enabled explicitly.
            disable: false
            prefixes: ['var_']

Rules enforcing prefixes and suffixes
#####################################

* `block_600 <block_rules.html#block-600>`_
* `block_601 <block_rules.html#block-601>`_
* `constant_015 <constant_rules.html#constant-015>`_
* `generate_017 <generate_rules.html#generate-017>`_
* `generic_020 <generic_rules.html#generic-020>`_
* `package_016 <package_rules.html#package-016>`_
* `package_017 <package_rules.html#package-017>`_
* `package_body_600 <package_body_rules.html#package-body-600>`_
* `package_body_601 <package_body_rules.html#package-body-601>`_
* `port_011 <port_rules.html#port-011>`_
* `port_025 <port_rules.html#port-025>`_
* `process_036 <process_rules.html#process-036>`_
* `signal_008 <signal_rules.html#signal-008>`_
* `subtype_004 <subtype_rules.html#subtype-004>`_
* `type_definition_015 <type_rules.html#type-015>`_
* `variable_012 <variable_rules.html#variable-012>`_
