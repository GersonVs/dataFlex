#!/bin/bash
echo "Removendo as migrações"

find apps/consumer/migrations -type f ! -name '__init__.py' -exec rm {} +
find apps/market/migrations -type f ! -name '__init__.py' -exec rm {} +