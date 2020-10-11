
from vsg import line
from vsg import parser
from vsg import token

from vsg.vhdlFile import classify

from vsg.vhdlFile import update
from vsg.vhdlFile import utils

from vsg.vhdlFile.classify import entity

from vsg.vhdlFile.classify_new import blank
from vsg.vhdlFile.classify_new import comment
from vsg.vhdlFile.classify_new import design_file
from vsg.vhdlFile.classify_new import whitespace

from vsg.vhdlFile.indent import loop_statement
from vsg.vhdlFile.indent import function_specification
from vsg.vhdlFile.indent import interface_element
from vsg.vhdlFile.indent import generate_statement
from vsg.vhdlFile.indent import generic_clause
from vsg.vhdlFile.indent import if_statement
from vsg.vhdlFile.indent import package_declaration


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
        self.hasArchitecture = False
        self.hasEntity = False
        self.lAllObjects = []
        self._processFile()
        self.filename = None

    def _processFile(self):

        self.lAllObjects = []

        dVars = {}
        dVars['fFoundProcessBegin'] = False
        dVars['SensitivityListFound'] = False
        dVars['fProcedureParameterEndDetected'] = False
        dVars['fProcedureIsDetected'] = False
        dVars['fProcedureBeginDetected'] = False
        dVars['fFunctionParameterEndDetected'] = False
        dVars['fFunctionIsDetected'] = False
        dVars['fFunctionBeginDetected'] = False
        dVars['fFunctionReturnTypeDetected'] = False
        dVars['iOpenParenthesis'] = 0
        dVars['iCloseParenthesis'] = 0
        dVars['iCurrentIndentLevel'] = 0
        dVars['iGenerateLevel'] = 0
        dVars['iIfLevel'] = 0
        dVars['fConstantArray'] = False
        dVars['iForLoopLevel'] = 0
        dVars['bFirstWhenSeen'] = False

        oLinePrevious = line.blank_line()

        for sLine in self.filecontent:
            oLine = line.line(sLine.replace('\t', '  ').rstrip())
            lTokens = oLine.get_zipped_tokens()
            lObjects = []
            for sToken in lTokens:
                lObjects.append(parser.item(sToken))

            blank.classify(lObjects, oLine)
            whitespace.classify(lTokens, lObjects)
            comment.classify(lTokens, lObjects)
            
            update.inside_attributes(dVars, self.lines[-1], oLine)

            classify.blank(oLine) # lTokens
#            classify.whitespace(lTokens, lObjects)
            classify.comment(dVars, lTokens, lObjects, oLine)


            classify.use(dVars, lTokens, lObjects, oLine)

            classify.entity.legacy(self, dVars, oLine)
            classify.assert_statement(self, dVars, lTokens, lObjects, oLine)

            classify.code_tags(dVars, oLine, oLinePrevious)

            classify.port(dVars, oLine)
            classify.generic(dVars, oLine) #lTokens

            classify.concurrent(dVars, oLine)
            classify.architecture(self, dVars, lTokens, lObjects, oLine)
            classify.package_body_old(dVars, oLine) # lTokens
            classify.block(self, dVars, oLine)
            classify.package(self, dVars, lTokens, lObjects, oLine)
            classify.component(dVars, lTokens, lObjects, oLine)
            classify.signal(self, dVars, oLine)
            classify.constant(self, dVars, lTokens, lObjects, oLine, oLinePrevious)
            classify.variable(self, dVars, lTokens, lObjects, oLine)
            classify.procedure(dVars, oLine, oLinePrevious)
            classify.process(dVars, oLine, self.lines)
            classify.generate(dVars, oLine, oLinePrevious)
            classify.attribute(dVars, lTokens, lObjects, oLine)
            classify.file_statement(dVars, lTokens, lObjects, oLine)

            classify.when(dVars, oLine, oLinePrevious)

            classify.with_statement(dVars, oLine)
            classify.for_loop(dVars, oLine)
            classify.while_loop(dVars, oLine)

            classify.if_statement(dVars, oLine)

            classify.case(self, dVars, oLine)
            classify.function(dVars, oLine)
            classify.type_definition_old(dVars, oLine)
            classify.subtype(dVars, oLine)

            classify.sequential(dVars, oLine)
            classify.variable_assignment(dVars, oLine)
            classify.wait(dVars, oLine)
            classify.after(dVars, oLine)

            # Check instantiation statements
            if oLine.insideArchitecture and not oLine.insideProcess and \
               not oLine.isConcurrentBegin and \
               not oLine.insideComponent and \
               not oLine.isGenerateKeyword and \
               not oLine.insideFunction and \
               not oLine.insideProcedure:
                classify.instantiation(dVars, oLine)

            # Add line to file
            self.lines.append(oLine)

            self.lAllObjects.extend(lObjects)
            self.lAllObjects.append(parser.carriage_return())

            oLinePrevious = oLine
            oLine.objects = lObjects

        design_file.tokenize(self.lAllObjects)

        for iLine, lLine in enumerate(split_on_carriage_return(self.lAllObjects)):
            self.lines[iLine + 1].objects = lLine
        self.set_indent_levels()
        self.set_token_indent()

    def update(self, lUpdates):
#        print('--> Update' + 80*'-')
        if len(lUpdates) == 0:
            return
        for oUpdate in lUpdates[::-1]:
