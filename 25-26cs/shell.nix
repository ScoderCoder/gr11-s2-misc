# generated flake to install pygame for the files in this repo which need pygame

let
    pkgs = import <nixpkgs> { };
in pkgs.mkShell {
        packages = [
            (pkgs.python3.withPackages (python-pkgs: with python-pkgs; [
                pygame-ce # community edition
            ]))
        ];
    }

