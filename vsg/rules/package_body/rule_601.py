
from vsg import token

from vsg.rules import token_prefix

lTokens = []
lTokens.append(token.package_body.package_simple_name)
lTokens.append(token.package_body.end_package_simple_name)


class rule_601(token_prefix):
    '''
    This rule checks for valid prefixes on package body identifiers.
    The default package prefix is *pkg_*.

    |configuring_prefix_and_suffix_rules_link|

    **Violation**

    .. code-block:: vhdl

       package body foo is

    **Fix**

    .. code-block:: vhdl

       package body pkg_foo is
    '''

    def __init__(self):
        token_prefix.__init__(self, 'package_body', '601', lTokens)
        self.prefixes = ['pkg_']
        self.solution = 'Package identifier'