#            print(self.lAllObjects)
            iStart = oUpdate.oTokens.iStartIndex
            lTokens = oUpdate.get_tokens()
            iEnd = oUpdate.oTokens.iEndIndex
#            print(f'{iStart} | {iEnd}') 
            self.lAllObjects[iStart:iEnd] = lTokens
#            print(self.lAllObjects)
#        print(self.lAllObjects)
        for iLine, lLine in enumerate(split_on_carriage_return(self.lAllObjects)):
#            print(lLine)
#            print(lLine)
            try:
                self.lines[iLine + 1].update_objects(lLine)
            except IndexError:
                oLine = line.line(' ')
                oLine.update_objects(lLine)
                self.lines.append(oLine)
        if iLine < len(self.lines):
            self.lines = self.lines[:iLine + 2]             
            

    def update_filecontent(self):
        self.filecontent = []
        for oLine in self.lines[1:]:
            self.filecontent.append(oLine.line)
        self.lines = [line.line('')]

    def get_lines(self):
        return self.lines

    def get_line(self, iLineNumber):
        return self.lines[iLineNumber]

    def insert_line(self, iLineNumber, oLine):
        self.lines.insert(iLineNumber, oLine)

    def remove_line(self, iLineNumber):
        self.lines.pop(iLineNumber)

    def get_lines_starting_with_item_or_whitespace_and_then_item(self, parserType):
        lReturn = []

        for iLine, oLine in enumerate(self.lines):
            if _does_line_start_with_item_or_whitespace_and_then_item(oLine, parserType):
                dEntry = _create_empty_return_dictionary()
                dEntry['metadata']['iStartLineNumber'] = iLine
                dEntry['metadata']['iEndLineNumber'] = iLine
                dEntry['lines'].append(oLine)
                lReturn.append(dEntry)

        return lReturn

    def convert_whitespace_only_lines_to_blank_lines(self):
        print('Entering convert_whitespace_only_lines_to_blank_lines')
        for iLine, oLine in enumerate(self.lines):
            print(f'[{oLine.line}]')
            if oLine.line.isspace() or oLine.line == '':
                print('Got Here')
                self.lines.pop(iLine)
                self.lines.insert(iLine, line.blank_line())
            
    def get_region_bounded_by_items(self, beginItem, endItem):
        lReturn = []
        dRegion = {}
        dRegion['metadata'] = {}
        dRegion['metadata']['iStartLineNumber'] = 0
        dRegion['metadata']['iEndLineNumber'] = 0
        dRegion['lines'] = []
        bRegionBeginFound = False
        bRegionEndFound = False
        for iLine, oLine in enumerate(self.lines):
            for oObject in oLine.objects:
                if isinstance(oObject, beginItem):
                    bRegionBeginFound = True
                    dRegion['metadata']['iStartLineNumber'] = iLine
                if isinstance(oObject, endItem):   
                    bRegionEndFound = True
                    dRegion['metadata']['iEndLineNumber'] = iLine
            if bRegionBeginFound:
                dRegion['lines'].append(oLine)
            if bRegionEndFound:
                lReturn.append(dRegion)
                dRegion = {}
                dRegion['metadata'] = {}
                dRegion['metadata']['iStartLineNumber'] = 0
                dRegion['metadata']['iEndLineNumber'] = 0
                dRegion['lines'] = []
                bRegionBeginFound = False
                bRegionEndFound = False
        return lReturn

    def set_indent_levels(self):
        '''
        Set the appropriate indent level for lines using item objects.
        '''
        dIndent = {}
        dIndent['insideContextDeclaration'] = False
        dIndent['level'] = 0
        for oLine in self.lines:

            if len(oLine.objects) == 0:
                continue

            if _does_line_start_with_item_or_whitespace_and_then_item(oLine, token.context_declaration.context_keyword):
                oLine.indentLevel = 0
                dIndent['insideContextDeclaration'] = True
            if _does_line_start_with_item_or_whitespace_and_then_item(oLine, token.context_declaration.end_keyword):
                oLine.indentLevel = 0
                dIndent['insideContextDeclaration'] = False
            if _does_line_start_with_item_or_whitespace_and_then_item(oLine, token.context_reference.keyword):
                if dIndent['insideContextDeclaration']:
                    oLine.indentLevel = 2
                else:
                    oLine.indentLevel = 1
            if _does_line_start_with_item_or_whitespace_and_then_item(oLine, token.library_clause.keyword):
                if dIndent['insideContextDeclaration']:
                    oLine.indentLevel = 1
                else:
                    oLine.indentLevel = 0
            if _does_line_start_with_item_or_whitespace_and_then_item(oLine, token.use_clause.keyword):
                if dIndent['insideContextDeclaration']:
                    oLine.indentLevel = 2
                else:
                    oLine.indentLevel = 1

            if _does_line_start_with_item_or_whitespace_and_then_item(oLine, token.architecture_body.architecture_keyword):
                dIndent['level'] = 1
                oLine.indentLevel = 0

            if _does_line_start_with_item_or_whitespace_and_then_item(oLine, token.architecture_body.begin_keyword):
                dIndent['level'] = 1
                oLine.indentLevel = 0

            if _does_line_start_with_item_or_whitespace_and_then_item(oLine, token.architecture_body.end_keyword):
                dIndent['level'] = 0
                oLine.indentLevel = 0

            if _does_line_start_with_item_or_whitespace_and_then_item(oLine, token.constant_declaration.assignment_operator):
                if type(oLine.objects[0]) == token.constant_declaration.assignment_operator:
                    if oLine.objects[0].get_value() == '(':
                        oLine.indentLevel = dIndent['level']
                        dIndent['level'] += 1
                    elif oLine.objects[0].get_value() == ')':
                        dIndent['level'] -= 1
                        oLine.indentLevel = dIndent['level']
                    else:
                        oLine.indentLevel = dIndent['level']
                else:
                    oObject = oLine.objects[1]
                    sValue = oObject.get_value()
                    if oLine.objects[1].get_value() == '(':
                        oLine.indentLevel = dIndent['level']
                        dIndent['level'] += 1
                    elif oLine.objects[1].get_value() == ')':
                        dIndent['level'] -= 1
                        oLine.indentLevel = dIndent['level']
                    else:
                        oLine.indentLevel = dIndent['level']

    def set_token_indent(self):
        '''
        Set the indent level of tokens.
        '''
        iIndent = 0
        bCarriageReturnFound = False
        iTokenCount = 0
        vLabelFound = False
        bLabelFound = False
        bLibraryFound = False 
        for oToken in self.lAllObjects:

            if isinstance(oToken, parser.whitespace):
                continue

            if isinstance(oToken, parser.blank_line):
                bLibraryFound = False 
                continue

            if isinstance(oToken, parser.carriage_return):
                continue

            if isinstance(oToken, token.context_declaration.context_keyword):
                oToken.set_indent(0)
                iIndent += 1 

            if isinstance(oToken, token.context_declaration.end_keyword):
                oToken.set_indent(0)
                iIndent -= 1

            if isinstance(oToken, token.library_clause.keyword):
                 oToken.set_indent(iIndent)
                 bLibraryFound = True
                 continue

            if isinstance(oToken, token.use_clause.keyword):
                 oToken.set_indent(iIndent + 1)
                 continue
            

            if isinstance(oToken, token.context_reference.keyword):
                 if bLibraryFound:
                     oToken.set_indent(iIndent + 1)
                 else:
                     oToken.set_indent(iIndent)
                 continue 

            if isinstance(oToken, token.entity_declaration.entity_keyword):
                oToken.set_indent(iIndent)
                iIndent += 1

            if isinstance(oToken, token.entity_declaration.end_keyword):
                iIndent -= 1
                oToken.set_indent(iIndent)

            if isinstance(oToken, token.architecture_body.architecture_keyword):
                oToken.set_indent(0)
                iIndent = 1 

            if isinstance(oToken, token.architecture_body.begin_keyword):
                oToken.set_indent(0)
                iIndent = 1

            if isinstance(oToken, token.architecture_body.end_keyword):
                oToken.set_indent(0)
                iIndent = 0 

            ###  Assertion statements

            if isinstance(oToken, token.concurrent_assertion_statement.label_name):
                oToken.set_indent(iIndent)
                bLabelFound = True
                iIndent += 1

            if isinstance(oToken, token.assertion_statement.label):
                oToken.set_indent(iIndent)
                bLabelFound = True
                iIndent += 1

            if isinstance(oToken, token.assertion.keyword):
                if not bLabelFound:
                  oToken.set_indent(iIndent)
                  iIndent += 1
                bLabelFound = False
                    
            if isinstance(oToken, token.assertion.report_keyword):
               oToken.set_indent(iIndent)
                    
            if isinstance(oToken, token.assertion.severity_keyword):
               oToken.set_indent(iIndent)

            if isinstance(oToken, token.assertion_statement.semicolon):
                iIndent -= 1

            if isinstance(oToken, token.concurrent_assertion_statement.semicolon):
                iIndent -= 1

            ### Attribute statements
            if isinstance(oToken, token.attribute_declaration.attribute_keyword):
               oToken.set_indent(iIndent)
          
            if isinstance(oToken, token.attribute_specification.attribute_keyword):
               oToken.set_indent(iIndent)

            ### case statements
            if isinstance(oToken, token.case_statement.case_label):
                oToken.set_indent(iIndent)
                bLabelFound = True
                iIndent += 1

            if isinstance(oToken, token.case_statement.case_keyword):
                if not bLabelFound:
                  oToken.set_indent(iIndent)
                  iIndent += 2
                bLabelFound = False
                    
            if isinstance(oToken, token.case_statement_alternative.when_keyword):
                oToken.set_indent(iIndent - 1)

            if isinstance(oToken, token.case_statement.end_keyword):
                oToken.set_indent(iIndent - 2)
                iIndent -= 2

            ### process statements
            if isinstance(oToken, token.process_statement.process_label):
                oToken.set_indent(iIndent)
                bLabelFound = True
                iIndent += 1

            if isinstance(oToken, token.process_statement.postponed_keyword):
                if not bLabelFound:
                  oToken.set_indent(iIndent)
                  iIndent += 1
                  bLabelFound = True
                else:
                  oToken.set_indent(iIndent - 1)

            if isinstance(oToken, token.process_statement.process_keyword):
                if not bLabelFound:
                  oToken.set_indent(iIndent)
                  iIndent += 1
                else:
                  oToken.set_indent(iIndent - 1)
                bLabelFound = False
                    
            if isinstance(oToken, token.process_statement.begin_keyword):
                oToken.set_indent(iIndent - 1)

            if isinstance(oToken, token.process_statement.end_keyword):
                oToken.set_indent(iIndent - 1)
                iIndent -= 1
           
            ### Null statements
            if isinstance(oToken, token.null_statement.label):
                oToken.set_indent(iIndent)

            if isinstance(oToken, token.null_statement.null_keyword):
                oToken.set_indent(iIndent)
                    
            ### Comments 
            if isinstance(oToken, parser.comment):
                oToken.set_indent(iIndent)
                    
            ### Components
            if isinstance(oToken, token.component_declaration.component_keyword):
                oToken.set_indent(iIndent)
                iIndent += 1
            if isinstance(oToken, token.component_declaration.end_keyword):
                iIndent -= 1
                oToken.set_indent(iIndent)

            ### Concurrent signal assignment
            if isinstance(oToken, token.concurrent_signal_assignment_statement.label_name):
                oToken.set_indent(iIndent)

            if isinstance(oToken, token.concurrent_signal_assignment_statement.postponed_keyword):
                oToken.set_indent(iIndent)

            if isinstance(oToken, token.concurrent_simple_signal_assignment.target):
                oToken.set_indent(iIndent)
           
            if isinstance(oToken, token.concurrent_conditional_signal_assignment.target):
                oToken.set_indent(iIndent)
           
            if isinstance(oToken, token.concurrent_selected_signal_assignment.with_keyword):
                oToken.set_indent(iIndent)
           
            ### Constant declaration 
            if isinstance(oToken, token.constant_declaration.constant_keyword):
                oToken.set_indent(iIndent)

            ### File declaration 
            if isinstance(oToken, token.file_declaration.file_keyword):
                oToken.set_indent(iIndent)

            if isinstance(oToken, token.file_open_information.open_keyword):
                oToken.set_indent(iIndent + 1)

            if isinstance(oToken, token.file_open_information.is_keyword):
                oToken.set_indent(iIndent + 1)

            iIndent, bLabelFound = loop_statement.set_indent(iIndent, bLabelFound, oToken)
            iIndent, bLabelFound = function_specification.set_indent(iIndent, bLabelFound, oToken)
            iIndent, bLabelFound = interface_element.set_indent(iIndent, bLabelFound, oToken)
            iIndent, bLabelFound = generate_statement.set_indent(iIndent, bLabelFound, oToken)
            iIndent, bLabelFound = generic_clause.set_indent(iIndent, bLabelFound, oToken)
            iIndent, bLabelFound = if_statement.set_indent(iIndent, bLabelFound, oToken)
            iIndent, bLabelFound = package_declaration.set_indent(iIndent, bLabelFound, oToken)
  
    def print_debug(self):
        for oLine in self.lines:
            print(f'{oLine.indentLevel} | {oLine.line}')
        

    def get_sequence_of_tokens_matching(self, lTokens):
        iLine = 1
        lTemp = []
        lReturn = []
        iMatchCount = 0
        iMatchLength = len(lTokens)
        iStart = 0
        for iIndex in range(0, len(self.lAllObjects)):

            if isinstance(self.lAllObjects[iIndex], lTokens[iMatchCount]):
                if iMatchCount == 0:
                    iStart = iIndex
                lTemp.append(self.lAllObjects[iIndex])
                iMatchCount +=1
                if iMatchCount == iMatchLength:
                    lReturn.append(Tokens(iStart, iLine, lTemp))
                    lTemp = []
                    iMatchCount = 0
            elif iMatchCount > 0:
                lTemp = []
                iMatchCount = 0

            if isinstance(self.lAllObjects[iIndex], parser.carriage_return):
                iLine +=1

        return lReturn

    def get_sequence_of_tokens_matching_bounded_by_tokens(self, lTokens, oStart, oEnd):
        iLine = 1
        lTemp = []
        lReturn = []
        iMatchCount = 0
        iMatchLength = len(lTokens)
        iStart = 0
        bCheck = False
        for iIndex in range(0, len(self.lAllObjects)):

            if isinstance(self.lAllObjects[iIndex], oStart):
                bCheck = True
                lTemp = []
                iMatchCount = 0
            if isinstance(self.lAllObjects[iIndex], oEnd):
                bCheck = False
                lTemp = []
                iMatchCount = 0

            if bCheck:
                if isinstance(self.lAllObjects[iIndex], lTokens[iMatchCount]):
                    if iMatchCount == 0:
                        iStart = iIndex
                    lTemp.append(self.lAllObjects[iIndex])
                    iMatchCount +=1
                    if iMatchCount == iMatchLength:
                        lReturn.append(Tokens(iStart, iLine, lTemp))
                        lTemp = []
                        iMatchCount = 0
                elif iMatchCount > 0:
                    lTemp = []
                    iMatchCount = 0

            if isinstance(self.lAllObjects[iIndex], parser.carriage_return):
                iLine +=1

        return lReturn

    def get_tokens_matching(self, lTokens):
        iLine = 1
        lReturn = []
        for iIndex in range(0, len(self.lAllObjects)):
            for oToken in lTokens:
                if isinstance(self.lAllObjects[iIndex], oToken):
                    lReturn.append(Tokens(iIndex, iLine, [self.lAllObjects[iIndex]]))

            if isinstance(self.lAllObjects[iIndex], parser.carriage_return):
                iLine +=1

        return lReturn

    def get_tokens_matching_in_range_bounded_by_tokens(self, lTokens, oStart, oEnd):
        iLine = 1
        lReturn = []
        bSearch = False
        for iIndex in range(0, len(self.lAllObjects)):
            if isinstance(self.lAllObjects[iIndex], oStart):
                bSearch = True
            if isinstance(self.lAllObjects[iIndex], oEnd):
                bSearch = False 
            if bSearch:
                for oToken in lTokens:
                    if isinstance(self.lAllObjects[iIndex], oToken):
                        lReturn.append(Tokens(iIndex, iLine, [self.lAllObjects[iIndex]]))

            if isinstance(self.lAllObjects[iIndex], parser.carriage_return):
                iLine +=1

        return lReturn

    def get_tokens_bounded_by(self, oLeft, oRight, include_trailing_whitespace=False):
        iLine = 1
        lTemp = []
        lReturn = []
        bStore = False
        bRightFound = False
        for iIndex in range(0, len(self.lAllObjects)):
            if isinstance(self.lAllObjects[iIndex], oLeft):
                bStore = True
                iStart = iIndex
                iStartLine = iLine
            if bStore:
                lTemp.append(self.lAllObjects[iIndex])
            if bRightFound:
                if isinstance(self.lAllObjects[iIndex], parser.whitespace):
                    lReturn.append(Tokens(iStart, iStartLine, lTemp))
                else:
                    lReturn.append(Tokens(iStart, iStartLine, lTemp[:-1]))
                bRightFound = False
                lTemp = []
                bStore = False
            if isinstance(self.lAllObjects[iIndex], oRight) and bStore:
                if not include_trailing_whitespace:
                    lReturn.append(Tokens(iStart, iStartLine, lTemp))
                    lTemp = []
                    bStore = False
                else:
                    bRightFound = True

            if isinstance(self.lAllObjects[iIndex], parser.carriage_return):
                iLine +=1

        return lReturn

    def get_tokens_bounded_by_token_when_between_tokens(self, oLeft, oRight, oStart, oEnd, include_trailing_whitespace=False):
        iLine = 1
        lTemp = []
        lReturn = []
        bStore = False
        bRightFound = False
        bSearch = False
        for iIndex in range(0, len(self.lAllObjects)):

            if isinstance(self.lAllObjects[iIndex], oStart):
                bSearch = True
            if isinstance(self.lAllObjects[iIndex], oEnd):
                bSearch = False

            if bSearch:
                if isinstance(self.lAllObjects[iIndex], oLeft):
                    bStore = True
                    iStart = iIndex
                    iStartLine = iLine
                if bStore:
                    lTemp.append(self.lAllObjects[iIndex])
                if bRightFound:
                    if isinstance(self.lAllObjects[iIndex], parser.whitespace):
                        lReturn.append(Tokens(iStart, iStartLine, lTemp))
                    else:
                        lReturn.append(Tokens(iStart, iStartLine, lTemp[:-1]))
                    bRightFound = False
                    lTemp = []
                    bStore = False
                if isinstance(self.lAllObjects[iIndex], oRight) and bStore:
                    if not include_trailing_whitespace:
                        lReturn.append(Tokens(iStart, iStartLine, lTemp))
                        lTemp = []
                        bStore = False
                    else:
                        bRightFound = True

            if isinstance(self.lAllObjects[iIndex], parser.carriage_return):
                iLine +=1

        return lReturn


    def get_tokens_at_beginning_of_line_matching(self, lTokens):
        iLine = 1
        lReturn = []
        for iIndex in range(0, len(self.lAllObjects)):
            if isinstance(self.lAllObjects[iIndex], parser.carriage_return):
                iLine +=1
                iStart = iIndex + 1
                for oToken in lTokens:
                    if utils.are_next_consecutive_token_types([parser.whitespace, oToken], iStart, self.lAllObjects):
                        lReturn.append(Tokens(iStart, iLine, self.lAllObjects[iStart:iStart + 2]))
                    elif utils.are_next_consecutive_token_types([oToken], iStart, self.lAllObjects):
                        lReturn.append(Tokens(iStart, iLine, [self.lAllObjects[iStart]]))

        return lReturn                    

    def get_line_above_line_starting_with_token(self, lTokens):
        lReturn = []
        iLine = 1
        lPreviousLine = []
        iPrevious = 0
        lCurrentLine = []
        iCurrent = 0
        for iIndex in range(0, len(self.lAllObjects)):

            if isinstance(self.lAllObjects[iIndex], parser.carriage_return):
                iLine +=1
                lPreviousLine = lCurrentLine.copy()
                iPrevious = iCurrent
                lCurrentLine = []
                iCurrent = iIndex + 1
                for oToken in lTokens:
                    if utils.are_next_consecutive_token_types([parser.whitespace, oToken], iCurrent, self.lAllObjects):
                        lReturn.append(Tokens(iPrevious, iLine, lPreviousLine))
                        break
                    if utils.are_next_consecutive_token_types([oToken], iCurrent, self.lAllObjects):
                        lReturn.append(Tokens(iPrevious, iLine, lPreviousLine))
                        break
            else:
                lCurrentLine.append(self.lAllObjects[iIndex])

        return lReturn                    

    def get_line_below_line_ending_with_token(self, lTokens):
        lReturn = []
        iLine = 1
        lCurrentLine = []
        lTemp = []
        bTokenFound = False
        bCrFound = False
        for iIndex in range(0, len(self.lAllObjects)):

            if not bTokenFound:
                for oToken in lTokens:
                    if isinstance(self.lAllObjects[iIndex], oToken):
                        if utils.are_next_consecutive_token_types([parser.carriage_return], iIndex + 1, self.lAllObjects):
                            bTokenFound = True
                            break
                        if utils.are_next_consecutive_token_types([parser.whitespace, parser.carriage_return], iIndex + 1, self.lAllObjects):
                            bTokenFound = True
                            break
                        if utils.are_next_consecutive_token_types([parser.whitespace, parser.comment, parser.carriage_return], iIndex + 1, self.lAllObjects):
                            bTokenFound = True
                            break
                        if utils.are_next_consecutive_token_types([parser.comment, parser.carriage_return], iIndex + 1, self.lAllObjects):
                            bTokenFound = True
                            break


            if bCrFound:
                lTemp.append(self.lAllObjects[iIndex])

            if isinstance(self.lAllObjects[iIndex], parser.carriage_return):
                if bCrFound:
                    lTemp.pop()
                    lReturn.append(Tokens(iStart, iLine, lTemp))
                    lTemp = []
                    bCrFound = False
                    bTokenFound = False
                elif bTokenFound:
                    bCrFound = True
                    iStart = iIndex + 1

                iLine +=1

        return lReturn                    

    def get_sequence_of_tokens_not_matching(self, lTokens):
        iLine = 1
        lTemp = []
        lReturn = []
        iMatchCount = 0
        iMatchLength = len(lTokens)
        iStart = 0
        iEnd = len(lTokens)
        for iIndex in range(0, len(self.lAllObjects)):
            if iMatchCount != 0:
                if type(self.lAllObjects[iIndex]) == lTokens[iMatchCount]:
                    iMatchCount += 1
                else:
                    lReturn.append(Tokens(iStart, iLine, lTemp))
                    lTemp = []
                    iMatchCount = 0
                if iMatchCount == iEnd:
                    lTemp = []
                    iMatchCount = 0
            if iMatchCount == 0:
                if isinstance(self.lAllObjects[iIndex], lTokens[0]):
                    iStart = iIndex
                    lTemp.append(self.lAllObjects[iIndex])
                    iMatchCount += 1

            if isinstance(self.lAllObjects[iIndex], parser.carriage_return):
                iLine +=1

        return lReturn

    def get_tokens_between_tokens_inclusive_while_storing_value_from_token(self, left_token, right_token, value_token ):
        iLine = 1
        lTemp = []
        lReturn = []
        iStart = 0
        sValue = None
        bStore = False
        for iIndex in range(0, len(self.lAllObjects)):

            if isinstance(self.lAllObjects[iIndex], left_token):
                bStore = True
                iStart = iIndex
                iLineNumber = iLine

            if bStore:
                lTemp.append(self.lAllObjects[iIndex])

            if isinstance(self.lAllObjects[iIndex], value_token):
                sValue = self.lAllObjects[iIndex].get_value()

            if isinstance(self.lAllObjects[iIndex], right_token):
                oTokens = Tokens(iStart, iLineNumber, lTemp)
                oTokens.set_token_value(sValue)
                lReturn.append(oTokens)
                lTemp = []
                bStore = False
                sValue = None

            if isinstance(self.lAllObjects[iIndex], parser.carriage_return):
                iLine +=1

        return lReturn

    def get_tokens_from_line(self, iLineNumber):
        iLine = 1
        lTemp = []
        iStart = 0
        bStore = False
        for iIndex in range(0, len(self.lAllObjects)):

            if bStore:
                lTemp.append(self.lAllObjects[iIndex])

            if isinstance(self.lAllObjects[iIndex], parser.carriage_return):
                iLine +=1
                if iLine == iLineNumber:
                    bStore = True
                    iStart = iIndex + 1
                if iLine == iLineNumber + 1:
                    return(Tokens(iStart, iLineNumber, lTemp))


    def get_consecutive_lines_starting_with_token_and_stopping_when_token_starting_line_is_found(self, search_token, stop_token):
        iLine = 1
        lTemp = []
        lReturn = []
        iStart = 0
        bStore = False
        bStop = False
        iLineNumber = None
        for iIndex in range(0, len(self.lAllObjects)):

            if bStore:
                lTemp.append(self.lAllObjects[iIndex])

            if bStop and isinstance(self.lAllObjects[iIndex], stop_token):
                oTokens = Tokens(iStart, iLineNumber, lTemp)
                lReturn.append(oTokens)
                bStore = False
                lTemp = []
                bStop = False

            if isinstance(self.lAllObjects[iIndex], parser.carriage_return):
                iLine +=1
                if not bStore:
                    if utils.are_next_consecutive_token_types([parser.whitespace, search_token], iIndex + 1, self.lAllObjects) or \
                       utils.are_next_consecutive_token_types([search_token], iIndex + 1, self.lAllObjects):
                           iStart = iIndex + 1
                           bStore = True
                           iLineNumber = iLine
                else:
                    if not utils.are_next_consecutive_token_types([parser.whitespace, search_token], iIndex + 1, self.lAllObjects) and \
                       not utils.are_next_consecutive_token_types([search_token], iIndex + 1, self.lAllObjects) and \
                       not utils.are_next_consecutive_token_types([parser.whitespace, stop_token], iIndex + 1, self.lAllObjects) and \
                       not utils.are_next_consecutive_token_types([stop_token], iIndex + 1, self.lAllObjects):
                           bStore = False
                           lTemp = []
                    if utils.are_next_consecutive_token_types([parser.whitespace, stop_token], iIndex + 1, self.lAllObjects) or \
                       utils.are_next_consecutive_token_types([stop_token], iIndex + 1, self.lAllObjects):
                        bStop = True
                       
        return lReturn

    def get_tokens_where_line_starts_with_token_until_ending_token_is_found(self, start_token, stop_token):
        iLine = 1
        lTemp = []
        lReturn = []
        iStart = 0
        bStore = False
        iLineNumber = None
        for iIndex in range(0, len(self.lAllObjects)):

            if bStore:
                lTemp.append(self.lAllObjects[iIndex])

            if isinstance(self.lAllObjects[iIndex], stop_token):
                oTokens = Tokens(iStart, iLineNumber, lTemp)
                lReturn.append(oTokens)
                bStore = False
                lTemp = []

            if isinstance(self.lAllObjects[iIndex], parser.carriage_return):
                iLine +=1
                if not bStore:
                    if utils.are_next_consecutive_token_types([parser.whitespace, start_token], iIndex + 1, self.lAllObjects) or \
                       utils.are_next_consecutive_token_types([start_token], iIndex + 1, self.lAllObjects):
                           iStart = iIndex + 1
                           bStore = True
                           iLineNumber = iLine
                       
        return lReturn


    def get_token_and_n_tokens_before_it(self, oToken, iTokens):
        iLine = 1
        lReturn = []
        iStart = 0
        for iIndex in range(0, len(self.lAllObjects)):
            if isinstance(self.lAllObjects[iIndex], oToken):
                iStart = iIndex - iTokens
                lReturn.append(Tokens(iStart, iLine, self.lAllObjects[iIndex - iTokens:iIndex + 1]))

            if isinstance(self.lAllObjects[iIndex], parser.carriage_return):
                iLine +=1

        return lReturn

    def get_token_and_n_tokens_before_it_in_between_tokens(self, lTokens, iTokens, oStart, oEnd):
        iLine = 1
        lReturn = []
        iStart = 0
        bSearch = False
        for iIndex in range(0, len(self.lAllObjects)):

            if isinstance(self.lAllObjects[iIndex], oStart):
                bSearch = True
            if isinstance(self.lAllObjects[iIndex], oEnd):
                bSearch = False

            if bSearch:
                for oToken in lTokens:
                    if isinstance(self.lAllObjects[iIndex], oToken):
                        iStart = iIndex - iTokens
                        lReturn.append(Tokens(iStart, iLine, self.lAllObjects[iIndex - iTokens:iIndex + 1]))
                        break

            if isinstance(self.lAllObjects[iIndex], parser.carriage_return):
                iLine +=1

        return lReturn

    def get_token_and_n_tokens_after_it(self, lTokens, iTokens):
        iLine = 1
        lReturn = []
        for iIndex in range(0, len(self.lAllObjects)):
            for oToken in lTokens:
                if isinstance(self.lAllObjects[iIndex], oToken):
                    lReturn.append(Tokens(iIndex, iLine, self.lAllObjects[iIndex:iTokens + iIndex + 1]))

            if isinstance(self.lAllObjects[iIndex], parser.carriage_return):
                iLine +=1

        return lReturn

    def get_token_and_n_tokens_after_it_when_between_tokens(self, lTokens, iTokens, oStart, oEnd):
        iLine = 1
        lReturn = []
        bSearch = False
        for iIndex in range(0, len(self.lAllObjects)):

            if isinstance(self.lAllObjects[iIndex], oStart):
                bSearch = True
            if isinstance(self.lAllObjects[iIndex], oEnd):
                bSearch = False

            if bSearch:
                for oToken in lTokens:
                    if isinstance(self.lAllObjects[iIndex], oToken):
                        lReturn.append(Tokens(iIndex, iLine, self.lAllObjects[iIndex:iTokens + iIndex + 1]))

            if isinstance(self.lAllObjects[iIndex], parser.carriage_return):
                iLine +=1

        return lReturn

    def get_blank_lines_below_line_ending_with_token(self, lTokens):
        lReturn = []
        iLine = 1
        lCurrentLine = []
        lTemp = []
        bTokenFound = False
        bCrFound = False
        for iIndex in range(0, len(self.lAllObjects)):

            if not bTokenFound:
                for oToken in lTokens:
                    if isinstance(self.lAllObjects[iIndex], oToken):
                        if utils.are_next_consecutive_token_types([parser.carriage_return], iIndex + 1, self.lAllObjects):
                            bTokenFound = True
                            iLineNumber = iLine
                            break
                        if utils.are_next_consecutive_token_types([parser.whitespace, parser.carriage_return], iIndex + 1, self.lAllObjects):
                            bTokenFound = True
                            iLineNumber = iLine
                            break
                        if utils.are_next_consecutive_token_types([parser.whitespace, parser.comment, parser.carriage_return], iIndex + 1, self.lAllObjects):
                            bTokenFound = True
                            iLineNumber = iLine
                            break
                        if utils.are_next_consecutive_token_types([parser.comment, parser.carriage_return], iIndex + 1, self.lAllObjects):
                            bTokenFound = True
                            iLineNumber = iLine
                            break


            if bCrFound:
                lTemp.append(self.lAllObjects[iIndex])

            if isinstance(self.lAllObjects[iIndex], parser.carriage_return):
                if not utils.are_next_consecutive_token_types([parser.blank_line, parser.carriage_return], iIndex + 1, self.lAllObjects):
                    if len(lTemp) > 2:
                        lReturn.append(Tokens(iStart, iLineNumber, lTemp))
                    elif len(lTemp) == 2:
                        lReturn.append(Tokens(iStart, iLineNumber, lTemp))


                    lTemp = []
                    bCrFound = False
                    bTokenFound = False

                elif bTokenFound and not bCrFound:
                    bCrFound = True
                    iStart = iIndex + 1

                iLine +=1

        return lReturn                    


    def get_blank_lines_above_line_starting_with_token(self, lTokens):
        lReturn = []
        iLine = 1
        bStore = False
        lTemp = []
        for iIndex in range(0, len(self.lAllObjects)):

            if isinstance(self.lAllObjects[iIndex], parser.blank_line):
                if not bStore:
                    iStart = iIndex
                bStore = True

            if bStore:
                lTemp.append(self.lAllObjects[iIndex])

            if isinstance(self.lAllObjects[iIndex], parser.carriage_return):
                iLine +=1
                iCurrent = iIndex + 1
                for oToken in lTokens:
                    if utils.are_next_consecutive_token_types([parser.whitespace, oToken], iCurrent, self.lAllObjects):
                        lReturn.append(Tokens(iStart, iLine, lTemp))
                        break
                    if utils.are_next_consecutive_token_types([oToken], iCurrent, self.lAllObjects):
                        lReturn.append(Tokens(iStart, iLine, lTemp))
                        break
             
                if not utils.are_next_consecutive_token_types([parser.blank_line, parser.carriage_return], iCurrent, self.lAllObjects):
                    bStore = False
                    lTemp = []

        return lReturn                    

    def get_association_elements_between_tokens(self, oStart, oEnd):
        iLine = 1
        lReturn = []
        bSearch = False
        bStore = False
        lTemp = []
        iLineNumber = None
        for iIndex in range(0, len(self.lAllObjects)):
            if isinstance(self.lAllObjects[iIndex], oStart):
                bSearch = True
            if isinstance(self.lAllObjects[iIndex], oEnd):
                bSearch = False 
                bStore = False
                if len(lTemp) > 0:
                    lReturn.append(Tokens(iStart, iLineNumber, lTemp))
                lTemp = []

            if bSearch:
                oToken = self.lAllObjects[iIndex]
                if isinstance(oToken, token.association_element.formal_part):
                    bStore = True
                    iStart = iIndex
                    iLineNumber = iLine
                if isinstance(oToken, token.association_element.actual_part) and not bStore:
                    bStore = True
                    iStart = iIndex
                    iLineNumber = iLine
                
                if isinstance(oToken, token.association_list.comma):
                    lReturn.append(Tokens(iStart, iLineNumber, lTemp))
                    lTemp = []
                    bStore = False

                if bStore:
                   lTemp.append(self.lAllObjects[iIndex])

            if isinstance(self.lAllObjects[iIndex], parser.carriage_return):
                iLine +=1

        return lReturn

    def get_lines_with_length_that_exceed_column(self, iColumn):
        iLine = 1
        lReturn = []
        lTemp = []
        bFirstTokenInLine = True
        for iIndex in range(0, len(self.lAllObjects)):

            if isinstance(self.lAllObjects[iIndex], parser.carriage_return):
                if utils.does_length_of_tokens_exceed(lTemp, iColumn):
                    lReturn.append(Tokens(iStart, iLine, lTemp))
                iLine +=1
                lTemp = []
                bFirstTokenInLine = True
                continue

            lTemp.append(self.lAllObjects[iIndex])
            if bFirstTokenInLine:
                iStart = iIndex
                bFirstTokenInLine

        return lReturn


