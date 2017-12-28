
from vsg.rules.package import uppercase_package_name_rule


class rule_008(uppercase_package_name_rule):
    '''
    Package rule 008 checks the package name is upper case on the closing "end package" line.
    '''

    def __init__(self):
        uppercase_package_name_rule.__init__(self, 'package', '008', 'isPackageEnd')
