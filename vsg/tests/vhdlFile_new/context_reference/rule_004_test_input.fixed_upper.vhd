
-- These should pass

context c1 is

  context CON1, CON2, CON3;

end context c1;

context CON2, CON3, CON4;

-- These should fail

context c1 is

  context CON1,
  CON2, CON3;

end context c1;

context CON2, CON3,
 CON4;

-- Try with distributed line

context c1 is

  context
  CON1
,
  CON2
,
  CON3
;

end context c1;

context
CON1
,
CON2
,
CON3
;
