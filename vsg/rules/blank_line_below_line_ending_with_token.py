
from vsg import parser
from vsg import violation

from vsg.rules import utils as rules_utils
from vsg.rule_group import blank_line


class blank_line_below_line_ending_with_token(blank_line.Rule):
    '''
    Checks for a blank line below a line ending with a given token

    Parameters
    ----------

    name : string
       The group the rule belongs to.

    identifier : string
       unique identifier.  Usually in the form of 00N.

    token: token object type list
       token object that a blank line below should appear
    '''

    def __init__(self, name, identifier, lTokens, lAllowTokens=None):
        blank_line.Rule.__init__(self, name=name, identifier=identifier)
        self.lTokens = lTokens
        self.lHierarchyLimits = None
        if lAllowTokens is None:
            self.lAllowTokens = []
        else:
            self.lAllowTokens = lAllowTokens
        self.style = 'require_blank_line'
        self.configuration.append('style')
        self.ignore_hierarchy = False


    def _get_tokens_of_interest(self, oFile):
        self._update_hierarchy_limits()
        self._update_allow_tokens()
        lReturn = []    
        if self.style == 'require_blank_line':
            if self.lHierarchyLimits is None:
                lToi = oFile.get_line_below_line_ending_with_token(self.lTokens)
            else:
                lToi = oFile.get_line_below_line_ending_with_token_with_hierarchy(self.lTokens, self.lHierarchyLimits)
            for oToi in lToi:
                oToi.style = 'require_blank_line'
                lReturn.append(oToi)
        elif self.style == 'no_blank_line':
            lToi = oFile.get_blank_lines_below_line_ending_with_token(self.lTokens, self.lHierarchyLimits)
            for oToi in lToi:
                oToi.style = 'no_blank_line'
                lReturn.append(oToi)
        return lReturn

    def _analyze(self, lToi):
        for oToi in lToi:
            if oToi.style == 'require_blank_line':
#                print('require_blank_line')
                self._analyze_require_blank_line(oToi, self.lAllowTokens)
            elif oToi.style == 'no_blank_line':
#                print('No_blank_line')
#                print(oToi.get_tokens())
#                print(oToi.get_line_number())
                self._analyze_no_blank_line(oToi, self.lAllowTokens)
#        if self.style == 'require_blank_line':
#            self._analyze_require_blank_line(lToi, self.lAllowTokens)
#        elif self.style == 'no_blank_line':
#            self._analyze_no_blank_line(lToi, self.lAllowTokens)

    def _fix_violation(self, oViolation):
        lTokens = oViolation.get_tokens()
        dAction = oViolation.get_action()
#        print(lTokens)
#        print(dAction)
        if dAction['action'] == 'Insert':
            rules_utils.insert_carriage_return(lTokens, 0)
            rules_utils.insert_blank_line(lTokens, 0)
            oViolation.set_tokens(lTokens)
        elif dAction['action'] == 'Remove':
            oViolation.set_tokens([])

    def _update_hierarchy_limits(self):
        if self.ignore_hierarchy:
            self.lHierarchyLimits = None

    def _update_allow_tokens(self):
        return None


    def _analyze_require_blank_line(self, oToi, lAllowTokens):
#        print('_analyze_require_blank_line')
        lTokens = oToi.get_tokens()
        if self._is_allowed_token(lAllowTokens, lTokens):
            return None
        if len(lTokens) == 1:
            if isinstance(lTokens[0], parser.blank_line):
                return None
        sSolution = 'Insert blank line below'
        oViolation = violation.New(oToi.get_line_number() - 1, oToi, sSolution)
        dAction = {}
        dAction['action'] = 'Insert'
        oViolation.set_action(dAction)
        self.add_violation(oViolation)


    def _analyze_no_blank_line(self, oToi, lAllowTokens):
#        print('_analyze_no_blank_line')
        sSolution = 'Remove blank lines below'
#        print(oToi.get_tokens())
#        print(oToi.get_line_number())
        oViolation = violation.New(oToi.get_line_number() - 1, oToi, sSolution)
        dAction = {}
        dAction['action'] = 'Remove'
        oViolation.set_action(dAction)
        self.add_violation(oViolation)


    def _is_allowed_token(self, lAllowTokens, lTokens):
        bSkip = False
        for oAllowToken in lAllowTokens:
            for oToken in lTokens:
                if isinstance(oToken, oAllowToken):
                    bSkip = True
                    break
            if bSkip:
               break
        if bSkip:
            return True
        return False
