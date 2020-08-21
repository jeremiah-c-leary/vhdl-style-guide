
from vsg import line

from vsg.vhdlFile.classify_new import blank
from vsg.vhdlFile.classify_new import whitespace
from vsg.vhdlFile.classify_new import comment
from vsg.vhdlFile.classify_new import architecture_body

from vsg import parser

from vsg import token

from vsg.vhdlFile import utils


class vhdlFile():
    '''
    Holds contents of a VHDL file.
    When a vhdlFile object is created, the contents of the file must be passed to it.
    A line object is created for each line read in.
    Then the line object attributes are updated.

    Parameters:

       filecontent: (list)

    Returns:

       fileobject
    '''
    def __init__(self, filecontent):
        self.filecontent = filecontent
        self.lines = [line.line('')]
        self._processFile()
        self.filename = None

    def _processFile(self):

        lAllObjects = []

        dVars = {}
        dVars['history'] = []
        dVars['history'].append('design_unit')

        for sLine in self.filecontent:
            oLine = line.line(sLine.replace('\t', '  ').rstrip())
            lTokens = oLine.get_zipped_tokens()
            lObjects = [] 
            for sToken in lTokens:
                lObjects.append(parser.item(sToken))
            
            blank.classify(lObjects, oLine)
            whitespace.classify(lTokens, lObjects)
            comment.classify(dVars, lTokens, lObjects, oLine)

            # Add line to file
            self.lines.append(oLine)

            lAllObjects.extend(lObjects)
            lAllObjects.append(parser.carriage_return())

        lNewObjects = []
        for iObject, oObject in enumerate(lAllObjects):
            if is_whitespace(oObject, lNewObjects):
                continue
#            if iObject > 0:
#                print('[' + ']['.join(dVars['history']) + ']')
#                print(f'{oObject.get_value()}')
            if utils.is_current_level(dVars, 'design_unit'):
                if utils.is_object('entity', token.entity.keyword, oObject, lNewObjects):
                   utils.push_level(dVars, 'entity_declaration')
                elif utils.is_object('architecture', token.architecture_body.keyword, oObject, lNewObjects):
                   utils.push_level(dVars, 'architecture_body')
                else:
                    lNewObjects.append(oObject)
                continue

            if utils.is_current_level(dVars, 'entity_declaration'):
                if oObject.get_value().lower() == 'is':
                   lNewObjects.append(token.entity.is_keyword(oObject.get_value()))
                elif oObject.get_value().lower() == 'end':
                   lNewObjects.append(token.entity.end_keyword(oObject.get_value()))
                elif oObject.get_value().lower() == 'entity':
                   lNewObjects.append(token.entity.end_entity_keyword(oObject.get_value()))
                elif oObject.get_value().lower() == ';':
                   lNewObjects.append(token.entity.semicolon())
                   utils.pop_level(dVars)
                else:
                    lNewObjects.append(oObject)
                continue
                    
            if utils.is_current_level(dVars, 'architecture_body'):
                if not architecture_body.classify(oObject, lNewObjects, dVars):
                    lNewObjects.append(oObject)
                continue

            if utils.is_current_level(dVars, 'architecture_declarative_part'):
                if oObject.get_value().lower() == 'begin':
                   lNewObjects.append(token.architecture_body.begin_keyword(oObject.get_value()))
                   utils.pop_level(dVars)
                   utils.push_level(dVars, 'architecture_statement_part')
                continue

            if utils.is_current_level(dVars, 'architecture_statement_part'):
                if is_concurrent_statement(iObject, oObject, lAllObjects, lNewObjects, dVars):
                    pass
                elif oObject.get_value().lower() == 'end':
                   lNewObjects.append(token.architecture_body.end_keyword(oObject.get_value()))
                   utils.pop_level(dVars)
                else:
                    lNewObjects.append(oObject)
                continue

            if utils.is_current_level(dVars, 'block_statement:begin_declaration'):
                if oObject.get_value().lower() == ':':
                    lNewObjects.append(token.block_statement.label_colon())
                elif oObject.get_value().lower() == 'block':
                   lNewObjects.append(token.block_statement.keyword(oObject.get_value()))
                elif have_guard_condition(iObject, lAllObjects):
                   print("need to process guard condition first")
                elif have_is_keyword(iObject, lAllObjects):
                   lNewObjects.append(token.block_statement.is_keyword(oObject.get_value()))
                elif oObject.get_value().lower() == 'begin':
                   lNewObjects.append(token.block_statement.begin_keyword(oObject.get_value()))
                   utils.pop_level(dVars)
                   utils.push_level(dVars, 'block_statement_part')
                else:
                    lNewObjects.append(oObject)
                continue

            if utils.is_current_level(dVars, 'block_statement_part'):
                if is_concurrent_statement(iObject, oObject, lAllObjects, lNewObjects, dVars):
                    pass
