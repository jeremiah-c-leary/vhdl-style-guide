
import rule
import re


class comment_rule(rule.rule):
    
    def __init__(self):
        rule.rule.__init__(self)
        self.name = 'comment'


class rule_001(comment_rule):
    '''Case rule 001 checks for the proper alignment of comments.'''

    def __init__(self):
        comment_rule.__init__(self)
        self.identifier = '001'
        self.solution = 'Ensure proper indentation of comment.'

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isComment:
                if oFile.lines[iLineNumber - 1].hasComment:
                    if oFile.lines[iLineNumber - 1].isComment:
                        if not oLine.commentColumn == (oLine.indentLevel * self.indentSize):
                            self.add_violation(iLineNumber)
                else:
                    if not oLine.commentColumn == (oLine.indentLevel * self.indentSize):
                        self.add_violation(iLineNumber)


class rule_002(comment_rule):
    '''Case rule 002 checks for the proper alignment of comments.'''

    def __init__(self):
        comment_rule.__init__(self)
        self.identifier = '002'
        self.solution = 'Ensure proper alignment of comment with previous line.'

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if iLineNumber > 0:
                oPreviousLine = oFile.lines[iLineNumber - 1]
            if not oLine.isComment and oLine.hasComment:
                if not oPreviousLine.isComment and oPreviousLine.hasComment:
                    if not oLine.commentColumn == oPreviousLine.commentColumn:
                        self.add_violation(iLineNumber)
                if oPreviousLine.isComment:
                    if not oPreviousLine.commentColumn == (oPreviousLine.indentLevel * self.indentSize):
                        if not oLine.commentColumn == oPreviousLine.commentColumn:
                            self.add_violation(iLineNumber)
            if oLine.isComment:
                if oPreviousLine.hasComment:
                    if not oPreviousLine.isComment:
                        if not oLine.commentColumn == oPreviousLine.commentColumn:
                            if not oLine.commentColumn == (oLine.indentLevel * self.indentSize):
                                self.add_violation(iLineNumber)


#TODO:
# multiline case alignment
# keywords are lower case



