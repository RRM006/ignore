const meals = [
  {
    time: "ভোর ৬টা",
    name: "হাঁটার আগে",
    kcal: 0,
    tag: "pre-walk",
    items: [
      { name: "গরম পানি + লেবুর রস", amount: "১ গ্লাস (২৫০ ml) + ১টা লেবু" },
    ],
    note: "খালি পেটে হাঁটা fat burn করে বেশি — ভারী কিছু খাবে না",
  },
  {
    time: "ভোর ৬–৭টা",
    name: "Exercise",
    kcal: null,
    tag: "exercise",
    items: [
      { name: "হাঁটা (দ্রুত)", amount: "২০ মিনিট" },
      { name: "জগিং", amount: "১৫ মিনিট" },
      { name: "দৌড় (৫+৫)", amount: "১০ মিনিট" },
      { name: "Freehand (গোসলের আগে)", amount: "১৫–২০ মিনিট" },
    ],
    note: "Exercise শেষে ৫০০ ml পানি খাবে",
  },
  {
    time: "সকাল ৮টা",
    name: "নাস্তা",
    kcal: 350,
    tag: "meal",
    items: [
      { name: "Omega-3 সেদ্ধ ডিম (গোটা)", amount: "২টা (১০০ গ্রাম)" },
      { name: "ডিমের সাদা অংশ", amount: "১টা (৩০ গ্রাম)" },
      { name: "আটার রুটি (তেল ছাড়া)", amount: "২টা (৬০ গ্রাম আটা)" },
      { name: "আদা চা / গ্রিন টি", amount: "১ কাপ — চিনি নেই" },
    ],
    note: null,
  },
  {
    time: "দুপুর ১টা",
    name: "মূল খাবার",
    kcal: 550,
    tag: "meal",
    items: [
      { name: "সালাদ — শসা + টমেটো + পেঁয়াজ (আগে খাবে)", amount: "২৫০ গ্রাম" },
      { name: "লাল চালের ভাত (রান্না)", amount: "১৫০ গ্রাম" },
      { name: "মাছ বা চিকেন ব্রেস্ট (সেদ্ধ/গ্রিল)", amount: "১২০ গ্রাম" },
      { name: "মসুর ডাল (রান্না)", amount: "১৫০ গ্রাম" },
      { name: "শাক বা সবজি (করলা/লাউ/ডাটা শাক)", amount: "১০০ গ্রাম" },
      { name: "সরিষার তেল (রান্নায় মোট)", amount: "৫ গ্রাম (১ চা চামচ)" },
    ],
    note: "সালাদ সবার আগে — blood sugar কম বাড়বে",
  },
  {
    time: "দুপুর ২টা",
    name: "খাবারের পরে",
    kcal: 100,
    tag: "meal",
    items: [
      { name: "টক দই — চিনি ছাড়া, low-fat", amount: "১৫০ গ্রাম (১ কাপ)" },
    ],
    note: "দুপুরের খাবারের ৩০ মিনিট পরে খাবে",
  },
  {
    time: "বিকাল ৪টা",
    name: "হালকা নাস্তা",
    kcal: 100,
    tag: "meal",
    items: [
      { name: "কাঠবাদাম", amount: "৮টা (১২ গ্রাম)" },
      { name: "আখরোট", amount: "৪টা (১৫ গ্রাম)" },
      { name: "আদা-হলুদ চা", amount: "১ কাপ — চিনি নেই" },
    ],
    note: null,
  },
  {
    time: "রাত ৭–৭:৩০টা",
    name: "রাতের খাবার (হালকা)",
    kcal: 300,
    tag: "meal",
    items: [
      { name: "আটার রুটি (তেল ছাড়া)", amount: "১টা (৩০ গ্রাম আটা)" },
      { name: "মাছ বা চিকেন ব্রেস্ট (সেদ্ধ/গ্রিল)", amount: "৮০ গ্রাম" },
      { name: "করলা ভাজি (প্রতিদিন অবশ্যই)", amount: "১০০ গ্রাম" },
      { name: "মসুর ডাল (রান্না)", amount: "১০০ গ্রাম" },
      { name: "যেকোনো সবজি (লাউ/শিম/পটল)", amount: "১০০ গ্রাম" },
      { name: "সরিষার তেল (রান্নায় মোট)", amount: "৩ গ্রাম (আধা চা চামচ)" },
    ],
    note: "৮:৩০ এর মধ্যে শেষ করবে — এরপর কিছু খাবে না",
  },
  {
    time: "রাত ১০টা",
    name: "ঘুমানোর আগে",
    kcal: 0,
    tag: "night",
    items: [
      { name: "গরম পানি", amount: "১ গ্লাস (২৫০ ml)" },
      { name: "মেথি বীজ — পানিতে ভিজিয়ে রাখো", amount: "১ চা চামচ (সকালে খাবে)" },
      { name: "Vitamin D supplement", amount: "ডাক্তারের পরামর্শ অনুযায়ী" },
    ],
    note: "রাত ১১টার মধ্যে ঘুমাবে — fat burn ঘুমে হয়",
  },
];

