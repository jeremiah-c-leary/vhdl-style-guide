
from vsg.rules import align_tokens_in_region_between_tokens_unless_between_tokens as Rule

from vsg import token

lAlign = []
lAlign.append(token.constant_declaration.assignment_operator)
lAlign.append(token.signal_declaration.assignment_operator)
lAlign.append(token.variable_declaration.assignment_operator)

lUnless = []
lUnless.append([token.subprogram_body.is_keyword,token.subprogram_body.begin_keyword])
lUnless.append([token.protected_type_body.body_keyword,token.protected_type_body.end_keyword])


class rule_400(Rule):
    '''
    '''

    def __init__(self):
        Rule.__init__(self, 'declarative_part', '400', lAlign, None, None, lUnless)
        self.solution = 'Align :='

    def _get_tokens_of_interest(self, oFile):
        return oFile.get_tokens_in_declarative_parts()
