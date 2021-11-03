
from vsg import violation


def check_for_case_violation(oToi, self, check_prefix=False, check_suffix=False, iIndex=0, iLine=None):
    sObjectValue = get_token_value(oToi, iIndex)
    iMyLine = get_violation_line(oToi, iLine)
    oViolation = None

    if is_lower_case_without_prefix_or_suffix_exception(self.case, check_prefix, check_suffix):
        oViolation = check_for_lower_case(sObjectValue, oToi, iIndex, iMyLine)

    if is_lower_case_with_prefix_exception(self.case, check_prefix, check_suffix):
        oViolation = check_for_lower_case_with_prefix_exception(sObjectValue, self, oToi, iIndex, iMyLine)

    if is_lower_case_with_suffix_exception(self.case, check_prefix, check_suffix):
        oViolation = check_for_lower_case_with_suffix_exception(sObjectValue, self, oToi, iIndex, iMyLine)

    if is_lower_case_with_prefix_and_suffix_exception(self.case, check_prefix, check_suffix):
        oViolation = check_for_lower_case_with_prefix_and_suffix_exceptions(sObjectValue, self, oToi, iIndex, iMyLine)

    if is_upper_case_without_prefix_or_suffix_exception(self.case, check_prefix, check_suffix):
        oViolation = check_for_upper_case(sObjectValue, oToi, iIndex, iMyLine)

    if is_upper_case_with_prefix_exception(self.case, check_prefix, check_suffix):
        oViolation = check_for_upper_case_with_prefix_exception(sObjectValue, self, oToi, iIndex, iMyLine)

    if is_upper_case_with_suffix_exception(self.case, check_prefix, check_suffix):
        oViolation = check_for_upper_case_with_suffix_exception(sObjectValue, self, oToi, iIndex, iMyLine)

    if is_upper_case_with_prefix_and_suffix_exception(self.case, check_prefix, check_suffix):
        oViolation = check_for_upper_case_with_prefix_and_suffix_exceptions(sObjectValue, self, oToi, iIndex, iMyLine)

    return oViolation


def get_token_value(oToi, iIndex):
    return oToi.get_tokens()[iIndex].get_value()


def prefix_detected(sString, lPrefixes):
    sLowerString = sString.lower()
    for sPrefix in lPrefixes:
       if sLowerString.startswith(sPrefix.lower()):
           return True
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


def create_case_violation(sActual, sExpected, oToi, iIndex, iLine):
    sSolution = 'Change "' + sActual + '" to "' + sExpected + '"'
    oViolation = violation.New(iLine, oToi, sSolution)
    dAction = {}
    dAction['value'] = sExpected
    dAction['index'] = iIndex
    oViolation.set_action(dAction)
    return oViolation


def get_violation_line(oToi, iLine):
    if iLine is None:
        return oToi.get_line_number()
    return iLine


def is_exception_enabled(lList):
    if len(lList) == 0:
        return False
    return True


def is_lower_case_without_prefix_or_suffix_exception(sCase, bPrefix, bSuffix):
    if sCase == 'lower' and not bPrefix and not bSuffix:
        return True
    return False


def is_lower_case_with_prefix_exception(sCase, bPrefix, bSuffix):
    if sCase == 'lower' and bPrefix and not bSuffix:
        return True
    return False


def is_lower_case_with_suffix_exception(sCase, bPrefix, bSuffix):
    if sCase == 'lower' and not bPrefix and bSuffix:
        return True
    return False


def is_lower_case_with_prefix_and_suffix_exception(sCase, bPrefix, bSuffix):
    if sCase == 'lower' and bPrefix and bSuffix:
        return True
    return False


def is_upper_case_without_prefix_or_suffix_exception(sCase, bPrefix, bSuffix):
    if sCase == 'upper' and not bPrefix and not bSuffix:
        return True
    return False


def is_upper_case_with_prefix_exception(sCase, bPrefix, bSuffix):
    if sCase == 'upper' and bPrefix and not bSuffix:
        return True
    return False


def is_upper_case_with_suffix_exception(sCase, bPrefix, bSuffix):
    if sCase == 'upper' and not bPrefix and bSuffix:
        return True
    return False


def is_upper_case_with_prefix_and_suffix_exception(sCase, bPrefix, bSuffix):
    if sCase == 'upper' and bPrefix and bSuffix:
        return True
    return False


def check_for_lower_case(sObjectValue, oToi, iIndex, iLine):
    if not sObjectValue.islower():
        return create_case_violation(sObjectValue, sObjectValue.lower(), oToi, iIndex, iLine)


def check_for_upper_case(sObjectValue, oToi, iIndex, iLine):
    if not sObjectValue.isupper():
        return create_case_violation(sObjectValue, sObjectValue.upper(), oToi, iIndex, iLine)


