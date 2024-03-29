
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ADD ASSIGN BY CBRACE DIV DIVIDE FROM ID MINUS MUL NEXT NUMBER OBRACE PLUS PRINT SUB TIMES TO W\n    program : statements\n\n    \n    statements : statement\n    \n   statements : statement NEXT statements\n   \n    statement : assignment_statement\n              | operation_statement\n              | print_statement\n              | expression\n\n    \n    assignment_statement : ASSIGN OBRACE ID CBRACE TO OBRACE expression CBRACE\n    \n    print_statement : PRINT OBRACE expression CBRACE\n\n    \n    operation_statement : MUL OBRACE statement  CBRACE BY OBRACE statement CBRACE\n                        | DIV OBRACE statement  CBRACE BY OBRACE statement CBRACE\n                        | ADD OBRACE statement  CBRACE W OBRACE statement CBRACE\n                        | SUB OBRACE statement  CBRACE FROM OBRACE statement CBRACE\n\n    \n\n    expression : expression expression TIMES\n               | expression expression DIVIDE\n               | expression expression PLUS\n               | expression expression MINUS\n\n\n    \n    expression : ID\n\n    \n    expression : NUMBER\n\n    '
    
_lr_action_items = {'ASSIGN':([0,16,19,20,21,22,47,48,49,50,],[8,8,8,8,8,8,8,8,8,8,]),'MUL':([0,16,19,20,21,22,47,48,49,50,],[10,10,10,10,10,10,10,10,10,10,]),'DIV':([0,16,19,20,21,22,47,48,49,50,],[11,11,11,11,11,11,11,11,11,11,]),'ADD':([0,16,19,20,21,22,47,48,49,50,],[12,12,12,12,12,12,12,12,12,12,]),'SUB':([0,16,19,20,21,22,47,48,49,50,],[13,13,13,13,13,13,13,13,13,13,]),'PRINT':([0,16,19,20,21,22,47,48,49,50,],[14,14,14,14,14,14,14,14,14,14,]),'ID':([0,7,9,15,16,17,18,19,20,21,22,23,25,26,27,28,34,46,47,48,49,50,51,],[9,9,-18,-19,9,9,29,9,9,9,9,9,-14,-15,-16,-17,9,9,9,9,9,9,9,]),'NUMBER':([0,7,9,15,16,17,19,20,21,22,23,25,26,27,28,34,46,47,48,49,50,51,],[15,15,-18,-19,15,15,15,15,15,15,15,-14,-15,-16,-17,15,15,15,15,15,15,15,]),'$end':([1,2,3,4,5,6,7,9,15,24,25,26,27,28,40,56,57,58,59,60,],[0,-1,-2,-4,-5,-6,-7,-18,-19,-3,-14,-15,-16,-17,-9,-8,-10,-11,-12,-13,]),'NEXT':([3,4,5,6,7,9,15,25,26,27,28,40,56,57,58,59,60,],[16,-4,-5,-6,-7,-18,-19,-14,-15,-16,-17,-9,-8,-10,-11,-12,-13,]),'CBRACE':([4,5,6,7,9,15,25,26,27,28,29,30,31,32,33,34,40,51,52,53,54,55,56,57,58,59,60,],[-4,-5,-6,-7,-18,-19,-14,-15,-16,-17,35,36,37,38,39,40,-9,56,57,58,59,60,-8,-10,-11,-12,-13,]),'OBRACE':([8,10,11,12,13,14,41,42,43,44,45,],[18,19,20,21,22,23,46,47,48,49,50,]),'TIMES':([9,15,17,25,26,27,28,],[-18,-19,25,-14,-15,-16,-17,]),'DIVIDE':([9,15,17,25,26,27,28,],[-18,-19,26,-14,-15,-16,-17,]),'PLUS':([9,15,17,25,26,27,28,],[-18,-19,27,-14,-15,-16,-17,]),'MINUS':([9,15,17,25,26,27,28,],[-18,-19,28,-14,-15,-16,-17,]),'TO':([35,],[41,]),'BY':([36,37,],[42,43,]),'W':([38,],[44,]),'FROM':([39,],[45,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'statements':([0,16,],[2,24,]),'statement':([0,16,19,20,21,22,47,48,49,50,],[3,3,30,31,32,33,52,53,54,55,]),'assignment_statement':([0,16,19,20,21,22,47,48,49,50,],[4,4,4,4,4,4,4,4,4,4,]),'operation_statement':([0,16,19,20,21,22,47,48,49,50,],[5,5,5,5,5,5,5,5,5,5,]),'print_statement':([0,16,19,20,21,22,47,48,49,50,],[6,6,6,6,6,6,6,6,6,6,]),'expression':([0,7,16,17,19,20,21,22,23,34,46,47,48,49,50,51,],[7,17,7,17,7,7,7,7,34,17,51,7,7,7,7,17,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> statements','program',1,'p_program','yacc.py',21),
  ('statements -> statement','statements',1,'p_Sstatement','yacc.py',29),
  ('statements -> statement NEXT statements','statements',3,'p_Mstatements','yacc.py',37),
  ('statement -> assignment_statement','statement',1,'p_statement','yacc.py',44),
  ('statement -> operation_statement','statement',1,'p_statement','yacc.py',45),
  ('statement -> print_statement','statement',1,'p_statement','yacc.py',46),
  ('statement -> expression','statement',1,'p_statement','yacc.py',47),
  ('assignment_statement -> ASSIGN OBRACE ID CBRACE TO OBRACE expression CBRACE','assignment_statement',8,'p_assignment_statement','yacc.py',56),
  ('print_statement -> PRINT OBRACE expression CBRACE','print_statement',4,'p_print_statement','yacc.py',65),
  ('operation_statement -> MUL OBRACE statement CBRACE BY OBRACE statement CBRACE','operation_statement',8,'p_operation_statement','yacc.py',73),
  ('operation_statement -> DIV OBRACE statement CBRACE BY OBRACE statement CBRACE','operation_statement',8,'p_operation_statement','yacc.py',74),
  ('operation_statement -> ADD OBRACE statement CBRACE W OBRACE statement CBRACE','operation_statement',8,'p_operation_statement','yacc.py',75),
  ('operation_statement -> SUB OBRACE statement CBRACE FROM OBRACE statement CBRACE','operation_statement',8,'p_operation_statement','yacc.py',76),
  ('expression -> expression expression TIMES','expression',3,'p_expression','yacc.py',93),
  ('expression -> expression expression DIVIDE','expression',3,'p_expression','yacc.py',94),
  ('expression -> expression expression PLUS','expression',3,'p_expression','yacc.py',95),
  ('expression -> expression expression MINUS','expression',3,'p_expression','yacc.py',96),
  ('expression -> ID','expression',1,'p_expression_variable','yacc.py',112),
  ('expression -> NUMBER','expression',1,'p_expression_number','yacc.py',124),
]
