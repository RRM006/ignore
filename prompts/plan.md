# 📅 My 6-Month Full-Stack + AI Developer Roadmap

> **Start Date:** [Fill in your start date]
> **Goal:** Get a Full-Stack Developer / AI-ML Engineer job
> **Stack:** Next.js · TypeScript · Tailwind CSS · Node.js · Express · FastAPI · PostgreSQL · Prisma · Vercel
> **Daily commitment:** 2–3 hours | 6 days/week
> **Method:** Vibe Coding — AI-assisted building with full understanding of every line

---

## 🗺️ THE BIG PICTURE

```
Month 1  → Setup + Git + Foundation + First 2 projects
Month 2  → React + TypeScript + Full-Stack basics + 2 projects
Month 3  → Backend + Auth + Database + 2 full-stack projects
Month 4  → AI Integration (OpenAI + LangChain + RAG) + AI project
Month 5  → Advanced projects + Open Source contributions + Docker basics
Month 6  → Capstone project + Portfolio polish + Job prep
```

**By the end you will have:**
- 10+ deployed, live projects on GitHub (portfolio-ready)
- 1+ open-source contribution (PR merged or issue raised)
- Real Git workflow experience (branches, commits, PRs, code reviews)
- AI/ML integration skills on top of full-stack foundations
- A resume with real project links and a deployed portfolio

---

## 🗂️ Folder Structure — Set This Up on Day 1

```
my-dev-journey/
├── _meta/
│   ├── context_prompt.md      ← Paste into AI every session
│   ├── plan.md                ← This file
│   ├── skill.md               ← Skills you're tracking progress on
│   ├── chatlog.md             ← Today's session log
│   └── historychat.md         ← Summary of all past sessions
├── projects/
│   ├── 01-personal-landing-page/
│   ├── 02-task-manager/
│   ├── 03-weather-dashboard/
│   ├── 04-expense-tracker/
│   ├── 05-url-shortener/
│   ├── 06-notes-app-with-auth/
│   ├── 07-job-application-tracker/
│   ├── 08-real-time-chat-app/
│   ├── 09-blog-cms/
│   ├── 10-ecommerce-store/
│   ├── 11-ai-powered-app/
│   └── 12-capstone/
├── notes/                     ← Quick notes, code snippets per topic
└── open-source/               ← Notes and log of open-source contributions
```

Each project folder is also its own **GitHub repository** with:
- A proper `README.md`
- Regular commits with meaningful messages
- A deployed live link (Vercel for frontend, Railway/Render for backend)

---

## ✅ Phase Completion Checklist

- [ ] Phase 0 — Setup complete
- [ ] Phase 1 — Foundation complete
- [ ] Phase 2 — Full-Stack basics complete
- [ ] Phase 3 — Backend + Auth + Database complete
- [ ] Phase 4 — AI Integration complete
- [ ] Phase 5 — Advanced + Open Source complete
- [ ] Phase 6 — Capstone + Job Prep complete
- [ ] Portfolio live with all projects
- [ ] Resume updated
- [ ] Actively applying to jobs

---

## ⚙️ PHASE 0 — One-Time Setup (Week 1, ~3 days)

**Goal:** Set up your entire workspace so you never waste time on setup again.

### Tools to Install (in this order)
- [ ] **Node.js** (v20+) — download from nodejs.org
- [ ] **Python** (v3.11+) — download from python.org
- [ ] **VS Code** or **Cursor** — your code editor (Cursor is better for vibe coding)
  - Extensions to install: Prettier, ESLint, GitLens, GitHub Copilot, Thunder Client
- [ ] **Git** — download from git-scm.com
- [ ] **GitHub account** — create at github.com
- [ ] **Vercel account** — create at vercel.com (free, link to GitHub)
- [ ] **Neon or Supabase account** — free PostgreSQL database in the cloud

### One-Time Terminal Setup

```bash
# Create your folder structure
mkdir my-dev-journey
cd my-dev-journey
mkdir -p _meta projects notes open-source
touch _meta/plan.md _meta/skill.md _meta/chatlog.md _meta/historychat.md

# Configure Git globally (run once)
git config --global user.name "Your Name"
git config --global user.email "your@email.com"
```

