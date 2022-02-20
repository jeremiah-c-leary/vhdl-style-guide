

from vsg import block_rule
from vsg import parser
from vsg import violation

from vsg.vhdlFile import utils


class rule_003(block_rule.Rule):
    '''
    This rule checks the block comment footer is correct.

    |configuring_block_comments_link|

    **Violation**

    .. code-block:: vhdl

       --+-------------[ Header ]==============
       --|  Comment
       --|  Comment
       ----------------------------------------

    **Fix**

    .. code-block:: vhdl

       --+-------------[ Header ]==============
       --|  Comment
       --|  Comment
       --+--------------------------[ Footer ]=
    '''

    def __init__(self):
        block_rule.Rule.__init__(self, 'block_comment', '003')
        self.footer_left = None
        self.footer_left_repeat = '-'
        self.footer_string = None
        self.footer_right_repeat = None
        self.footer_alignment = 'center'
        self.max_footer_column = 120
        self.configuration.extend(['footer_left', 'footer_left_repeat', 'footer_string', 'footer_right_repeat', 'footer_alignment', 'max_footer_column'])

    def analyze_comments(self, oToi):

        iLine, lTokens = utils.get_toi_parameters(oToi)
        iComments = utils.count_token_types_in_list_of_tokens(parser.comment, lTokens)

        iComment = 0
        for oToken in lTokens:
            iLine = utils.increment_line_number(iLine, oToken)
            iComment = utils.increment_comment_counter(iComment, oToken)

            if last_comment(iComment, iComments):
                analyze_footer(self, oToken, iLine, oToi)


def last_comment(iComment, iComments):
    if iComment == iComments:
        return True
    return False


def analyze_footer(self, oToken, iLine, oToi):
    sFooter = self.build_footer(oToken)
    sComment = oToken.get_value()

    if block_rule.is_footer(sComment):
        self.set_token_indent(oToken)
        if sComment != sFooter:
            sSolution = 'Change block comment footer to : ' + sFooter
            oViolation = violation.New(iLine, oToi, sSolution)
            self.add_violation(oViolation)
