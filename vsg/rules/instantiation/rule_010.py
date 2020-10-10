
from vsg.rules import align_tokens_in_region_between_tokens

from vsg import token

lAlign = []
lAlign.append(token.association_element.assignment)

oStart = token.component_instantiation_statement.label_colon
oEnd = token.component_instantiation_statement.semicolon


class rule_010(align_tokens_in_region_between_tokens):
    '''
    Ensures the alignment of the => operator for each generic and port in the instantiation.
    '''

    def __init__(self):
        align_tokens_in_region_between_tokens.__init__(self, 'instantiation', '010', lAlign, oStart, oEnd)
        self.solution = 'Inconsistent alignment of "=>" in generic or port assignments of instantiation.'
