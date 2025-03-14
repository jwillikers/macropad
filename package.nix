{
  stdenvNoCC,
}:
stdenvNoCC.mkDerivation {
  pname = "macropad";
  version = "0.1.0";

  src = ./.;

  installPhase = ''
    runHook preInstall
    install -D --mode=0644 --target-directory=$out/bin code.py
    runHook postInstall
  '';
}
