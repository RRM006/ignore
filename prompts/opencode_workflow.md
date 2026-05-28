# 🤖 opencode Daily Workflow Guide
> Save this in: `my-dev-journey/_meta/opencode_workflow.md`
> Read this EVERY day before starting. This is how you use AI without it hallucinating, forgetting, or going off track.

---

## 🧠 The Core Problem (Read This First)

AI has NO memory between sessions. Every time you start opencode, it starts completely fresh — it doesn't remember you, your project, your rules, or what you did yesterday.

This means YOU are responsible for:
1. **Telling it where you are** — every single session
2. **Telling it the rules** — every single session
3. **Making it write logs** — so you have a record
4. **Checking it hasn't gone off track** — while you work
5. **Telling it to summarize** — before you stop

This file teaches you exactly how to do all 5.

---

## 📁 What Files to Give opencode

Every session, opencode needs to read these files IN THIS ORDER:

| # | File | Why opencode needs it |
|---|------|----------------------|
| 1 | `_meta/context_engineering_master.md` | Rules for how to teach you. The most important file. |
| 2 | `_meta/historychat.md` | Last 2–3 sessions — so it knows what you did before |
| 3 | `_meta/chatlog.md` | Today's session log — it will write to this |
| 4 | `_meta/skill.md` | Your exact skill level — so it doesn't over/under explain |
| 5 | `_meta/plan.md` | The roadmap — so it knows what phase and week you're on |

You do NOT need to give it `README.md` every session — only on Day 1.

---

## ⚡ PART 1 — How to Start opencode

### Step 1 — Open your terminal and go to your project folder

```bash
cd Desktop/my-dev-journey
```

Always run opencode from INSIDE your project folder. This is how it can see your files.

### Step 2 — Start opencode

```bash
opencode
```

A chat interface opens inside your terminal.

### Step 3 — Paste the SESSION OPENER (copy this every day, fill in the blanks)

```
=== SESSION START ===

STEP 1 — READ THESE FILES FIRST (do not respond until you have read all of them):
- _meta/context_engineering_master.md  ← your rules. Follow ALL of them.
- _meta/historychat.md                 ← read the last 2-3 session blocks
- _meta/chatlog.md                     ← today's session log. You will write to this.
- _meta/skill.md                       ← my exact skill level. Never assume I know more.
- _meta/plan.md                        ← my roadmap. Know what week and phase I'm on.

STEP 2 — CONFIRM you read them by telling me:
- What phase and week am I on right now?
- What did I do in my last session?
- What is my skill level in [the area we're working on today]?
- What is TODAY's goal based on the plan?

STEP 3 — TODAY'S SESSION CONTEXT:
- Date: [FILL IN: e.g. 2025-06-01]
- Project: [FILL IN: e.g. "Phase 0 Setup" or "Project 1 — Landing Page"]
- Last thing I did: [FILL IN: copy 2-3 lines from historychat.md OR write "First session ever"]
- Today's goal: [FILL IN: e.g. "Set up my folder structure and push to GitHub"]
- I am stuck on / confused about: [FILL IN: or write "Nothing yet"]
- My current code: [FILL IN: paste relevant code OR write "Starting fresh"]

STEP 4 — RULES REMINDER (always follow these):
- Explain EVERY line of code. What it does. Why it's there. What breaks if I remove it.
- One step at a time. Wait for me to say "done" before moving to the next step.
- After every working feature, remind me to: git add . && git commit -m "message" && git push
- Never give me a wall of code. Break it into the smallest possible pieces.
- If I am confused, slow down and use a simpler analogy.
- At the END of this session, update _meta/chatlog.md with the full session summary.

Now confirm you read everything and tell me the 4 things from STEP 2.
=== END ===
```

**If opencode confirms correctly → you're ready to work.**
**If it gets something wrong → paste the SESSION OPENER again and say "Re-read the files."**

---

## 📅 PART 2 — What to Do Every Day (Full Daily Workflow)

