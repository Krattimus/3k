#!/bin/bash
#curl -X POST https://www.3kpi.icu/api/area/ -H "Content-Type: application/json" -d "{\"name\" : \"$1\", \"dungeon\" : \"false\", \"room_count\" : $2, \"wizard\" : \"$3\"}"

curl --location "https://api.openai.com/v1/images/generations" \
--header "Authorization: Bearer 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" \
--header "Content-Type: application/json" \
--header "Cookie: __cf_bm=5keMMMocu7nmnRclBj7_NhPZwrf573LVJ8hoQRIU1W4-1704442402-1-ATS5+C1tXrWxA3ZlKhg5WTEc0fDKeylWjIK19O6TgahyaBaD+sgMa4LGhNqZa+KkG6nh8GcXKpmP6aYNC0wm2Ag=; _cfuvid=TZgb9Ydz7s6yky9G5BsylQejpEZ4ll1sBD_CLXQDlUE-1704442402745-0-604800000" \
--data "{
    \"prompt\" : \"$1\"
}"