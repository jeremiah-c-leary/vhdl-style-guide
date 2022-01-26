
from vsg import token

from vsg.rules import single_space_between_token_pairs

lTokens = []
lTokens.append([token.package_body.package_keyword, token.package_body.body_keyword])
lTokens.append([token.package_body.body_keyword, token.package_body.package_simple_name])
lTokens.append([token.package_body.package_simple_name, token.package_body.is_keyword])


class rule_100(single_space_between_token_pairs):
    '''
    This rule checks for a single space between **package**, **body** and **is** keywords.

    **Violation**

    .. code-block:: vhdl

       package    body  FIFO_PKG   is

    **Fix**

    .. code-block:: vhdl

       package body FIFO_PKG is
    '''
    def __init__(self):
        single_space_between_token_pairs.__init__(self, 'package_body', '100', lTokens)
        self.solution = 'Ensure a single space between the *package* keyword and *body* keyword and identifier and *is* keyword.'
