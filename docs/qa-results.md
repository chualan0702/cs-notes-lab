# 實作與延伸紀錄

## 2026-11-16：建立規則後實作
先建立並讀取 AGENTS.md，再建立共用版型、JSON 範本、建置程式與驗證器。初版有分頁、TLB、管線三篇筆記。實際執行結果：Built 3 notes, 5 HTML pages, 6 quiz questions；validate.py 通過 3 篇資料、6 題、5 頁、站內連結及手冊副本一致性檢查；node --check assets/app.js 通過。

## 2026-11-16：依同一份規則新增 deadlock
重新讀取 README.md、範本與既有 TLB JSON，新增 content/notes/deadlock.json。未修改共用 CSS、JavaScript 或建置程式。重新建置後自動產生死結詳情頁、首頁第 4 張卡、作業系統分類內容，以及第 7、8 題測驗。
實際執行結果：Built 4 notes, 6 HTML pages, 8 quiz questions；validate.py 通過 4 篇資料、8 題、6 頁及全部站內連結；node --check assets/app.js 通過。這證明新增主題可以只寫資料，不必重新設計頁面。

## 驗證範圍
程式驗證涵蓋 schema、答案索引、內部連結目標、六個章節與 AGENTS.md 副本。算例核對：分頁 5572 bytes 位址值、TLB 120 ns、管線 28 ns / 約 3.57 倍。瀏覽器互動與部署結果另於完成後補記，不以靜態檢查冒充實際操作。

## 公開網站驗收（2026-11-16）
GitHub Actions 完成完整專案建置與驗證，GitHub Pages 顯示網站已上線。公開網址：https://chualan0702.github.io/cs-notes-lab/ 。
瀏覽器實測：搜尋 TLB 得到 1 篇；不存在的關鍵字顯示空結果；作業系統分類顯示死結 1 篇；死結頁六章節正常。測驗未作答顯示提醒，錯答及正答各有文字回饋，返回首頁後已複習標記保留。測試手機寬度設定為 375px，瀏覽器可用內容寬度為 360px；首頁、死結頁、規則頁的 scrollWidth 與 clientWidth 均相等，沒有水平溢出。這是目前瀏覽器的驗收，不代表已涵蓋所有瀏覽器或所有無障礙情境。
初始化完成後，將一次性來源匯入流程改為持續驗證：每次 push / pull request 檢查建置、schema、站內連結、JavaScript 語法及 dist 是否與來源一致，避免未來誤用初始化流程覆蓋新增內容。
