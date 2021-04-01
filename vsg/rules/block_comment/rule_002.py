
import string

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

    def analyze(self, oFile):

        self._print_debug_message('Analyzing rule: ' + self.unique_id)
        lToi = self._get_tokens_of_interest(oFile)

        lUpdate = []

        for oToi in lToi:
            iLine, lTokens = utils.get_toi_parameters(oToi)

            iComments = utils.count_token_types_in_list_of_tokens(parser.comment, lTokens)

            iComment = 0
            for iToken, oToken in enumerate(lTokens):
                iLine = utils.increment_line_number(iLine, oToken)

                if isinstance(oToken, parser.comment):
                    iComment += 1
                    if iComment == 1:
                        if not is_header(oToken.get_value()):
                            break
                    elif iComment > 1 and iComment < iComments:
                        if not self.allow_indenting:
                            oToken.set_indent(0)

                        if self.comment_left is None:
                            continue

                        if isinstance(lTokens[iToken - 1], parser.whitespace):
                            if not self.allow_indenting:
                                break

                        sHeader = '--'
                        sHeader += self.comment_left
                        sComment = oToken.get_value()
                        if not sComment.startswith(sHeader):
                            sSolution = 'Comment must start with ' + sHeader
                            oViolation = violation.New(iLine, oToi, sSolution)
                            self.add_violation(oViolation)

            if not self.allow_indenting:
                lUpdate.append(violation.New(0, oToi, ''))

        if not self.allow_indenting:
            oFile.update(lUpdate)


def is_header(sComment):
    try:
        if sComment[2] not in string.punctuation:
            return False
        if sComment[2] == '!':
            return False
        if sComment[3] not in string.punctuation:
            return False
    except IndexError:
        return True
    return True
