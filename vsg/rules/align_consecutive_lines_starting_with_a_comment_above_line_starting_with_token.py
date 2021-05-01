

from vsg import parser
from vsg import rule
from vsg import violation

from vsg.rules import utils as rules_utils


class align_consecutive_lines_starting_with_a_comment_above_line_starting_with_token(rule.Rule):
    '''
    Checks for a single space between two tokens.

    Parameters
    ----------

    name : string
       The group the rule belongs to.

    identifier : string
       unique identifier.  Usually in the form of 00N.

    token : token object
       reference token to align comments with
    '''

    def __init__(self, name, identifier, token, bIncrement=False):
        rule.Rule.__init__(self, name=name, identifier=identifier)
        self.solution = None
        self.phase = 4
        self.subphase = 2
        self.token = token
        self.bIncrement = bIncrement

    def analyze(self, oFile):
        self._print_debug_message('Analyzing rule: ' + self.unique_id)
        lToi = oFile.get_consecutive_lines_starting_with_token_and_stopping_when_token_starting_line_is_found(parser.comment, self.token)
        lUpdate = []
        for oToi in lToi:
            lTokens = oToi.get_tokens()
            iLine = oToi.get_line_number()

            iTargetIndent = lTokens[-1].get_indent()
            iWhitespaceLength = iTargetIndent * self.indentSize

            lUpdate = []

            for iIndex in range(0, len(lTokens)):
               oToken = lTokens[iIndex]

               if isinstance(oToken, self.token):
                   break

               if iIndex == 0:
                   if isinstance(lTokens[0], parser.whitespace):
                       if len(lTokens[0].get_value()) != iWhitespaceLength:
                           oLineTokens = oFile.get_tokens_from_line(iLine)
                           oViolation = violation.New(iLine, oLineTokens, self.solution)
                           dAction = {}
                           dAction['type'] = 'adjust'
                           dAction['adjust'] = iWhitespaceLength
                           oViolation.set_action(dAction)
                           self.add_violation(oViolation)
                       self._adjust_token_indent(lTokens[1], iTargetIndent)
                   else:
                       oLineTokens = oFile.get_tokens_from_line(iLine)
                       oViolation = violation.New(iLine, oLineTokens, self.solution)
                       dAction = {}
                       dAction['type'] = 'insert'
                       dAction['adjust'] = iWhitespaceLength
                       oViolation.set_action(dAction)
                       self.add_violation(oViolation)
                       self._adjust_token_indent(lTokens[0], iTargetIndent)

               if isinstance(oToken, parser.carriage_return):
                   iLine += 1
                   if isinstance(lTokens[iIndex + 1], parser.whitespace):
                       if len(lTokens[iIndex + 1].get_value()) != iWhitespaceLength:
                           oLineTokens = oFile.get_tokens_from_line(iLine)
                           oViolation = violation.New(iLine, oLineTokens, self.solution)
                           dAction = {}
                           dAction['type'] = 'adjust'
                           dAction['adjust'] = iWhitespaceLength
                           oViolation.set_action(dAction)
                           self.add_violation(oViolation)
                       self._adjust_token_indent(lTokens[iIndex + 2], iTargetIndent)
                   else:
                       oLineTokens = oFile.get_tokens_from_line(iLine)
                       oViolation = violation.New(iLine, oLineTokens, self.solution)
                       dAction = {}
                       dAction['type'] = 'insert'
                       dAction['adjust'] = iWhitespaceLength
                       oViolation.set_action(dAction)
                       self.add_violation(oViolation)
                       self._adjust_token_indent(lTokens[iIndex + 1], iTargetIndent)

            lUpdate.append(violation.New(0, oToi, ''))

        oFile.update(lUpdate)

    def _fix_violation(self, oViolation):
        lTokens = oViolation.get_tokens()
        dAction = oViolation.get_action()
        if dAction['type'] == 'adjust':
            lTokens[0].set_value(' ' * dAction['adjust'])
        elif dAction['type'] == 'insert':
            rules_utils.insert_whitespace(lTokens, 0, dAction['adjust'])
        oViolation.set_tokens(lTokens)

    def _adjust_token_indent(self, oToken, iIndent):
        oToken.set_indent(iIndent)
