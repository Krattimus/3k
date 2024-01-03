#!/bin/bash
curl -X POST https://www.3kpi.icu/api/area/ -H "Content-Type: application/json" -d "{\"name\" : \"$1\", \"dungeon\" : \"false\", \"room_count\" : $2, \"wizard\" : \"$3\"}"
