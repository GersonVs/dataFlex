#!/bin/bash
echo "Removendo as migrações"

find apps/authentication/migrations -type f ! -name '__init__.py' -exec rm {} +
find apps/market/migrations -type f ! -name '__init__.py' -exec rm {} +