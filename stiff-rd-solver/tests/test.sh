#!/bin/bash
set -u
mkdir -p /logs/verifier

python -m pytest /tests/test_profile.py --ctrf /logs/verifier/ctrf.json -q
RC=$?

if [ "$RC" -eq 0 ]; then
  printf '1' > /logs/verifier/reward.txt
else
  printf '0' > /logs/verifier/reward.txt
fi
exit 0
