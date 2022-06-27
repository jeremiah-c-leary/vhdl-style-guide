
from vsg import token

from vsg.rules.whitespace_between_token_pairs import Rule

lTokens = []
lTokens.append([token.package_declaration.end_keyword, token.package_declaration.end_package_keyword])
lTokens.append([token.package_declaration.end_package_keyword, token.package_declaration.end_package_simple_name])


class rule_009(Rule):
    '''
    This rule checks for a single space between the **end** and **package** keywords and package name.

    |configuring_whitespace_rules_link|

    **Violation**

    .. code-block:: vhdl

       end   package   FIFO_PKG;

    **Fix**

    .. code-block:: vhdl

       end package FIFO_PKG;
    '''
    def __init__(self):
        Rule.__init__(self, 'package', '009', lTokens)
