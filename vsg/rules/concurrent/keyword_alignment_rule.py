
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
                concurrent_keyword_alignment(self, iStartGroupIndex, self.sKeyword, lGroup)
                lGroup = []
                iStartGroupIndex = None
            if fGroupFound:
                lGroup.append(oLine)

    def _fix_violations(self, oFile):
        fix.keyword_alignment(self, oFile)


def concurrent_keyword_alignment(self, iLineNumber, sKeyword, lGroup):
    '''
    Checks keywords in a group of line objects are aligned in the same column.

    Parameters:

      self: (rule object)

      iLineNumber: (integer)

      sKeyword: (string)

      lGroup: (list of line objects)
    '''
    iKeywordAlignment = None
    iMaximumKeywordColumn = 0
    sViolationRange = str(iLineNumber) + '-' + str(iLineNumber + len(lGroup) - 1)
    self.dFix['violations'][sViolationRange] = {}
    self.dFix['violations'][sViolationRange]['line'] = {}

    for iIndex, oGroupLine in enumerate(lGroup):
        if sKeyword in oGroupLine.line and oGroupLine.isConcurrentBegin:
            self.dFix['violations'][sViolationRange]['line'][iLineNumber + iIndex] = {}
            self.dFix['violations'][sViolationRange]['line'][iLineNumber + iIndex]['keywordColumn'] = oGroupLine.line.find(sKeyword)

            iMaximumKeywordColumn = check.get_maximum_keyword_column(oGroupLine, sKeyword, iMaximumKeywordColumn)

            iKeywordAlignment = check.update_keyword_alignment(oGroupLine, sKeyword, iKeywordAlignment)

            if not iKeywordAlignment == oGroupLine.line.find(sKeyword):
                check.add_range_violation(self, sViolationRange)

    self.dFix['violations'][sViolationRange]['maximumKeywordColumn'] = iMaximumKeywordColumn
