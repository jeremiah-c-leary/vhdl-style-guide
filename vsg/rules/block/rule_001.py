
from vsg import parser
from vsg.token import block_statement as token

from vsg.rules import move_token_sequences_left_of_token

lSequences = []
lSequences.append([token.block_label, token.label_colon, token.block_keyword])
lSequences.append([token.block_label, token.label_colon, parser.whitespace, token.block_keyword])
lSequences.append([token.block_label, parser.whitespace, token.label_colon, token.block_keyword])
lSequences.append([token.block_label, parser.whitespace, token.label_colon, parser.whitespace, token.block_keyword])

oLeftToken = token.block_keyword


class rule_001(move_token_sequences_left_of_token):
    '''
    This rule checks the block label and the **block** keyword are on the same line.
    Keeping the label and generate on the same line reduces excessive indenting.

    **Violation**

    .. code-block:: vhdl

       block_label :
         block is

    **Fix**

    .. code-block:: vhdl

       block_label : block is
    '''

    def __init__(self):
        move_token_sequences_left_of_token.__init__(self, 'block', '001', lSequences, oLeftToken)
        self.solution = 'Ensure block label is on the same line as *block* keyword.'
