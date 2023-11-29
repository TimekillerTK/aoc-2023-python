{ pkgs, ... }:

{
  # https://devenv.sh/basics/

  # EnvVars
  env.GREET = "aoc-2023-python";

  # https://devenv.sh/scripts/
  scripts.hello.exec = "echo Environment $GREET";

  enterShell = ''
    hello
  '';

  # https://devenv.sh/languages/
  languages.python = {
    enable = true;
    version = "3.11.6";
    poetry = {
      enable = true;
      activate.enable = true;
      install.enable = true;
    };
  };

  # https://devenv.sh/pre-commit-hooks/
  # pre-commit.hooks.shellcheck.enable = true;

  # https://devenv.sh/processes/
  # processes.ping.exec = "ping example.com";

  # See full reference at https://devenv.sh/reference/options/
}