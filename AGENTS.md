# CS Notes Lab：給 AI 協作者的專案手冊

## 1. 目的與交付
本專案是給大學資科學生使用的繁體中文計概複習網站。目標是把「觀念、算例、易錯點、自我測驗」整理成可持續新增的知識卡。每次工作先讀本檔、README.md 與 templates/note-template.json；新增筆記時再讀一份既有 JSON。不要把任務理解成重做整個網站。
交付物：更新後的原始內容、由建置程式產生的可瀏覽網站、驗證結果與變更紀錄。公開網站不包含學號、帳密或私人課堂檔案。

## 2. 檔案責任與命名
- content/notes/<slug>.json：唯一的筆記資料來源。slug 使用小寫英文單字與連字號，例如 virtual-memory。不得重複。
- templates/note-template.json：新增內容的結構範本；保留所有欄位。
- assets/style.css、assets/app.js：共用樣式與互動；不要為新筆記複製另一套設計。
- scripts/build.py：讀取 JSON，產生 dist/index.html、dist/notes/<slug>.html、dist/rules.html，並複製靜態資源與 AGENTS.md。
- scripts/validate.py：檢查資料格式、答案範圍、slug、章節與站內連結。
- docs/change-log.md：寫明本次新增或修正、原因及實際驗證結果。
- dist/：產生成果，不得手改；修改來源後重新建置。
檔名採 kebab-case，文字檔使用 UTF-8。禁止引入 node_modules、API 金鑰、追蹤器或未授權圖片。

## 3. 頁面與視覺規範
使用原生 HTML/CSS/JavaScript 與 Python 標準函式庫建置，不需要套件安裝。網站需能部署在 GitHub Pages 的專案子路徑，所以所有站內 URL 使用相對路徑。
視覺固定使用深綠 #173c34、米白 #f6f5ef、橘色 #ed9b65，字體優先系統繁體中文字體。首頁有導覽、學習說明、搜尋、分類篩選、筆記卡與規則入口。詳細頁固定順序為：學習目標 → 核心觀念 → 例題與解析 → 常見錯誤 → 自我測驗 → 參考資料。每頁需有返回首頁入口。
手機 375px 不得出現水平捲動；按鈕可鍵盤操作、有可見焦點；表單須有 label。內容至少 16px、行高至少 1.6。不要只靠顏色表示測驗正誤。不得新增沒有作用的按鈕。

## 4. 筆記資料契約
JSON 必須包含：
- slug、title、category、summary、minutes、updated、objectives、concepts、example、mistakes、quiz、sources。
- category 僅能是「記憶體」「計算機組織」「作業系統」；增加分類需同步修改本手冊及驗證器。
- minutes 為正整數；updated 用 YYYY-MM-DD，填實際內容修改日期。
- objectives 至少 2 個字串；concepts 至少 2 個 {term, explanation} 物件。
- example 為 {question, steps, answer}，steps 至少 2 步；計算題需交代假設與單位。
- mistakes 至少 2 個字串，指出錯在哪裡與正確觀念。
- quiz 至少 2 題，每題 {question, options, answer, explanation}；options 恰好 4 個互異選項，answer 為 0 到 3 的整數索引，explanation 必須解釋答案。
- sources 至少 1 個 {label, url}，僅用 https 公開教材；筆記是原創整理，禁止整段複製來源。來源只列實際作為整理依據的教材，不虛構閱讀經驗。
內容以繁體中文撰寫，專有名詞第一次出現加英文。不可虛構成績、使用人數、測試、引用或個人學習心得；不確定的知識先確認再寫。

## 5. 新增內容 SOP
1. 回報任務理解：主題、要新增的檔案、是否需修改共用程式。
2. 複製範本到 content/notes/<slug>.json，按照上述契約填寫。
3. 對照既有筆記的深度與格式；算例手算核對，自我測驗核對答案及解析。
4. 執行 python3 scripts/build.py，再執行 python3 scripts/validate.py。首頁卡片與詳情頁由程式自動建立，不另改索引。
5. 可用瀏覽器時，實測搜尋、分類、測驗答對與答錯、顯示解析、返回首頁及手機寬度；無法做時明說，不能宣稱已測。
6. 更新 docs/change-log.md，回報修改檔案、實際通過檢查及限制。不得刪除其他筆記或整站換版。

## 6. 修改邊界與驗收
修正文案只改目標 JSON；改 schema 時必須同步範本、本檔、建置器及驗證器。localStorage 僅存本站學習完成標記，清除瀏覽器資料可能遺失，不宣稱跨裝置同步。DOM 插入使用 textContent 或建置期 HTML escaping，不把任意輸入直接送入 innerHTML。
驗收條件：資料契約全部通過、每篇詳細頁具備六個章節、首頁收錄所有筆記、站內連結沒有遺漏、無外部執行依賴、互動有明確回饋、GitHub 原始碼與部署內容相同。發布只在使用者授權範圍內，不能覆寫既有不相關專案。

## 7. 下一次可直接使用的交辦
「請先讀 AGENTS.md、README.md 和 templates/note-template.json，依現有規範新增『死結的四個必要條件』筆記，slug 使用 deadlock。保留網站設計，加入一個資源等待例子與兩題含解析的測驗，執行建置及驗證，最後列出修改檔案與檢查結果。」
