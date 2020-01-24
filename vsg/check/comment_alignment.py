import re

has_comment_re = re.compile(r'^(?:".*"|[^"\n])*?(?P<comment>--.*)', re.IGNORECASE)

def comment_alignment(self, iLineNumber, lGroup):
    '''
    Checks comments in a group of line objects are aligned in the same column.

    Parameters:

      self: (rule object)

      iLineNumber: (integer)

      lGroup: (list of line objects)
    '''
    CommentColumns = []
    sViolationRange = str(iLineNumber) + '-' + str(iLineNumber + len(lGroup) - 1)

    self.dFix['violations'].setdefault(sViolationRange, {}).setdefault('line', {})

    for iIndex, oGroupLine in enumerate(lGroup):
        match = has_comment_re.match(oGroupLine.line)
        if match is None:
            continue
        column = match.start("comment")

        self.dFix['violations'][sViolationRange]['line'][iLineNumber + iIndex] = {}
        self.dFix['violations'][sViolationRange]['line'][iLineNumber + iIndex]['commentColumn'] = column

        CommentColumns.append(column)

        if CommentColumns[0] != column:
            if sViolationRange not in self.violations:
                self.add_violation(sViolationRange)

    self.dFix['violations'][sViolationRange]['maximumCommentColumn'] = max(CommentColumns + [0])
