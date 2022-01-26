
from vsg.rules import token_case

from vsg import token

lTokens = []
lTokens.append(token.instantiated_unit.entity_keyword)


class rule_027(token_case):
    '''
    This rule checks the **entity** keyword has proper case in direct instantiations.

    Refer to the section `Configuring Uppercase and Lowercase Rules <configuring.html#configuring-uppercase-and-lowercase-rules>`_ for information on changing the default case.

    **Violation**

    .. code-block:: vhdl

       INSTANCE_NAME : ENTITY library.ENTITY_NAME

    **Fix**

    .. code-block:: vhdl

       INSTANCE_NAME : entity library.ENTITY_NAME
    '''

    def __init__(self):
        token_case.__init__(self, 'instantiation', '027', lTokens)
        self.groups.append('case::keyword')
