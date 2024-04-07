
--This should pass
context con1 is

end context;

context con2 is

end context;

--This should fail
context con3 is

end;

context con4 is

end
;

-- Split declaration across lines
context
con5
is

end
context
;
