
from vsg import rule
from vsg import parser
from vsg import token
from vsg import violation

from vsg.rules import utils as rules_utils

from vsg.vhdlFile import utils


lTokenPairs = []
lTokenPairs.append([token.constant_declaration.assignment_operator, token.constant_declaration.semicolon])


class rule_014(rule.Rule):
    '''
    Checks the indent of multiline constants that are not arrays.

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
        rule.Rule.__init__(self, 'constant', '014')
        self.solution = 'Align one space after assignment operator'
        self.phase = 5
        self.subphase = 4
        self.lTokenPairs = lTokenPairs
        self.bExcludeLastToken = False

    def analyze(self, oFile):
        lToi = []
        for lTokenPair in self.lTokenPairs:
            aToi = oFile.get_tokens_bounded_by(lTokenPair[0], lTokenPair[1], bExcludeLastToken=self.bExcludeLastToken)
            lToi = utils.combine_two_token_class_lists(lToi, aToi)

        for oToi in lToi:

            iLine, lTokens = utils.get_toi_parameters(oToi)

            if utils.are_next_consecutive_token_types_ignoring_whitespace([parser.open_parenthesis], 1, lTokens):
                continue

            iStartColumn = calculate_start_column(oFile, oToi)
            lColumn = []
            lColumn.append(iStartColumn)
            bCheckAlignment = False
            iFirstColumn = oFile.get_column_of_token_index(oToi.get_start_index())
            iColumn = iFirstColumn
            iPreviousColumn = 0
            iIndent = 0
#            print('-'*80)
            for iToken, oToken in enumerate(lTokens):

                iLine = utils.increment_line_number(iLine, oToken)

                if isinstance(oToken, parser.carriage_return):
                    bCheckAlignment = True
                    iPreviousColumn = lColumn[-1]
                    iColumn = 0
                    if isinstance(lTokens[iToken + 1], parser.whitespace):
                        iIndent = len(lTokens[iToken + 1].get_value())
                    else:
                        iIndent = 0
                    continue

                if isinstance(oToken, parser.blank_line):
                    bCheckAlignment = False
                    continue

                iColumn += len(oToken.get_value())

                if isinstance(oToken, parser.open_parenthesis):
                    lColumn.append(iColumn + iPreviousColumn - iIndent)

                if isinstance(oToken, parser.close_parenthesis):
                    lColumn.pop()

                if bCheckAlignment:
                    if isinstance(oToken, parser.whitespace):
                        if len(oToken.get_value()) != lColumn[-1]:
                            dAction = {}
                            dAction['line'] = iLine
                            dAction['column'] = lColumn[-1]
                            dAction['action'] = 'adjust'
                            dAction['indent'] = iIndent
                            dAction['previous'] = iPreviousColumn
                            oViolation = violation.New(iLine, oToi.extract_tokens(iToken, iToken), self.solution)
                            oViolation.set_action(dAction)
                            self.add_violation(oViolation)
#                            print(dAction)
                    else:
                        if lColumn != 0:
                            dAction = {}
                            if isinstance(oToken, parser.open_parenthesis):
                                dAction['column'] = lColumn[-2]
                            else:
                                dAction['column'] = lColumn[-1]
                            dAction['action'] = 'insert'
                            oViolation = violation.New(iLine, oToi.extract_tokens(iToken, iToken), self.solution)
                            oViolation.set_action(dAction)
                            self.add_violation(oViolation)
                    bCheckAlignment = False

    def _fix_violation(self, oViolation):
        lTokens = oViolation.get_tokens()
        dAction = oViolation.get_action()

        if dAction['action'] == 'adjust':
            lTokens[0].set_value(' '*dAction['column'])
        else:
            rules_utils.insert_whitespace(lTokens, 0, dAction['column'])

        oViolation.set_tokens(lTokens)


def calculate_start_column(oFile, oToi):
    iReturn = oFile.get_column_of_token_index(oToi.get_start_index())
    iReturn += len(oToi.get_tokens()[0].get_value())
    iReturn += 1
    return iReturn