```
BEFORE YOU START (5 minutes)
  ↓
1. Open historychat.md → read your last session summary
2. Open plan.md → check what week you're on and today's task
3. Open chatlog.md → create a new session block at the top of Part 1
   (copy the template from inside chatlog.md)
  ↓
START opencode
  ↓
4. cd Desktop/my-dev-journey
5. opencode
6. Paste the SESSION OPENER (fill in the blanks)
7. Wait for opencode to confirm it read all files
  ↓
DURING SESSION (2-3 hours)
  ↓
8. Work step by step — one task at a time
9. Use the CHECK-IN message every 30-45 minutes (see Part 3)
10. git commit after every working feature
11. Add notes to chatlog.md as you go
  ↓
END OF SESSION (15 minutes)
  ↓
12. Paste the SESSION CLOSER (see Part 4) — makes AI write the logs
13. Copy SUMMARY BLOCK from chatlog.md → paste into historychat.md
14. git push everything
15. Close opencode
```

---

## 🔄 PART 3 — How to Talk to opencode While Working

### To start a task

```
I want to [describe what you want to build in plain English].
Start by explaining what we need to do BEFORE writing any code.
Then build it step by step — one piece at a time.
Wait for me to say "done" or "I understand" before moving on.
```

### To understand code it wrote

```
Explain every line of this code:
- What does this line do?
- Why is it needed here?
- What happens if I remove it?
- Is there another way to do this?
```

### To check if you understood

```
I'm going to explain this back to you in my own words.
Tell me if I understood it correctly or where I went wrong:
[write your explanation here]
```

### When you're confused

```
I don't understand [specific thing].
Explain it like I have never heard of it before.
Use a real-life analogy first, then show me the code.
```

### When something breaks

```
I got this error: [paste the EXACT error message]
Do NOT just fix it. First explain:
1. What caused this error?
2. Why did it happen?
3. What does the fix do and why does it work?
Then fix it step by step.
```

### When you want an alternative approach

```
Is there another way to do what we just built?
Show me one alternative and explain the difference in simple terms.
Which one would a real company use and why?
```

---

## 🔒 PART 4 — How to Prevent Hallucination and Keep AI on Track

Hallucination = AI confidently tells you something wrong, or invents code that doesn't work.
This happens when AI "guesses" instead of using your actual files.

### Rule 1 — Always make it CONFIRM before starting

Never let opencode just start working. Always make it confirm what it read:

```
Before you write any code — tell me:
1. What phase and week am I on?
2. What is my skill level in this area?
3. What exactly are we building today?
If any of these are wrong, stop and I'll correct you.
```

### Rule 2 — The 30-minute CHECK-IN (paste this every 30-45 minutes)

```
=== CHECK-IN ===
Stop and tell me:
1. What have we done so far in this session?
2. What step are we on right now?
3. What is the next step after this?
4. Are we still on track with today's goal: [repeat your goal here]?
5. Is there anything I should understand before we continue?
=== END ===
```

This forces the AI to "reset" and confirm it hasn't drifted.

### Rule 3 — If it writes code you don't understand, STOP IT

```
Wait. Before we continue — I don't understand what we just wrote.
Do not add anything new yet.
Go back and explain [specific part] in the simplest way possible.
```

### Rule 4 — If it seems to be going in the wrong direction

```
Stop. I think we might be going off track.
Re-read _meta/plan.md and _meta/context_engineering_master.md.
Today's goal was: [repeat your goal].
Are we still building toward that? If not, what should we change?
```

### Rule 5 — Never let it write more than 20-30 lines without explaining

```
Stop before writing more code.
Explain what you're about to write and WHY before you write it.
I want to understand the plan before I see the code.
```

---

## 📝 PART 5 — How to Make AI Log Everything Automatically

At the END of every session, paste this SESSION CLOSER. This tells opencode to write the logs for you.

