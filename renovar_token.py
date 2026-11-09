"""renovar_token.py: pede ao Instagram um token renovado e o entrega so pela saida padrao,
que o workflow passa direto para o segredo do GitHub. Nunca aparece no registro."""
import json
import os
import sys
import urllib.error
import urllib.parse
import urllib.request

API = os.environ.get("IG_API_BASE", "https://graph.instagram.com").rstrip("/")
q = urllib.parse.urlencode({"grant_type": "ig_refresh_token", "access_token": os.environ["IG_TOKEN"]})
try:
    with urllib.request.urlopen(f"{API}/refresh_access_token?{q}", timeout=60) as r:
        novo = json.load(r)["access_token"]
except urllib.error.HTTPError as e:
    sys.exit(f"Instagram recusou a renovacao: HTTP {e.code}")
except (urllib.error.URLError, TimeoutError, KeyError, json.JSONDecodeError) as e:
    sys.exit(f"Falha ao renovar: {type(e).__name__}")
sys.stdout.write(novo)
