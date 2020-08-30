
from vsg import line

from vsg.vhdlFile.classify_new import blank
from vsg.vhdlFile.classify_new import whitespace
from vsg.vhdlFile.classify_new import comment
from vsg.vhdlFile.classify_new import architecture_body
from vsg.vhdlFile.classify_new import entity_declaration
from vsg.vhdlFile.classify_new import generate_statement
from vsg.vhdlFile.classify_new import block_statement
from vsg.vhdlFile.classify_new import concurrent_statement

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
        dVars['blue'] = False

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
            if not type(oObject) == parser.item:
                lNewObjects.append(oObject)
                continue

#            print('[' + ']['.join(dVars['history']) + ']')
            #print(oObject.get_value())

            if utils.is_current_level(dVars, 'design_unit'):
                if entity_declaration.check_for(oObject, lNewObjects, dVars):
                   utils.push_level(dVars, 'entity_declaration:begin_declaration')
                elif architecture_body.check_for(oObject, lNewObjects, dVars):
                   utils.push_level(dVars, 'architecture_body:begin_declaration')
                else:
                    lNewObjects.append(oObject)
                    continue

            ###################################################################
            # entity_declaration
            ###################################################################
            if utils.is_current_level(dVars, 'entity_declaration:begin_declaration'):
                if entity_declaration.classify_begin_declaration(oObject, lNewObjects, dVars):
                    continue
                else:
                    lNewObjects.append(oObject)
                    continue

            if utils.is_current_level(dVars, 'entity_header'):
                utils.pop_level(dVars)
                utils.push_level(dVars, 'entity_declarative_part')

            if utils.is_current_level(dVars, 'entity_declarative_part'):
                utils.pop_level(dVars)
                utils.push_level(dVars, 'entity_statement_part')

            if utils.is_current_level(dVars, 'entity_statement_part'):
                utils.pop_level(dVars)
                utils.push_level(dVars, 'entity_declaration:end_declaration')

            if utils.is_current_level(dVars, 'entity_declaration:end_declaration'):
                if entity_declaration.classify_end_declaration(oObject, lNewObjects, dVars):
                    continue            

            ###################################################################
            # architecture_body
            ###################################################################
            if utils.is_current_level(dVars, 'architecture_body:begin_declaration'):
                if architecture_body.classify_begin_declaration(oObject, lNewObjects, dVars):
                    continue

            if utils.is_current_level(dVars, 'architecture_declarative_part'):
                if oObject.get_value().lower() == 'begin':
                    lNewObjects.append(token.architecture_body.begin_keyword(oObject.get_value()))
                    utils.pop_level(dVars)
                    utils.push_level(dVars, 'architecture_statement_part')
                continue

            if utils.is_current_level(dVars, 'architecture_statement_part'):
                if concurrent_statement.is_it(iObject, oObject, lAllObjects, lNewObjects, dVars):
                    continue
                elif oObject.get_value().lower() == 'end':
                    utils.pop_level(dVars)
                    utils.push_level(dVars, 'architecture_body:end_declaration')
                else:
                    lNewObjects.append(oObject)
                    continue

            if utils.is_current_level(dVars, 'architecture_body:end_declaration'):
                if architecture_body.classify_end_declaration(oObject, lNewObjects, dVars):
                    continue


            ###################################################################
            # block_statement
            ###################################################################
            if utils.is_current_level(dVars, 'block_statement:begin_declaration'):
                if block_statement.tokenize_begin_declaration(iObject, oObject, lAllObjects, lNewObjects, dVars):
                    continue
                else:
                    lNewObjects.append(oObject)
                continue

            if utils.is_current_level(dVars, 'block_statement_part'):
                if concurrent_statement.is_it(iObject, oObject, lAllObjects, lNewObjects, dVars):
                    continue
                elif oObject.get_value().lower() == 'end':
                    lNewObjects.append(token.block_statement.end_keyword(oObject.get_value()))
                    utils.pop_level(dVars)
                else:
                    lNewObjects.append(oObject)
                continue

            if utils.is_current_level(dVars, 'block_statement:end_declaration'):
                block_statement.tokenize_end_declaration(iObject, oObject, lAllObjects, lNewObjects, dVars)               
                continue


            ###################################################################
            # for generate
            ###################################################################

            if utils.is_current_level(dVars, 'for_generate_statement:begin_declaration'):
                if generate_statement.tokenize(iObject, oObject, lAllObjects, lNewObjects, dVars):
                    continue
                else:
                    lNewObjects.append(oObject)
                continue

            if utils.is_current_level(dVars, 'generate_statement_body'):
                if concurrent_statement.is_it(iObject, oObject, lAllObjects, lNewObjects, dVars):
                    continue
                else:
                    utils.pop_level(dVars)

            if utils.is_current_level(dVars, 'for_generate_statement:end_declaration'):
                if generate_statement.tokenize(iObject, oObject, lAllObjects, lNewObjects, dVars):
                    continue
                else:
                    lNewObjects.append(token.for_generate_statement.end_generate_label(oObject.get_value()))
                continue

            ###################################################################
            # if generate
            ###################################################################

            if utils.is_current_level(dVars, 'if_generate_statement:begin_declaration'):
                if generate_statement.tokenize(iObject, oObject, lAllObjects, lNewObjects, dVars):
                    continue
                else:
                    lNewObjects.append(oObject)
                continue

            if utils.is_current_level(dVars, 'generate_statement_body'):
                if concurrent_statement.is_it(iObject, oObject, lAllObjects, lNewObjects, dVars):
                    continue
                else:
                    utils.pop_level(dVars)

            if utils.is_current_level(dVars, 'if_generate_statement:elsif_declaration'):
                if generate_statement.tokenize(iObject, oObject, lAllObjects, lNewObjects, dVars):
                    continue

            if utils.is_current_level(dVars, 'if_generate_statement:else_declaration'):
                if generate_statement.tokenize(iObject, oObject, lAllObjects, lNewObjects, dVars):
                    continue

            if utils.is_current_level(dVars, 'if_generate_statement:end_declaration'):
                if generate_statement.tokenize(iObject, oObject, lAllObjects, lNewObjects, dVars):
                    continue
                else:
                    lNewObjects.append(token.if_generate_statement.end_generate_label(oObject.get_value()))
                continue

#        for oObject in lNewObjects:
#            print(f'{oObject} | {oObject.get_value()}')

#        print('-'*80)

        for iLine, lLine in enumerate(split_on_carriage_return(lNewObjects)):
            self.lines[iLine + 1].objects = lLine
        


def split_on_carriage_return(lObjects):
    lReturn = []
    lMyObjects = []
    iLine = 1
    for oObject in lObjects:
        if type(oObject) == parser.carriage_return:
            lReturn.append(lMyObjects)
            iLine += 1
            lMyObjects = []
        else:
            lMyObjects.append(oObject)
    if len(lMyObjects) > 0:
        lReturn.append(lMyObjects)
    return lReturn


def is_whitespace(oObject, lNewObjects):
    if type(oObject) == parser.carriage_return:
        return True
    if type(oObject) == parser.blank_line:
        return True
    if type(oObject) == parser.comment:
        return True
    if type(oObject) == parser.whitespace:
        return True
    return False

