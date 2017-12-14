
architecture ARCH of ENTITY1 is

  type a is (B, C, D, E ,F, G);

   type a is ( B, C,
    D, E,
    -- This is a comment
    F, G);

 type a is range 0 to 9;

begin

end architecture ARCH;

package PACK is

  type A is (B, C, D, E ,F, G);

  type  a is  (B, C,
    D, E,
    -- This is a comment
      F, G);

  TYPE a is range 0 to 9;

  type a  is (--This is a comment
    A, B,
    -- comment
    C
  );

  a <= b;
  type a is (
    A, B,

    -- comment
    C
  );
  a <= b;

    subtype a is range 0 to 9;

begin

end package PACK;