const tagColors = {
  "pre-walk": { bg: "#f0f9ff", border: "#bae6fd", label: "#0369a1" },
  "exercise":  { bg: "#f0fdf4", border: "#86efac", label: "#166534" },
  "meal":      { bg: "#ffffff", border: "#e2e8f0", label: "#1e293b" },
  "night":     { bg: "#f8f8f8", border: "#e2e8f0", label: "#475569" },
};

const kcalDist = [
  { time: "নাস্তা ৮টা",    kcal: 350, pct: 24 },
  { time: "দুপুর ১টা",     kcal: 550, pct: 38 },
  { time: "টক দই ২টা",    kcal: 100, pct: 7  },
  { time: "বিকাল ৪টা",    kcal: 100, pct: 7  },
  { time: "রাত ৭:৩০টা",   kcal: 300, pct: 21 },
  { time: "বিবিধ",          kcal: 0,   pct: 3  },
];

const banned = [
  "চিনি ও সব ধরনের মিষ্টি",
  "ভাজা যেকোনো কিছু",
  "গরুর মাংস ও অর্গান মিট",
  "ইলিশ ও চিংড়ি",
  "কোল্ড ড্রিংক ও ফলের জুস",
  "বিরিয়ানি / পোলাও",
  "বিস্কুট / কেক / পাউরুটি",
  "পরোটা / লুচি",
  "ঘি / মাখন / ফুল ক্রিম দুধ",
  "রাতে ভাত",
];

