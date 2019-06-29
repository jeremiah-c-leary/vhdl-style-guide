
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

    def _pre_analyze(self):
        self.lGroup = []
        self.fGroupFound = False
        self.iStartGroupIndex = None

    def _analyze(self, oFile, oLine, iLineNumber):
        if oLine.__dict__[self.sStartGroupTrigger] and not self.fGroupFound:
            self.fGroupFound = True
            self.iStartGroupIndex = iLineNumber
        if oLine.__dict__[self.sEndGroupTrigger] and self.fGroupFound:
            self.lGroup.append(oLine)
            self.fGroupFound = False
            check.keyword_alignment(self, self.iStartGroupIndex, self.sKeyword, self.lGroup)
            self.lGroup = []
            self.iStartGroupIndex = None
        if self.fGroupFound:
            if isinstance(self.sLineTrigger, list):
                for sTrigger in self.sLineTrigger:
                    if oLine.__dict__[sTrigger]:
                        lGroup.append(oLine)
            elif oLine.__dict__[self.sLineTrigger]:
                self.lGroup.append(oLine)
            else:
                self.lGroup.append(line.line('Removed line'))

    def _fix_violations(self, oFile):
        fix.keyword_alignment(self, oFile)
