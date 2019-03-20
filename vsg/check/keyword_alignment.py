
def keyword_alignment(self, iLineNumber, sKeyword, lGroup):
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
    try:
        self.dFix['violations'][sViolationRange]['line'] = {}
    except KeyError:
        self.dFix['violations'][sViolationRange] = {}
        self.dFix['violations'][sViolationRange]['line'] = {}

    for iIndex, oGroupLine in enumerate(lGroup):
        if sKeyword in oGroupLine.line:
            self.dFix['violations'][sViolationRange]['line'][iLineNumber + iIndex] = {}
            self.dFix['violations'][sViolationRange]['line'][iLineNumber + iIndex]['keywordColumn'] = oGroupLine.line.find(sKeyword)

            iMaximumKeywordColumn = get_maximum_keyword_column(oGroupLine, sKeyword, iMaximumKeywordColumn)

            iKeywordAlignment = update_keyword_alignment(oGroupLine, sKeyword, iKeywordAlignment)

            if not iKeywordAlignment == oGroupLine.line.find(sKeyword):
                add_range_violation(self, sViolationRange)

    self.dFix['violations'][sViolationRange]['maximumKeywordColumn'] = iMaximumKeywordColumn


def get_maximum_keyword_column(oLine, sKeyword, iMaximumKeywordColumn):
    '''
    Return the highest column count a keyword is found.

    Parameters:

      oLine: (line object)

      sKeyword: (string)

      iMaximumKeywordColumn: (integer)

    Returns: (integer)
    '''
    if oLine.line.find(sKeyword) > iMaximumKeywordColumn:
        return oLine.line.find(sKeyword)
    return iMaximumKeywordColumn


def update_keyword_alignment(oLine, sKeyword, iKeywordAlignment):
    '''
    Returns the column where the keyword was detected.

    Parameters:

      oLine: (line object)

      sKeyword: (string)

      iKeywordAlignment: (integer)

    Returns: (integer)
    '''
    if not iKeywordAlignment:
        return oLine.line.find(sKeyword)
    return iKeywordAlignment


def add_range_violation(self, sViolationRange):
    '''
    Appends a range violation to the violation list if it does not already exist.

    Parameters:

      self: (rule object)

      sViolationRange: (string)
    '''
    if sViolationRange not in self.violations:
        self.add_violation(sViolationRange)