### Git Basics to Learn in Phase 0
Ask your AI to explain each of these one at a time:
- What is Git? What is GitHub? What is the difference?
- `git init`, `git add`, `git commit`, `git push`, `git pull`
- `git branch`, `git checkout -b`, `git merge`
- What is a Pull Request (PR)?
- How to create a GitHub repo and connect it to a local folder

**Mini practice:** Create a test folder, init a repo, write a README.md, push it to GitHub. This is your Day 1 commit.

### GitHub Habits to Build from Day 1

| Habit | When |
|-------|------|
| Commit after every small working change | Every session |
| Write meaningful commit messages (see format below) | Every commit |
| Push at the end of every session | Daily |
| Create a new branch for each feature | From Phase 3 onward |
| Write a README for every project | Before deploying |
| Open issues for your own TODOs | From Phase 2 onward |

**Good commit message format:**
```
✅ "feat: add URL shortening form UI"
✅ "feat: set up Prisma schema for URLs table"
✅ "fix: redirect not working for unknown short codes"
✅ "deploy: add Vercel config and environment variables"

❌ "update"    ❌ "fix stuff"    ❌ "asdfgh"
```

---

## 📗 PHASE 1 — Foundation + First Projects (Month 1)

**Goal by end of Phase 1:** You understand HTML, CSS, JavaScript, and async/await. You have 3 small projects pushed to GitHub.

---

### 🗓️ Week 2 — HTML + CSS Basics

**Goal:** Build a simple webpage that looks good, pushed to GitHub.

#### What to Learn
- HTML: structure, tags, semantic HTML (`header`, `main`, `section`, `article`, `footer`)
- CSS: selectors, box model, flexbox, grid, basic responsive design
- Tailwind CSS: utility classes, how it differs from plain CSS
- How browsers read and render HTML + CSS

#### Tasks
- [ ] Build a simple personal landing page (your name, about, links, skills)
- [ ] Use flexbox for layout
- [ ] Make it responsive (looks good on mobile too)
- [ ] Push to GitHub with meaningful commit messages

#### 🏁 Milestone
> A live webpage with your name on it, pushed to GitHub.

#### AI Prompt to Use
```
I'm building a simple personal webpage with HTML and CSS. I want to understand
every tag and every CSS property. Start by explaining what HTML really is and
how a browser reads it. Then let's build step by step.
```

---

### 🚀 PROJECT 1 — Personal Landing Page

**Real-world example:** Every developer's personal website  
**Stack:** HTML + CSS + Tailwind CSS  
**GitHub repo:** `01-personal-landing-page`

**Features to build:**
- Home page (your name, title, short bio)
- About section
- Projects section (cards — even if empty for now)
- Skills section
- Contact section / links (GitHub, LinkedIn)

**What you learn:**
- HTML structure and semantic tags
- Responsive layout with Tailwind CSS
- Deploying to Vercel (free, one command)
- Git workflow: commits, push, live link

**Deploy:** Push to GitHub → connect to Vercel → get a live link. Share it.

---

### 🗓️ Week 3 — JavaScript Fundamentals

**Goal:** Understand JS well enough to make a webpage interactive.

#### What to Learn
- Variables (`let`, `const`), data types, operators
- Functions (regular and arrow functions)
- Arrays and Objects — what they are and how to use them
- DOM manipulation: `querySelector`, `addEventListener`, `innerHTML`
- Events: click, input, submit
- Control flow: `if/else`, loops (`for`, `forEach`, `map`)

#### Tasks
- [ ] Add interactivity to your landing page (dark/light mode toggle, or a counter)
- [ ] Build a simple calculator (HTML + CSS + JS)
- [ ] Understand: what is the DOM? Why do we manipulate it?

#### 🏁 Milestone
> A working JS calculator, pushed to GitHub.

#### AI Prompt to Use
```
Explain to me what JavaScript really is. Why does it exist?
What does it mean that JS runs "in the browser"? Then let's
build a calculator step by step. Explain every line.
```

---

### 🚀 PROJECT 2 — Task Manager (Vanilla JS)

