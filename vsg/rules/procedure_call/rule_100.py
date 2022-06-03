
from vsg import token

from vsg.rules.whitespace_between_token_pairs import Rule

lTokens = []
lTokens.append([token.concurrent_procedure_call_statement.label_name, token.concurrent_procedure_call_statement.label_colon])
lTokens.append([token.concurrent_procedure_call_statement.label_colon, token.concurrent_procedure_call_statement.postponed_keyword])
lTokens.append([token.concurrent_procedure_call_statement.label_colon, token.procedure_call.procedure_name])
lTokens.append([token.concurrent_procedure_call_statement.postponed_keyword, token.procedure_call.procedure_name])

lTokens.append([token.procedure_call_statement.label, token.procedure_call_statement.label_colon])
lTokens.append([token.procedure_call_statement.label_colon, token.procedure_call.procedure_name])


class rule_100(Rule):
    '''
    This rule checks for a single space between the following block elements:  label, label colon, **postponed** keyword and the *procedure* name.

    **Violation**

    .. code-block:: vhdl

       procedure_label   :    postponed   WR_EN(parameter);

    **Fix**

    .. code-block:: vhdl

       procedure_label : postponed WR_EN(parameter);
    '''
    def __init__(self):
        Rule.__init__(self, 'procedure_call', '100', lTokens)
        self.solution = 'Ensure a single space between the label, colon, *postponed* keyword and procedure_name.'
