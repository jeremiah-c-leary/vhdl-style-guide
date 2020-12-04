
from vsg import rule
from vsg import token
from vsg import violation


class rule_016(rule.Rule):
    '''
    Checks a process has a label.

    Parameters
    ----------

    name : string
       The group the rule belongs to.

    identifier : string
       unique identifier.  Usually in the form of 00N.

    lTokens : list of parser object types
       object types to check the prefix

    lSuffixes: string list
       acceptable suffixes
    '''

    def __init__(self):
        rule.Rule.__init__(self, 'process', '016')
        self.solution = 'Add label for process'
        self.phase = 1
        self.fixable = False

    def analyze(self, oFile):
        lKeywords = oFile.get_tokens_matching([token.process_statement.process_keyword])
        lLabels = oFile.get_tokens_matching([token.process_statement.process_label])

        iPreviousIndex = 0
        for oKeyword in lKeywords:
            iCurrentIndex = oKeyword.get_start_index()
            for oLabel in lLabels:
                iLabelIndex = oLabel.get_start_index()
                if iPreviousIndex < iLabelIndex and iLabelIndex < iCurrentIndex:
                    break
            else:
                oViolation = violation.New(oKeyword.get_line_number(), oKeyword, self.solution)
                self.add_violation(oViolation)
            iPreviousIndex = iCurrentIndex
