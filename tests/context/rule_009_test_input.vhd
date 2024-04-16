
--This should pass
context c1 is

end context c1;

--These should fail
context c1 is
end
context c1;

context
c1
is

end

context -- Some comment
c1;

context c1 is

end -- Some comment
context -- Some other comment
c1;

context c1  -- Yet another comment, comment
  -- Some comment
is

end
 -- Comment again

context c1;

-- Test with missing end context keyword

context c1 is

end;

context c2 is

end context c2;
