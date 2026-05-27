# 🚀 my-dev-journey — My Developer Learning System

> **My personal roadmap to becoming a Full-Stack Developer + AI/ML Engineer.**
> Built with: Next.js · TypeScript · Tailwind CSS · Node.js · Express · FastAPI · PostgreSQL · Prisma · Vercel
> Timeline: 6 months · 2–3 hours/day · Starting: [Add your start date]

---

## 👤 About This Repo

This is my learning workspace. I am a CS student building real-world full-stack projects from scratch using AI-assisted coding (Vibe Coding). Every project here is deployed live, pushed to GitHub with a clean commit history, and built to understand — not just copy-paste.

**Goal:** Get hired as a Full-Stack Developer.

---

## 📁 Folder Structure

```
my-dev-journey/
│
├── _meta/                           ← All tracking files live here
│   ├── README.md                    ← You are here
│   ├── context_prompt.md            ← Paste into any AI before starting work
│   ├── plan.md                      ← Full 6-month roadmap with all phases and projects
│   ├── skill.md                     ← Every skill being learned, with progress rating
│   ├── chatlog.md                   ← Detailed log of TODAY's session (reset each session)
│   └── historychat.md               ← Permanent short summary of all past sessions
│
├── projects/                        ← All coding projects (each = its own GitHub repo)
│   ├── 01-personal-landing-page/
│   ├── 02-task-manager/
│   ├── 03-weather-dashboard/
│   ├── 04-expense-tracker/
│   ├── 05-url-shortener/
│   ├── 06-notes-app-with-auth/
│   ├── 07-job-application-tracker/
│   ├── 08-ai-powered-app/
│   ├── 09-real-time-chat-app/
│   ├── 10-blog-cms/
│   ├── 11-ecommerce-store/
│   └── 12-capstone/
│
├── notes/                           ← Quick notes, code snippets, written in my own words
│
└── open-source/                     ← Tracking my open-source contributions
    └── log.md
```

---

## 📋 What Each File Does

| File | Purpose | When to Use |
|------|---------|-------------|
| `context_prompt.md` | Master AI prompt with full context about who I am | Paste at the start of EVERY AI chat session |
| `plan.md` | Full 6-month roadmap, all phases and projects | Read at the start of each week |
| `skill.md` | Every skill tracked with progress level and proof links | Update every Thursday + after finishing a project |
| `chatlog.md` | Detailed log of today's session | Fill in DURING and AFTER each session |
| `historychat.md` | One-line summary of every session ever | Add one row AFTER each session; paste into AI at start of new session |

---

## 📦 Projects

| # | Project | Stack Highlights | Live | Repo |
|---|---------|-----------------|------|------|
| 01 | Personal Landing Page | HTML, CSS, Tailwind | — | — |
| 02 | Task Manager | HTML, CSS, JS, localStorage | — | — |
| 03 | Weather Dashboard | JS, fetch, async/await | — | — |
| 04 | Expense Tracker | React, TS, Node.js, PostgreSQL | — | — |
| 05 | URL Shortener | Next.js, Prisma, PostgreSQL | — | — |
| 06 | Notes App with Auth | Next.js, Express, JWT | — | — |
| 07 | Job Application Tracker | Next.js, Supabase, OAuth | — | — |
| 08 | AI-Powered App | React, FastAPI, OpenAI, LangChain | — | — |
| 09 | Real-Time Chat App | Next.js, Socket.io, PostgreSQL | — | — |
| 10 | Blog / CMS | Next.js, Prisma, Cloudinary | — | — |
| 11 | E-Commerce Store | Next.js, Stripe, Prisma | — | — |
| 12 | Capstone | Full stack (choice) | — | — |

> Update the Live and Repo columns as you deploy each project.

---

## ⚡ Quick Start — Do This on Day 1

### Step 1: Install all required tools

- [ ] VS Code — https://code.visualstudio.com
- [ ] Node.js (LTS) — https://nodejs.org
- [ ] Python (v3.11+) — https://python.org
- [ ] Git — https://git-scm.com
- [ ] GitHub account — https://github.com
- [ ] Vercel account — https://vercel.com (free, link to GitHub)
- [ ] Neon or Supabase account — free cloud PostgreSQL database

### Step 2: Create your folder and push to GitHub

```bash
# Create the folder structure
mkdir my-dev-journey
cd my-dev-journey
mkdir -p _meta projects notes open-source
touch _meta/context_prompt.md _meta/plan.md _meta/skill.md _meta/chatlog.md _meta/historychat.md

# Initialize Git and make your first commit
git init
git add .
git commit -m "init: start my dev journey"
```

Then go to GitHub.com:
1. Click "New repository"
2. Name it: `my-dev-journey`
3. Keep it **public** (shows employers you're active)
4. Copy the remote URL and run:

```bash
git remote add origin https://github.com/YOUR-USERNAME/my-dev-journey.git
git branch -M main
git push -u origin main
```

### Step 3: Read `plan.md` — start at Phase 0, Week 1

### Step 4: Before every AI session, open `context_prompt.md`, copy the prompt block, and fill in the SESSION CONTEXT section at the bottom

---

## 🔄 Daily Workflow

```
START SESSION
    ↓
Open chatlog.md → create a new session block for today
    ↓
Copy context_prompt.md → paste into AI (Claude / ChatGPT / Cursor)
Fill in today's goal in the SESSION CONTEXT section
    ↓
Work on your task — code, learn, build (small steps, understand every line)
    ↓
git add . && git commit -m "feat: describe what you built and why"
git push
    ↓
Fill in chatlog.md (what you did, what you learned, what blocked you)
    ↓
Add one-line summary row to historychat.md
    ↓
Update skill.md if you learned or practiced something new
    ↓
END SESSION
```

---

## 🤖 How I Use AI to Learn (Vibe Coding)

I don't just ask AI to write code for me. My process:

1. **I describe what I want to build** in plain English
2. **AI helps me write the code** step by step
3. **I ask AI to explain every line** — what it does, why it's there, what alternatives exist
4. **I understand it before moving on** — no blind copy-paste
5. **I git commit** after every working feature
6. **I update my logs** (`chatlog.md` → `historychat.md`) after every session

---

## 🔁 Git Commit Habit

```bash
# After every working feature or meaningful change:
git add .
git commit -m "feat: describe what was built"
git push
```

**Commit message format:**
- `feat:` — new feature added
- `fix:` — bug fixed
- `style:` — UI or styling changes
- `chore:` — setup, config, cleanup
- `docs:` — README or documentation update

---

## 🌍 Open Source Contributions

Starting from Month 5, I contribute to real open-source projects on GitHub.

- Fork → Clone → Branch → Code → PR → Review → Merge
- All contributions tracked in `open-source/log.md`

---

## 📈 Progress

- **Started:** [DATE]
- **Current Phase:** Phase 0 — Setup
- **Projects Completed:** 0 / 12
- **Open Source PRs:** 0

---

## ❗ The Most Important Rule

**If you don't understand a line of code — stop. Ask. Don't move on.**

The goal is not to finish fast. The goal is to understand deeply.
Small steps every day beat big steps once a week. 1 hour daily > 7 hours on Sunday.

**You got this. Start today.**