**Real-world example:** A basic Todoist or Apple Reminders  
**Stack:** HTML + CSS + JavaScript (no framework yet)  
**GitHub repo:** `02-task-manager`

**Why start here:** Every app has CRUD (Create, Read, Update, Delete). This teaches that in the simplest way possible.

**Features to build:**
1. Add a task
2. Mark a task as done
3. Delete a task
4. Filter: All / Active / Completed
5. Save tasks so they don't disappear on refresh (localStorage)

**What you learn:**
- DOM manipulation (how JavaScript talks to HTML)
- Event listeners (what happens when you click a button)
- localStorage (browser memory that persists)
- How to structure a small project

---

### 🗓️ Week 4 — JavaScript: Async + Fetch

**Goal:** Understand how JS fetches data from the internet.

#### What to Learn
- `fetch()` — how to get data from an API
- `async/await` — what is asynchronous? Why does it exist?
- JSON — what it is, how to parse it
- Error handling: `try/catch`

**Why async/await matters:** Every real app talks to a server. That's always async. This is one of the most important things to understand early.

#### AI Prompt to Use
```
Explain async/await to me using a real-life analogy. Why can't I just write
normal code top-to-bottom? What problem does async solve? Then show me
how fetch() works with async/await, step by step.
```

---

### 🚀 PROJECT 3 — Weather Dashboard

**Real-world example:** weather.com, any weather widget  
**Stack:** HTML + CSS + JavaScript + OpenWeatherMap API (free)  
**GitHub repo:** `03-weather-dashboard`

**Features to build:**
- User types a city name
- App fetches and shows: temperature, weather condition, humidity, wind speed
- Handle errors gracefully (city not found, no internet)

**What you learn:**
- `fetch()` and `async/await` in a real context
- Reading and parsing API responses (JSON)
- Error handling with `try/catch`
- How real APIs work (keys, endpoints, responses)

---

## 📘 PHASE 2 — React + TypeScript + Full-Stack Basics (Month 2)

**Goal by end of Phase 2:** You can build a React + TypeScript frontend, and you understand why both exist.

---

### 🗓️ Week 5–6 — React Fundamentals

**Goal:** Understand why React exists and build something with it.

#### What to Learn
- Why React? What problem does it solve over plain HTML/JS?
- Components — what they are and why we split UI into them
- JSX — what it is and why it looks like HTML inside JavaScript
- Props — passing data between components
- State with `useState` — what is "state" and why does it matter?
- `useEffect` — when and why to use it
- Lists and keys in React
- React project structure (what each file and folder does)

#### How to Start a React Project
```bash
npm create vite@latest my-project -- --template react-ts
cd my-project
npm install
npm run dev
```

#### AI Prompt to Use
```
I'm learning React for the first time. Before we write any code, explain to me:
what problem does React solve? Why would I use it instead of plain JavaScript?
Use a real-world analogy. Then let's set up a project step by step.
```

---

### 🗓️ Week 7–8 — TypeScript Introduction

**Goal:** Understand why TypeScript exists and start using it.

#### What to Learn
- What is TypeScript? Why do companies use it?
- Types: `string`, `number`, `boolean`, `array`, `object`
- Interfaces and type definitions
- How TypeScript catches bugs BEFORE you run the code
- How to add TypeScript to a React project

---

### 🚀 PROJECT 4 — Expense Tracker (React + TypeScript + Backend)

**Real-world example:** Splitwise, YNAB, any budgeting app  
**Stack:** React + TypeScript (frontend) + Node.js + Express (backend) + PostgreSQL  
**GitHub repo:** `04-expense-tracker`

**Why this project:** First time connecting a React frontend to a real backend and database.

**Features to build:**
1. Add an expense (name, amount, category, date)
2. View all expenses in a list
3. See total spent this month
4. Delete an expense
5. Simple bar chart showing spending by category (Recharts or Chart.js)
6. Data saved in PostgreSQL (persists after refresh)

**What you learn:**
- How a React frontend sends data to an Express backend (fetch/axios)
- How a backend saves data to a database (SQL basics)
- REST API design (GET, POST, DELETE routes)
- Environment variables (`.env` files — never push these to GitHub)
- `.gitignore` — what it is and why `.env` must be in it
- Deploying: Vercel (frontend) + Railway (backend)

