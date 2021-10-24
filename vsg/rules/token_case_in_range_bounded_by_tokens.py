
from vsg import rule
from vsg import violation


class token_case_in_range_bounded_by_tokens(rule.Rule):
    '''
    Checks the case for words.

    Parameters
    ----------

    name : string
       The group the rule belongs to.

    identifier : string
       unique identifier.  Usually in the form of 00N.

    trigger : parser object type
       object type to apply the case check against
    '''

    def __init__(self, name, identifier, lTokens, oStart, oEnd):
        rule.Rule.__init__(self, name=name, identifier=identifier)
        self.solution = None
        self.phase = 6
        self.case = 'lower'
        self.configuration.append('case')
        self.lTokens = lTokens
        self.oStart = oStart
        self.oEnd = oEnd
        self.prefix_exceptions = []
        self.suffix_exceptions = []

    def _get_tokens_of_interest(self, oFile):
        return oFile.get_tokens_matching_in_range_bounded_by_tokens(self.lTokens, self.oStart, self.oEnd)

    def _analyze(self, lToi):
        check_prefix = is_exception_enabled(self.prefix_exceptions)
        check_suffix = is_exception_enabled(self.suffix_exceptions)
        for oToi in lToi:
            sObjectValue = oToi.get_tokens()[0].get_value()
            if self.case == 'lower' and not check_prefix and not check_suffix:
                if not sObjectValue.islower():
                    oViolation = create_violation(sObjectValue, sObjectValue.lower(), oToi)
                    self.add_violation(oViolation)
            if self.case == 'lower' and check_prefix and not check_suffix:
                if prefix_detected(sObjectValue, self.prefix_exceptions):
                    sDesiredPrefix = get_matched_prefix(sObjectValue, self.prefix_exceptions)
                    sActualPrefix = extract_prefix(sObjectValue, sDesiredPrefix)
                    sConstant = remove_prefix(sObjectValue, sActualPrefix)
                    sExpected = sDesiredPrefix + sConstant.lower()
                    if sObjectValue != sExpected:
                        oViolation = create_violation(sObjectValue, sExpected, oToi)
                        self.add_violation(oViolation)
                elif not sObjectValue.islower():
                    oViolation = create_violation(sObjectValue, sObjectValue.lower(), oToi)
                    self.add_violation(oViolation)
            if self.case == 'lower' and not check_prefix and check_suffix:
                if suffix_detected(sObjectValue, self.suffix_exceptions):
                    sDesiredSuffix = get_matched_suffix(sObjectValue, self.suffix_exceptions)
                    sActualSuffix = extract_suffix(sObjectValue, sDesiredSuffix)
                    sConstant = remove_suffix(sObjectValue, sActualSuffix)
                    sExpected = sConstant.lower() + sDesiredSuffix
                    if sObjectValue != sExpected:
                        oViolation = create_violation(sObjectValue, sExpected, oToi)
                        self.add_violation(oViolation)
                elif not sObjectValue.islower():
                    oViolation = create_violation(sObjectValue, sObjectValue.lower(), oToi)
                    self.add_violation(oViolation)
            if self.case == 'lower' and check_prefix and check_suffix:
                if prefix_detected(sObjectValue, self.prefix_exceptions) and suffix_detected(sObjectValue, self.suffix_exceptions):
                    sDesiredPrefix = get_matched_prefix(sObjectValue, self.prefix_exceptions)
                    sActualPrefix = extract_prefix(sObjectValue, sDesiredPrefix)
                    sConstant = remove_prefix(sObjectValue, sActualPrefix)
                    sDesiredSuffix = get_matched_suffix(sConstant, self.suffix_exceptions)
                    sActualSuffix = extract_suffix(sConstant, sDesiredSuffix)
                    sConstant = remove_suffix(sConstant, sActualSuffix)
                    sExpected = sDesiredPrefix + sConstant.lower() + sDesiredSuffix
                    if sObjectValue != sExpected:
                        oViolation = create_violation(sObjectValue, sExpected, oToi)
                        self.add_violation(oViolation)
                elif not sObjectValue.islower():
                    oViolation = create_violation(sObjectValue, sObjectValue.lower(), oToi)
                    self.add_violation(oViolation)
            if self.case == 'upper' and not check_prefix and not check_suffix:
                if not sObjectValue.isupper():
                    oViolation = create_violation(sObjectValue, sObjectValue.upper(), oToi)
                    self.add_violation(oViolation)
            if self.case == 'upper' and check_prefix and not check_suffix:
                if prefix_detected(sObjectValue, self.prefix_exceptions):
                    sDesiredPrefix = get_matched_prefix(sObjectValue, self.prefix_exceptions)
                    sActualPrefix = extract_prefix(sObjectValue, sDesiredPrefix)
                    sConstant = remove_prefix(sObjectValue, sActualPrefix)
                    sExpected = sDesiredPrefix + sConstant.upper()
                    if sObjectValue != sExpected:
                        oViolation = create_violation(sObjectValue, sExpected, oToi)
                        self.add_violation(oViolation)
                elif not sObjectValue.isupper():
                    oViolation = create_violation(sObjectValue, sObjectValue.upper(), oToi)
                    self.add_violation(oViolation)
            if self.case == 'upper' and not check_prefix and check_suffix:
                if suffix_detected(sObjectValue, self.suffix_exceptions):
                    sDesiredSuffix = get_matched_suffix(sObjectValue, self.suffix_exceptions)
                    sActualSuffix = extract_suffix(sObjectValue, sDesiredSuffix)
                    sConstant = remove_suffix(sObjectValue, sActualSuffix)
                    sExpected = sConstant.upper() + sDesiredSuffix
                    if sObjectValue != sExpected:
                        oViolation = create_violation(sObjectValue, sExpected, oToi)
                        self.add_violation(oViolation)
                elif not sObjectValue.isupper():
                    oViolation = create_violation(sObjectValue, sObjectValue.upper(), oToi)
                    self.add_violation(oViolation)
            if self.case == 'upper' and check_prefix and check_suffix:
                if prefix_detected(sObjectValue, self.prefix_exceptions) and suffix_detected(sObjectValue, self.suffix_exceptions):
                    sDesiredPrefix = get_matched_prefix(sObjectValue, self.prefix_exceptions)
                    sActualPrefix = extract_prefix(sObjectValue, sDesiredPrefix)
                    sConstant = remove_prefix(sObjectValue, sActualPrefix)
                    sDesiredSuffix = get_matched_suffix(sConstant, self.suffix_exceptions)
                    sActualSuffix = extract_suffix(sConstant, sDesiredSuffix)
                    sConstant = remove_suffix(sConstant, sActualSuffix)
                    sExpected = sDesiredPrefix + sConstant.upper() + sDesiredSuffix
                    if sObjectValue != sExpected:
                        oViolation = create_violation(sObjectValue, sExpected, oToi)
                        self.add_violation(oViolation)
                elif not sObjectValue.isupper():
                    oViolation = create_violation(sObjectValue, sObjectValue.upper(), oToi)
                    self.add_violation(oViolation)

    def _fix_violation(self, oViolation):
        lTokens = oViolation.get_tokens()
        dAction = oViolation.get_action()
        lTokens[0].set_value(dAction['value'])
        oViolation.set_tokens(lTokens)


