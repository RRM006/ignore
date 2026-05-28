# 📖 START_HERE.md — Your Complete Operating Manual

> Read this file once fully before your first session.
> After that, use it as a reference whenever you're unsure what to do.
> This file tells you: what to give Opencode, what to say, how to start,
> what to do every day, and how to make sure Opencode never forgets or goes off track.

---

## 🗂️ THE 6 FILES AND WHAT EACH ONE DOES FOR OPENCODE

You have 6 files. Each one serves a specific job when working with Opencode or any AI.

| File | What It Does FOR Opencode | When to Give It |
|------|--------------------------|-----------------|
| `context_engineering_prompt.md` | Tells Opencode WHO you are, your level, your stack, and HOW to behave with you | Every single session — paste this FIRST |
| `plan.md` | Tells Opencode WHERE you are in your 6-month journey and WHAT the project is | Paste the relevant phase section at session start |
| `skill.md` | Tells Opencode EXACTLY what you know and don't know so it doesn't over-explain or under-explain | Paste the "Skill Snapshot" block at session start |
| `chatlog.md` | Opencode reads this to know what happened in THIS session and writes to it during/after | Open it alongside your session; tell Opencode to update it |
| `historychat.md` | Opencode reads this to know EVERYTHING that happened in ALL past sessions | Paste the last 2–3 summary blocks at session start |
| `README.md` | Your folder overview — Opencode doesn't need this, it's for you and GitHub visitors | Only if Opencode asks about project structure |

---

## ✅ HOW TO START — Your First-Ever Session (Do This Once)

### Step 1 — Set up the folder
```bash
mkdir my-dev-journey
cd my-dev-journey
mkdir projects notes open-source
```
Copy all your `.md` files into this folder.

### Step 2 — Push the folder to GitHub
```bash
git init
git add .
git commit -m "init: start my dev journey"
```
Go to github.com → New Repository → name it `my-dev-journey` → copy the URL, then:
```bash
git remote add origin https://github.com/YOUR-USERNAME/my-dev-journey.git
git branch -M main
git push -u origin main
```

### Step 3 — Open Opencode in this folder
```bash
cd my-dev-journey
opencode
```

### Step 4 — Paste your opening message (see exact template below)

---

## 🌅 WHAT TO DO EVERY DAY — Your Daily Routine

```
BEFORE you open Opencode:
  1. Open chatlog.md → create a new session block (copy the template)
  2. Open historychat.md → find the last 2–3 SESSION SUMMARY blocks
  3. Open skill.md → find the "Paste Into AI" snapshot block
  4. Know your goal for today (check plan.md if unsure)

WHEN you open Opencode:
  5. Paste your Session Opening Message (template below)
  6. Wait for Opencode to confirm it understood — don't start coding yet
  7. Work step by step — one task at a time
  8. Ask Opencode to explain every line before moving on

AFTER the session (before closing Opencode):
  9.  Tell Opencode: "Update my chatlog.md with today's session"
  10. Tell Opencode: "Write the SESSION SUMMARY block for historychat.md"
  11. Run: git add . && git commit -m "session: [date] — [what you did]" && git push
  12. Update skill.md if you learned something new
```

---

## 💬 EXACT WORDS TO USE WITH OPENCODE

### 🟢 SESSION OPENING MESSAGE — Paste this at the start of EVERY session

```
[PASTE YOUR FULL context_engineering_prompt.md HERE]

---

MY SKILL SNAPSHOT RIGHT NOW:
[PASTE the "Paste Into AI" block from skill.md HERE]

---

MY RECENT HISTORY (last 2–3 sessions):
[PASTE the last 2–3 SESSION SUMMARY blocks from historychat.md HERE]

---

TODAY'S SESSION:
- Date: [today's date]
- Phase: Month [X], Week [X]
- Project: [project name]
- Where I left off: [copy from your last historychat.md entry]
- My goal for today: [one specific thing — e.g. "Set up Prisma schema for the URL Shortener"]
- Current blocker (if any): [or write "None"]

Before we start coding, confirm back to me:
1. What is my skill level?
2. What project are we working on?
3. What is our goal for today?
4. What is the first step we should take?
```

**Why this works:** You are giving Opencode your identity, your history, your level, and today's goal all at once. It cannot forget what it never knew — so you give it everything upfront.

---

### 🔵 WHEN OPENCODE WRITES CODE — Say this every time

```
Before you write any code, explain to me:
1. What this code does in plain English
2. Why we need it here
3. What would break if we removed it
4. Is there another way to do this? What are the trade-offs?

Then write the code in small chunks — one step at a time.
Wait for me to say "I understand" or "done" before moving to the next step.
```

---

### 🟡 WHEN YOU DON'T UNDERSTAND SOMETHING — Say this

```
Stop. I don't understand [the specific thing].
Explain it to me like I am 15 years old.
Use a real-world analogy first, then show me the code.
Don't move forward until I confirm I understand.
```

---

### 🟠 CHECKPOINT — Say this every 30–45 minutes during a session

```
Checkpoint: Tell me —
1. What have we accomplished so far in this session?
2. What is the current state of the code?
3. What is our next step?
4. Are we still on track for today's goal?
```

**Why this works:** This forces Opencode to "reset" its understanding and catch any drift before it gets worse. It also helps YOU stay aware of where you are.

---

### 🔴 WHEN OPENCODE SEEMS OFF TRACK OR CONFUSED — Say this

```
Stop. I think we've drifted from the goal.
Our goal for today was: [restate your goal]
What we have actually done so far: [describe]
Are we still working toward that goal?
If not, what went wrong and how do we get back on track?
```

