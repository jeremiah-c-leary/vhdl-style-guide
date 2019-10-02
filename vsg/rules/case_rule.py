
from vsg import rule
from vsg import fix
from vsg import check
from vsg import utils


class case_rule(rule.rule):
    '''
    Checks for and fixes words that are not lowercase.

    Parameters
    ----------

    name : string
       The group the rule belongs to.

    identifier : string
       unique identifier.  Usually in the form of 00N.

    sTrigger : string
       The line attribute the rule applies to.

    extractFun : extract function
        Function to be used to extract words.

    Attribute
    ----------

    self.phase : integer = 6
       Sets the phase the rule will run in.

    self.solution : string = None
       Instructions on how to fix the violation.
    '''

    def __init__(self, name=None, identifier=None, sTrigger=None, extractFunction=None):
        rule.rule.__init__(self, name, identifier)
        self.phase = 6
        self.solution = None
        self.sTrigger = sTrigger
        self.extractFunction = extractFunction
        self.case = 'lower'
        self.words = []

    def _analyze(self, oFile, oLine, iLineNumber):
        if oLine.__dict__[self.sTrigger]:
            self.words = self.words + self.extractFunction(oLine)
            if self.case == 'lower':
                    check_function = check.is_lowercase
            else:
                    check_function = check.is_uppercase

            for word in self.words:
                check_function(self, word, iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            print('***')
            print(self.words)
            print('***')
            for word in self.words:
                print(word)

                if self.case == 'lower':
                    fix_function = fix.lower_case
                else:
                    fix_function = fix.upper_case

                fix_function(self, oFile.lines[iLineNumber], word)