**Project structure:**
```
04-expense-tracker/
├── frontend/    (React + TypeScript + Vite)
└── backend/     (Node.js + Express + TypeScript + Prisma + PostgreSQL)
```

---

## 📙 PHASE 3 — Backend + Auth + Database (Month 3)

**Goal by end of Phase 3:** You can build a complete full-stack application with user authentication and a real database.

---

### 🗓️ Week 9–10 — Node.js + Express Deep Dive

**Goal:** Build real, tested APIs.

#### What to Learn
- What is a backend? What is a server? Why do we need one?
- What is Node.js? How is it different from browser JS?
- Express.js: routes, middleware, request/response cycle
- REST API: GET, POST, PUT/PATCH, DELETE — what each does
- Tools: Thunder Client (VS Code extension) to test APIs
- CORS — what it is and why it blocks your requests (every beginner hits this)

#### AI Prompt to Use
```
I'm learning backend development for the first time. Explain to me:
what is a server? What is an API? What is REST? Use real-world analogies.
Then let's build a simple Express API step by step. Explain every line.
```

---

### 🗓️ Week 11 — PostgreSQL + Prisma

**Goal:** Store data in a real database.

#### What to Learn
- What is a database? Why not just use a file or localStorage?
- SQL basics: `SELECT`, `INSERT`, `UPDATE`, `DELETE`
- What is PostgreSQL? How to set it up (locally or on Neon/Supabase free tier)
- What is Prisma ORM? Why use it instead of raw SQL?
- Prisma schema, migrations, Prisma Client
- What a migration is and why it matters
- Database design: tables, columns, foreign keys, relations

---

### 🗓️ Week 12 — Authentication

**Goal:** Understand how login/logout/signup really works.

#### What to Learn
- What authentication is and why it's hard to get right
- JWT (JSON Web Tokens) — what they are, how they work
- Password hashing with bcrypt — NEVER store plain-text passwords
- Protected routes — only logged-in users can access certain pages
- Sessions vs JWTs — trade-offs
- NextAuth.js / Clerk — industry-standard auth libraries
- Environment variables for secrets

---

### 🚀 PROJECT 5 — URL Shortener

**Real-world example:** bit.ly, tinyurl.com  
**Stack:** Next.js + TypeScript + Tailwind + Prisma + PostgreSQL (Neon)  
**GitHub repo:** `05-url-shortener`

**Features to build:**
1. User enters a long URL → app generates a short code (e.g., `myapp.com/abc123`)
2. Short URL redirects to original
3. Click count tracked per link
4. Dashboard showing all links + click statistics
5. User login so each user only sees their own links

**What you learn:**
- Next.js App Router (frontend + backend in one — very common in jobs)
- URL redirects in Next.js
- Prisma schema design
- Data analytics (counting, aggregating)
- Recharts or Chart.js for stats display
- Deploying a full-stack Next.js app to Vercel

---

### 🚀 PROJECT 6 — Notes App with Authentication

**Real-world example:** Notion, Apple Notes, Evernote  
**Stack:** Next.js + TypeScript + Tailwind + Node.js + Express + Prisma + PostgreSQL  
**GitHub repo:** `06-notes-app-with-auth`

**Features to build:**
1. User registration and login (JWT authentication)
2. Create, read, update, delete notes
3. Each user only sees their own notes
4. Protected routes (frontend + backend)

**What you learn:**
- Full authentication flow end to end
- Password hashing with bcrypt
- JWT creation and validation
- Protected API routes
- Protected frontend routes (redirect to login if not authenticated)

---

### 🚀 PROJECT 7 — Job Application Tracker

**Real-world example:** A tool you'll actually use during your own job search  
**Stack:** Next.js + TypeScript + Tailwind + Supabase + GitHub OAuth  
**GitHub repo:** `07-job-application-tracker`

**Why this project:** You will actually use it. It's also a great portfolio piece that shows you solve real problems.

