
from vsg import line
from vsg import parser
from vsg import token

from vsg.token import adding_operator
from vsg.token import direction
from vsg.token import logical_operator
from vsg.token import miscellaneous_operator
from vsg.token import multiplying_operator
from vsg.token import relational_operator

from vsg.vhdlFile import classify
from vsg.vhdlFile import extract
from vsg.vhdlFile import update
from vsg.vhdlFile import utils

from vsg.vhdlFile.classify import entity

from vsg.vhdlFile.classify_new import blank
from vsg.vhdlFile.classify_new import comment
from vsg.vhdlFile.classify_new import design_file
from vsg.vhdlFile.classify_new import whitespace

from vsg.vhdlFile.indent import loop_statement
from vsg.vhdlFile.indent import function_specification
from vsg.vhdlFile.indent import procedure_specification
from vsg.vhdlFile.indent import interface_element
from vsg.vhdlFile.indent import generate_statement
from vsg.vhdlFile.indent import generic_clause
from vsg.vhdlFile.indent import port_clause
from vsg.vhdlFile.indent import if_statement
from vsg.vhdlFile.indent import package_declaration
from vsg.vhdlFile.indent import simple_signal_assignment
from vsg.vhdlFile.indent import signal_declaration
from vsg.vhdlFile.indent import subtype_declaration
from vsg.vhdlFile.indent import type_declaration
from vsg.vhdlFile.indent import variable_declaration
from vsg.vhdlFile.indent import variable_assignment_statement
from vsg.vhdlFile.indent import wait_statement
from vsg.vhdlFile.indent import component_instantiation_statement
from vsg.vhdlFile.indent import generic_map_aspect
from vsg.vhdlFile.indent import port_map_aspect
from vsg.vhdlFile.indent import association_element


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
        post_token_assignments(self.lAllObjects)

        for iLine, lLine in enumerate(split_on_carriage_return(self.lAllObjects)):
            self.lines[iLine + 1].objects = lLine

        self.set_token_indent()
        set_token_hierarchy_value(self.lAllObjects)

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
                 if bLibraryFound:
                     oToken.set_indent(iIndent + 1)
                 else:
                     oToken.set_indent(iIndent)
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

            ### Variable declaration 
            if isinstance(oToken, token.variable_declaration.variable_keyword):
                oToken.set_indent(iIndent)

            ### File declaration 
            if isinstance(oToken, token.file_declaration.file_keyword):
                oToken.set_indent(iIndent)

            if isinstance(oToken, token.file_open_information.open_keyword):
                oToken.set_indent(iIndent + 1)

            if isinstance(oToken, token.file_open_information.is_keyword):
                oToken.set_indent(iIndent + 1)

            iIndent, bLabelFound = loop_statement.set_indent(iIndent, bLabelFound, oToken)
            iIndent, bLabelFound = procedure_specification.set_indent(iIndent, bLabelFound, oToken)
            iIndent, bLabelFound = function_specification.set_indent(iIndent, bLabelFound, oToken)
            iIndent, bLabelFound = interface_element.set_indent(iIndent, bLabelFound, oToken)
            iIndent, bLabelFound = generate_statement.set_indent(iIndent, bLabelFound, oToken)
            iIndent, bLabelFound = generic_clause.set_indent(iIndent, bLabelFound, oToken)
            iIndent, bLabelFound = port_clause.set_indent(iIndent, bLabelFound, oToken)
            iIndent, bLabelFound = if_statement.set_indent(iIndent, bLabelFound, oToken)
            iIndent, bLabelFound = package_declaration.set_indent(iIndent, bLabelFound, oToken)
            iIndent, bLabelFound = simple_signal_assignment.set_indent(iIndent, bLabelFound, oToken)
            iIndent, bLabelFound = signal_declaration.set_indent(iIndent, bLabelFound, oToken)
            iIndent, bLabelFound = subtype_declaration.set_indent(iIndent, bLabelFound, oToken)
            iIndent, bLabelFound = type_declaration.set_indent(iIndent, bLabelFound, oToken)
            iIndent, bLabelFound = variable_declaration.set_indent(iIndent, bLabelFound, oToken)
            iIndent, bLabelFound = variable_assignment_statement.set_indent(iIndent, bLabelFound, oToken)
            iIndent, bLabelFound = wait_statement.set_indent(iIndent, bLabelFound, oToken)
            iIndent, bLabelFound = component_instantiation_statement.set_indent(iIndent, bLabelFound, oToken)
            iIndent, bLabelFound = generic_map_aspect.set_indent(iIndent, bLabelFound, oToken)
            iIndent, bLabelFound = port_map_aspect.set_indent(iIndent, bLabelFound, oToken)
            iIndent, bLabelFound = association_element.set_indent(iIndent, bLabelFound, oToken)
  
    def print_debug(self):
        for oLine in self.lines:
            print(f'{oLine.indentLevel} | {oLine.line}')
        

    def get_all_tokens(self):
        return extract.get_all_tokens(self.lAllObjects)

    def get_sequence_of_tokens_matching(self, lTokens):
        return extract.get_sequence_of_tokens_matching(lTokens, self.lAllObjects)

    def get_sequence_of_tokens_matching_bounded_by_tokens(self, lTokens, oStart, oEnd):
        return extract.get_sequence_of_tokens_matching_bounded_by_tokens(lTokens, oStart, oEnd, self.lAllObjects)

    def get_tokens_matching(self, lTokens):
        return extract.get_tokens_matching(lTokens, self.lAllObjects)

    def get_n_token_after_tokens(self, iToken, lTokens):
        return extract.get_n_token_after_tokens(iToken, lTokens, self.lAllObjects)

    def get_n_token_after_tokens_between_tokens(self, iToken, lTokens, oStart, oEnd):
        return extract.get_n_token_after_tokens_between_tokens(iToken, lTokens, oStart, oEnd, self.lAllObjects)

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

    def get_tokens_bounded_by(self, oLeft, oRight, include_trailing_whitespace=False, bExcludeLastToken=False):
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
                    if bExcludeLastToken:
                        lTemp.pop()
                        if isinstance(lTemp[-1], parser.whitespace):
                            lTemp.pop()
                        if isinstance(lTemp[-1], parser.carriage_return):
                            lTemp.pop()
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

    def get_tokens_at_beginning_of_line_matching_between_tokens(self, lTokens, oStart, oEnd, bIncludePreCarriageReturn=False):
        iLine = 1
        lReturn = []
        bSearch = False
        for iIndex in range(0, len(self.lAllObjects)):

            if bIncludePreCarriageReturn:
                for oToken in lTokens:
                    if utils.are_next_consecutive_token_types([parser.carriage_return, oToken], iIndex, self.lAllObjects):
                        bSearch = True
                    if utils.are_next_consecutive_token_types([parser.carriage_return, parser.whitespace, oToken], iIndex, self.lAllObjects):
                        bSearch = True
            else:
                if isinstance(self.lAllObjects[iIndex], oStart):
                    bSearch = True
            if isinstance(self.lAllObjects[iIndex], oEnd):
                bSearch = False

            
            if isinstance(self.lAllObjects[iIndex], parser.carriage_return):
                iLine +=1
                iStart = iIndex + 1
                if bSearch :
                    for oToken in lTokens:
                        if utils.are_next_consecutive_token_types([parser.whitespace, oToken], iStart, self.lAllObjects):
                            lReturn.append(Tokens(iStart, iLine, self.lAllObjects[iStart:iStart + 2]))
                        elif utils.are_next_consecutive_token_types([oToken], iStart, self.lAllObjects):
                            lReturn.append(Tokens(iStart, iLine, [self.lAllObjects[iStart]]))

        return lReturn                    

    def get_column_of_token_index(self, iToken):
        return extract.get_column_of_token_index(iToken, self.lAllObjects)

    def get_line_above_line_starting_with_token(self, lTokens):
        return extract.get_line_above_line_starting_with_token(lTokens, self.lAllObjects)

    def get_line_above_line_starting_with_token_with_hierarchy(self, lTokens, lHierarchy):
        return extract.get_line_above_line_starting_with_token_with_hierarchy(lTokens, self.lAllObjects, lHierarchy)

    def get_line_below_line_ending_with_token(self, lTokens):
        return extract.get_line_below_line_ending_with_token(lTokens, self.lAllObjects)

    def get_line_below_line_ending_with_token_with_hierarchy(self, lTokens, lHierarchy):
        return extract.get_line_below_line_ending_with_token_with_hierarchy(lTokens, self.lAllObjects, lHierarchy)

    def get_if_statement_conditions(self):
        return extract.get_if_statement_conditions(self.lAllObjects)

    def get_n_tokens_before_and_after_tokens(self, iToken, lTokens):
        return extract.get_n_tokens_before_and_after_tokens(iToken, lTokens, self.lAllObjects)

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

    def get_interface_elements_between_tokens(self, oStart, oEnd, include_end_of_line_comments=False):
        iLine = 1
        lReturn = []
        bSearch = False
        bStore = False
        lTemp = []
        iLineNumber = None
        for iIndex in range(0, len(self.lAllObjects)):
            oToken = self.lAllObjects[iIndex]
            if isinstance(oToken, oStart):
                bSearch = True
                continue
            if isinstance(oToken, oEnd):
                bSearch = False 
                bStore = False
                if len(lTemp) > 0:
                    for i in range(1, 3):
                        if isinstance(lTemp[-1], parser.whitespace):
                            lTemp.pop()
                            continue
                        if isinstance(lTemp[-1], parser.carriage_return):
                            lTemp.pop()
                            continue
                        break 
                    lReturn.append(Tokens(iStart, iLineNumber, lTemp))
                lTemp = []
                continue

            if bSearch:
                if not isinstance(oToken, parser.whitespace) and not isinstance(oToken, parser.carriage_return) and not isinstance(oToken, parser.comment) and not bStore:
                    bStore = True
                    iStart = iIndex
                    iLineNumber = iLine
                
                if isinstance(oToken, token.interface_list.semicolon):
                    lReturn.append(Tokens(iStart, iLineNumber, lTemp))
                    lTemp = []
                    bStore = False

                if bStore:
                   lTemp.append(oToken)

            if isinstance(oToken, parser.carriage_return):
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

    def get_tokens_starting_with_token_and_ending_with_one_of_possible_tokens(self, lStartTokens, lEndTokens):
        iLine = 1
        lReturn = []
        lTemp = []
        bStore = False

        for iIndex in range(0, len(self.lAllObjects)):
            oToken = self.lAllObjects[iIndex]

            if bStore:
                for oEndToken in lEndTokens:
                    if isinstance(oToken, oEndToken):
                        lReturn.append(Tokens(iStart, iStartLine, lTemp))
                        bStore = False
                        lTemp = []

            if bStore:
                if len(lTemp) == 0:
                    if not is_whitespace(oToken):
                        iStartLine = iLine
                        iStart = iIndex
                        lTemp.append(oToken)
                else:
                    lTemp.append(oToken)

            for oStartToken in lStartTokens:
                if isinstance(oToken, oStartToken):
                    bStore = True

            if isinstance(self.lAllObjects[iIndex], parser.carriage_return):
                iLine +=1

        return lReturn


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

    def extract_tokens(self, iStart, iEnd):
        lTokens = self.lTokens[iStart:iEnd + 1]
        iStartIndex = iStart + self.iStartIndex
        iLine = self.iLine
        for iIndex in range(0, iStart + 1):
            if isinstance(self.lTokens[iIndex], parser.carriage_return):
                iLine += 1
        return Tokens(iStartIndex, iLine, lTokens)

    def get_start_index(self):
        return self.iStartIndex


