
from vsg import block_rule
from vsg import parser
from vsg import violation

from vsg.vhdlFile import utils


class rule_002(block_rule.Rule):
    '''
    Checks the case for words.

    Parameters
    ----------

    name : string
       The group the rule belongs to.

    identifier : string
       unique identifier.  Usually in the form of 00N.

    '''

    def __init__(self):
        block_rule.Rule.__init__(self, 'block_comment', '002')
        self.comment_left = None
        self.configuration.append('comment_left')

    def _analyze(self, lToi):
        if self.comment_left is None:
            return

        for oToi in lToi:
            iLine, lTokens = utils.get_toi_parameters(oToi)

            iComments = utils.count_token_types_in_list_of_tokens(parser.comment, lTokens)

            iComment = 0
            for iToken, oToken in enumerate(lTokens):
                iLine = utils.increment_line_number(iLine, oToken)
                
                if isinstance(oToken, parser.comment):
                    iComment += 1
                    if iComment > 1 and iComment < iComments:

                        if isinstance(lTokens[iToken - 1], parser.whitespace):
                            iWhitespace = len(lTokens[iToken - 1].get_value())
                        else:
                            iWhitespace = 0

                        sHeader = '--'
                        sHeader += self.comment_left
                        sComment = oToken.get_value()
                        if not sComment.startswith(sHeader):
                            sSolution = 'Comment must start with ' + sHeader
                            oViolation = violation.New(iLine, oToi, sSolution)
                            self.add_violation(oViolation)
