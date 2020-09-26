

from vsg import parser
from vsg import rule_item
from vsg import violation

from vsg.vhdlFile import utils


class align_tokens_in_region_between_tokens_unless_between_tokens(rule_item.Rule):
    '''
    Checks for a single space between two tokens.

    Parameters
    ----------

    name : string
       The group the rule belongs to.

    identifier : string
       unique identifier.  Usually in the form of 00N.

    lTokens : token object list
       List of tokens to align

    left_token : token object
       The first token that defines the region

    right_token : token object
       The second token that defines the region

    lUnless : token object pairs list
       A list of pairs of tokens to in which to exclude alignment
    '''

    def __init__(self, name, identifier, lTokens, left_token, right_token, lUnless):
        rule_item.Rule.__init__(self, name=name, identifier=identifier)
        self.solution = None
        self.phase = 5
        self.lTokens = lTokens
        self.left_token = left_token
        self.right_token = right_token
        self.lUnless = lUnless
        ## attributes below are configurable by the user

        self.compact_alignment = True
        self.configuration.append('compact_alignment')

        self.blank_line_ends_group = True
        self.configuration.append('blank_line_ends_group')
        self.comment_line_ends_group = True
        self.configuration.append('comment_line_ends_group')


    def analyze(self, oFile):

        lIncludeLines = []
        if not self.blank_line_ends_group:
            lIncludeLines.append(parser.blank_line)
        if not self.comment_line_ends_group:
            lIncludeLines.append(parser.comment)

        dAnalysis = {}

        lToi = oFile.get_tokens_bounded_by(self.left_token, self.right_token)
        for oToi in lToi:
            lTokens = oToi.get_tokens()
            iLine = oToi.get_line_number()
            iColumn = 0
            bTokenFound = False
            iToken = -1
            bSkip = False
            oEndSkipToken = None

            for iIndex in range(0, len(lTokens)):
               iToken += 1
               oToken = lTokens[iIndex]

               bSkip, oEndSkipToken = check_for_exclusions(oToken, bSkip, oEndSkipToken, self.lUnless)

               if not bTokenFound and not bSkip:
                   for oSearch in self.lTokens:
                       if isinstance(oToken, oSearch):
                           bTokenFound = True
                           dAnalysis[iLine] = {}
                           dAnalysis[iLine]['token_column'] = iColumn
                           dAnalysis[iLine]['token_index'] = iToken
                           dAnalysis[iLine]['line_number'] = iLine
                           dAnalysis[iLine]['token_value'] = oToken.get_value()
                           if isinstance(lTokens[iIndex -1], parser.whitespace):
                               dAnalysis[iLine]['left_column'] = iColumn - len(lTokens[iIndex - 1].get_value())
                           else:
                               dAnalysis[iLine]['left_column'] = iColumn
                           break

                   iColumn += len(oToken.get_value())
               
               if isinstance(oToken, parser.carriage_return):
                   iLine += 1
                   iColumn = 0
                   bTokenFound = False
                   iToken = -1
                   if self.comment_line_ends_group:
                       if utils.are_next_consecutive_token_types([parser.whitespace, parser.comment], iIndex + 1, lTokens) or \
                          utils.are_next_consecutive_token_types([parser.comment], iIndex + 1, lTokens):
                           add_adjustments_to_dAnalysis(dAnalysis, self.compact_alignment)

                           for iKey in list(dAnalysis.keys()):
                               if dAnalysis[iKey]['adjust'] != 0:
                                   oLineTokens = oFile.get_tokens_from_line(iKey)
                                   sSolution = 'Move ' + dAnalysis[iKey]['token_value'] + ' ' + str(dAnalysis[iKey]['adjust']) + ' columns' 
                                   oViolation = violation.New(oLineTokens.get_line_number(), oLineTokens, sSolution)
                                   oViolation.set_action(dAnalysis[iKey])
                                   self.violations.append(oViolation)

                           dAnalysis = {}
                   if self.blank_line_ends_group:
                       if utils.are_next_consecutive_token_types([parser.blank_line], iIndex + 1, lTokens):
                           add_adjustments_to_dAnalysis(dAnalysis, self.compact_alignment)

                           for iKey in list(dAnalysis.keys()):
                               if dAnalysis[iKey]['adjust'] != 0:
                                   oLineTokens = oFile.get_tokens_from_line(iKey)
                                   sSolution = 'Move ' + dAnalysis[iKey]['token_value'] + ' ' + str(dAnalysis[iKey]['adjust']) + ' columns' 
                                   oViolation = violation.New(oLineTokens.get_line_number(), oLineTokens, sSolution)
                                   oViolation.set_action(dAnalysis[iKey])
                                   self.violations.append(oViolation)

                           dAnalysis = {}
                       
                       

            add_adjustments_to_dAnalysis(dAnalysis, self.compact_alignment)


            for iKey in list(dAnalysis.keys()):
                if dAnalysis[iKey]['adjust'] != 0:
                    oLineTokens = oFile.get_tokens_from_line(iKey)
                    sSolution = 'Move ' + dAnalysis[iKey]['token_value'] + ' ' + str(dAnalysis[iKey]['adjust']) + ' columns' 
                    oViolation = violation.New(oLineTokens.get_line_number(), oLineTokens, sSolution)
                    oViolation.set_action(dAnalysis[iKey])
                    self.violations.append(oViolation)


    def fix(self, oFile):
        '''
        Applies fixes for any rule violations.
        '''
        if self.fixable:
            self.analyze(oFile)
            self._print_debug_message('Fixing rule: ' + self.name + '_' + self.identifier)
            self._fix_violation(oFile)
            self.violations = []

    def _fix_violation(self, oFile):
        for oViolation in self.violations:
            lTokens = oViolation.get_tokens()
            dAction = oViolation.get_action()
            iTokenIndex = dAction['token_index']

            if isinstance(lTokens[iTokenIndex - 1], parser.whitespace):
                iLen = len(lTokens[iTokenIndex - 1].get_value())
                lTokens[iTokenIndex - 1].set_value(' '*(iLen + dAction['adjust']))
            else:
                lTokens.insert(iTokenIndex, parser.whitespace(' '*dAction['adjust']))
            oViolation.set_tokens(lTokens)
        oFile.update(self.violations)