```
=== SESSION CLOSER ===

We are done for today. Before I close, do these 4 things IN ORDER:

THING 1 — Update _meta/chatlog.md
Fill in ALL the sections in today's session block (Part 1):
- What I Actually Did (bullet points of everything we built)
- What I Learned (explain each concept in simple words a beginner would use)
- What Confused Me (be honest — what was hard today)
- Blockers (any errors we hit and how we fixed them)
- Files Changed (list every file we created or edited and why)
- Goal for Next Session (what should I start with next time?)

THING 2 — Write the SUMMARY BLOCK
Write the full summary block at the bottom of today's chatlog entry.
Use this exact format:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
DATE: [today's date]
PROJECT: [project name + phase]
WHAT WAS DONE:
  - [bullet 1]
  - [bullet 2]
  - [bullet 3]
WHAT WAS LEARNED:
  - [short explanation in simple words]
NEXT SESSION GOAL:
  - [exactly what to start next time]
GIT STATUS: Pushed ✅ / Not pushed ❌
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

THING 3 — Update _meta/skill.md
List every skill we practiced today.
Tell me which icon to change each one to: ⬜ → 🔵 → 🟡 → 🟠 → 🟢

THING 4 — Give me my git commit message
Write a good commit message for today's work in this format:
feat: [describe what was built]
Example: feat: set up folder structure and pushed to GitHub

Then remind me to run:
git add .
git commit -m "[the message you just wrote]"
git push
=== END ===
```

After opencode does all 4 things:
- Copy the SUMMARY BLOCK it wrote → paste it at the top of `historychat.md`
- Run the git commands it gave you

---

## 🧭 PART 6 — How to Keep AI on the Correct Path

These are signs that opencode has gone off track, and what to do.

| Sign | What it means | What to say |
|------|--------------|-------------|
| It writes code you don't understand at all | Going too fast | "Stop. Explain the last thing you wrote before continuing." |
| It skips explaining a line | Breaking the rules | "You didn't explain that line. What does it do and why?" |
| It writes 50+ lines at once | Going too fast | "Too much at once. Break this into smaller steps." |
| It uses a word you don't know | Assumed knowledge | "What is [word]? Explain it in one sentence before continuing." |
| It contradicts what it said earlier | Hallucinating | "Earlier you said [X] but now you're saying [Y]. Which is correct and why?" |
| It seems to be building the wrong thing | Off track | "Stop. Re-read my goal for today. Is this still heading toward that?" |
| It says 'just do X' without explaining | Breaking the rules | "Don't say 'just'. Explain what X is and why I need to do it." |

---

## 📊 PART 7 — The Complete File System (What Each File Does in One Line)

```
_meta/
├── context_engineering_master.md  ← GIVE THIS EVERY SESSION. It's your rules + who you are.
├── plan.md                        ← GIVE THIS EVERY SESSION. It's your roadmap.
├── skill.md                       ← GIVE THIS EVERY SESSION. It's your skill level.
├── chatlog.md                     ← GIVE THIS EVERY SESSION. AI writes here during session.
├── historychat.md                 ← GIVE THIS EVERY SESSION. AI reads last 2-3 entries.
├── README.md                      ← Give only on Day 1 or when starting a new project.
└── opencode_workflow.md           ← This file. Read it before every session. Don't give to AI.
```

**opencode_workflow.md (this file) is FOR YOU — not for the AI.**
It's your cheat sheet for running every session correctly.

---

## 🔁 PART 8 — Quick Reference Card (Print This or Keep It Open)

```
EVERY SESSION:
  cd Desktop/my-dev-journey
  opencode
  → paste SESSION OPENER (fill in date, project, goal)
  → wait for AI to confirm it read everything

EVERY 30-45 MINUTES:
  → paste CHECK-IN message

WHEN STUCK OR CONFUSED:
  → "Stop. Explain [specific thing] before we continue."

AFTER EVERY WORKING FEATURE:
  → git add . && git commit -m "feat: describe what you built" && git push

END OF SESSION:
  → paste SESSION CLOSER
  → copy SUMMARY BLOCK → paste into historychat.md
  → run git push
  → close opencode
```

---

## ❗ The Most Important Rule

**The AI is a tool. YOU are in control.**

If the AI goes too fast → stop it.
If the AI writes something you don't understand → stop it.
If the AI seems off track → stop it.

You are never "bothering" the AI by asking it to slow down, repeat, or re-explain.
That is exactly what it's there for.

---

*Save this file in `_meta/opencode_workflow.md` | Read before every session | Do not give this file to the AI*
