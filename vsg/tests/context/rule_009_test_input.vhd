
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

context

end -- Some comment
context -- Some other comment
c1;

context c1  -- Yet another commet
  -- Some comment
is

end 
 -- Comment again

context c1;

-- Test with missing end context keyword

context c1 is

end;