#                if is_block_statement(iObject, lAllObjects):
#                   lNewObjects.append(token.block_statement.label_name(oObject.get_value()))
#                   utils.push_level(dVars, 'block_statement:begin_declaration')
                elif oObject.get_value().lower() == 'end':
                    lNewObjects.append(token.block_statement.end_keyword(oObject.get_value()))
                    utils.pop_level(dVars)
                    utils.push_level(dVars, 'block_statement:end_declaration')
                else:
                    lNewObjects.append(oObject)
                continue

            if utils.is_current_level(dVars, 'block_statement:end_declaration'):
                if oObject.get_value().lower() == 'block':
                    lNewObjects.append(token.block_statement.end_block_keyword(oObject.get_value()))
                elif oObject.get_value().lower() == ';':
                    lNewObjects.append(token.block_statement.semicolon())
                    utils.pop_level(dVars)
                else:
                    lNewObjects.append(token.block_statement.end_block_label(oObject.get_value()))
                continue

            if utils.is_current_level(dVars, 'for_generate_statement:begin_declaration'):
                if oObject.get_value().lower() == ':':
                    lNewObjects.append(token.for_generate_statement.label_colon())
                elif oObject.get_value().lower() == 'for':
                   lNewObjects.append(token.for_generate_statement.for_keyword(oObject.get_value()))
                elif oObject.get_value().lower() == 'generate':
                   lNewObjects.append(token.for_generate_statement.generate_keyword(oObject.get_value()))
                   utils.pop_level(dVars)
                   utils.push_level(dVars, 'for_generate_statement:end_declaration')
                   utils.push_level(dVars, 'generate_statement_body')
                else:
                    lNewObjects.append(oObject)
                continue

            if utils.is_current_level(dVars, 'generate_statement_body'):
                if is_concurrent_statement(iObject, oObject, lAllObjects, lNewObjects, dVars):
                    pass
                else:
                    utils.pop_level(dVars)

            if utils.is_current_level(dVars, 'for_generate_statement:end_declaration'):
                if oObject.get_value().lower() == 'end':
                    lNewObjects.append(token.for_generate_statement.end_keyword(oObject.get_value()))
                elif oObject.get_value().lower() == 'generate':
                    lNewObjects.append(token.for_generate_statement.end_generate_keyword(oObject.get_value()))
                elif oObject.get_value().lower() == ';':
                    lNewObjects.append(token.for_generate_statement.semicolon())
                    utils.pop_level(dVars)
                else:
                    lNewObjects.append(token.for_generate_statement.end_generate_label(oObject.get_value()))
                continue

#        for oObject in lNewObjects:
#            print(f'{oObject} | {oObject.get_value()}')

#        print('-'*80)

        for iLine, lLine in enumerate(split_on_carriage_return(lNewObjects)):
            self.lines[iLine + 1].objects = lLine
        

#        oLine.objects = lNewObjects



def split_on_carriage_return(lObjects):
    lReturn = []
    lMyObjects = []
    iLine = 1
    for oObject in lObjects:
        if type(oObject) == parser.carriage_return:
#            print(lObjects)
            lReturn.append(lMyObjects)
            iLine += 1
            lMyObjects = []
        else:
            lMyObjects.append(oObject)
    if len(lMyObjects) > 0:
#        print(lObjects)
        lReturn.append(lMyObjects)
    return lReturn

def is_block_statement(iObject, lAllObjects):
    iItemCount = 0
    iIndex = iObject
    try:
        while iItemCount < 3:
            if type(lAllObjects[iIndex]) == parser.item:
                iItemCount += 1
            iIndex += 1
        else:
            if lAllObjects[iIndex-1].get_value().lower() == 'block':
                return True
    except IndexError:
        return False
    return False

def have_guard_condition(iObject, lAllObjects):
    iItemCount = 0
    iIndex = iObject
    while iItemCount < 1:
        if type(lAllObjects[iIndex]) == parser.item:
            iItemCount += 1
            if lAllObjects[iIndex].get_value().lower() == '(':
                return True
        iIndex += 1
    return False

def have_is_keyword(iObject, lAllObjects):
    iItemCount = 0
    iIndex = iObject
    while iItemCount < 1:
        if type(lAllObjects[iIndex]) == parser.item:
            iItemCount += 1
            if lAllObjects[iIndex].get_value().lower() == 'is':
                return True
        iIndex += 1
    return False


def is_concurrent_statement(iObject, oObject, lAllObjects, lNewObjects, dVars):
    if is_block_statement(iObject, lAllObjects):
        lNewObjects.append(token.block_statement.label_name(oObject.get_value()))
        utils.push_level(dVars, 'block_statement:begin_declaration')
        return True
    if is_generate_statement(iObject, oObject, lAllObjects, lNewObjects, dVars):
        lNewObjects.append(token.for_generate_statement.label_name(oObject.get_value()))
        utils.push_level(dVars, 'for_generate_statement:begin_declaration')
        return True
    return False


def is_whitespace(oObject, lNewObjects):
    if type(oObject) == parser.carriage_return:
        lNewObjects.append(oObject)
        return True
    if type(oObject) == parser.blank_line:
        lNewObjects.append(oObject)
        return True
    if type(oObject) == parser.comment:
        lNewObjects.append(oObject)
        return True
    if type(oObject) == parser.whitespace:
        lNewObjects.append(oObject)
        return True
    return False

def is_generate_statement(iObject, oObject, lAllObjects, lNewObjects, dVars):
    if is_for_generate_statement(iObject, oObject, lAllObjects, lNewObjects, dVars):
        return True
    return False

def is_for_generate_statement(iObject, oObject, lAllObjects, lNewObjects, dVars):
    iItemCount = 0
    iIndex = iObject
    try:
        while iItemCount < 3:
            if type(lAllObjects[iIndex]) == parser.item:
                iItemCount += 1
            iIndex += 1
        else:
            if lAllObjects[iIndex-1].get_value().lower() == 'for':
                return True
    except IndexError:
        return False
    return False
