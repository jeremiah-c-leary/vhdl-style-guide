
from vsg import parser
from vsg.token import process_statement as token

from vsg.rules import move_token_sequences_left_of_token

lSequences = []
lSequences.append([token.process_label, token.label_colon, token.process_keyword])
lSequences.append([token.process_label, token.label_colon, parser.whitespace, token.process_keyword])
lSequences.append([token.process_label, parser.whitespace, token.label_colon, token.process_keyword])
lSequences.append([token.process_label, parser.whitespace, token.label_colon, parser.whitespace, token.process_keyword])

oLeftToken = token.process_keyword


class rule_032(move_token_sequences_left_of_token):
    '''
    This rule checks the process label is on the same line as the process keyword.

    **Violation**

    .. code-block:: vhdl

       proc_1 :

       process(all) is

    **Fix**

    .. code-block:: vhdl

       proc_1 : process(all) is
    '''

    def __init__(self):
        move_token_sequences_left_of_token.__init__(self, 'process', '032', lSequences, oLeftToken)
        self.solution = 'Ensure process label is on the same line as *process* keyword.'
