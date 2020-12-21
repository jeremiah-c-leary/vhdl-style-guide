
from vsg.rules import align_tokens_in_region_between_tokens

from vsg import token

lAlign = []
lAlign.append(token.element_declaration.colon)

oStartToken = token.record_type_definition.record_keyword

oEndToken = token.record_type_definition.end_keyword


class rule_400(align_tokens_in_region_between_tokens):
    '''
    Aligns colons for elements of a record.
    '''

    def __init__(self):
        align_tokens_in_region_between_tokens.__init__(self, 'type', '400', lAlign, oStartToken, oEndToken)
