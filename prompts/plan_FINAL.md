# 📋 plan.md — My Full-Stack Developer Roadmap

> **Goal:** Land a Full-Stack Developer job
> **Stack:** Next.js · TypeScript · Tailwind CSS · PostgreSQL · Prisma · Vercel
> **Time:** 2–3 hours/day · 6 days/week · 6 months
> **Method:** Vibe Coding — AI-assisted building with full understanding of every line
> **Start Date:** [Fill in your start date]

---

## 🗺️ THE BIG PICTURE

```
Phase 0  (Week 1)      → One-time setup: tools, Git, workspace
Phase 1  (Weeks 2–4)   → Project 01: URL Shortener
Phase 2  (Weeks 5–8)   → Project 02: Task Manager with Auth
Phase 3  (Weeks 9–12)  → Project 03: Real-Time Chat App
Phase 4  (Weeks 13–16) → Project 04: Blog / CMS  ← Open Source starts here
Phase 5  (Weeks 17–20) → Project 05: E-Commerce Store
Phase 6  (Weeks 21–26) → Project 06: Capstone + Job Prep
```

**By the end you will have:**
- 6 deployed, live projects on GitHub (portfolio-ready)
- 1+ open-source contribution (PR merged or issue raised)
- Real Git workflow experience (branches, commits, PRs)
- Confidence to build any full-stack app from scratch
- A resume with real project links and a strong GitHub profile

---

## ✅ PHASE COMPLETION CHECKLIST

- [ ] Phase 0 — Setup complete
- [ ] Phase 1 — URL Shortener deployed
- [ ] Phase 2 — Task Manager with Auth deployed
- [ ] Phase 3 — Chat App deployed
- [ ] Phase 4 — Blog/CMS deployed + first OSS contribution
- [ ] Phase 5 — E-Commerce deployed
- [ ] Phase 6 — Capstone deployed + job applications sent

---

## ⚙️ PHASE 0 — ONE-TIME SETUP (Week 1, ~3 days)

**Goal:** Set up your entire workspace so you never waste time on setup again.

### Tools to Install (in this order)
- [ ] **Node.js** (v20+) — download from nodejs.org
- [ ] **VS Code** or **Cursor** — code editor (Cursor is better for vibe coding)
- [ ] **Git** — download from git-scm.com
- [ ] **GitHub account** — create at github.com
- [ ] **Vercel account** — create at vercel.com (free, link to GitHub)
- [ ] **Neon or Supabase account** — free PostgreSQL database in the cloud

### Folder Setup (run once in your terminal)
```bash
mkdir my-dev-journey
cd my-dev-journey
mkdir projects notes open-source
touch plan.md skill.md chatlog.md historychat.md context_engineering_prompt.md
```

### Git Global Setup (run once)
```bash
git config --global user.name "Your Name"
git config --global user.email "your@email.com"
```

### What to Learn in Week 1
Ask your AI assistant to explain these one at a time — do not rush:
- What is Git? What is GitHub? What is the difference?
- What do `git init`, `git add`, `git commit`, `git push` actually do?
- What is a branch? What is a pull request?
- How do you create a GitHub repo and link it to a local folder?

**Mini practice:** Create a test folder, `git init` it, write a README.md, commit it, push to GitHub. This is your first commit ever — screenshot it.

### AI Prompt to Use This Week
```
I just set up Git and GitHub for the first time. Walk me through
creating my first repo, linking it to GitHub, and making my first commit.
Explain every single Git command — what it does, why we need it, and
what happens if I skip it.
```

### Milestone 🏁
> Your `my-dev-journey` folder is on GitHub with your first commit pushed.

---

## 📦 PHASE 1 — PROJECT 01: URL Shortener (Weeks 2–4)

**Real-world example:** bit.ly, tinyurl.com
**Stack:** Next.js 14+ · TypeScript · Tailwind CSS · PostgreSQL · Prisma · Vercel

