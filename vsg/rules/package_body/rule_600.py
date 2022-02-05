
from vsg import token

from vsg.rules import token_suffix

lTokens = []
lTokens.append(token.package_body.package_simple_name)
lTokens.append(token.package_body.end_package_simple_name)


class rule_600(token_suffix):
    '''
    This rule checks for valid suffixes on package body identifiers.
    The default package suffix is *_pkg*.

    |configuring_prefix_and_suffix_rules_link|

    **Violation**

    .. code-block:: vhdl

       package body foo is

    **Fix**

    .. code-block:: vhdl

       package body foo_pkg is
    '''

    def __init__(self):
        token_suffix.__init__(self, 'package_body', '600', lTokens)
        self.suffixes = ['_pkg']
