
from vsg import parser


class keyword(parser.keyword):
    '''
    unique_id = predefined_attribute : keyword
    '''

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class event_keyword(keyword):
    '''
    unique_id = predefined_attribute : event_keyword
    '''
    def __init__(self, sString):
        keyword.__init__(self, sString)


values = []
# Type attributes
values.append('ascending')
values.append('base')
values.append('high')
values.append('image')
values.append('left')
values.append('leftof')
values.append('low')
values.append('pos')
values.append('pred')
values.append('right')
values.append('rightof')
values.append('succ')
values.append('val')
values.append('value')

# Array attributes
values.append('ascending')
values.append('high')
values.append('left')
values.append('length')
values.append('low')
values.append('range')
values.append('reverse_range')
values.append('right')

# Signal attributes
values.append('active')
values.append('delayed')
values.append('driving')
values.append('driving_value')
values.append('event')
values.append('last_event')
values.append('last_active')
values.append('last_value')
values.append('quiet')
values.append('stable')
values.append('transaction')

# Everything attributes
values.append('instance_name')
values.append('path_name')
values.append('simple_name')