### What This App Does
- User pastes a long URL (e.g., `https://example.com/some/very/long/path`)
- App generates a short code (e.g., `myapp.com/abc123`)
- When anyone visits the short URL, they get redirected to the original

### Why Start Here
- Small enough to finish in 3 weeks
- Covers the full stack in one project: form → API route → database → redirect
- Real feature used by millions of apps
- Gets you comfortable with Next.js before adding complexity

### Week 2 — Frontend + Project Structure

**What to learn:**
- What is Next.js? How is it different from plain React?
- What is the App Router? What is a page, a layout, a component?
- What is TypeScript and why do companies use it?
- What is Tailwind CSS? How is it different from writing plain CSS?

**Tasks:**
- [ ] Create your Next.js project: `npx create-next-app@latest url-shortener --typescript --tailwind --eslint`
- [ ] Understand every file and folder that was generated (ask AI to explain each one)
- [ ] Build the UI: input box, "Shorten" button, result display area
- [ ] Understand: what is a React component, what is JSX, what is `useState`

**AI Prompt to Use:**
```
I just created my first Next.js project. Before we write any code,
explain to me: what is Next.js, how is it different from plain React,
and what does each file in the generated project do? Then let's build
the URL input form step by step. Explain every line.
```

**Milestone 🏁**
> The URL shortener UI is built and looks clean. Pushed to GitHub.

### Week 3 — Backend + Database

**What to learn:**
- What is a database? Why can't we just use a JavaScript array?
- What is PostgreSQL? What is Prisma? What is an ORM?
- What is an API route in Next.js? How is it different from a page?
- What is a database schema? What is a migration?

**Tasks:**
- [ ] Set up PostgreSQL on Neon (free cloud database — no local install needed)
- [ ] Install Prisma: `npm install prisma @prisma/client`
- [ ] Define your first schema: a `Url` model with `id`, `originalUrl`, `shortCode`, `createdAt`
- [ ] Run your first migration: `npx prisma migrate dev --name init`
- [ ] Write the API route: receive URL → generate short code → save to database

**AI Prompt to Use:**
```
I'm setting up a PostgreSQL database with Prisma for the first time.
Explain to me: what is a database schema? What is a migration and why
do we need it? What does Prisma actually do — why not write raw SQL?
Then walk me through setting up Neon and connecting it to my Next.js app.
```

**Milestone 🏁**
> Prisma is connected to your cloud database. You can save a URL to the database via the API route.

### Week 4 — Connect + Deploy

**What to learn:**
- How does a Next.js frontend call its own API route?
- What is a redirect? How does Next.js handle it?
- What are environment variables? Why must `.env` NEVER go to GitHub?
- How does Vercel deployment work?

**Tasks:**
- [ ] Connect frontend to backend: form submits → API route → database → show short URL
- [ ] Add redirect: visiting `/abc123` fetches the original URL from the database and redirects
- [ ] Create `.env.local` for secrets, add `.env*.local` to `.gitignore`
- [ ] Deploy to Vercel (connect GitHub repo → Vercel deploys automatically)
- [ ] Write a proper `README.md` with screenshots and live link

**Git commit message examples for this project:**
```
✅ "feat: add URL shortening form UI"
✅ "feat: set up Prisma schema for URLs table"
✅ "feat: implement short code generation in API route"
✅ "fix: redirect not working for unknown short codes"
✅ "deploy: add environment variables to Vercel"

❌ "update"
❌ "fix stuff"
❌ "final"
❌ "asdfjkl"
```

**Milestone 🏁**
> **Project 01 complete.** Live URL at a Vercel link. Clean README. All code on GitHub.

---

## 🗂️ PHASE 2 — PROJECT 02: Task Manager with Auth (Weeks 5–8)

**Real-world example:** Todoist, Notion tasks, Trello
**Stack:** Next.js · TypeScript · Tailwind · PostgreSQL · Prisma · NextAuth.js

### What This App Does
- User can sign up and log in
- Each user has their own private task list
- Tasks can be created, marked done, edited, and deleted
- Logged-out users cannot see any data

