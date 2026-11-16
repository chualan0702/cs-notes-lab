# CS Notes Lab | 資科學習筆記

可延伸的繁體中文計概筆記網站。以 AGENTS.md 管理 AI 的工作方式，以 JSON 管理內容，以 Python 標準函式庫產生靜態網站。學習者可搜尋、篩選、作答並標記已複習；不需要登入，也沒有外部執行依賴。

## 從這裡開始
AI 協作者請先讀 [AGENTS.md](AGENTS.md) 與 [筆記範本](templates/note-template.json)。

```sh
python3 scripts/build.py
python3 scripts/validate.py
python3 -m http.server 8000 --directory dist
```

瀏覽 http://localhost:8000。新增筆記只需在 content/notes/ 新增符合範本的 JSON，再執行建置與驗證。詳細格式、開發順序、修改界線與驗收標準都在 AGENTS.md。

## 專案結構
- AGENTS.md：AI 工作規則及驗收契約。
- content/notes/：原創整理的筆記資料；每篇包含六個固定章節。
- templates/：可重用的內容範本。
- assets/：共用樣式、搜尋、分類、測驗與本機複習標記。
- scripts/：靜態建置與資料/連結驗證。
- docs/change-log.md：實際開發與延伸驗證紀錄。
- dist/：完整可部署成果；不可直接修改。

## GitHub Pages
Repository Settings → Pages → Deploy from a branch → main / (root)。根目錄 index.html 會轉向 dist/index.html；內部連結均為相對路徑，適用專案子目錄。GitHub 網頁編輯器也能新增 JSON，但修改後要重新執行 Python 建置並上傳 dist。

## 工作分工與限制
本專案由 ChatGPT 協助撰寫規則、原創整理學習內容與實作；算例為自行設計的教學例子，參考資料連向公開教材。不是校方官方講義，也沒有使用者成績或雲端同步。已複習標記只保留在目前瀏覽器。詳細測試結果以 docs/change-log.md 為準。
