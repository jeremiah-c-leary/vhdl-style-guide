
def identifier_alignment(self, iLineNumber, lGroup):
    '''
    Checks identifiers in a group of line objects are aligned in the same column.

    Parameters:

      self: (rule object)

      iLineNumber: (integer)

      lGroup: (list of line objects)
    '''
    iMaximumIdentifierColumn = 0
    iMaximumIdentifierLength = 0
    iMaximumKeywordLength = 0
    sViolationRange = str(iLineNumber) + '-' + str(iLineNumber + len(lGroup) - 1)
    self.dFix['violations'][sViolationRange] = {}
    self.dFix['violations'][sViolationRange]['line'] = {}

    for iIndex, oGroupLine in enumerate(lGroup):
        if oGroupLine.isConstant or oGroupLine.isVariable or oGroupLine.isFileKeyword:
            self.dFix['violations'][sViolationRange]['line'][iLineNumber + iIndex] = {}
            iIdentifierAlignment = find_identifier(oGroupLine.line)
            self.dFix['violations'][sViolationRange]['line'][iLineNumber + iIndex]['identifierColumn'] = iIdentifierAlignment

            sKeyword, sIdentifier = parse_keyword_identifier(oGroupLine.line)

            iMaximumIdentifierLength = max(iMaximumIdentifierLength, len(sIdentifier))

            iMaximumKeywordLength = max(iMaximumKeywordLength, len(sKeyword))

            iMaximumIdentifierColumn = max(iMaximumIdentifierColumn, iIdentifierAlignment)

            if not iIdentifierAlignment == iMaximumIdentifierColumn:
                add_range_violation(self, sViolationRange)

    self.dFix['violations'][sViolationRange]['maximumIdentifierColumn'] = iMaximumIdentifierColumn
    self.dFix['violations'][sViolationRange]['maximumIdentifierLength'] = iMaximumIdentifierLength
    self.dFix['violations'][sViolationRange]['maximumKeywordLength'] = iMaximumKeywordLength


def find_identifier(sString):

    fKeywordFound = False
    fSpaceAfterKeywordFound = False
    for iIndex, sChar in enumerate(sString):
        if not sChar.isspace() and not fKeywordFound:
            fKeywordFound = True
        if sChar.isspace() and fKeywordFound:
            fSpaceAfterKeywordFound = True
        if not sChar.isspace() and fSpaceAfterKeywordFound:
            return iIndex


def add_range_violation(self, sViolationRange):
    '''
    Appends a range violation to the violation list if it does not already exist.

    Parameters:

      self: (rule object)

      sViolationRange: (string)
    '''
    if sViolationRange not in self.violations:
        self.add_violation(sViolationRange)


def parse_keyword_identifier(sString):
    lLine = sString.split()
    return lLine[0], lLine[1]
