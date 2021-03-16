
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
    Checks the label for a block is on the same line as the block keyword.
    '''

    def __init__(self):
        move_token_sequences_left_of_token.__init__(self, 'block', '001', lSequences, oLeftToken)
        self.solution = 'Ensure block label is on the same line as *block* keyword.'
