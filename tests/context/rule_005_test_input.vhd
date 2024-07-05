
--This should pass
context c1 is

end context c1;

--These should fail
context
c1 is
end context c1;

context
 c1
is

end context c1;

context
 c1  -- Some comment
is

end context c1;

context  -- Yet another comment, comment
 c1  -- Some comment
is

end context c1;
