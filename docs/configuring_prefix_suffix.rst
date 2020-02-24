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
