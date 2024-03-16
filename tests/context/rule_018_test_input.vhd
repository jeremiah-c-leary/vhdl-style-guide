
--This should pass
context c1 is

end context c1;

--This should fail
context c1 is

end    context c1;

context c1 is

end  context c1;


context c1 is

end       context c1;

-- This should pass
context c1 is

end;

-- Split declaration across lines
context
c1
is

end
context
c1
;
