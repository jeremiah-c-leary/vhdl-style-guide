
from vsg import parser
from vsg import violation

from vsg.rule_group import blank_line
from vsg.vhdlFile import utils


class rule_012(blank_line.Rule):
    '''
    This rule enforces a maximum number of consecutive blank lines.

    **Violation**

    .. code-block:: vhdl

      a <= b;


      c <= d;

    **Fix**

    .. code-block:: vhdl

      a <= b;

      c <= d;

    .. NOTE::

      The default is set to 1.
      This can be changed by setting the *numBlankLines* attribute to another number.

      .. code-block:: json

         {
             "rule":{
                 "whitespace_012":{
                     "numBlankLines":3
                 }
             }
         }
    '''

    def __init__(self):
        blank_line.Rule.__init__(self, 'whitespace', '012')
        self.solution = None
        self.phase = 3
        self.subphase = 3
        self.numBlankLines = 1
        self.configuration.append('numBlankLines')

    def _get_tokens_of_interest(self, oFile):
        return [oFile.get_all_tokens()]

    def _analyze(self, lToi):
        oToi = lToi[0]
        iLine, lTokens = utils.get_toi_parameters(oToi)
        iCount = 0
        for iToken, oToken in enumerate(lTokens[:len(lTokens) - 1]):
            iLine = utils.increment_line_number(iLine, oToken)

            if isinstance(oToken, parser.blank_line):
                if iCount == 0:
                    iLineNumber = iLine
                    iStartToken = iToken
                iCount += 1

            if isinstance(oToken, parser.carriage_return):
                if not isinstance(lTokens[iToken + 1], parser.blank_line):
                    if iCount > self.numBlankLines:
                        sSolution = 'Remove ' + str(iCount - self.numBlankLines) + ' blank line(s) below'
                        lExtractedTokens = oToi.extract_tokens(iStartToken, iToken)
                        oViolation = violation.New(iLineNumber, lExtractedTokens, sSolution)
                        dAction = {}
                        dAction['remove'] = iCount - self.numBlankLines
                        oViolation.set_action(dAction)
                        self.add_violation(oViolation)

                    iCount = 0

    def _fix_violation(self, oViolation):
        lTokens = oViolation.get_tokens()
        dAction = oViolation.get_action()
        lTokens = lTokens[2*dAction['remove']:]
        oViolation.set_tokens(lTokens)
