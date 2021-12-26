
from vsg.rules import token_case

from vsg import token

lTokens = []
lTokens.append(token.instantiated_unit.component_keyword)


class rule_031(token_case):
    '''
    This rule checks the component keyword has proper case in component instantiations that use the **component** keyword.

    Refer to the section `Configuring Uppercase and Lowercase Rules <configuring.html#configuring-uppercase-and-lowercase-rules>`_ for information on changing the default case.

    **Violation**

    .. code-block:: vhdl

       instance_name : COMPONENT entity_name

    **Fix**

    .. code-block:: vhdl

       instance_name : component entity_name
    '''

    def __init__(self):
        token_case.__init__(self, 'instantiation', '031', lTokens)
        self.groups.append('case::keyword')
