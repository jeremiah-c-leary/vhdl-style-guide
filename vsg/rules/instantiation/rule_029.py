
from vsg import rule
from vsg import check
from vsg import fix
from vsg import line


class rule_029(rule.rule):
    '''
    Entity rule 029 ensures the alignment of comments in an instantiation.
    '''

    def __init__(self):
        rule.rule.__init__(self)
        self.name = 'instantiation'
        self.identifier = '029'
        self.solution = 'Inconsistent alignment of comments in instantiation.'
        self.phase = 6
        self.lGroup = []
        self.fGroupFound = False
        self.iStartGroupIndex = None

    def _analyze(self, oFile, oLine, iLineNumber):
            self.fGroupFound, self.iStartGroupIndex = search_for_group(self.fGroupFound, oLine, self.iStartGroupIndex, iLineNumber)
            if oLine.isInstantiationPortEnd:
                self.lGroup.append(oLine)
                self.fGroupFound = False
                check.keyword_alignment(self, self.iStartGroupIndex, '--', self.lGroup)
                self.lGroup = []
                self.iStartGroupIndex = None
            store_lines_for_group(self.fGroupFound, oLine, self.lGroup)

    def _fix_violations(self, oFile):
        fix.keyword_alignment(self, oFile)


def search_for_group(fGroupFound, oLine, iStartGroupIndex, iLineNumber):
    if not fGroupFound and oLine.insideInstantiation:
        return True, iLineNumber
    return fGroupFound, iStartGroupIndex


def store_lines_for_group(fGroupFound, oLine, lGroup):
    if fGroupFound:
        if oLine.hasComment and not oLine.isComment:
            lGroup.append(oLine)
        else:
            lGroup.append(line.line('Removed line'))
