\# 📄 Product Requirements Document (PRD)  
\#\# 📌 Product Name  
\*\*DSE Live Price Checker Extension\*\*  
\---  
\#\# 🎯 1\. Objective  
Build a lightweight browser extension that allows users to:  
\* Input a \*\*stock name (symbol)\*\* and \*\*buy price\*\*  
\* Fetch \*\*live or latest trade price (LTP)\*\* from DSE  
\* Instantly calculate:  
  \* Current price (in BDT)  
  \* Profit/Loss (in BDT)  
  \* Percentage change  
\---  
\#\# 🌐 2\. Data Sources (Mandatory Links)  
The extension will fetch and parse data from:  
\* \[DSE Current Market Price (CBUL)\](https://www.dsebd.org/cbul.php?utm\_source=chatgpt.com)  
\* \[DSE Live Quotes TXT Feed\](https://www.dsebd.org/datafile/quotes.txt?utm\_source=chatgpt.com)  
\* \[DSE Closing Price Data\](https://www.dsebd.org/dse\_close\_price.php?utm\_source=chatgpt.com)  
\#\#\# Notes:  
\* \`quotes.txt\` provides structured raw data (fastest option)  
\* \`cbul.php\` provides UI-based live market watch  
\* \`dse\_close\_price.php\` for fallback / historical reference  
\---  
\#\# 👤 3\. Target Users  
\* Retail investors in Bangladesh 🇧🇩  
\* Day traders  
\* Beginners tracking simple profit/loss  
\--  
\#\# 🧩 4\. Core Features  
\#\#\# 🔍 4.1 Stock Search  
\* Input field for:  
  \* Stock Symbol (e.g., BEXIMCO, GP, SQURPHARMA)  
  \* Buy Price (BDT)  
\---  
\#\#\# 📊 4.2 Live Price Fetching  
\* Fetch from \`quotes.txt\` (primary source)  
\* Parse:  
  \* Symbol  
  \* Last Trade Price (LTP)  
\* Refresh interval:  
  \* Manual refresh  
  \* Auto-refresh every 5–10 seconds (optional)  
\---  
\#\#\# 🧮 4.3 Profit/Loss Calculator  
Formula:  
\`\`\`  
Profit/Loss \= (LTP \- Buy Price) × Quantity (optional)  
\`\`  
Display:

\* Current Price  
\* Profit/Loss (BDT)  
\* Profit/Loss (%)  
\--  
\#\#\# 🎨 4.4 UI Display  
\* Minimal popup UI (Chrome extension popup)  
\* Show:  
  \* Stock Name  
  \* Last Price  
  \* Buy Price  
  \* Profit/Loss  
\* Color coding:

  \* 🟢 Green → Profit  
  \* 🔴 Red → Loss

\---  
\#\#\# 🔔 4.5 Alerts (Phase 2\)  
\* Notify when:  
  \* Price crosses target  
  \* Profit/Loss threshold reached  
\---  
\#\# 🧱 5\. Technical Requirements  
\#\#\# 🖥️ Frontend  
\* HTML \+ CSS \+ JavaScript  
\* Chrome Extension (Manifest V3)  
\---  
\#\#\# ⚙️ Backend Logic (Client-side only)  
\* Fetch API:  
\`\`\`js  
fetch("https://www.dsebd.org/datafile/quotes.txt")  
\`\`\`  
\* Parse text file:  
  \* Likely CSV or structured text format  
  \* Split by line → find symbol → extract LTP  
\---  
\#\#\# 🔄 Data Handling  
Example flow:  
1\. Fetch \`quotes.txt\`  
2\. Split lines  
3\. Find matching stock symbol  
4\. Extract LTP field  
5\. Calculate result  
\---  
\#\# 📦 6\. Architecture

\`\`\`  
User Input → Extension Popup → Fetch quotes.txt → Parse Data → Display Result  
\`\`\`  
\---  
\#\# ⚠️ 7\. Constraints & Risks

\* ❗ DSE does not provide official public API  
\* ❗ Data format may change without notice  
\* ❗ CORS issues may occur → may need proxy  
\* ❗ Website downtime risk

\---

\#\# 🔐 8\. Permissions (Chrome Extension)

\`\`\`json  
{  
  "permissions": \["storage"\],  
  "host\_permissions": \[  
    "https://www.dsebd.org/\*"  
  \]  
}  
\`\`\`

\---  
\#\# 🚀 9\. MVP Scope  
Include:  
\* Stock search  
\* Fetch LTP from \`quotes.txt\`  
\* Profit/Loss calculation  
\* Simple UI  
Exclude (later phases):  
\* Charts  
\* Portfolio tracking  
\* Notifications  
\---  
\#\# 📈 10\. Future Enhancements  
\* 📊 Graph (price history)  
\* 💼 Multi-stock portfolio  
\* 🔔 Smart alerts  
\* 📱 Mobile version  
\* 🌐 Backend API caching---  
\#\# ✅ 11\. Success Metrics  
\* Fast response (\<2 sec)  
\* Accurate price matching  
\* Low error rate in parsing  
\* User retention (daily usage)  
\---  
\#\# 💡 12\. Example User Flow  
1\. User opens extension  
2\. Inputs:  
   \* Stock: \`GP\`  
   \* Buy Price: \`300\`  
3\. Clicks "Check"  
4\. Extension shows:  
   \* LTP: 315  
   \* Profit: \+15 BDT  
   \* Profit %: \+5%  
\---

