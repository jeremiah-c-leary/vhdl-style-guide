
from vsg.rules import token_case_with_prefix_suffix

from vsg import token

lTokens = []
lTokens.append(token.entity_designator.entity_tag)


class rule_502(token_case_with_prefix_suffix):
    '''
    This rule checks the *entity_designator* has proper case.

    Refer to the section `Configuring Uppercase and Lowercase Rules <configuring.html#configuring-uppercase-and-lowercase-rules>`_ for information on changing the default case.

    **Violation**

    .. code-block:: vhdl

       attribute coordinate of COMP_1, COMP_2 : component is (0.0, 17.5);

    **Fix**

    .. code-block:: vhdl

       attribute coordinate of comp_1, comp_2 : component is (0.0, 17.5);
    '''

    def __init__(self):
        token_case_with_prefix_suffix.__init__(self, 'entity_specification', '502', lTokens)
        self.groups.append('case::name')
