
from vsg import token

from vsg.rules import single_space_between_token_pairs

lTokens = []
lTokens.append([token.package_declaration.package_keyword, token.package_declaration.identifier])
lTokens.append([token.package_declaration.identifier, token.package_declaration.is_keyword])


class rule_002(single_space_between_token_pairs):
    '''
    This rule checks for a single space between **package** and **is** keywords.

    **Violation**

    .. code-block:: vhdl

       package   FIFO_PKG   is

    **Fix**

    .. code-block:: vhdl

       package FIFO_PKG is
    '''
    def __init__(self):
        single_space_between_token_pairs.__init__(self, 'package', '002', lTokens)
        self.solution = 'Ensure a single space between the *package* keyword and identifier and *is* keyword.'
