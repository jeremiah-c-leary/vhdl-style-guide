
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

    def _analyze(self, lToi):

        for oToi in lToi:
            lTokens = oToi.get_tokens()

            if isinstance(lTokens[0], parser.whitespace):
                iWhitespace = len(lTokens[0].get_value())
            else:
                iWhitespace = 0

            sHeader = '--'
            if self.header_left is not None:
                sHeader += self.header_left

            if self.header_string is None:
                sHeader += self.header_left_repeat * (self.max_header_column - iWhitespace - len(sHeader))
            elif self.header_alignment == 'center':
                iLength = int((self.max_header_column - iWhitespace - len(sHeader) - len(self.header_string)) / 2)
                sHeader += self.header_left_repeat * (iLength)
                sHeader += self.header_string
                sHeader += self.header_right_repeat * (self.max_header_column - len(sHeader))
            elif self.header_alignment == 'left':
                sHeader += self.header_left_repeat
                sHeader += self.header_string
                iLength = self.max_header_column - iWhitespace - len(sHeader)
                sHeader += self.header_right_repeat * (self.max_header_column - len(sHeader))
            elif self.header_alignment == 'right':
                iLength = self.max_header_column - iWhitespace - len(sHeader) - len(self.header_string) - 1
                sHeader += self.header_left_repeat * (iLength)
                sHeader += self.header_string
                sHeader += self.header_right_repeat

            for iToken, oToken in enumerate(lTokens):
                if isinstance(oToken, parser.comment):
                    sComment = oToken.get_value()
                    try:
                        if not sComment[2].isalnum():
                            if sComment != sHeader:
                                sSolution = 'Change block comment header to : ' + sHeader
                                oViolation = violation.New(oToi.get_line_number(), oToi, sSolution)
                                self.add_violation(oViolation)
                        break
                    except IndexError:
                        break
