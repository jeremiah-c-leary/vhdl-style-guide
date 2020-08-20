
from vsg import line

from vsg.vhdlFile.classify_new import blank
from vsg.vhdlFile.classify_new import whitespace
from vsg.vhdlFile.classify_new import comment

from vsg import parser

from vsg import token


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
            if type(oObject) == parser.carriage_return:
                lNewObjects.append(oObject)
                continue
            if type(oObject) == parser.blank_line:
                lNewObjects.append(oObject)
                continue
            if type(oObject) == parser.comment:
                lNewObjects.append(oObject)
                continue
            if type(oObject) == parser.whitespace:
                lNewObjects.append(oObject)
                continue
#            if iObject > 0:
#                print('[' + ']['.join(dVars['history']) + ']')
#                print(oObject.get_value())
            if current_level(dVars) == 'design_unit':
                if oObject.get_value().lower() == 'entity':
                   lNewObjects.append(token.entity.keyword(oObject.get_value()))
                   push_level(dVars, 'entity_declaration')
                elif oObject.get_value().lower() == 'architecture':
                   lNewObjects.append(token.architecture_body.keyword(oObject.get_value()))
                   push_level(dVars, 'architecture_body')
                else:
                    lNewObjects.append(oObject)
                continue

            if current_level(dVars) == 'entity_declaration':
                if oObject.get_value().lower() == 'is':
                   lNewObjects.append(token.entity.is_keyword(oObject.get_value()))
                elif oObject.get_value().lower() == 'end':
                   lNewObjects.append(token.entity.end_keyword(oObject.get_value()))
                elif oObject.get_value().lower() == 'entity':
                   lNewObjects.append(token.entity.end_entity_keyword(oObject.get_value()))
                elif oObject.get_value().lower() == ';':
                   lNewObjects.append(token.entity.semicolon())
                   pop_level(dVars)
                else:
                    lNewObjects.append(oObject)
                continue
                    
            if current_level(dVars) == 'architecture_body':
                if oObject.get_value().lower() == 'is':
                   lNewObjects.append(token.architecture_body.is_keyword(oObject.get_value()))
                   push_level(dVars, 'architecture_declarative_part')
                elif oObject.get_value().lower() == 'of':
                   lNewObjects.append(token.architecture_body.of_keyword(oObject.get_value()))
                elif oObject.get_value().lower() == 'architecture':
                   lNewObjects.append(token.architecture_body.end_architecture_keyword(oObject.get_value()))
                elif oObject.get_value().lower() == ';':
                   lNewObjects.append(token.architecture_body.semicolon())
                   pop_level(dVars)
                else:
                    lNewObjects.append(oObject)
                continue

            if current_level(dVars) == 'architecture_declarative_part':
                if oObject.get_value().lower() == 'begin':
                   lNewObjects.append(token.architecture_body.begin_keyword(oObject.get_value()))
                   pop_level(dVars)
                   push_level(dVars, 'architecture_statement_part')
                continue

            if current_level(dVars) == 'architecture_statement_part':
                if is_block_statement(iObject, lAllObjects):
                   lNewObjects.append(token.block_statement.label_name(oObject.get_value()))
                   push_level(dVars, 'block_statement:begin_declaration')
                elif oObject.get_value().lower() == 'end':
                   lNewObjects.append(token.architecture_body.end_keyword(oObject.get_value()))
                   pop_level(dVars)
                else:
                    lNewObjects.append(oObject)
                continue

            if current_level(dVars) == 'block_statement:begin_declaration':
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
                   pop_level(dVars)
                   push_level(dVars, 'block_statement_part')
                else:
                    lNewObjects.append(oObject)
                continue

            if current_level(dVars) == 'block_statement_part':
                if is_block_statement(iObject, lAllObjects):
                   lNewObjects.append(token.block_statement.label_name(oObject.get_value()))
                   push_level(dVars, 'block_statement:begin_declaration')
                elif oObject.get_value().lower() == 'end':
                    lNewObjects.append(token.block_statement.end_keyword(oObject.get_value()))
                    pop_level(dVars)
                    push_level(dVars, 'block_statement:end_declaration')
                else:
                    lNewObjects.append(oObject)
                continue

            if current_level(dVars) == 'block_statement:end_declaration':
                if oObject.get_value().lower() == 'block':
                    lNewObjects.append(token.block_statement.end_block_keyword(oObject.get_value()))
                elif oObject.get_value().lower() == ';':
                    lNewObjects.append(token.block_statement.semicolon())
                    pop_level(dVars)
                else:
                    lNewObjects.append(token.block_statement.end_block_label(oObject.get_value()))
                continue

#        for oObject in lNewObjects:
#            print(f'{oObject} | {oObject.get_value()}')

#        print('-'*80)

        for iLine, lLine in enumerate(split_on_carriage_return(lNewObjects)):
            self.lines[iLine + 1].objects = lLine
        

#        oLine.objects = lNewObjects


def pop_level(dVars):
    dVars['history'].pop()

def push_level(dVars, level):
    dVars['history'].append(level)

def current_level(dVars):
    return dVars['history'][-1]


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
    while iItemCount < 3:
        if type(lAllObjects[iIndex]) == parser.item:
            iItemCount += 1
        iIndex += 1
    else:
        if lAllObjects[iIndex-1].get_value().lower() == 'block':
            return True
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