### Why This Project
- Authentication is in every real app — you must know how it works
- CRUD (Create, Read, Update, Delete) is the foundation of all apps
- "Who is this user?" is the most fundamental question in software

### Week 5 — Authentication Setup

**What to learn:**
- What is authentication? What is the difference between auth and authorization?
- What is NextAuth.js? What is a session? What is a JWT?
- What is bcrypt? Why do we NEVER store plain-text passwords?
- What is a cookie? How does it keep you logged in?

**Tasks:**
- [ ] Install NextAuth.js: `npm install next-auth`
- [ ] Set up email + password login (or Google OAuth — ask AI to help you choose)
- [ ] Add a `User` model to your Prisma schema
- [ ] Test: sign up, log in, log out — verify it works

**AI Prompt to Use:**
```
I'm adding authentication to a Next.js app for the first time.
Before we write code, explain to me: what is a session, what is a JWT,
and what is the difference? Also explain what bcrypt does and why
passwords must never be stored as plain text. Then let's set up
NextAuth.js step by step.
```

**Milestone 🏁**
> You can sign up, log in, and log out. Sessions persist on refresh.

### Week 6 — Tasks Feature + Database

**What to learn:**
- What is a database relation? What is a foreign key?
- How do you link tasks to the user who created them?
- What are Prisma queries? (`findMany`, `create`, `update`, `delete`)

**Tasks:**
- [ ] Add a `Task` model to Prisma schema (linked to `User` with a foreign key)
- [ ] Write API routes: GET tasks, POST task, DELETE task, PATCH task (mark done)
- [ ] Each route checks who the logged-in user is before touching the database

**Milestone 🏁**
> Tasks are saved to the database and linked to the correct user.

### Week 7 — Frontend + Protected Routes

**What to learn:**
- What is a protected route? How do you redirect users who are not logged in?
- What is Next.js middleware? What does it do?
- How does a React component fetch data from an API route?

**Tasks:**
- [ ] Build the task list UI: task card, checkbox, delete button, add-task form
- [ ] Add middleware to redirect unauthenticated users to the login page
- [ ] Each user only sees their own tasks — verify this is enforced in the API, not just the UI

**Milestone 🏁**
> Logged-in users see only their own tasks. Logged-out users are redirected to login.

### Week 8 — Polish + Deploy

**Tasks:**
- [ ] Add loading states (skeleton loaders or spinners)
- [ ] Add error messages for failed actions
- [ ] Add `.env` variables to Vercel, redeploy
- [ ] Write README with screenshots, push to GitHub

**Milestone 🏁**
> **Project 02 complete.** Live, deployed, full-stack app with real authentication.

---

## 💬 PHASE 3 — PROJECT 03: Real-Time Chat App (Weeks 9–12)

**Real-world example:** WhatsApp Web, Slack, Discord
**Stack:** Next.js · TypeScript · Tailwind · Prisma · Pusher (real-time)

### What This App Does
- Users join a chat room with a display name
- Messages appear instantly for everyone in the room (no page refresh needed)
- Message history is stored in the database
- Simple, clean UI with message bubbles

### Why This Project
- Real-time is a key skill for mid-to-senior roles
- Teaches you the difference between HTTP (request/response) and WebSockets (push)
- Very impressive in a portfolio — most beginners never build this

### Week 9 — Real-Time Fundamentals + Setup

**What to learn:**
- What is HTTP? What is a WebSocket? What is the difference?
- What is Pusher? Why use a service instead of building WebSockets yourself?
- What is an "event"? What is "pub/sub" (publish/subscribe)?

**Tasks:**
- [ ] Create a Pusher account (free tier)
- [ ] Install Pusher: `npm install pusher pusher-js`
- [ ] Add a `Message` model to Prisma (content, sender, room, timestamp)
- [ ] Write a test: trigger a Pusher event and see it appear in another browser tab

