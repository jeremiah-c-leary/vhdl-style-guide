
from vsg import token

from vsg.rules import single_space_between_token_pairs

lTokens = []
lTokens.append([token.concurrent_procedure_call_statement.label_name, token.concurrent_procedure_call_statement.label_colon])
lTokens.append([token.concurrent_procedure_call_statement.label_colon, token.concurrent_procedure_call_statement.postponed_keyword])
lTokens.append([token.concurrent_procedure_call_statement.label_colon, token.procedure_call.procedure_name])
lTokens.append([token.concurrent_procedure_call_statement.postponed_keyword, token.procedure_call.procedure_name])

lTokens.append([token.procedure_call_statement.label, token.procedure_call_statement.label_colon])
lTokens.append([token.procedure_call_statement.label_colon, token.procedure_call.procedure_name])


class rule_100(single_space_between_token_pairs):
    '''
    Checks for a single spaces between keywords in the opening part of a procedure_call statement.
    '''
    def __init__(self):
        single_space_between_token_pairs.__init__(self, 'procedure_call', '100', lTokens)
        self.solution = 'Ensure a single space between the label, colon, *postponed* keyword and procedure_name.'