def is_exception_enabled(lList):
    if len(lList) == 0:
        return False
    return True 


def prefix_detected(sString, lPrefixes):
    sLowerString = sString.lower()
    for sPrefix in lPrefixes:
       if sLowerString.startswith(sPrefix.lower()):
           return True
    else:
        return False 

def get_matched_prefix(sString, lPrefixes):
    sLowerString = sString.lower()
    for sPrefix in lPrefixes:
       if sLowerString.startswith(sPrefix.lower()):
           return sPrefix

def extract_prefix(sString, sPrefix):
    return sString[0:len(sPrefix)]

def remove_prefix(sString, sPrefix):
    return sString[len(sPrefix):]


def suffix_detected(sString, lSuffixes):
    sLowerString = sString.lower()
    for sSuffix in lSuffixes:
       if sLowerString.endswith(sSuffix.lower()):
           return True
    else:
        return False 

def get_matched_suffix(sString, lSuffixes):
    sLowerString = sString.lower()
    for sSuffix in lSuffixes:
       if sLowerString.endswith(sSuffix.lower()):
           return sSuffix

def extract_suffix(sString, sSuffix):
    return sString[len(sString) - len(sSuffix):]

def remove_suffix(sString, sSuffix):
    return sString[0:len(sString) - len(sSuffix)]


def create_violation(sActual, sExpected, oToi):
    sSolution = 'Change "' + sActual + '" to "' + sExpected + '"'
    oViolation = violation.New(oToi.get_line_number(), oToi, sSolution)
    dAction = {}
    dAction['value'] = sExpected
    oViolation.set_action(dAction)
    return oViolation

