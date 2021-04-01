
import string

from vsg import block_rule
from vsg import parser
from vsg import violation

from vsg.vhdlFile import utils


class rule_003(block_rule.Rule):
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
        block_rule.Rule.__init__(self, 'block_comment', '003')
        self.footer_left = None
        self.footer_left_repeat = '-'
        self.footer_string = None
        self.footer_right_repeat = None
        self.footer_alignment = 'center'
        self.max_footer_column = 120
        self.configuration.extend(['footer_left', 'footer_left_repeat', 'footer_string', 'footer_right_repeat', 'footer_alignment', 'max_footer_column'])

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
                    if iComment == iComments:

                        if not self.allow_indenting:
                            if isinstance(lTokens[iToken - 1], parser.whitespace):
                                break
                            else:
                                oToken.set_indent(0)

                        iWhitespace = self.indentSize * oToken.get_indent()

                        sFooter = '--'
                        if self.footer_left is not None:
                            sFooter += self.footer_left
                            iFooter_left = len(self.footer_left)
                        else:
                            iFooter_left = 0

                        if self.footer_string is None:
                            sFooter += self.footer_left_repeat * (self.max_footer_column - iWhitespace - len(sFooter))
                        elif self.footer_alignment == 'center':
                            iLength = int((self.max_footer_column - iWhitespace - len(self.footer_string)) / 2) - iFooter_left - 2
                            sFooter += self.footer_left_repeat * (iLength)
                            sFooter += self.footer_string
                            sFooter += self.footer_right_repeat * (self.max_footer_column - len(sFooter))
                        elif self.footer_alignment == 'left':
                            sFooter += self.footer_left_repeat
                            sFooter += self.footer_string
                            iLength = self.max_footer_column - iWhitespace - len(sFooter)
                            sFooter += self.footer_right_repeat * (self.max_footer_column - len(sFooter))
                        elif self.footer_alignment == 'right':
                            iLength = self.max_footer_column - iWhitespace - len(sFooter) - len(self.footer_string) - 1
                            sFooter += self.footer_left_repeat * (iLength)
                            sFooter += self.footer_string
                            sFooter += self.footer_right_repeat

                        sComment = oToken.get_value()
                        try:
                            if is_footer(sComment):
                                if not self.allow_indenting:
                                    oToken.set_indent(0)
                                if sComment != sFooter:
                                    sSolution = 'Change block comment footer to : ' + sFooter
                                    oViolation = violation.New(iLine, oToi, sSolution)
                                    self.add_violation(oViolation)
                                    break
                        except IndexError:
                            break

            if not self.allow_indenting:
                lUpdate.append(violation.New(0, oToi, ''))

        if not self.allow_indenting:
            oFile.update(lUpdate)


def is_footer(sComment):
    try:
        if sComment[2] not in string.punctuation:
            return False
        if sComment[2] == '!':
            return False
        if sComment[3] not in string.punctuation:
            return False
        return True
    except IndexError:
        return True
    return True