def post_token_assignments(lTokens):
    for iToken, oToken in enumerate(lTokens):
        if isinstance(oToken, parser.todo):
            sValue = oToken.get_value()
            if sValue == '&':
                lTokens[iToken] = adding_operator.concat()
                continue
            if sValue  == '+':
                lTokens[iToken] = adding_operator.plus()
                continue
            if sValue == '(':
                lTokens[iToken] = parser.open_parenthesis()
                continue
            if sValue == ')':
                lTokens[iToken] = parser.close_parenthesis()
                continue
            if sValue == ',':
                lTokens[iToken] = parser.comma()
                continue
            if sValue.lower() == 'to':
                lTokens[iToken] = token.direction.to(sValue)
                continue
            if sValue.lower() == 'downto':
                lTokens[iToken] = token.direction.downto(sValue)
                continue
            if sValue.lower() == 'and':
                lTokens[iToken] = token.logical_operator.and_operator(sValue)
                continue
            if sValue.lower() == 'or':
                lTokens[iToken] = token.logical_operator.or_operator(sValue)
                continue
            if sValue.lower() == 'nand':
                lTokens[iToken] = token.logical_operator.nand_operator(sValue)
                continue
            if sValue.lower() == 'nor':
                lTokens[iToken] = token.logical_operator.nor_operator(sValue)
                continue
            if sValue.lower() == 'xor':
                lTokens[iToken] = token.logical_operator.xor_operator(sValue)
                continue
            if sValue.lower() == 'xnor':
                lTokens[iToken] = token.logical_operator.xnor_operator(sValue)
                continue
            if sValue.lower() == '**':
                lTokens[iToken] = token.miscellaneous_operator.double_star(sValue)
                continue
            if sValue.lower() == 'abs':
                lTokens[iToken] = token.miscellaneous_operator.abs_operator(sValue)
                continue
            if sValue.lower() == 'not':
                lTokens[iToken] = token.miscellaneous_operator.not_operator(sValue)
                continue

            if sValue.lower() == '*':
                lTokens[iToken] = token.multiplying_operator.star(sValue)
                continue
            if sValue.lower() == '/':
                lTokens[iToken] = token.multiplying_operator.slash(sValue)
                continue
            if sValue.lower() == 'mod':
                lTokens[iToken] = token.multiplying_operator.mod_operator(sValue)
                continue
            if sValue.lower() == 'rem':
                lTokens[iToken] = token.multiplying_operator.rem_operator(sValue)
                continue

            if sValue == '=':
                lTokens[iToken] = token.relational_operator.equal(sValue)
                continue



            if sValue == "'":
                lTokens[iToken] = parser.tic(sValue)
                continue
            if sValue.lower() == 'event':
                lTokens[iToken] = parser.event_keyword(sValue)
                continue

            ### IEEE values
            if sValue.lower() == 'rising_edge':
                lTokens[iToken] = token.ieee.std_logic_1164.function.rising_edge(sValue)
                continue
            if sValue.lower() == 'falling_edge':
                lTokens[iToken] = token.ieee.std_logic_1164.function.falling_edge(sValue)
                continue

            if len(sValue) == 3 and sValue.startswith("'") and sValue.endswith("'"):
                lTokens[iToken] = parser.character_literal(sValue)
                continue
 


def set_token_hierarchy_value(lTokens):
    iIfHierarchy = 0
    for iToken, oToken in enumerate(lTokens):
        if isinstance(oToken, token.if_statement.if_keyword):
            oToken.set_hierarchy(iIfHierarchy)
            iIfHierarchy += 1
        if isinstance(oToken, token.if_statement.semicolon):
            iIfHierarchy -= 1
            oToken.set_hierarchy(iIfHierarchy)
