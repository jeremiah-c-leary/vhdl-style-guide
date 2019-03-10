import re
import copy


def code_tags(dVars, oLine, oLinePrevious):

    if oLinePrevious.hasCodeTag:
        oLine.hasCodeTag = True
        oLine.codeTags = copy.deepcopy(oLinePrevious.codeTags)

    if re.match('^\s*--\s*vsg_off$', oLine.line):
        oLine.hasCodeTag = True
        oLine.codeTags['vsg_off'] = []

    if re.match('^\s*--\s*vsg_on$', oLinePrevious.line):
        oLine.hasCodeTag = False
        del oLine.codeTags['vsg_off']

    if re.match('^\s*--\s*vsg_off\s+\w', oLine.line):
        oLine.hasCodeTag = True
        lRules = oLine.line.split()[2::]
        for sRule in lRules:
            try:
                oLine.codeTags['vsg_off'].append(sRule)
            except KeyError:
                oLine.codeTags['vsg_off'] = [sRule]

    if re.match('^\s*--\s*vsg_on\s+\w', oLinePrevious.line):
        lRules = oLinePrevious.line.split()[2::]
        for sRule in lRules:
            oLine.codeTags['vsg_off'].remove(sRule)
        if len(oLine.codeTags['vsg_off']) == 0:
            oLine.hasCodeTag = False
            del oLine.codeTags['vsg_off']
