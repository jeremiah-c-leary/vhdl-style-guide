
from vsg import token

from vsg.rules import token_prefix

lTokens = []
lTokens.append(token.package_declaration.identifier)
lTokens.append(token.package_declaration.end_package_simple_name)


class rule_017(token_prefix):
    '''
    This rule checks for valid prefixes on package identifiers.
    The default package prefix is *pkg_*.

    |configuring_prefix_and_suffix_rules_link|

    **Violation**

    .. code-block:: vhdl

       package foo is

    **Fix**

    .. code-block:: vhdl

       package pkg_foo is
    '''

    def __init__(self):
        token_prefix.__init__(self, 'package', '017', lTokens)
        self.prefixes = ['pkg_']
        self.solution = 'Package identifier'
