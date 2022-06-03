
from vsg import token

from vsg.rules.whitespace_between_token_pairs import Rule

lTokens = []
lTokens.append([token.package_declaration.package_keyword, token.package_declaration.identifier])
lTokens.append([token.package_declaration.identifier, token.package_declaration.is_keyword])


class rule_002(Rule):
    '''
    This rule checks for a single space between **package** and **is** keywords.

    |configuring_whitespace_rules_link|

    **Violation**

    .. code-block:: vhdl

       package   FIFO_PKG   is

    **Fix**

    .. code-block:: vhdl

       package FIFO_PKG is
    '''
    def __init__(self):
        Rule.__init__(self, 'package', '002', lTokens)
