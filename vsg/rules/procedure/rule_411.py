
from vsg.rules import align_tokens_in_region_between_tokens

from vsg import token

lAlign = []
lAlign.append(token.interface_signal_declaration.assignment)
lAlign.append(token.interface_constant_declaration.assignment)
lAlign.append(token.interface_variable_declaration.assignment)


class rule_411(align_tokens_in_region_between_tokens):
    '''
    Component rule 411 ensures the alignment of the assignment for each parameter in the procedure declaration.
    '''

    def __init__(self):
        align_tokens_in_region_between_tokens.__init__(
            self, 'procedure', '411', lAlign,
            token.procedure_specification.open_parenthesis, token.procedure_specification.close_parenthesis)
        self.solution = 'Align :.'
