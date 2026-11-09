{
  description = "GPU Atlas — static GPU provider catalogue, Cloudflare deploy, analytics";

  inputs.nixpkgs.url = "github:NixOS/nixpkgs/nixpkgs-unstable";

  outputs = { self, nixpkgs }:
    let
      systems = [ "aarch64-darwin" "x86_64-darwin" "aarch64-linux" "x86_64-linux" ];
      forAll = f: nixpkgs.lib.genAttrs systems (system: f nixpkgs.legacyPackages.${system});
    in {
      devShells = forAll (pkgs: {
        default = pkgs.mkShell {
          packages = [
            pkgs.python312
            pkgs.uv
            pkgs.nodejs_22
            pkgs.wrangler
            pkgs.gnumake
            pkgs.git
            pkgs.cacert
          ];
          shellHook = ''
            echo "GPU Atlas shell"
            echo "  python   $(python3 --version | cut -d' ' -f2)"
            echo "  node     $(node --version)"
            echo "  wrangler $(wrangler --version 2>/dev/null | tail -1)"
            echo "  make check · make deploy · make analytics"
          '';
        };
      });

      formatter = forAll (pkgs: pkgs.nixpkgs-fmt);
    };
}
