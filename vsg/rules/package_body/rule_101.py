
from vsg import token

from vsg.rules.whitespace_between_token_pairs import Rule

lTokens = []
lTokens.append([token.package_body.end_keyword, token.package_body.end_package_keyword])
lTokens.append([token.package_body.end_package_keyword, token.package_body.end_body_keyword])
lTokens.append([token.package_body.end_body_keyword, token.package_body.end_package_simple_name])


class rule_101(Rule):
    '''
    This rule checks for a single space between the **end**, **package** and **body** keywords and package name.

    |configuring_whitespace_rules_link|

    **Violation**

    .. code-block:: vhdl

       end   package   body    FIFO_PKG;

    **Fix**

    .. code-block:: vhdl

       end package  body   FIFO_PKG;
    '''
    def __init__(self):
        Rule.__init__(self, 'package_body', '101', lTokens)
