
from vsg import rule
from vsg import check
from vsg import fix


class keyword_alignment_rule(rule.rule):
    '''
    Checks for keyword alignment in consecutive concurrent statements.

    Parameters
    ----------

    name : string
       The group the rule belongs to.

    identifier : string
       unique identifier.  Usually in the form of 00N.

    Attributes
    ----------

    sKeyword : string
       The keyword to align.

    sStartGroupTrigger: string
       The line attribute which marks the start of a group to align.

    sEndGroupTrigger: string
       The line attribute which ends the group to align.
       NOTE:  This is inversed to allow for grouping of consecutive lines.
    '''

    def __init__(self, name, identifier):
        rule.rule.__init__(self, name, identifier)
        self.phase = 5
        self.sKeyword = None
        self.sStartGroupTrigger = None
        self.sEndGroupTrigger = None

    def analyze(self, oFile):
        lGroup = []
        fGroupFound = False
        iStartGroupIndex = None
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.__dict__[self.sStartGroupTrigger] and not fGroupFound:
                fGroupFound = True
                iStartGroupIndex = iLineNumber
            if not oLine.__dict__[self.sEndGroupTrigger] and fGroupFound:
                fGroupFound = False
                check.keyword_alignment(self, iStartGroupIndex, self.sKeyword, lGroup)
                lGroup = []
                iStartGroupIndex = None
            if fGroupFound:
                lGroup.append(oLine)

    def _fix_violations(self, oFile):
        fix.keyword_alignment(self, oFile)
