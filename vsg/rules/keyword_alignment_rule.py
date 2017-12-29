
from vsg import rule
from vsg import check
from vsg import fix
from vsg import line


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

    sLineTrigger : string
       Stores lines in a group which match this attribute.
    '''

    def __init__(self, name=None, identifier=None):
        rule.rule.__init__(self, name, identifier)
        self.phase = 5
        # The following is filled out by the user
        self.sKeyword = None
        self.sStartGroupTrigger = None
        self.sEndGroupTrigger = None
        self.sLineTrigger = None

    def analyze(self, oFile):
        lGroup = []
        fGroupFound = False
        iStartGroupIndex = None
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.__dict__[self.sStartGroupTrigger] and not fGroupFound:
                fGroupFound = True
                iStartGroupIndex = iLineNumber
            if oLine.__dict__[self.sEndGroupTrigger] and fGroupFound:
                lGroup.append(oLine)
                fGroupFound = False
                check.keyword_alignment(self, iStartGroupIndex, self.sKeyword, lGroup)
                lGroup = []
                iStartGroupIndex = None
            if fGroupFound:
                if oLine.__dict__[self.sLineTrigger]:
                    lGroup.append(oLine)
                else:
                    lGroup.append(line.line('Removed line'))

    def _fix_violations(self, oFile):
        fix.keyword_alignment(self, oFile)
