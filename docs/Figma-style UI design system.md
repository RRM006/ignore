Here’s a **Figma-style UI design system \+ screen layout** for your **DSE Live Price Checker Chrome Extension** — clean, modern, and easy to implement.

---

# **🎨 1\. Design Style Direction (Figma Concept)**

Inspired by modern extension UIs:

* Minimal popup layout (like Chrome extensions)  
* Card-based design  
* Clear typography \+ strong color signals (profit/loss)

👉 Many modern tools convert UI ideas into Figma layouts with auto components and structured layers ([RocketPen \- AI Figma Generator](https://rocketpen.art/?utm_source=chatgpt.com)) — so we’ll follow a **component-based design system**.

---

# **📱 2\. Extension Popup Size**

Typical Chrome popup:

Width: 320px  
Height: 400–500px

---

# **🧱 3\. Main Screen Layout (Figma Frame)**

## **🔲 Frame: “DSE Tracker Popup”**

\----------------------------------  
| 🔵 Header                      |  
|--------------------------------|  
| 🔍 Input Section              |  
|--------------------------------|  
| 📊 Result Card               |  
|--------------------------------|  
| 🔁 Refresh / Status           |  
\----------------------------------

---

# **🧩 4\. UI Components Breakdown**

## **🔵 4.1 Header**

**Design:**

* Background: \#0F172A (dark navy)  
* Title: **“DSE Live Tracker”**  
* Font: Inter / Poppins  
* Right side:  
  * 🔄 Refresh icon

---

## **🔍 4.2 Input Section**

**Fields:**

1. **Stock Symbol Input**  
   * Placeholder: `Enter stock (e.g., GP)`  
2. **Buy Price Input**  
   * Placeholder: `Enter buy price`  
3. **Check Button**  
   * Text: `Check Price`  
   * Color: \#2563EB (blue)  
   * Rounded: 8px

---

## **📊 4.3 Result Card (Core UI)**

**Card Layout:**

\-------------------------  
| GP                    |  
|-----------------------|  
| LTP: 315 BDT          |  
| Buy: 300 BDT          |  
|-----------------------|  
| Profit: \+15 BDT       |  
| \+5.00%               |  
\-------------------------

**Design Rules:**

* Card background: \#F8FAFC  
* Border radius: 12px  
* Shadow: subtle

### **Color Logic:**

| State | Color |
| ----- | ----- |
| Profit | 🟢 \#16A34A |
| Loss | 🔴 \#DC2626 |

## **🔁 4.4 Footer / Status**

* “Last updated: 12:30 PM”  
* Small text (gray)  
* Optional spinner when loading

---

# **🎯 5\. Figma Component System**

Create reusable components:

### **🧩 Components**

* Input Field  
* Button  
* Stock Card  
* Status Text

### **📐 Spacing System**

* 8px grid  
* Padding: 16px  
* Gap: 12px

---

# **🎨 6\. Color Palette**

| Purpose | Color |
| ----- | ----- |
| Primary | \#2563EB |
| Background | \#F1F5F9 |
| Card | \#FFFFFF |
| Profit | \#16A34A |
| Loss | \#DC2626 |
| Text | \#0F172A |

---

# **🔤 7\. Typography**

| Type | Size |
| ----- | ----- |
| Title | 16–18px |
| Body | 14px |
| Small | 12px |

Font:

* Inter (recommended)

---

# **⚡ 8\. Interaction Flow (UX)**

1. User opens extension  
2. Inputs stock \+ buy price  
3. Clicks **Check Price**  
4. Loader shows  
5. Result card appears

---

# **🧪 9\. Empty & Error States**

### **Empty State**

* “Enter stock to get started”

### **Error State**

* “Stock not found”

---

# **🧠 10\. Pro UX Tips (Important)**

* Auto-uppercase stock symbol  
* Remember last input (local storage)  
* Show loading spinner  
* Debounce API calls

---

# **🧾 11\. Figma Frame Naming**

Frame: DSE Extension  
 ├── Header  
 ├── Input Section  
 ├── Result Card  
 ├── Footer

---