**AI Prompt to Use:**
```
I'm about to learn about real-time features for the first time.
Before we write code, explain to me: what is the difference between
HTTP and WebSockets? What does "real-time" actually mean technically?
What is Pusher and why would I use it instead of building WebSockets
myself? Use a real-world analogy.
```

**Milestone 🏁**
> You can trigger a Pusher event from one tab and see it in another.

### Week 10–11 — Build + Connect

**Tasks:**
- [ ] Build chat UI: message list, message input, send button
- [ ] POST endpoint: when user sends a message → save to database → trigger Pusher event
- [ ] Client subscribes to Pusher channel → new messages appear instantly
- [ ] Add chat rooms (users can join different rooms by name)

**Milestone 🏁**
> Two browser tabs in the same room see each other's messages in real time.

### Week 12 — Polish + Deploy

**Tasks:**
- [ ] Add usernames and timestamps to messages
- [ ] Show online user count in a room
- [ ] Deploy to Vercel, write README

**Milestone 🏁**
> **Project 03 complete.** Real-time chat app, live and deployed.

---

## 📝 PHASE 4 — PROJECT 04: Blog / CMS Platform + Open Source Begins (Weeks 13–16)

**Real-world example:** Medium, dev.to, Hashnode
**Stack:** Next.js · TypeScript · Tailwind · Prisma · Cloudinary (images)

### What This App Does
- Admin can write and publish blog posts (rich text editor)
- Public visitors can read all published posts — no login required
- Posts have a title, content, cover image, and date
- Admin view is protected; public view is open

### Why This Project
- Content management is in nearly every company's product
- Teaches image uploads, SEO basics, and separating public vs. admin views
- Introduces Next.js features like static generation and dynamic routing

### Week 13–14 — Build Core Features

**What to learn:**
- What is a rich text editor? (`react-quill` or `tiptap`)
- What is an image upload? How does Cloudinary work?
- What is SEO? What are `meta` tags? How does Next.js handle them?
- What is `generateStaticParams`? What is dynamic routing in Next.js?

**Tasks:**
- [ ] Add `Post` model to Prisma (title, content, coverImage, published, createdAt)
- [ ] Build admin editor: rich text + image upload to Cloudinary
- [ ] Build public blog listing page: all published posts as cards
- [ ] Build public post page: individual post at `/blog/[slug]`
- [ ] Protect the admin routes with NextAuth middleware

**Milestone 🏁**
> Admin can write and publish a post. Public visitors can read it at a real URL.

### ⭐ Open Source Contributions Begin (Week 13 — 30 min/day)

Starting now, spend 30 minutes per day on open source work, alongside building Project 04.

**How to find your first issue:**
1. Go to https://goodfirstissue.dev or search GitHub: `label:"good first issue" language:TypeScript`
2. Look for repos tagged `good-first-issue`, `hacktoberfest`, or `help-wanted`
3. Start small: fix a typo in docs, improve a README, fix a small bug — **these count**
4. Suggested beginner-friendly repos: `facebook/docusaurus`, `vercel/next.js` (docs), `t3-oss/create-t3-app`

**Your contribution workflow:**
```
1. Find a repo with a "good first issue" label
2. Comment on the issue: "I'd like to work on this" (claim it)
3. Fork the repo (copy it to your GitHub)
4. Clone your fork: git clone [your-fork-url]
5. Create a branch: git checkout -b fix/your-issue-name
6. Make your change
7. Commit: git commit -m "fix: describe what you fixed"
8. Push: git push origin fix/your-issue-name
9. Open a Pull Request on GitHub with a clear description
10. Respond to reviewer comments politely
11. Get it merged! 🎉
```

**Log every contribution in:** `open-source/log.md`

### Week 15–16 — Polish + Deploy

**Tasks:**
- [ ] Add post slugs (URL-friendly titles)
- [ ] Add SEO meta tags to each post page
- [ ] Deploy to Vercel, write README with screenshots

**Milestone 🏁**
> **Project 04 complete.** Public blog live. First open source PR submitted.

