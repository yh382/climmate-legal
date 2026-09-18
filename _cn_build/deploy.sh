#!/usr/bin/env bash
# Build the CN edition (yanuclimb.cn) and rsync it to the Aliyun box. See build.py next to this file.
#   _cn_build/deploy.sh              build + deploy + smoke-check
#   _cn_build/deploy.sh --build-only build into _site_cn/ and stop
# Lives under _cn_build/ (underscore dir) so GitHub Pages' Jekyll never publishes it on the global site.
# Server access: root@47.116.104.19 over SSH key (one-time `ssh-copy-id`); override with CN_HOST.
set -euo pipefail
cd "$(dirname "$0")/.."
HOST="${CN_HOST:-root@47.116.104.19}"
VENV=_cn_build/.venv
if [ ! -x "$VENV/bin/python" ]; then
  python3 -m venv "$VENV"
  "$VENV/bin/pip" install -q markdown
fi
"$VENV/bin/python" _cn_build/build.py
# guard: never rsync --delete an empty/partial build over the live site
for f in index.html privacy/index.html terms/index.html assets/styles.css; do
  [ -f "_site_cn/$f" ] || { echo "✗ _site_cn/$f missing — refusing to deploy"; exit 1; }
done
[ "${1:-}" = "--build-only" ] && exit 0
rsync -az --delete --no-owner --no-group --chmod=Du=rwx,Dgo=rx,Fu=rw,Fgo=r _site_cn/ "$HOST:/opt/climmate/www/"
for p in / /privacy/ /terms/ /third-party-sdk/; do
  printf '%-20s %s\n' "$p" "$(curl -s -o /dev/null -m 15 -w '%{http_code}' "https://yanuclimb.cn$p")"
done
