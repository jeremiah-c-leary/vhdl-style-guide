
from vsg import block_rule
from vsg import parser
from vsg import violation

from vsg.vhdlFile import utils


class rule_002(block_rule.Rule):
    '''
    This rule checks the **comment_left** attribute exists for all comments.

    |configuring_block_comments_link|

    **Violation**

    .. code-block:: vhdl

       --+-------------[ Header ]==============
       --   Comment
       --   Comment
       ----------------------------------------

    **Fix**

    .. code-block:: vhdl

       --+-------------[ Header ]==============
       --|  Comment
       --|  Comment
       ----------------------------------------
    '''

    def __init__(self):
        block_rule.Rule.__init__(self, 'block_comment', '002')
        self.comment_left = None
        self.configuration.append('comment_left')

    def analyze(self, oFile):

        self._print_debug_message('Analyzing rule: ' + self.unique_id)
        lToi = self._get_tokens_of_interest(oFile)

        for oToi in lToi:
            iLine, lTokens = utils.get_toi_parameters(oToi)

            iComments = utils.count_token_types_in_list_of_tokens(parser.comment, lTokens)

            iComment = 0
            for iToken, oToken in enumerate(lTokens):
                iLine = utils.increment_line_number(iLine, oToken)

                if isinstance(oToken, parser.comment):
                    iComment += 1
                    if iComment == 1:
                        if not block_rule.is_header(oToken.get_value()):
                            break
                    elif iComment > 1 and iComment < iComments:
                        if self.allow_indenting:
                            oToken.is_block_comment = False
                        else:
                            oToken.set_indent(0)
                            oToken.is_block_comment = True
                            oToken.block_comment_indent = 0

                        if self.comment_left is None:
                            continue

                        sHeader = '--'
                        sHeader += self.comment_left
                        sComment = oToken.get_value()
                        if not sComment.startswith(sHeader):
                            sSolution = 'Comment must start with ' + sHeader
                            oViolation = violation.New(iLine, oToi, sSolution)
                            self.add_violation(oViolation)
