
from vsg.rules import token_case

from vsg import token

lTokens = []
lTokens.append(token.alias_declaration.alias_keyword)


class rule_500(token_case):
    '''
    This rule checks the **alias** keyword has proper case.

    Refer to the section `Configuring Uppercase and Lowercase Rules <configuring.html#configuring-uppercase-and-lowercase-rules>`_ for information on changing the default case.

    **Violation**

    .. code-block:: vhdl

       ALIAS alias_designator is name;

    **Fix**

    .. code-block:: vhdl

       alias alias_designator is name;
    '''

    def __init__(self):
        token_case.__init__(self, 'alias_declaration', '500', lTokens)
        self.groups.append('case::keyword')
