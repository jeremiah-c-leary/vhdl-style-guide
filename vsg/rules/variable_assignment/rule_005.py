
from vsg.rules import align_tokens_in_region_between_tokens_unless_between_tokens

from vsg import token

lAlign = []
lAlign.append(token.simple_variable_assignment.assignment)
lAlign.append(token.conditional_variable_assignment.assignment)
lAlign.append(token.selected_variable_assignment.assignment)

oStart = token.process_statement.begin_keyword
oEnd = token.process_statement.end_keyword

lUnless = []


class rule_005(align_tokens_in_region_between_tokens_unless_between_tokens):
    '''
    This rule checks the alignment of **:=** operators over multiple lines.
    
    Following extra configurations are supported:
    
    * :code:`if_control_statements_end_group`.
    * :code:`case_control_statements_end_group`,
    
    
    Refer to the section `Configuring Keyword Alignment Rules <configuring.html#configuring-keyword-alignment-rules>`_ for information on changing the configurations.
    
    **Violation**
    
    .. code-block:: vhdl
    
         counter := 0;
         count := counter + 1;
    
    **Fix**
    
    .. code-block:: vhdl
    
         counter := 0;
         count   := counter + 1;
    '''

    def __init__(self):
        align_tokens_in_region_between_tokens_unless_between_tokens.__init__(self, 'variable_assignment', '005', lAlign, oStart, oEnd, lUnless)
        self.solution = 'Align identifer.'
        self.if_control_statements_ends_group = True
        self.case_control_statements_ends_group = True