**Features to build:**
1. Dashboard showing all applications grouped by status: Applied / Interview / Offer / Rejected
2. Add a new application (company, role, date applied, link, notes)
3. Update status as it progresses
4. Add notes after each interview
5. Filter and search applications
6. Export to CSV
7. Login with GitHub OAuth

**What you learn:**
- OAuth (login with Google/GitHub — used in almost every real app)
- Dashboard UI design with Tailwind
- More complex database relationships
- File export (CSV generation)
- Advanced filtering and search

---

## 📕 PHASE 4 — AI Integration (Month 4)

**Goal by end of Phase 4:** You can build AI-powered features into a full-stack application. You switch to Python + FastAPI for the backend here because Python is the industry standard for AI/ML work.

---

### 🗓️ Week 13 — FastAPI Basics (Python Backend)

**Goal:** Learn FastAPI so you can build AI-ready backends in Python.

#### What to Learn
- What FastAPI is — a Python web framework (like Express, but Python)
- Why Python for AI: it has the best AI/ML libraries
- FastAPI basics: install, create first endpoint, run locally
- REST API in Python: same concepts as Node.js/Express, different syntax
- SQLAlchemy ORM: what it is, why we use it (write Python, not SQL)
- Connecting FastAPI to PostgreSQL
- Auto-generated API docs (Swagger UI — FastAPI gives this free)

#### AI Prompt to Use
```
I know Node.js/Express already. Now teach me FastAPI in Python.
What's the same? What's different? Start from installing FastAPI
and building my first endpoint. Explain every line.
```

---

### 🗓️ Week 14 — OpenAI API Basics

#### What to Learn
- What an LLM is in plain terms
- OpenAI API: get an API key, make your first call in Python
- Prompt engineering basics — how to write effective prompts
- System prompts vs user prompts
- Streaming responses (the "typewriter" effect like ChatGPT)
- Handling API responses and errors
- Cost management — how API pricing works, how to avoid surprise bills

---

### 🗓️ Week 15 — LangChain Basics

#### What to Learn
- What LangChain is — a framework for building AI apps
- Chains — connecting prompts together in sequence
- Memory — making AI remember conversation context
- Build a simple chatbot with memory in Python

---

### 🗓️ Week 16 — RAG (Retrieval Augmented Generation)

#### What to Learn
- What RAG is — AI that answers questions from YOUR documents
- Embeddings — turning text into numbers (vectors) so AI can search it
- Vector databases: Chroma (simple, local) for starters
- Build: upload a PDF → ask questions about it

---

### 🚀 PROJECT 8 — AI-Powered Application

**Real-world example:** ChatPDF, Notion AI, GitHub Copilot  
**Stack:** React + TypeScript (frontend) + FastAPI + Python (backend) + OpenAI + LangChain  
**GitHub repo:** `08-ai-powered-app`

**Choose one of these ideas (pick what excites you most):**
- **AI Study Assistant** — upload your notes/PDF, ask questions about them (uses RAG)
- **AI Resume Reviewer** — paste a resume, get structured feedback
- **AI Code Explainer** — paste code, get a plain-English explanation
- **AI Chat with your Task Manager** — natural language: "show me tasks due this week"

**What you learn:**
- Integrating OpenAI API into a real product
- LangChain chains and memory
- RAG pipeline (embeddings + vector search + generation)
- Streaming AI responses to the frontend
- Prompt engineering in a production context
- Full-stack app with React frontend + FastAPI backend

---

## 📓 PHASE 5 — Advanced Projects + Open Source (Month 5)

**Goal by end of Phase 5:** You have your most impressive portfolio project live. You have made a real open-source contribution.

---

### 🗓️ Week 17–18 — Open Source Contributions

**Goal:** Make your first real pull request to an existing project on GitHub.

#### What Open Source Contributing Means
- Real projects on GitHub that anyone can improve
- You find a bug or small task, fix it, submit a PR (pull request)
- Maintainer reviews and merges your code
- Shows up on your GitHub profile — proof you can work in a team codebase

