
from vsg.rules import align_tokens_in_region_between_tokens

from vsg import token

lAlign = []
lAlign.append(token.interface_signal_declaration.colon)
lAlign.append(token.interface_constant_declaration.colon)
lAlign.append(token.interface_variable_declaration.colon)


class rule_410(align_tokens_in_region_between_tokens):
    '''
    Component rule 410 ensures the alignment of the colon for each port in the procedure declaration.
    '''

    def __init__(self):
        align_tokens_in_region_between_tokens.__init__(
            self, 'procedure', '410', lAlign,
            token.procedure_specification.open_parenthesis, token.procedure_specification.close_parenthesis)
        self.solution = 'Align :.'
