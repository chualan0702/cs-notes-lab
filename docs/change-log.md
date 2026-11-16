# 實作與延伸紀錄

## 2026-11-16：建立規則後實作
先建立並讀取 AGENTS.md，再建立共用版型、JSON 範本、建置程式與驗證器。初版有分頁、TLB、管線三篇筆記。實際執行結果：Built 3 notes, 5 HTML pages, 6 quiz questions；validate.py 通過 3 篇資料、6 題、5 頁、站內連結及手冊副本一致性檢查；node --check assets/app.js 通過。

## 2026-11-16：依同一份規則新增 deadlock
重新讀取 README.md、範本與既有 TLB JSON，新增 content/notes/deadlock.json。未修改共用 CSS、JavaScript 或建置程式。重新建置後自動產生死結詳情頁、首頁第 4 張卡、作業系統分類內容，以及第 7、8 題測驗。
實際執行結果：Built 4 notes, 6 HTML pages, 8 quiz questions；validate.py 通過 4 篇資料、8 題、6 頁及全部站內連結；node --check assets/app.js 通過。這證明新增主題可以只寫資料，不必重新設計頁面。

## 驗證範圍
程式驗證涵蓋 schema、答案索引、內部連結目標、六個章節與 AGENTS.md 副本。算例核對：分頁 5572 bytes 位址值、TLB 120 ns、管線 28 ns / 約 3.57 倍。瀏覽器互動與部署結果另於完成後補記，不以靜態檢查冒充實際操作。
