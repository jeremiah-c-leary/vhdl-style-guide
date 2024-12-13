
package foo is new my_generic_pkg
  generic map (
    g_my_generic => 2
  );

package pkg_foo is new my_generic_pkg
  generic map (
    g_my_generic => 2
  );

package foo_pkg is new my_generic_pkg
  generic map (
    g_my_generic => 2
  );
