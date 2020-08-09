'''
This module contains functions for rules to fix issues.
'''
from vsg import parser


def indent(self, oLine):
    '''
    Fixes indent violations.

    Parameters:

      self: (rule object)

      oLine: (line object)
    '''
    lObjects = oLine.get_objects()
    indentSpaces = oLine.indentLevel * self.indentSize * ' '
    if type(lObjects[0]) == parser.whitespace:
        lObjects[0].set_value(indentSpacs)
    else:
        lObjects.insert(0, parser.whitespace(indentSpaces))
    oLine.update_objects(lObjects)