#### Step-by-Step: Your First Contribution
1. Go to https://goodfirstissue.dev or search GitHub for `good first issue`
2. Filter by: JavaScript, TypeScript, Python, or React
3. Look for issues labeled `good first issue`, `beginner friendly`, or `help wanted`
4. Read the issue carefully + read the repo's `CONTRIBUTING.md`
5. Comment: "I'd like to work on this" (claim the issue before starting)
6. Fork the repo → clone it → create a branch → make changes → push → open PR
7. Write a clear PR description (what you changed and why)
8. Respond to code review comments politely

**Suggested repos to start with:**
- `freeCodeCamp/freeCodeCamp` — docs and curriculum fixes
- `facebook/docusaurus` — documentation improvements
- `public-apis/public-apis` — add or fix API entries
- `t3-oss/create-t3-app` — docs and small fixes
- Any project you actually use

#### GitHub Skills to Practice
- [ ] Fork a repo
- [ ] Clone a forked repo locally
- [ ] Create a branch for your change: `git checkout -b fix/issue-name`
- [ ] Open a Pull Request with a clear description
- [ ] Respond to code review comments
- [ ] Create a GitHub Issue to report a bug you found yourself

#### 🏁 Milestone
> At least 1 merged pull request to an open-source project.

---

### 🗓️ Week 19–20 — Docker Basics + CI/CD

#### What to Learn
- What Docker is — packaging your app so it runs the same anywhere
- Dockerfile basics, docker-compose basics
- Dockerize your FastAPI backend
- What CI/CD is — automating tests and deploys
- GitHub Actions basics — run a simple action on push

---

### 🚀 PROJECT 9 — Real-Time Chat App

**Real-world example:** WhatsApp Web, Slack, Discord  
**Stack:** Next.js + TypeScript + Node.js + Socket.io + PostgreSQL  
**GitHub repo:** `09-real-time-chat-app`

**Features to build:**
1. User authentication (login/signup)
2. Real-time messaging — messages appear instantly for everyone, no page refresh
3. Multiple chat rooms
4. Message history stored in database
5. Online/offline user status
6. Timestamps on messages

**What you learn:**
- WebSockets — what they are and how they differ from regular HTTP
- Socket.io — real-time communication library
- Event-driven programming
- Managing real-time state in React

---

### 🚀 PROJECT 10 — Blog / CMS Platform

**Real-world example:** Medium, dev.to, Hashnode  
**Stack:** Next.js + TypeScript + Tailwind + Prisma + PostgreSQL  
**GitHub repo:** `10-blog-cms`

**Features to build:**
1. Admin can write and publish blog posts (rich text editor)
2. Public users can read posts, no login required
3. Posts have title, content, cover image, publish date, tags
4. SEO meta tags for each post
5. Image uploads stored on Cloudinary (free tier)

**What you learn:**
- Rich text editing
- File uploads (multipart form data)
- Cloud storage with Cloudinary
- SEO meta tags and image optimization
- Admin vs public views (role-based access)

---

### 🚀 PROJECT 11 — E-Commerce Store

**Real-world example:** A small Shopify store  
**Stack:** Next.js + TypeScript + Tailwind + Prisma + PostgreSQL + Stripe  
**GitHub repo:** `11-ecommerce-store`

**Features to build:**
1. Browse products with images, prices, descriptions
2. Add to cart, update quantities, remove items
3. Checkout with Stripe (test mode — no real money needed)
4. Order confirmation page
5. Order history for logged-in users

**What you learn:**
- Stripe payments integration (highly valued skill)
- Cart state management in React
- Product catalog and database design
- Handling webhooks (Stripe notifying your app of payment events)
- Most complex project so far — shows real growth

---

## 📒 PHASE 6 — Capstone + Portfolio + Job Prep (Month 6)

**Goal:** Build one final impressive project, polish everything, and start applying.

---

### 🗓️ Week 21–23 — Capstone Project

**Pick ONE of these (choose what genuinely excites you):**

**Option A: Developer Portfolio Site (v2)**
Your own personal website showcasing all your projects. Should be impressive enough that a hiring manager stays on it.
- Includes: project showcase, about page, contact form, blog (optional), animations

**Option B: SaaS Product Starter**
A simple software-as-a-service tool (e.g., AI writing assistant, resume builder, habit tracker with AI insights)
- Includes: Auth, payments (Stripe), AI API (OpenAI/Claude), dashboard

