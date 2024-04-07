--------------------------------------------------------------------------------
0 |
--------------------------------------------------------------------------------
1 |
<class 'vsg.parser.blank_line'>
--------------------------------------------------------------------------------
2 | architecture rtl of fifo is
<class 'vsg.token.architecture_body.architecture_keyword'>
<class 'vsg.token.architecture_body.identifier'>
<class 'vsg.token.architecture_body.of_keyword'>
<class 'vsg.token.architecture_body.entity_name'>
<class 'vsg.token.architecture_body.is_keyword'>
--------------------------------------------------------------------------------
3 |
<class 'vsg.parser.blank_line'>
--------------------------------------------------------------------------------
4 | begin
<class 'vsg.token.architecture_body.begin_keyword'>
--------------------------------------------------------------------------------
5 |
<class 'vsg.parser.blank_line'>
--------------------------------------------------------------------------------
6 |   a <= b('0');
<class 'vsg.token.concurrent_simple_signal_assignment.target'>
<class 'vsg.token.concurrent_simple_signal_assignment.assignment'>
<class 'vsg.token.todo.name'>
<class 'vsg.token.todo.open_parenthesis'>
<class 'vsg.parser.character_literal'>
<class 'vsg.token.todo.close_parenthesis'>
<class 'vsg.token.concurrent_simple_signal_assignment.semicolon'>
--------------------------------------------------------------------------------
7 |
<class 'vsg.parser.blank_line'>
--------------------------------------------------------------------------------
8 |   a <= b(x, y, z);
<class 'vsg.token.concurrent_simple_signal_assignment.target'>
<class 'vsg.token.concurrent_simple_signal_assignment.assignment'>
<class 'vsg.token.todo.name'>
<class 'vsg.token.todo.open_parenthesis'>
<class 'vsg.parser.todo'>
<class 'vsg.parser.comma'>
<class 'vsg.parser.todo'>
<class 'vsg.parser.comma'>
<class 'vsg.parser.todo'>
<class 'vsg.token.todo.close_parenthesis'>
<class 'vsg.token.concurrent_simple_signal_assignment.semicolon'>
--------------------------------------------------------------------------------
9 |
<class 'vsg.parser.blank_line'>
--------------------------------------------------------------------------------
10 |   a <= b(x(3, 4, 5), y(6, 7, 8), z(9, 0, 1));
<class 'vsg.token.concurrent_simple_signal_assignment.target'>
<class 'vsg.token.concurrent_simple_signal_assignment.assignment'>
<class 'vsg.token.todo.name'>
<class 'vsg.token.todo.open_parenthesis'>
<class 'vsg.token.todo.name'>
<class 'vsg.token.todo.open_parenthesis'>
<class 'vsg.parser.todo'>
<class 'vsg.parser.comma'>
<class 'vsg.parser.todo'>
<class 'vsg.parser.comma'>
<class 'vsg.parser.todo'>
<class 'vsg.token.todo.close_parenthesis'>
<class 'vsg.parser.comma'>
<class 'vsg.token.todo.name'>
<class 'vsg.token.todo.open_parenthesis'>
<class 'vsg.parser.todo'>
<class 'vsg.parser.comma'>
<class 'vsg.parser.todo'>
<class 'vsg.parser.comma'>
<class 'vsg.parser.todo'>
<class 'vsg.token.todo.close_parenthesis'>
<class 'vsg.parser.comma'>
<class 'vsg.token.todo.name'>
<class 'vsg.token.todo.open_parenthesis'>
<class 'vsg.parser.todo'>
<class 'vsg.parser.comma'>
<class 'vsg.parser.todo'>
<class 'vsg.parser.comma'>
<class 'vsg.parser.todo'>
<class 'vsg.token.todo.close_parenthesis'>
<class 'vsg.token.todo.close_parenthesis'>
<class 'vsg.token.concurrent_simple_signal_assignment.semicolon'>
--------------------------------------------------------------------------------
11 |
<class 'vsg.parser.blank_line'>
--------------------------------------------------------------------------------
12 |   a <= (x(3, 4, 5), y(6, 7, 8), z(9, 0, 1));
<class 'vsg.token.concurrent_simple_signal_assignment.target'>
<class 'vsg.token.concurrent_simple_signal_assignment.assignment'>
<class 'vsg.token.aggregate.open_parenthesis'>
<class 'vsg.token.todo.name'>
<class 'vsg.token.todo.open_parenthesis'>
<class 'vsg.parser.todo'>
<class 'vsg.parser.comma'>
<class 'vsg.parser.todo'>
<class 'vsg.parser.comma'>
<class 'vsg.parser.todo'>
<class 'vsg.token.todo.close_parenthesis'>
<class 'vsg.parser.comma'>
<class 'vsg.token.todo.name'>
<class 'vsg.token.todo.open_parenthesis'>
<class 'vsg.parser.todo'>
<class 'vsg.parser.comma'>
<class 'vsg.parser.todo'>
<class 'vsg.parser.comma'>
<class 'vsg.parser.todo'>
<class 'vsg.token.todo.close_parenthesis'>
<class 'vsg.parser.comma'>
<class 'vsg.token.todo.name'>
<class 'vsg.token.todo.open_parenthesis'>
<class 'vsg.parser.todo'>
<class 'vsg.parser.comma'>
<class 'vsg.parser.todo'>
<class 'vsg.parser.comma'>
<class 'vsg.parser.todo'>
<class 'vsg.token.todo.close_parenthesis'>
<class 'vsg.token.aggregate.close_parenthesis'>
<class 'vsg.token.concurrent_simple_signal_assignment.semicolon'>
--------------------------------------------------------------------------------
13 |
<class 'vsg.parser.blank_line'>
--------------------------------------------------------------------------------
14 |   a <= ((3, 4, 5), (6, 7, 8), (9, 0, 1));
<class 'vsg.token.concurrent_simple_signal_assignment.target'>
<class 'vsg.token.concurrent_simple_signal_assignment.assignment'>
<class 'vsg.token.aggregate.open_parenthesis'>
<class 'vsg.token.aggregate.open_parenthesis'>
<class 'vsg.parser.todo'>
<class 'vsg.parser.comma'>
<class 'vsg.parser.todo'>
<class 'vsg.parser.comma'>
<class 'vsg.parser.todo'>
<class 'vsg.token.aggregate.close_parenthesis'>
<class 'vsg.parser.comma'>
<class 'vsg.token.aggregate.open_parenthesis'>
<class 'vsg.parser.todo'>
<class 'vsg.parser.comma'>
<class 'vsg.parser.todo'>
<class 'vsg.parser.comma'>
<class 'vsg.parser.todo'>
<class 'vsg.token.aggregate.close_parenthesis'>
<class 'vsg.parser.comma'>
<class 'vsg.token.aggregate.open_parenthesis'>
<class 'vsg.parser.todo'>
<class 'vsg.parser.comma'>
<class 'vsg.parser.todo'>
<class 'vsg.parser.comma'>
<class 'vsg.parser.todo'>
<class 'vsg.token.aggregate.close_parenthesis'>
<class 'vsg.token.aggregate.close_parenthesis'>
<class 'vsg.token.concurrent_simple_signal_assignment.semicolon'>
--------------------------------------------------------------------------------
15 |
<class 'vsg.parser.blank_line'>
--------------------------------------------------------------------------------
16 |   a <= a, b;
<class 'vsg.token.concurrent_simple_signal_assignment.target'>
<class 'vsg.token.concurrent_simple_signal_assignment.assignment'>
<class 'vsg.parser.todo'>
<class 'vsg.token.waveform.comma'>
<class 'vsg.parser.todo'>
<class 'vsg.token.concurrent_simple_signal_assignment.semicolon'>
--------------------------------------------------------------------------------
17 |
<class 'vsg.parser.blank_line'>
--------------------------------------------------------------------------------
18 |   a <= b(x => 3, y => 2, z => 1);
<class 'vsg.token.concurrent_simple_signal_assignment.target'>
<class 'vsg.token.concurrent_simple_signal_assignment.assignment'>
<class 'vsg.token.todo.name'>
<class 'vsg.token.todo.open_parenthesis'>
<class 'vsg.parser.todo'>
<class 'vsg.token.element_association.assignment'>
<class 'vsg.parser.todo'>
<class 'vsg.parser.comma'>
<class 'vsg.parser.todo'>
<class 'vsg.token.element_association.assignment'>
<class 'vsg.parser.todo'>
<class 'vsg.parser.comma'>
<class 'vsg.parser.todo'>
<class 'vsg.token.element_association.assignment'>
<class 'vsg.parser.todo'>
<class 'vsg.token.todo.close_parenthesis'>
<class 'vsg.token.concurrent_simple_signal_assignment.semicolon'>
--------------------------------------------------------------------------------
19 |
<class 'vsg.parser.blank_line'>
--------------------------------------------------------------------------------
20 | end architecture;
<class 'vsg.token.architecture_body.end_keyword'>
<class 'vsg.token.architecture_body.end_architecture_keyword'>
<class 'vsg.token.architecture_body.semicolon'>
