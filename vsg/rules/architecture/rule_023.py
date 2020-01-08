
from vsg import rule
from vsg import check
from vsg import fix
from vsg import line


class rule_023(rule.rule):
    '''
    Architecture rule 023 ensures the alignment of comments.
    '''

    def __init__(self):
        rule.rule.__init__(self, name='architecture', identifier='023')
        self.phase = 7
        self.solution = 'Inconsistent alignment of comments.'
        self.sStartGroupTrigger = 'isArchitectureKeyword'
        self.sEndGroupTrigger = 'isArchitectureBegin'
        self.sLineTrigger = 'hasInlineComment'

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
            check.comment_alignment(self, self.iStartGroupIndex, self.lGroup)
            self.lGroup = []
            self.iStartGroupIndex = None
        if self.fGroupFound:
            if isinstance(self.sLineTrigger, list):
                for sTrigger in self.sLineTrigger:
                    if oLine.__dict__[sTrigger]:
                        self.lGroup.append(oLine)
            elif oLine.__dict__[self.sLineTrigger]:
                self.lGroup.append(oLine)
            else:
                self.lGroup.append(line.line('Removed line'))

    def _fix_violations(self, oFile):
        fix.comment_alignment(self, oFile)