**Option C: Job Board**
Post jobs, apply to them, filter by stack/location/salary
- Includes: Auth, job listings, search + filter, application tracking

**Option D: Finance Tracker with AI**
Track income, expenses, savings goals — with AI-generated insights
- Includes: Charts (Recharts), AI summaries, budget goals, alerts

**Option E: Developer Tool**
A CLI tool or VS Code extension that solves a real developer problem
- Example: Auto-generates boilerplate code, or explains error messages

**What makes a good capstone:**
- Solves a REAL problem someone would actually use
- Has user authentication
- Has a real database
- Is deployed and accessible online (live link)
- Has a clean README with screenshots and a demo video (2 minutes)
- Shows at least 15 meaningful commits — proof of your build process

---

### 🗓️ Week 24 — Code Review Practice

- [ ] Review 3 projects from other beginners on GitHub
- [ ] Open constructive, helpful issues on their repos
- [ ] Ask for a code review on one of your own projects (post in dev communities)
- [ ] Apply review feedback to your own code
- [ ] Document learnings in `open-source/log.md`

---

### 🗓️ Week 25 — Portfolio Polish

- [ ] All projects deployed with live links
- [ ] Every GitHub repo has a proper README:
  - What it does (2–3 sentences)
  - Tech stack used
  - How to run it locally
  - Screenshots or GIF demo
  - Live link
- [ ] Pin your best 4–5 projects on your GitHub profile
- [ ] Update your GitHub profile README (who you are, your stack, your projects, contact)
- [ ] Record a 2-minute demo video for your capstone project
- [ ] Write case studies for top 2 projects: problem → how you solved it → what you learned

---

### 🗓️ Week 26 — Job Prep

#### Resume
- [ ] List your 3 best projects with links and 1-line impact statements
  - Not just "built a task manager" → "Built a full-stack task manager with JWT auth, deployed on Vercel/Render"
- [ ] List your tech stack clearly
- [ ] List your GitHub contributions and open-source work
- [ ] Mention: "Built 10+ full-stack projects from scratch over 6 months"

#### LinkedIn
- [ ] Add all projects to the Featured section
- [ ] Update skills section with your full stack
- [ ] Add GitHub link
- [ ] Connect with other developers

#### Interview Prep
- [ ] Practice explaining each project out loud: "Walk me through how this project works"
- [ ] Be able to answer: what is JWT, what is REST, what is a database index, what is async/await, what is a component, what is state
- [ ] System design basics: "What happens when you type a URL and press Enter?"
- [ ] Do 10–15 JavaScript coding challenges on LeetCode (easy level only)

---

## 📦 All Projects Summary

| # | Project | Phase | Stack | Key Skills |
|---|---------|-------|-------|------------|
| 1 | Personal Landing Page | 1 | HTML + CSS + Tailwind | HTML, CSS, Flexbox, Vercel deploy |
| 2 | Task Manager (Vanilla JS) | 1 | HTML + CSS + JavaScript | DOM, Events, localStorage, CRUD |
| 3 | Weather Dashboard | 1 | HTML + CSS + JS + API | fetch, async/await, JSON, APIs |
| 4 | Expense Tracker | 2 | React + TS + Node + PostgreSQL | Full-stack basics, REST API |
| 5 | URL Shortener | 3 | Next.js + Prisma + PostgreSQL | App Router, redirects, analytics |
| 6 | Notes App with Auth | 3 | Next.js + Express + JWT | Authentication, protected routes |
| 7 | Job Application Tracker | 3 | Next.js + Supabase + OAuth | OAuth, dashboard, CSV export |
| 8 | AI-Powered App | 4 | React + FastAPI + OpenAI | LLMs, RAG, LangChain, streaming |
| 9 | Real-Time Chat App | 5 | Next.js + Socket.io + PostgreSQL | WebSockets, real-time, events |
| 10 | Blog / CMS | 5 | Next.js + Prisma + Cloudinary | File uploads, rich text, SEO |
| 11 | E-Commerce Store | 5 | Next.js + Stripe + Prisma | Payments, cart, webhooks |
| 12 | Capstone | 6 | Full stack (your choice) | Everything combined |
| + | Open Source Contributions | 5–6 | Various | Git workflow, PR, code review |

