
from vsg.rules import align_tokens_in_region_between_tokens_unless_between_tokens

from vsg import token

lAlign = []
lAlign.append(token.full_type_declaration.identifier)
lAlign.append(token.incomplete_type_declaration.identifier)
lAlign.append(token.file_declaration.identifier)
lAlign.append(token.signal_declaration.identifier)
lAlign.append(token.constant_declaration.identifier)
lAlign.append(token.subtype_declaration.identifier)
lAlign.append(token.variable_declaration.identifier)

lUnless = []
lUnless.append([token.procedure_specification.procedure_keyword, token.subprogram_body.semicolon])


class rule_015(align_tokens_in_region_between_tokens_unless_between_tokens):
    '''
    Checks the alignment of declaration identifiers in the function declarative region.
    '''

    def __init__(self):
        align_tokens_in_region_between_tokens_unless_between_tokens.__init__(self, 'function', '015', lAlign, token.subprogram_body.is_keyword, token.subprogram_body.begin_keyword, lUnless)
        self.solution = 'Align identifer.'
