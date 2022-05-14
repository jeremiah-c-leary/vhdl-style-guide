
from vsg import token

from vsg.rules.whitespace_between_token_pairs import Rule

lTokens = []
lTokens.append([token.package_body.package_keyword, token.package_body.body_keyword])
lTokens.append([token.package_body.body_keyword, token.package_body.package_simple_name])
lTokens.append([token.package_body.package_simple_name, token.package_body.is_keyword])


class rule_100(Rule):
    '''
    This rule checks for a single space between **package**, **body** and **is** keywords.

    |configuring_whitespace_rules_link|

    **Violation**

    .. code-block:: vhdl

       package    body  FIFO_PKG   is

    **Fix**

    .. code-block:: vhdl

       package body FIFO_PKG is
    '''
    def __init__(self):
        Rule.__init__(self, 'package_body', '100', lTokens)