---

## 🛒 PHASE 5 — PROJECT 05: E-Commerce Store (Weeks 17–20)

**Real-world example:** Small Shopify store, any online product listing
**Stack:** Next.js · TypeScript · Tailwind · Prisma · Stripe

### What This App Does
- Browse products with images, prices, and descriptions
- Add items to cart, update quantities
- Checkout with Stripe (test mode — no real money)
- Order confirmation page

### Why This Project
- Payments and cart logic appear in most business applications
- Stripe integration is a highly valued, frequently-listed job skill
- Most complex project so far — shows real growth

### Week 17–18 — Product Catalog + Cart

**What to learn:**
- How do you manage cart state across pages in Next.js? (React Context or Zustand)
- What is an optimistic UI update?
- How do you display images from a database with Next.js Image optimization?

**Tasks:**
- [ ] Add `Product` and `Order` models to Prisma
- [ ] Build product listing page and individual product page
- [ ] Build cart: add to cart, update quantity, remove item
- [ ] Cart state persists (localStorage or server-side)

**Milestone 🏁**
> Users can browse products and manage a cart.

### Week 19–20 — Stripe + Deploy

**What to learn:**
- What is Stripe? What is a payment intent?
- What is a webhook? How does Stripe tell your app a payment succeeded?
- What is test mode in Stripe? (Use `4242 4242 4242 4242` as a test card)

**Tasks:**
- [ ] Install Stripe: `npm install stripe @stripe/stripe-js`
- [ ] Create checkout session from cart → redirect to Stripe checkout
- [ ] Handle webhook: payment success → create Order in database → show confirmation
- [ ] Deploy to Vercel, write README

**AI Prompt to Use:**
```
I'm integrating Stripe payments for the first time. Before we write code,
explain to me: what is a payment intent, what is a checkout session, and
what is a webhook? Why does Stripe need to "call back" to my server?
Use a real-world analogy.
```

**Milestone 🏁**
> **Project 05 complete.** Full checkout flow works end-to-end in test mode.

---

## 🏆 PHASE 6 — PROJECT 06: Capstone + Job Prep (Weeks 21–26)

### Week 21–23: Capstone Project

Pick ONE that excites you most. This is your most impressive portfolio project.

| Option | Description | New Skills |
|--------|-------------|------------|
| **Developer Portfolio Site** | Your personal website showcasing all 5 projects | Animations, contact form |
| **Job Board** | Post jobs, apply, filter by stack/location | Complex filtering, roles |
| **Finance Tracker** | Track income/expenses, visualize with charts | Recharts, data aggregation |
| **Recipe App with AI** | Generate recipes using the Claude API | AI API integration |

**What every capstone must have:**
- User authentication
- A real database with at least 2 related models
- Deployed and accessible online with a live link
- Clean README with screenshots
- At least 10 meaningful commits showing progress over time

### Week 24 — Portfolio Polish

- [ ] All 6 projects deployed with live links and clean READMEs
- [ ] Pin your best 4 projects on your GitHub profile
- [ ] Update your GitHub profile README (about you, stack, project links)
- [ ] Add screenshots and a short "what I learned" paragraph to each project's README

### Week 25 — Open Source: Final Push

- [ ] Aim for at least 1 meaningful PR merged (beyond docs/typo fixes)
- [ ] Your contribution log in `open-source/log.md` is up to date
- [ ] Add your open source contribution to your resume

### Week 26 — Job Preparation

**Resume:**
- [ ] List your 3 best projects with live links and GitHub links
- [ ] List your tech stack explicitly
- [ ] Frame projects with impact, not just description:
  - ❌ "Built a task manager app"
  - ✅ "Built a full-stack task manager with NextAuth.js authentication, deployed on Vercel, with protected API routes and a PostgreSQL database via Prisma"

**LinkedIn:**
- [ ] Add all 6 projects with links and screenshots
- [ ] Update skills section with your stack
- [ ] Write a short "About" section describing your journey

