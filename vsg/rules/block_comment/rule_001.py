
import math
import string

from vsg import block_rule
from vsg import parser
from vsg import violation


class rule_001(block_rule.Rule):
    '''
    Checks the case for words.

    Parameters
    ----------

    name : string
       The group the rule belongs to.

    identifier : string
       unique identifier.  Usually in the form of 00N.

    trigger : parser object type
       object type to apply the case check against



    '''

    def __init__(self):
        block_rule.Rule.__init__(self, 'block_comment', '001')
        self.header_left = None
        self.header_left_repeat = '-'
        self.header_string = None
        self.header_right_repeat = None
        self.header_alignment = 'center'
        self.max_header_column = 120
        self.configuration.extend(['header_left', 'header_left_repeat', 'header_string', 'header_right_repeat', 'header_alignment', 'max_header_column'])

    def analyze(self, oFile):

        self._print_debug_message('Analyzing rule: ' + self.unique_id)
        lToi = self._get_tokens_of_interest(oFile)

        lUpdate = []

        for oToi in lToi:
            lTokens = oToi.get_tokens()

            if isinstance(lTokens[0], parser.comment):
                iWhitespace = self.indentSize * lTokens[0].get_indent()
            else:
                iWhitespace = self.indentSize * lTokens[1].get_indent()


            sHeader = '--'

            if self.header_left is not None:
                sHeader += self.header_left
                iHeader_left = len(self.header_left)
            else:
                iHeader_left = 0

            if self.header_string is None:
                sHeader += self.header_left_repeat * (self.max_header_column - iWhitespace - len(sHeader))
            elif self.header_alignment == 'center':
                iLeft = math.floor((self.max_header_column - iWhitespace - len(self.header_string)) / 2) - iHeader_left - 2
                sLeft = self.header_left_repeat * iLeft
                iRight = self.max_header_column - iWhitespace - 2 - iHeader_left - len(self.header_string) - iLeft
                sRight = self.header_right_repeat * iRight
#                print(f'({self.max_header_column} - {iWhitespace} - {len(self.header_string)}) / 2  - {iHeader_left} = {iLeft}')
                sHeader += sLeft + self.header_string + sRight
            elif self.header_alignment == 'left':
                sHeader += self.header_left_repeat
                sHeader += self.header_string
                iLength = self.max_header_column - iWhitespace - len(sHeader)
                sHeader += self.header_right_repeat * iLength
            elif self.header_alignment == 'right':
                iLength = self.max_header_column - iWhitespace - len(sHeader) - len(self.header_string) - 1
                sHeader += self.header_left_repeat * iLength
                sHeader += self.header_string
                sHeader += self.header_right_repeat

            for oToken in lTokens:
                if isinstance(oToken, parser.comment):
                    sComment = oToken.get_value()
                    try:
                        if is_header(sComment):
                            if not self.allow_indenting:
                                oToken.set_indent(0)
                            if sComment != sHeader:
                                sSolution = 'Change block comment header to : ' + sHeader
                                oViolation = violation.New(oToi.get_line_number(), oToi, sSolution)
                                self.add_violation(oViolation)
                        break
                    except IndexError:
                        break
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

#         1         2         3         4         5         6         7         8
#-------------------------------<-    80 chars    ->-----------------------------
#------------------------------<-    80 chars    ->------------------------------
