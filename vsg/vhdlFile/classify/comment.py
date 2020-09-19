
import re

# Regex to find comments that ignores contents of double quoted strings,
# for example, "--" : a two bit std_logic_vector literal of don't cares.
has_comment_re = re.compile(r'^(?:".*"|[^"\n])*?(?P<comment>--.*)', re.IGNORECASE)

comment_only_re = re.compile(r'^\s*--')


def comment(dVars, lTokens, lObjects, oLine):
    # Check for comment lines
    match = has_comment_re.match(oLine.line)
    if match is None:
        return
    oLine.hasComment = True
    oLine.commentColumn = match.start("comment")
    if comment_only_re.match(oLine.line) is not None:
        oLine.isComment = True
        oLine.indentLevel = dVars['iCurrentIndentLevel']
    else:
        oLine.hasInlineComment = True
