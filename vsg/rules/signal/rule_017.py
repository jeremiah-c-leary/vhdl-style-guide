
from vsg import rule
from vsg import utils


class rule_017(rule.rule):
    '''
    Signal rule 017 handles formatting of multiple signal identifiers defined in a single signal declaration.
    '''
    def __init__(self):
        rule.rule.__init__(self, 'signal', '017')
        self.solution = 'TBD'
        self.phase = 1
        self.fixable = False  # Temporary

    def _pre_analyze(self):
        self.lSignalLines = []

    def _analyze(self, oFile, oLine, iLineNumber):
        if oLine.isSignal and oLine.isEndSignal:
            analyze_single_line(self, oLine, iLineNumber)
        elif oLine.isSignal and not oLine.isEndSignal:
            self.lSignalLines.append([iLineNumber, oLine])
        elif oLine.insideSignal:
            self.lSignalLines.append([iLineNumber, oLine])
            if oLine.isEndSignal:
                analyze_multi_line(self) 
                self.lSignalLines = []


def analyze_single_line(self, oLine, iLineNumber):
    lIdentifiers = []
    for sTok in oLine.get_tokens()[1:]:
       if sTok == ',':
           continue
       if sTok == ':':
           break
       lIdentifiers.append(sTok)
    if not len(lIdentifiers) == 1:
       dViolation = utils.create_violation_dict(iLineNumber)
       self.add_violation(dViolation)

        
def analyze_multi_line(self):
    iArrayIndex = -1
    iStartLine = get_start_line(self.lSignalLines)
    for iLineNumber, oLine in self.lSignalLines:
        iArrayIndex += 1
        lTokens = get_tokens(iArrayIndex, oLine)
        lTokens = extract_identifiers(lTokens)
        check_number_of_tokens(self, iStartLine, lTokens)


def check_number_of_tokens(self, iStartLine, lTokens):
    if not len(lTokens) == 1:
        dViolation = utils.create_violation_dict(iStartLine)
        self.add_violation(dViolation)
            

def get_start_line(lLines):
    return lLines[0][0]


def get_tokens(iArrayIndex, oLine):
    lReturn = []
    if iArrayIndex == 0:
        lReturn = oLine.get_tokens()[1:]
    else:
        lReturn = oLine.get_tokens()
    return lReturn
    

def extract_identifiers(lTokens):
    lReturn = remove_comma_tokens(lTokens)
    lReturn = remove_colon_and_after_tokens(lReturn)
    return lReturn


def remove_comma_tokens(lTokens):
    lReturn = []
    for sTok in lTokens:
        if not sTok == ',':
            lReturn.append(sTok)
    return lReturn


def remove_colon_and_after_tokens(lTokens):
    lReturn = []
    for sTok in lTokens:
        if not sTok == ':':
            lReturn.append(sTok)
        else:
            break
    return lReturn