def check_for_lower_case_with_prefix_exception(sObjectValue, self, oToi, iIndex, iLine):
    if prefix_detected(sObjectValue, self.prefix_exceptions):
        sDesiredPrefix = get_matched_prefix(sObjectValue, self.prefix_exceptions)
        sActualPrefix = extract_prefix(sObjectValue, sDesiredPrefix)
        sConstant = remove_prefix(sObjectValue, sActualPrefix)
        sExpected = sDesiredPrefix + sConstant.lower()
        if sObjectValue != sExpected:
            return create_case_violation(sObjectValue, sExpected, oToi, iIndex, iLine)
    else:
        return check_for_lower_case(sObjectValue, oToi, iIndex, iLine)


def check_for_upper_case_with_prefix_exception(sObjectValue, self, oToi, iIndex, iLine):
    if prefix_detected(sObjectValue, self.prefix_exceptions):
        sDesiredPrefix = get_matched_prefix(sObjectValue, self.prefix_exceptions)
        sActualPrefix = extract_prefix(sObjectValue, sDesiredPrefix)
        sConstant = remove_prefix(sObjectValue, sActualPrefix)
        sExpected = sDesiredPrefix + sConstant.upper()
        if sObjectValue != sExpected:
            return create_case_violation(sObjectValue, sExpected, oToi, iIndex, iLine)
    else:
        return check_for_upper_case(sObjectValue, oToi, iIndex, iLine)


def check_for_lower_case_with_suffix_exception(sObjectValue, self, oToi, iIndex, iLine):
    if suffix_detected(sObjectValue, self.suffix_exceptions):
        sDesiredSuffix = get_matched_suffix(sObjectValue, self.suffix_exceptions)
        sActualSuffix = extract_suffix(sObjectValue, sDesiredSuffix)
        sConstant = remove_suffix(sObjectValue, sActualSuffix)
        sExpected = sConstant.lower() + sDesiredSuffix
        if sObjectValue != sExpected:
            return create_case_violation(sObjectValue, sExpected, oToi, iIndex, iLine)
    else:
        return check_for_lower_case(sObjectValue, oToi, iIndex, iLine)


def check_for_upper_case_with_suffix_exception(sObjectValue, self, oToi, iIndex, iLine):
    if suffix_detected(sObjectValue, self.suffix_exceptions):
        sDesiredSuffix = get_matched_suffix(sObjectValue, self.suffix_exceptions)
        sActualSuffix = extract_suffix(sObjectValue, sDesiredSuffix)
        sConstant = remove_suffix(sObjectValue, sActualSuffix)
        sExpected = sConstant.upper() + sDesiredSuffix
        if sObjectValue != sExpected:
            return create_case_violation(sObjectValue, sExpected, oToi, iIndex, iLine)
    else:
        return check_for_upper_case(sObjectValue, oToi, iIndex, iLine)


def check_for_lower_case_with_prefix_and_suffix_exceptions(sObjectValue, self, oToi, iIndex, iLine):
    if prefix_detected(sObjectValue, self.prefix_exceptions) and suffix_detected(sObjectValue, self.suffix_exceptions):
        sDesiredPrefix = get_matched_prefix(sObjectValue, self.prefix_exceptions)
        sActualPrefix = extract_prefix(sObjectValue, sDesiredPrefix)
        sConstant = remove_prefix(sObjectValue, sActualPrefix)
        sDesiredSuffix = get_matched_suffix(sConstant, self.suffix_exceptions)
        sActualSuffix = extract_suffix(sConstant, sDesiredSuffix)
        sConstant = remove_suffix(sConstant, sActualSuffix)
        sExpected = sDesiredPrefix + sConstant.lower() + sDesiredSuffix
        if sObjectValue != sExpected:
            return create_case_violation(sObjectValue, sExpected, oToi, iIndex, iLine)
    else:
        return check_for_lower_case(sObjectValue, oToi, iIndex, iLine)


def check_for_upper_case_with_prefix_and_suffix_exceptions(sObjectValue, self, oToi, iIndex, iLine):
    if prefix_detected(sObjectValue, self.prefix_exceptions) and suffix_detected(sObjectValue, self.suffix_exceptions):
        sDesiredPrefix = get_matched_prefix(sObjectValue, self.prefix_exceptions)
        sActualPrefix = extract_prefix(sObjectValue, sDesiredPrefix)
        sConstant = remove_prefix(sObjectValue, sActualPrefix)
        sDesiredSuffix = get_matched_suffix(sConstant, self.suffix_exceptions)
        sActualSuffix = extract_suffix(sConstant, sDesiredSuffix)
        sConstant = remove_suffix(sConstant, sActualSuffix)
        sExpected = sDesiredPrefix + sConstant.upper() + sDesiredSuffix
        if sObjectValue != sExpected:
            return create_case_violation(sObjectValue, sExpected, oToi, iIndex, iLine)
    else:
        return check_for_upper_case(sObjectValue, oToi, iIndex, iLine)
