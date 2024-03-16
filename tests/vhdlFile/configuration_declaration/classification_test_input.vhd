
configuration blah of blah is
end blah;

configuration blah of blah is
  for beh
  end for beh;
end blah;

configuration blah of blah is
  use blah.blah.blah;
end blah;

configuration blah of blah is
  attribute attribute_designator of entity_designator : entity is 0;
end blah;

configuration blah of blah is
  group identifier : group_template_name ( group_constituent, group_constituent );
end blah;

configuration blah of blah is
  use blah.blah.blah;
  attribute attribute_designator of entity_designator : entity is 0;
  group identifier : group_template_name ( group_constituent, group_constituent );
  use blah.blah.blah;
  group identifier : group_template_name ( group_constituent, group_constituent );
  attribute attribute_designator of entity_designator : entity is 0;
end blah;

configuration blah of blah is
  for generate_statement_label ( generate_specification )
  end for;
end configuration blah;

configuration blah of blah is
  for beh
      use blah.blah.blah;
      use my.my.my;
  end for;
end configuration blah;

configuration blah of blah is
  for beh
      use blah.blah.blah;
      for beh2
      end for;
  end for;
end configuration blah;

configuration blah of blah is
  for beh
      use blah.blah.blah;
      for all : component_name
      end for;
  end for;
end configuration blah;

configuration blah of blah is
  for beh
      use blah.blah.blah;
      for others : component_name
      end for;
  end for;
end configuration blah;

configuration blah of blah is
  for beh
      use blah.blah.blah;
      for instantiation_label : component_name
      end for;
  end for;
end configuration blah;

configuration blah of blah is
  for beh
      use blah.blah.blah;
      for instantiation_label : component_name
         use open;
      end for;
  end for;
end configuration blah;

configuration blah of blah is
  for beh
      use blah.blah.blah;
      for instantiation_label : component_name
         use configuration configuration_name;
      end for;
  end for;
end configuration blah;

configuration blah of blah is
  for beh
      use blah.blah.blah;
      for instantiation_label : component_name
         use entity entity_name;
      end for;
  end for;
end configuration blah;

configuration blah of blah is
  for beh
      use blah.blah.blah;
      for instantiation_label : component_name
         use entity entity_name(architecture_name);
      end for;
  end for;
end configuration blah;

configuration blah of blah is
  for beh
      use blah.blah.blah;
      for instantiation_label : component_name
          generic map (
             formal_part => actual_part,
             actual_part
          );
      end for;
  end for;
end configuration blah;

configuration blah of blah is
  for beh
      use blah.blah.blah;
      for instantiation_label : component_name
          port map (
             formal_part => actual_part,
             actual_part
          );
      end for;
  end for;
end configuration blah;

configuration blah of blah is
  for beh
      use blah.blah.blah;
      for instantiation_label : component_name
         use entity entity_name(architecture_name)
          generic map (
             formal_part => actual_part,
             actual_part
          )
          port map (
             formal_part => actual_part,
             actual_part
          );
          for beh2
              use blah2.blah2.blah2;
              for instantiation_label : component_name
                 use entity entity_name2(architecture_name2)
                  generic map (
                     formal_part2 => actual_part2,
                     actual_part2
                  )
                  port map (
                     formal_part2 => actual_part2,
                     actual_part2
                  );
              end for;
          end for;
      end for;
  end for;
end configuration blah;