export default function MealChart() {
  const totalKcal = meals.reduce((s, m) => s + (m.kcal || 0), 0);

  return (
    <div style={{ fontFamily: "'Segoe UI', Arial, sans-serif", maxWidth: 680, margin: "0 auto", padding: 14, background: "#f7f8fc", minHeight: "100vh" }}>

      {/* Header */}
      <div style={{ background: "#1a2a4a", borderRadius: 12, padding: "16px 20px", marginBottom: 12, textAlign: "center" }}>
        <div style={{ color: "white", fontSize: 18, fontWeight: 700 }}>মাশরাফী — দৈনিক খাবার চার্ট</div>
        <div style={{ color: "#93c5fd", fontSize: 12, marginTop: 4 }}>বয়স ২৫ · ওজন ৮৩ kg · উচ্চতা ৫'৪" · BMI 31.4 · লক্ষ্য ৬৮–৭০ kg</div>
        <div style={{ marginTop: 8, display: "flex", justifyContent: "center", gap: 6, flexWrap: "wrap" }}>
          {["Fatty Liver","Pre-Diabetic","High Cholesterol","High Uric Acid","Vit D ঘাটতি"].map(c => (
            <span key={c} style={{ background: "rgba(255,255,255,0.13)", color: "#e0eaff", fontSize: 11, padding: "2px 9px", borderRadius: 20 }}>{c}</span>
          ))}
        </div>
      </div>

      {/* Calorie summary */}
      <div style={{ background: "white", border: "1.5px solid #e2e8f0", borderRadius: 10, padding: "12px 16px", marginBottom: 12 }}>
        <div style={{ display: "flex", alignItems: "center", justifyContent: "space-between", marginBottom: 10 }}>
          <div>
            <span style={{ fontSize: 26, fontWeight: 800, color: "#1a2a4a" }}>{totalKcal}</span>
            <span style={{ fontSize: 13, color: "#64748b", marginLeft: 5 }}>kcal / দিন</span>
          </div>
          <div style={{ display: "flex", gap: 8 }}>
            {[["প্রোটিন","~110g"],["কার্বস","~170g"],["ফ্যাট","~48g"]].map(([l,v]) => (
              <div key={l} style={{ background: "#f1f5f9", borderRadius: 8, padding: "5px 10px", textAlign: "center" }}>
                <div style={{ fontSize: 12, fontWeight: 700, color: "#1a2a4a" }}>{v}</div>
                <div style={{ fontSize: 10, color: "#94a3b8" }}>{l}</div>
              </div>
            ))}
          </div>
        </div>
        {/* kcal bar */}
        <div style={{ fontSize: 11, color: "#64748b", marginBottom: 4 }}>ক্যালরি বন্টন</div>
        <div style={{ display: "flex", height: 18, borderRadius: 6, overflow: "hidden", gap: 1 }}>
          {kcalDist.filter(d => d.kcal > 0).map((d, i) => {
            const colors = ["#3b82f6","#10b981","#8b5cf6","#f59e0b","#ef4444"];
            return (
              <div key={i} title={`${d.time}: ${d.kcal} kcal`}
                style={{ width: `${d.pct}%`, background: colors[i % colors.length], display: "flex", alignItems: "center", justifyContent: "center" }}>
                <span style={{ color: "white", fontSize: 9, fontWeight: 700 }}>{d.kcal}</span>
              </div>
            );
          })}
        </div>
        <div style={{ display: "flex", gap: 8, marginTop: 5, flexWrap: "wrap" }}>
          {kcalDist.filter(d => d.kcal > 0).map((d, i) => {
            const colors = ["#3b82f6","#10b981","#8b5cf6","#f59e0b","#ef4444"];
            return (
              <div key={i} style={{ display: "flex", alignItems: "center", gap: 3 }}>
                <div style={{ width: 8, height: 8, borderRadius: 2, background: colors[i % colors.length] }} />
                <span style={{ fontSize: 10, color: "#64748b" }}>{d.time}</span>
              </div>
            );
          })}
        </div>
      </div>

      {/* Meal cards */}
      {meals.map((meal, i) => {
        const tc = tagColors[meal.tag] || tagColors["meal"];
        return (
          <div key={i} style={{ background: "white", border: `1.5px solid ${tc.border}`, borderRadius: 10, marginBottom: 8, overflow: "hidden" }}>
            <div style={{ background: tc.bg, padding: "9px 14px", display: "flex", alignItems: "center", justifyContent: "space-between", borderBottom: `1px solid ${tc.border}` }}>
              <div style={{ display: "flex", alignItems: "center", gap: 8 }}>
                <span style={{ background: "#1a2a4a", color: "white", fontSize: 10, fontWeight: 700, padding: "2px 9px", borderRadius: 20, whiteSpace: "nowrap" }}>{meal.time}</span>
                <span style={{ fontSize: 13, fontWeight: 700, color: "#1a2a4a" }}>{meal.name}</span>
              </div>
              {meal.kcal > 0 && (
                <span style={{ fontSize: 13, fontWeight: 700, color: tc.label, background: "white", padding: "2px 10px", borderRadius: 20, border: `1px solid ${tc.border}` }}>{meal.kcal} kcal</span>
              )}
              {meal.kcal === null && (
                <span style={{ fontSize: 11, color: "#166534", background: "#dcfce7", padding: "2px 10px", borderRadius: 20 }}>~280 kcal burn</span>
              )}
            </div>
            <div style={{ padding: "7px 14px" }}>
              {meal.items.map((item, j) => (
                <div key={j} style={{ display: "flex", justifyContent: "space-between", alignItems: "center", padding: "5px 0", borderBottom: j < meal.items.length - 1 ? "1px dashed #f1f5f9" : "none" }}>
                  <span style={{ fontSize: 13, color: "#334155" }}>
                    {meal.tag === "exercise" ? "⏱" : "▸"} {item.name}
                  </span>
                  <span style={{ fontSize: 12, fontWeight: 600, color: "#1a2a4a", background: "#f0f4ff", padding: "2px 9px", borderRadius: 6, whiteSpace: "nowrap", marginLeft: 8 }}>{item.amount}</span>
                </div>
              ))}
              {meal.note && (
                <div style={{ marginTop: 6, background: "#fffbea", border: "1px solid #fde68a", borderRadius: 6, padding: "5px 10px", fontSize: 11, color: "#78350f" }}>
                  ⚠ {meal.note}
                </div>
              )}
            </div>
          </div>
        );
      })}

      {/* Water */}
      <div style={{ background: "#eff6ff", border: "1.5px solid #93c5fd", borderRadius: 10, padding: "10px 14px", marginBottom: 10 }}>
        <div style={{ fontSize: 13, fontWeight: 700, color: "#1d4ed8", marginBottom: 4 }}>💧 পানি — সারাদিন ৩.৫ থেকে ৪ লিটার</div>
        <div style={{ display: "flex", gap: 6, flexWrap: "wrap" }}>
          {[["Exercise পরে","৫০০ ml"],["সকাল","১ লিটার"],["দুপুর","১.৫ লিটার"],["বিকাল ও রাত","১ লিটার"]].map(([t,v]) => (
            <div key={t} style={{ background: "white", border: "1px solid #bfdbfe", borderRadius: 7, padding: "4px 10px", textAlign: "center" }}>
              <div style={{ fontSize: 12, fontWeight: 700, color: "#1d4ed8" }}>{v}</div>
              <div style={{ fontSize: 10, color: "#64748b" }}>{t}</div>
            </div>
          ))}
        </div>
        <div style={{ fontSize: 11, color: "#1e40af", marginTop: 5 }}>Uric acid 8.6 — পানি ছাড়া এটা কমবে না</div>
      </div>

      {/* Banned */}
      <div style={{ background: "white", border: "1.5px solid #fecaca", borderRadius: 10, overflow: "hidden", marginBottom: 10 }}>
        <div style={{ background: "#fef2f2", padding: "8px 14px", borderBottom: "1px solid #fecaca" }}>
          <span style={{ fontSize: 13, fontWeight: 700, color: "#b91c1c" }}>✗ যা একদম খাবে না</span>
        </div>
        <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", padding: "4px 8px" }}>
          {banned.map((b, i) => (
            <div key={i} style={{ fontSize: 12, color: "#b91c1c", padding: "4px 8px", borderBottom: i < banned.length - 2 ? "1px dashed #fee2e2" : "none" }}>
              ✗ {b}
            </div>
          ))}
        </div>
      </div>

      {/* Weekly fish rotation */}
      <div style={{ background: "white", border: "1.5px solid #d1fae5", borderRadius: 10, padding: "10px 14px", marginBottom: 10 }}>
        <div style={{ fontSize: 13, fontWeight: 700, color: "#065f46", marginBottom: 6 }}>🐟 সপ্তাহে মাছ ঘুরিয়ে খাবে</div>
        <div style={{ display: "flex", gap: 6, flexWrap: "wrap" }}>
          {["রুই","কাতলা","তেলাপিয়া","পাবদা","শোল","টেংরা","বেলে"].map(f => (
            <span key={f} style={{ background: "#ecfdf5", border: "1px solid #a7f3d0", color: "#065f46", fontSize: 12, padding: "3px 10px", borderRadius: 20 }}>{f}</span>
          ))}
        </div>
        <div style={{ fontSize: 11, color: "#64748b", marginTop: 5 }}>ইলিশ ও চিংড়ি খাবে না — uric acid বাড়াবে</div>
      </div>

      {/* Footer */}
      <div style={{ background: "#1a2a4a", borderRadius: 10, padding: "10px 16px", textAlign: "center" }}>
        <div style={{ color: "#93c5fd", fontSize: 11, lineHeight: 1.7 }}>
          ডাক্তার দেখানোর আগে করো → Liver Ultrasound · HbA1c · HBsAg · Anti-HCV · Fasting Insulin · Urine Microalbumin
        </div>
        <div style={{ color: "white", fontSize: 12, fontWeight: 600, marginTop: 6 }}>
          প্রতি সপ্তাহে ওজন মাপবে — মাসে ৩–৩.৫ kg কমলে সঠিক পথে আছো
        </div>
      </div>
    </div>
  );
}