---

## 📅 Daily Schedule Template (2–3 hrs/day)

```
Session Example (2.5 hrs):
├── 0:00 – 0:15  Review yesterday's chatlog / what you were doing
├── 0:15 – 1:45  Build with AI (one focused task, understand every line)
├── 1:45 – 2:00  Review what you built, ask AI to explain unclear parts
├── 2:00 – 2:15  Git commit + push
└── 2:15 – 2:30  Update chatlog.md + historychat.md
```

## 📅 Weekly Routine

| Day | Focus |
|-----|-------|
| Monday | Learn a new concept (read + take notes in notes/) |
| Tuesday | Apply concept — code it yourself, AI explains each line |
| Wednesday | Continue building the project |
| Thursday | Continue building + git push everything |
| Friday | Review, fix bugs, refactor, update skill.md |
| Saturday | Open source: find an issue or review someone's PR |
| Sunday | Rest — or catch up if behind |

---

## 🔄 Open Source Contribution Workflow

```
For Every Contribution:
1.  Find repo with "good first issue" label
2.  Fork the repo (copies it to your GitHub)
3.  Clone your fork: git clone [your-fork-url]
4.  Create a branch: git checkout -b fix/your-issue-name
5.  Make your change
6.  Commit: git commit -m "fix: describe what you fixed"
7.  Push: git push origin fix/your-issue-name
8.  Open Pull Request on GitHub with a clear description
9.  Respond to reviewer comments
10. Get it merged! 🎉

Log every contribution in: open-source/log.md
```

---

## 💡 The Vibe Coding Rules

When using AI to help you code:
1. **Never paste code you don't understand** — ask AI to explain it first
2. **Ask "why" before "what"** — why this approach, not just what it does
3. **Ask for alternatives** — "is there another way to do this?"
4. **Try to break it** — what happens if I change this? Ask AI to predict, then test it
5. **Teach it back** — after AI explains, close the chat and explain it to yourself in plain words

---

## 📌 Rules I Follow — Never Break These

1. **Never copy code I don't understand** — ask AI to explain it first
2. **Always git push before ending a session** — no exceptions
3. **One project at a time** — finish before starting the next
4. **Small commits** — commit after every working feature, not once a week
5. **Update my logs** — `chatlog.md` and `historychat.md` after every session
6. **Stuck for more than 15–30 minutes?** Ask AI. But ask it to explain, not just fix
7. **Small steps every day beat big steps once a week** — 1 hour daily > 7 hours on Sunday
8. **Build things you actually care about** — passion is what gets you through stuck moments

---

## 📊 Progress Tracker

### Projects
| # | Project | Started | Deployed | GitHub Link | Live Link |
|---|---------|---------|----------|-------------|-----------|
| 1 | Personal Landing Page | [ ] | [ ] | — | — |
| 2 | Task Manager (Vanilla JS) | [ ] | [ ] | — | — |
| 3 | Weather Dashboard | [ ] | [ ] | — | — |
| 4 | Expense Tracker | [ ] | [ ] | — | — |
| 5 | URL Shortener | [ ] | [ ] | — | — |
| 6 | Notes App with Auth | [ ] | [ ] | — | — |
| 7 | Job Application Tracker | [ ] | [ ] | — | — |
| 8 | AI-Powered App | [ ] | [ ] | — | — |
| 9 | Real-Time Chat App | [ ] | [ ] | — | — |
| 10 | Blog / CMS | [ ] | [ ] | — | — |
| 11 | E-Commerce Store | [ ] | [ ] | — | — |
| 12 | Capstone | [ ] | [ ] | — | — |

### Open Source
| Date | Repo | Issue / PR | Status |
|------|------|------------|--------|
| — | — | — | — |

---

*Plan created: [DATE] | Next review: [DATE + 1 month] | Stack: Next.js · TypeScript · Tailwind · Node.js · Express · FastAPI · PostgreSQL · Prisma · OpenAI · Vercel*
