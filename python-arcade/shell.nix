# Use this file with nix-shell or similar tools; see https://nixos.org/
with import <nixpkgs> {};

mkShell {
  buildInputs = [ python3 ];

  shellHook = ''
    export LD_LIBRARY_PATH="${pkgs.libglvnd}/lib:${pkgs.xorg.libX11}/lib:${pkgs.freetype}/lib:${pkgs.fontconfig.lib}/lib";
    . .venv/bin/activate # Guide: https://api.arcade.academy/en/latest/install/linux.html
  '';
}
