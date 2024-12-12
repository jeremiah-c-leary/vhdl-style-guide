
package my_pkg is new my_generic_pkg
  generic map (
    g_my_generic => 2
  );

package my_pkg is new MY_GENERIC_PKG
  generic map (
    g_my_generic => 2
  );