def _create_empty_return_dictionary():
    dReturn = {}
    dReturn['metadata'] = {}
    dReturn['metadata']['iStartLineNumber'] = 0
    dReturn['metadata']['iEndLineNumber'] = 0
    dReturn['lines'] = []
    return dReturn


def _does_line_start_with_item_or_whitespace_and_then_item(oLine, parserType):
    if isinstance(oLine.get_object(0), parserType):
        return True
    if isinstance(oLine.get_object(0), parser.whitespace) and isinstance(oLine.get_object(1), parserType):
        return True
    return False


def is_whitespace(oObject):
    if type(oObject) == parser.carriage_return:
        return True
    if type(oObject) == parser.blank_line:
        return True
    if type(oObject) == parser.comment:
        return True
    if type(oObject) == parser.whitespace:
        return True
    return False

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


class Tokens():

    def __init__(self, iStartIndex, iLine, lTokens):

        self.iStartIndex = iStartIndex
        self.lTokens = lTokens
        self.iLine = iLine
        self.iEndIndex = iStartIndex + len(lTokens)
        self.sTokenValue = None

    def get_tokens(self):
        return self.lTokens

    def set_tokens(self, lTokens):
        self.lTokens = lTokens

    def get_line_number(self):
        return self.iLine

    def set_token_value(self, sToken):
        self.sTokenValue = sToken

    def get_token_value(self):
        return self.sTokenValue