**Interview Prep:**
- [ ] Practice explaining each project out loud: "Walk me through how this works end-to-end"
- [ ] Review key concepts: JWT, REST, what happens when you type a URL, what is a database index, what is async/await
- [ ] Do 10 JavaScript coding challenges on LeetCode (easy level only — this is not the focus)
- [ ] Record a 2-minute demo video of your capstone project

---

## 📊 PROGRESS TRACKER

### Projects

| # | Project | Started | Deployed | GitHub | Live Link | Status |
|---|---------|---------|----------|--------|-----------|--------|
| 1 | URL Shortener | [ ] | [ ] | — | — | ⬜ |
| 2 | Task Manager + Auth | [ ] | [ ] | — | — | ⬜ |
| 3 | Real-Time Chat App | [ ] | [ ] | — | — | ⬜ |
| 4 | Blog / CMS | [ ] | [ ] | — | — | ⬜ |
| 5 | E-Commerce Store | [ ] | [ ] | — | — | ⬜ |
| 6 | Capstone | [ ] | [ ] | — | — | ⬜ |

**Status key:** ⬜ Not started &nbsp; 🔄 In progress &nbsp; ✅ Done

### Open Source

| Date | Repo | Issue / PR | Type | Status |
|------|------|------------|------|--------|
| — | — | — | — | — |

---

## 📅 DAILY SCHEDULE TEMPLATE (2.5 hours example)

```
├── 0:00 – 0:15  Review yesterday's chatlog / what I was working on
├── 0:15 – 1:45  Build with AI (focus on ONE small task — not the whole feature)
├── 1:45 – 2:00  Review what you built — ask AI to explain anything unclear
├── 2:00 – 2:15  Git commit and push
└── 2:15 – 2:30  Update chatlog.md and historychat.md
```

## 🗓️ WEEKLY ROUTINE

| Day | Focus |
|-----|-------|
| Monday | Learn a new concept (read, watch, ask AI to explain) |
| Tuesday | Apply it — write code, understand every line |
| Wednesday | Continue building the current project |
| Thursday | Continue building + git push before you stop |
| Friday | Open source: find an issue, review a PR, or make a contribution |
| Saturday | Review the week: refactor messy code, update skill.md |
| Sunday | Plan next week, update chatlog.md and historychat.md |

---

## ⚙️ GITHUB HABITS (Build These From Day 1)

| Habit | When to do it |
|-------|---------------|
| Commit after every small, working change | Every session |
| Write meaningful commit messages (see examples above) | Every commit |
| Push to GitHub before ending any session | Daily |
| Create a new branch for each feature | From Phase 2 onward |
| Write a README before a project is "done" | End of each phase |
| Open issues on your own repo for TODOs | From Phase 1 onward |
| Respond to any PR review comments within 24 hours | During open source work |

---

## 💡 VIBE CODING RULES

When using AI to help you code:

1. **Never paste code without reading it** — ask the AI to explain every line first
2. **Ask "why" before "what"** — why this approach, not just what it does
3. **Ask for alternatives** — "Is there another way to do this? What are the trade-offs?"
4. **Try to break it** — what happens if you remove this line? Ask AI to predict, then test it
5. **Teach it back** — after AI explains something, close the chat and explain it to yourself in plain words. If you can't, you don't understand it yet.

---

## 📌 RULES I NEVER BREAK

1. **Never copy code I don't understand.** Ask AI to explain it first.
2. **Push to GitHub every session** — even tiny changes. No exceptions.
3. **One project at a time.** Finish before starting the next.
4. **Understand before moving on.** If a line confuses me, I stop and ask.
5. **Small commits** — commit after every feature, not once a week.
6. **Update my logs** — `chatlog.md` and `historychat.md` after every session.
7. **Stuck for more than 15 minutes?** Ask AI. But ask it to explain, not just fix.

---

*Plan created: [DATE] | Next review: [DATE + 1 month] | Current phase: Phase 0, Week 1*
