
from vsg.rules import token_case_in_range_bounded_by_tokens

from vsg import token

lTokens = []
lTokens.append(token.type_mark.name)

oStartToken = token.attribute_declaration.colon

oEndToken = token.attribute_declaration.semicolon


class rule_502(token_case_in_range_bounded_by_tokens):
    '''
    This rule checks the *type_mark* has proper case.
    
    Refer to the section `Configuring Uppercase and Lowercase Rules <configuring.html#configuring-uppercase-and-lowercase-rules>`_ for information on changing the default case.
    
    **Violation**
    
    .. code-block:: vhdl
    
       attribute max_delay : TIME;
    
    **Fix**
    
    .. code-block:: vhdl
    
       attribute max_delay : time;
    '''

    def __init__(self):
        token_case_in_range_bounded_by_tokens.__init__(self, 'attribute_declaration', '502', lTokens, oStartToken, oEndToken)
        self.groups.append('case::name')