def add_adjustments_to_dAnalysis(dAnalysis, compact_alignment):
    iMaxLeftColumn = 0
    iMinLeftColumn = 9999999999999999
    iMaxTokenColumn = 0
    iMinTokenColumn = 9999999999999999

    for iKey in list(dAnalysis.keys()):
        iMaxLeftColumn = max(iMaxLeftColumn, dAnalysis[iKey]['left_column'])
        iMinLeftColumn = min(iMinLeftColumn, dAnalysis[iKey]['left_column'])
        iMaxTokenColumn = max(iMaxTokenColumn, dAnalysis[iKey]['token_column'])
        iMinTokenColumn = min(iMinTokenColumn, dAnalysis[iKey]['token_column'])

    if compact_alignment:
        for iKey in list(dAnalysis.keys()):
            dAnalysis[iKey]['adjust'] = iMaxLeftColumn - dAnalysis[iKey]['token_column'] + 1
    else:
        for iKey in list(dAnalysis.keys()):
            dAnalysis[iKey]['adjust'] = iMaxTokenColumn - dAnalysis[iKey]['token_column']


def check_for_exclusions(oToken, bSkip, oEndSkipToken, lUnless):
    if bSkip:
        if isinstance(oToken, oEndSkipToken):
            return False, None
    else:
        for lTokenPairs in lUnless:
            if isinstance(oToken, lTokenPairs[0]):
                return True, lTokenPairs[1]
                
    return bSkip, oEndSkipToken
    
