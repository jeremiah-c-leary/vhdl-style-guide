Configuring Suffix Rules
------------------------

There are several rules that enforce specific suffixes in different name identifiers and labels.
It is noted in the documentation, what the default suffixes for each such rule.

All suffix rules are disabled by default.
The default suffixes for each of these rules can be overridden using a configuration.

.. NOTE::  Some elements have both prefix and suffix rules.  Depending on the desired style, either or both can be enabled.

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


Rules enforcing suffixes
########################

* `block_600 <block_rules.html#block-600>`_
* `package_016 <package_rules.html#package-016>`_
* `package_body_600 <package_body_rules.html#package-body-600>`_
* `port_025 <port_rules.html#port-025>`_
