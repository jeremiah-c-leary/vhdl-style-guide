
from vsg.rules.package import uppercase_package_name_rule


class rule_010(uppercase_package_name_rule):
    '''
    Package rule 010 checks the package name is upper case in the package declaration.
    '''

    def __init__(self):
        uppercase_package_name_rule.__init__(self, 'package', '010', 'isPackageKeyword')
