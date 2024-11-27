
architecture RTL of ENTITY_NAME is

  --
  -- full_type_declaration ::=
  --   type identifier is type_definition;
  --
  -- type_definition ::=
  --    scalar_type_definition
  --  | composite_type_definition
  --  | access_type_definition
  --  | file_type_definition
  --  | protected_type_definition
  --
  -- scalar_type_definition ::=
  --    enumeration_type_definition
  --  | integer_type_definition
  --  | floating_type_definition
  --  | physical_type_definition



  -- [full-type_declaration][type_definition][scalar_type_definition][enumeration_type_definition]

  type T_SIM_TEST_STATUS is (
    SIM_TEST_STATUS_CREATED,
    SIM_TEST_STATUS_ACTIVE,
    SIM_TEST_STATUS_ENDED,
    SIM_TEST_STATUS_ZOMBI
  );

  -- [full-type_declaration][type_definition][scalar_type_definition][integer_type_definition]
  type my_type is range 0 to 5;

  type my_type is range -10 to -5;

  -- [full-type_declaration][type_definition][scalar_type_definition][floating_type_definition]
  type my_type is range 0.156 to 5.679;

  type my_type is range -10.45 to -5.99;

  -- [full-type_declaration][type_definition][scalar_type_definition][physical_type_definition]
  type my_type is range 0 to 20 units
    primary_unit_declaration;
  end units;

  type my_type is range 0 to 20 units
    primary_unit_declaration;
  end units physical_type_simple_name;

  type my_type is range 0 to 20 units
    pud;
    sud = 10 pud;
  end units physical_type_simple_name;

  type my_type is range 0 to 20 units
    pud;
    sud1 = 10 pud;
    sud2 = 10 sud1;
    sud3 = 10 sud2;
  end units physical_type_simple_name;

  type EXAMPLE_T is record
    axis : m_axis_o(0)'SUBTYPE;
  end record EXAMPLE_T;

begin

end architecture RTL;
