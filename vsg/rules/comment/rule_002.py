
from vsg.rules.comment import comment_rule


# class rule_002(comment_rule):
#     '''Case rule 002 checks for the proper alignment of comments.'''
#
#     def __init__(self):
#         comment_rule.__init__(self)
#         self.identifier = '002'
#         self.solution = 'Ensure proper alignment of comment with previous line.'
#         self.phase = 5
#
#     def analyze(self, oFile):
#         for iLineNumber, oLine in enumerate(oFile.lines):
#             if iLineNumber > 0:
#                 oPreviousLine = oFile.lines[iLineNumber - 1]
#             if not oLine.isComment and oLine.hasComment:
#                 if oLine.isCaseWhenKeyword:
#                     if not oPreviousLine.isComment and oPreviousLine.hasComment:
#                         if not oLine.commentColumn == oPreviousLine.commentColumn:
#                             self.add_violation(iLineNumber)
#                     if oPreviousLine.isComment:
#                         if not oPreviousLine.commentColumn == (oPreviousLine.indentLevel * self.indentSize) and \
#                            not oPreviousLine.commentColumn == ((oPreviousLine.indentLevel - 1) * self.indentSize):
#                             if not oLine.commentColumn == oPreviousLine.commentColumn:
#                                 self.add_violation(iLineNumber)
#                 else:
#                     if not oPreviousLine.isComment and oPreviousLine.hasComment:
#                         if not oLine.commentColumn == oPreviousLine.commentColumn:
#                             self.add_violation(iLineNumber)
#                     if oPreviousLine.isComment:
#                         if not oPreviousLine.commentColumn == (oPreviousLine.indentLevel * self.indentSize):
#                             if not oLine.commentColumn == oPreviousLine.commentColumn:
#                                 self.add_violation(iLineNumber)
#             if oLine.isComment:
#                 if oPreviousLine.hasComment:
#                     if not oPreviousLine.isComment:
#                         if not oLine.commentColumn == oPreviousLine.commentColumn:
#                             if not oLine.commentColumn == (oLine.indentLevel * self.indentSize):
#                                 self.add_violation(iLineNumber)
