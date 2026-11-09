"""adicionar.py: coloca um Reel aprovado na fila.
  python adicionar.py reel05 2026-11-12T18:30:00-03:00
Copia reel05/reel05.mp4 e reel05/cover.jpg e usa a legenda do Instagram de reel05/post.md."""
import json
import os
import re
import shutil
import sys
from datetime import datetime, timezone

HERE = os.path.dirname(os.path.abspath(__file__))
FILA = os.path.join(HERE, "fila.json")
PROJETO = os.environ.get("REELS_DIR", os.path.dirname(HERE))


def main():
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    rid, quando = sys.argv[1], sys.argv[2]
    d = datetime.fromisoformat(quando)
    if d.tzinfo is None:
        sys.exit("Informe o fuso na data, por exemplo 2026-11-12T18:30:00-03:00")
    if d <= datetime.now(timezone.utc):
        sys.exit("Essa data ja passou.")

    pasta = os.path.join(PROJETO, rid)
    video, capa = os.path.join(pasta, f"{rid}.mp4"), os.path.join(pasta, "cover.jpg")
    for arq in (video, capa):
        if not os.path.exists(arq):
            sys.exit(f"Arquivo nao encontrado: {arq}")
    if os.path.getsize(video) > 100_000_000:
        sys.exit("O video passa de 100 MB.")
    with open(os.path.join(pasta, "post.md"), encoding="utf-8") as f:
        m = re.search(r"## Legenda do Instagram\s*```[^\n]*\n(.*?)\n```", f.read(), re.S)
    if not m:
        sys.exit("Nao achei a secao '## Legenda do Instagram' no post.md.")
    legenda = m.group(1).strip()
    if len(legenda) > 2200:
        sys.exit(f"Legenda com {len(legenda)} caracteres; o limite e 2200.")

    with open(FILA, encoding="utf-8") as f:
        dados = json.load(f)
    if any(i["id"] == rid for i in dados["itens"]):
        sys.exit(f"{rid} ja esta na fila.")
    destino = os.path.join(HERE, "fila", rid)
    os.makedirs(destino, exist_ok=True)
    shutil.copyfile(video, os.path.join(destino, "video.mp4"))
    shutil.copyfile(capa, os.path.join(destino, "capa.jpg"))
    dados["itens"].append({"id": rid, "quando": d.isoformat(), "status": "pendente", "legenda": legenda})
    dados["itens"].sort(key=lambda i: i["quando"])
    with open(FILA, "w", encoding="utf-8") as f:
        json.dump(dados, f, ensure_ascii=False, indent=2)
        f.write("\n")
    print(f"na fila: {rid} em {d.isoformat()} ({len(legenda)} caracteres de legenda)")


if __name__ == "__main__":
    main()
