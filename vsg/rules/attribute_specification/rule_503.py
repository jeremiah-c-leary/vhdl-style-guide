
from vsg.rules import token_case

from vsg import token

lTokens = []
lTokens.append(token.attribute_specification.is_keyword)


class rule_503(token_case):
    '''
    This rule checks the **is** keyword has proper case.
    
    Refer to the section `Configuring Uppercase and Lowercase Rules <configuring.html#configuring-uppercase-and-lowercase-rules>`_ for information on changing the default case.
    
    **Violation**
    
    .. code-block:: vhdl
    
       attribute coordinate of comp_1 : component IS (0.0, 17.5);
    
    **Fix**
    
    .. code-block:: vhdl
    
       attribute coordinate of comp_1 : component is (0.0, 17.5);
    '''

    def __init__(self):
        token_case.__init__(self, 'attribute_specification', '503', lTokens)
        self.groups.append('case::keyword')
