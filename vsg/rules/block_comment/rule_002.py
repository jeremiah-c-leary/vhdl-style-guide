
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

    def _analyze(self, lToi):

        for oToi in lToi:
            iLine, lTokens = utils.get_toi_parameters(oToi)

            iComments = utils.count_token_types_in_list_of_tokens(parser.comment, lTokens)

            iComment = 0
            for iToken, oToken in enumerate(lTokens):
                iLine = utils.increment_line_number(iLine, oToken)

                if isinstance(oToken, parser.comment):
                    iComment += 1
                    if first_comment_is_not_a_header(oToken, iComment):
                        break
                    elif middle_comment(iComment, iComments):
                        analyze_comment(self, oToken, oToi, iLine)


def first_comment_is_not_a_header(oToken, iComment):
    if iComment == 1:
        if not block_rule.is_header(oToken.get_value()):
            return True
    return False


def middle_comment(iComment, iComments):
    if iComment > 1 and iComment < iComments:
        return True
    return False


def analyze_comment(self, oToken, oToi, iLine):

    self.set_token_indent(oToken)

    if self.comment_left is None:
        return None

    sHeader = self.build_comment(oToken)
    sComment = oToken.get_value()
    if not sComment.startswith(sHeader):
        sSolution = 'Comment must start with ' + sHeader
        oViolation = violation.New(iLine, oToi, sSolution)
        self.add_violation(oViolation)
