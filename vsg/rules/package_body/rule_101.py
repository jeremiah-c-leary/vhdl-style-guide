
from vsg import token

from vsg.rules import single_space_between_token_pairs

lTokens = []
lTokens.append([token.package_body.end_keyword, token.package_body.end_package_keyword])
lTokens.append([token.package_body.end_package_keyword, token.package_body.end_body_keyword])
lTokens.append([token.package_body.end_body_keyword, token.package_body.end_package_simple_name])


class rule_101(single_space_between_token_pairs):
    '''
    This rule checks for a single space between the **end**, **package** and **body** keywords and package name.

    **Violation**

    .. code-block:: vhdl

       end   package   body    FIFO_PKG;

    **Fix**

    .. code-block:: vhdl

       end package  body   FIFO_PKG;
    '''
    def __init__(self):
        single_space_between_token_pairs.__init__(self, 'package_body', '101', lTokens)
        self.solution = 'Ensure a single space between the *package* keyword and *body* keyword and identifier and *is* keyword.'
