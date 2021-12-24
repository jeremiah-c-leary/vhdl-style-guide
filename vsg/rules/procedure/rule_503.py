
from vsg.rules import token_case

from vsg import token

lTokens = []
lTokens.append(token.subprogram_body.begin_keyword)


class rule_503(token_case):
    '''
    This rule checks the **begin** keyword has proper case.
    
    Refer to the section `Configuring Uppercase and Lowercase Rules <configuring.html#configuring-uppercase-and-lowercase-rules>`_ for information on changing the default case.
    
    **Violation**
    
    .. code-block:: vhdl
    
       procedure average_samples is
       BEGIN
    
    **Fix**
    
    .. code-block:: vhdl
    
       procedure average_samples is
       begin
    '''

    def __init__(self):
        token_case.__init__(self, 'procedure', '503', lTokens)
        self.groups.append('case::keyword')