---

### 📝 TO MAKE OPENCODE LOG THE SESSION — Say this at the end

```
We're done for today. Please do the following:

1. Update my chatlog.md with today's full session.
   Use the session template format. Fill in:
   - What we did
   - What I learned (in simple words)
   - Any blockers we hit and how we solved them
   - Files we changed
   - Git commits made
   - My goal for next session

2. Write the SESSION SUMMARY block I need to copy into historychat.md.
   Use the ━━━ format from my chatlog template.

3. Tell me the git commit message I should use right now.
```

---

### 🧠 TO MAKE OPENCODE UPDATE YOUR SKILL FILE — Say this

```
Based on what we worked on today, tell me:
- Which skills in my skill.md should I update?
- What level should each one move to (🟡 / 🟠 / 🟢 / ✅)?
- Which new skills should I add that aren't in the file yet?
```

---

### 🔍 TO VERIFY OPENCODE IS NOT HALLUCINATING — Say this when something feels wrong

```
I want to verify this before we continue.
Show me exactly where in the code this is happening.
Don't explain — show me the actual file and line number.
```

and/or:

```
Are you certain about this? If you're not 100% sure, say so.
I would rather you say "I don't know" than give me a wrong answer.
```

**Why this works:** Opencode (like all AI) sometimes confidently states wrong things. Asking it to show you the actual code or admit uncertainty catches most hallucinations before they cause problems.

---

### 🌿 TO START A NEW FEATURE OR NEW FILE — Say this

```
Before we write anything:
1. What folder should this file go in and why?
2. What should we name it and why?
3. How does this connect to what we already built?
4. What is the simplest possible version we can build first?
```

---

### 🐛 WHEN YOU HIT AN ERROR — Say this

```
I got this error: [paste the full error message]

Before you fix it:
1. What does this error mean in plain English?
2. What caused it?
3. Where exactly in the code is the problem?
4. How should we think about fixing it?

Then fix it step by step. Explain each change.
```

---

### 🔀 FOR OPEN SOURCE WORK (GitHub contributions) — Say this

```
I want to contribute to this open source project: [paste repo URL]

Help me:
1. Understand what this project does before touching any code
2. Find a good first issue suitable for my skill level
3. Understand what the issue is asking me to do
4. Walk me through the fork → clone → branch → code → PR workflow
5. Review my code before I submit the PR

Go slowly. I am new to contributing to other people's code.
```

---

## 🔒 HOW TO MAKE SURE OPENCODE STAYS ON THE CORRECT PATH

The three things that cause Opencode to drift or hallucinate:

| Problem | What Causes It | How to Prevent It |
|---------|---------------|-------------------|
| Forgets your level | Long session, no reminder | Paste skill snapshot at start every time |
| Goes off-topic | Vague goals | Give ONE specific goal per session, not many |
| Confidently wrong | No verification | Use the Checkpoint prompt every 30–45 min |
| Loses session context | Long conversations | Use the Session Opening Message every single time |
| Skips explaining code | No reminder | Add "explain every line" to every code request |

**The single most important habit:** Every session, paste the full opening message. Every session. Without exception. Opencode has no memory between sessions — YOU are its memory. The files are its memory. If you don't paste the context, it starts from zero.

---

## 📁 HOW YOUR FILES CONNECT TO EACH OTHER (The Flow)

```
context_engineering_prompt.md
        ↓
    (WHO you are + HOW to teach you)
        ↓
    skill.md snapshot
        ↓
    (WHAT you know right now)
        ↓
    historychat.md (last 2–3 summaries)
        ↓
    (WHAT happened before today)
        ↓
    plan.md (current phase section)
        ↓
    (WHERE you are in the 6-month journey)
        ↓
  ┌─────────────────────────┐
  │   OPENCODE SESSION      │
  │   (today's work)        │
  └─────────────────────────┘
        ↓
    chatlog.md
        ↓
    (WHAT happened today — full detail)
        ↓
    historychat.md (new summary added)
        ↓
    skill.md (updated levels)
        ↓
    git push (code saved to GitHub)
```

Everything flows into the next session. Each session feeds the next one.

---

## ⚠️ COMMON MISTAKES AND HOW TO AVOID THEM

| Mistake | What Happens | What to Do Instead |
|---------|-------------|-------------------|
| Starting a session without pasting context | Opencode treats you as a stranger and skips explanations | Always paste the full opening message first |
| Accepting code you don't understand | You get stuck in the next session | Stop and ask "explain every line" before moving on |
| Setting too many goals in one session | Nothing gets finished properly | Pick ONE goal per session and finish it |
| Skipping chatlog.md at session end | You lose the context for next session | 5 minutes at end = saves 30 minutes next session |
| Not pushing to GitHub | Work gets lost, no progress history | `git push` is the last thing you do every session |
| Moving on when confused | Confusion stacks up and becomes overwhelming | Say "Stop. I don't understand X." every single time |

---

## 🗓️ YOUR WEEK AT A GLANCE

| Day | What to do |
|-----|-----------|
| Mon | Learn a new concept — ask Opencode to explain it, build a tiny example |
| Tue | Apply it — build the next feature of your current project |
| Wed | Continue building — one step further |
| Thu | Continue building + update skill.md at end |
| Fri | Open source work: find an issue, make a contribution, or do a code review |
| Sat | Review the week: clean up messy code, read what you wrote |
| Sun | Update historychat.md weekly review, plan next week's goal |

---

*This file is your guide. When you're confused about what to do — come here first.*
*Last updated: [DATE]*
