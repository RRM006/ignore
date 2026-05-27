# 🛠️ skill.md — Skills Tracker

> **Why this file exists:**
> When you're learning for 6 months, it's easy to feel like you're not improving. This file tracks every skill you've built, at what level, and proves it with a real project link.
> In a job interview, you can look here and confidently say "I built X with Y — here's the link."
>
> **How to update it:**
> After each session, find the skill you practiced and move its status forward.
> Every Thursday (per your weekly routine), ask your AI:
> *"Based on what we worked on this week, tell me which skills I should update in my skill.md and to what level."*

---

## 📊 Status Key

| Status | Meaning |
|--------|---------|
| ⬜ | Not started — haven't touched it yet |
| 🟡 | Learning — I've seen it but need to look things up constantly |
| 🟠 | Comfortable — I can use it with occasional help |
| 🟢 | Can do it — I can use it without help |
| ✅ | Confident — I can use it AND explain it to someone else |

Once a skill reaches 🟢 or ✅, you can honestly list it on your resume.

---

## 🖥️ DEVELOPER TOOLS

| Skill | Status | Last Practiced | Notes |
|-------|--------|---------------|-------|
| Terminal / Command Line basics (`cd`, `ls`, `mkdir`, `pwd`) | ⬜ | — | |
| npm basics (`install`, `run`, scripts) | ⬜ | — | |
| VS Code: basic usage and shortcuts | ⬜ | — | |
| Git: `add`, `commit`, `push`, `pull`, `status`, `log` | ⬜ | — | Daily use |
| Git: branching (`git checkout -b`) | ⬜ | — | From Phase 2 onward |
| Git: merge + resolving conflicts | ⬜ | — | |
| GitHub: creating repos, cloning | ⬜ | — | |
| GitHub: pull requests | ⬜ | — | |
| GitHub: issues and labels | ⬜ | — | |
| GitHub: code review | ⬜ | — | |
| `.gitignore` | ⬜ | — | |
| `.env` files — what they are, why secrets go here | ⬜ | — | NEVER push to GitHub |
| Reading error messages and stack traces | ⬜ | — | |
| Using browser DevTools | ⬜ | — | |

---

## 📝 JAVASCRIPT & TYPESCRIPT

| Skill | Status | Used In | Notes |
|-------|--------|---------|-------|
| Variables (`let`, `const`), functions, loops | ⬜ | — | |
| Arrays and objects | ⬜ | — | |
| Arrow functions, destructuring, spread operator | ⬜ | — | ES6+ syntax |
| `async/await` and Promises | ⬜ | — | Used in EVERY API call |
| `fetch()` — calling APIs from the browser | ⬜ | — | |
| Error handling (`try/catch`) | ⬜ | — | |
| `import` / `export` (modules) | ⬜ | — | |
| JSON — what it is, how to parse it | ⬜ | — | |
| **TypeScript: why it exists** | ⬜ | — | Our main language |
| TypeScript: basic types (`string`, `number`, `boolean`) | ⬜ | — | |
| TypeScript: arrays and object types | ⬜ | — | |
| TypeScript: interfaces | ⬜ | — | |
| TypeScript: typing React props and state | ⬜ | — | |
| Fixing TypeScript errors | ⬜ | — | |

---

## ⚛️ REACT

| Skill | Status | Used In | Notes |
|-------|--------|---------|-------|
| What React is and why it exists | ⬜ | — | |
| Functional components | ⬜ | — | Building blocks of UI |
| JSX — what it is | ⬜ | — | |
| Props — passing data between components | ⬜ | — | |
| State with `useState` | ⬜ | — | |
| `useEffect` hook | ⬜ | — | |
| Lists and `.map()` with keys | ⬜ | — | |
| Conditional rendering | ⬜ | — | |
| Forms in React (controlled inputs) | ⬜ | — | |
| Context API (sharing state globally) | ⬜ | — | |
| Fetching data in React (with loading + error states) | ⬜ | — | |

---

## 🔲 NEXT.JS (Full-Stack Framework)

| Skill | Status | Used In | Notes |
|-------|--------|---------|-------|
| What Next.js is and why we use it over plain React | ⬜ | — | |
| App Router: pages, layouts, folders | ⬜ | — | Our routing system |
| Server components vs Client components | ⬜ | — | Important concept |
| API Routes — writing backend code in Next.js | ⬜ | — | |
| Dynamic routes (`[id]`, `[slug]`) | ⬜ | — | |
| `loading.tsx` and `error.tsx` | ⬜ | — | |
| Next.js middleware | ⬜ | Project 02 | Protecting routes |
| Image optimization with `next/image` | ⬜ | — | |
| Environment variables in Next.js | ⬜ | — | `.env.local` |
| Deployment to Vercel | ⬜ | — | |

---

## 🎨 TAILWIND CSS

| Skill | Status | Used In | Notes |
|-------|--------|---------|-------|
| What Tailwind is and how it differs from plain CSS | ⬜ | — | |
| Utility classes (padding, margin, flex, grid) | ⬜ | — | |
| Responsive design with Tailwind (`sm:`, `md:`, `lg:`) | ⬜ | — | |
| Dark mode with Tailwind | ⬜ | — | |

---

## 🗄️ DATABASE & PRISMA

| Skill | Status | Used In | Notes |
|-------|--------|---------|-------|
| What a database is and why it exists | ⬜ | — | |
| What SQL is | ⬜ | — | |
| Basic SQL (`SELECT`, `INSERT`, `UPDATE`, `DELETE`) | ⬜ | — | |
| What PostgreSQL is | ⬜ | — | Our database |
| Tables, rows, columns, data types | ⬜ | — | |
| Database relationships (one-to-many, many-to-many) | ⬜ | — | |
| What an ORM is and why we use it | ⬜ | — | |
| **Prisma schema** — defining models | ⬜ | Project 01 | |
| Prisma migrations | ⬜ | Project 01 | How we change DB structure safely |
| Prisma Client queries (`create`, `findMany`, `update`, `delete`) | ⬜ | Project 01 | |
| Connecting to Neon (cloud PostgreSQL) | ⬜ | Project 01 | |

---

## 🔐 AUTHENTICATION

| Skill | Status | Used In | Notes |
|-------|--------|---------|-------|
| What authentication is vs authorization | ⬜ | — | |
| Sessions vs JWT tokens | ⬜ | — | |
| Cookies — what they are, how they keep you logged in | ⬜ | — | |
| Password hashing with bcrypt | ⬜ | Project 02 | NEVER store plain passwords |
| NextAuth.js setup | ⬜ | Project 02 | |
| Protected routes with Next.js middleware | ⬜ | Project 02 | |
| OAuth (Login with Google/GitHub) | ⬜ | Project 04 | |

---

## ⚡ REAL-TIME (WEBSOCKETS)

| Skill | Status | Used In | Notes |
|-------|--------|---------|-------|
| What "real-time" means technically | ⬜ | — | |
| HTTP vs WebSocket — the difference | ⬜ | — | |
| Pusher — what it is and why use a service | ⬜ | Project 03 | |
| Pub/sub pattern (publish and subscribe) | ⬜ | Project 03 | |
| Events: triggering and listening | ⬜ | Project 03 | |

---

## 💳 PAYMENTS (STRIPE)

| Skill | Status | Used In | Notes |
|-------|--------|---------|-------|
| What Stripe is | ⬜ | — | |
| Stripe test mode (fake card: `4242 4242 4242 4242`) | ⬜ | Project 05 | |
| Creating a Stripe checkout session | ⬜ | Project 05 | |
| Webhooks — what they are, why Stripe needs them | ⬜ | Project 05 | |

---

## ☁️ DEPLOYMENT

| Skill | Status | Used In | Notes |
|-------|--------|---------|-------|
| Deploy to Vercel (frontend + Next.js) | ⬜ | Project 01 | One-click via GitHub |
| Environment variables in production (Vercel dashboard) | ⬜ | Project 01 | |
| Deploy backend to Railway | ⬜ | — | If separate backend needed |
| Custom domain basics | ⬜ | — | |

---

## 🤖 AI / VIBE CODING

| Skill | Status | Last Practiced | Notes |
|-------|--------|---------------|-------|
| Using AI to understand code (not just copy it) | ⬜ | — | |
| Writing effective prompts for AI | ⬜ | — | |
| Using Cursor or Copilot in VS Code | ⬜ | — | |
| Reviewing AI-generated code critically | ⬜ | — | |
| Knowing when NOT to use AI | ⬜ | — | |

---

## 🌍 OPEN SOURCE

| Skill | Status | Proof (PR/Issue link) | Notes |
|-------|--------|-----------------------|-------|
| Forking a repository | ⬜ | — | |
| Cloning a fork locally | ⬜ | — | |
| Creating a branch for your fix | ⬜ | — | |
| Reading an issue and understanding what's needed | ⬜ | — | |
| Writing a clear PR description | ⬜ | — | |
| Responding to code review feedback | ⬜ | — | |
| Having a PR merged | ⬜ | — | |

---

## 💼 SOFT / PROFESSIONAL SKILLS

| Skill | Status | Notes |
|-------|--------|-------|
| Can explain a project end-to-end in 2 minutes | ⬜ | Key interview skill |
| Can read someone else's code and follow it | ⬜ | |
| Can find and read official documentation | ⬜ | |
| Can break a feature into small steps before coding | ⬜ | |
| Can estimate how long a task will take | ⬜ | |
| Can write a useful README for a project | ⬜ | |

---

## 🤖 PASTE INTO AI: MY SKILL SNAPSHOT

> Copy this block and paste it at the START of any AI session so it knows exactly where you are.
> Update the symbols as you progress, then paste the updated version each time.

```
My current skill levels (adjust your explanations to match these):

TOOLS:     Terminal[⬜]  Git[⬜]  GitHub[⬜]  VSCode[⬜]  npm[⬜]

JS/TS:     JS-basics[⬜]  async-await[⬜]  fetch[⬜]
           TypeScript[⬜]  TS-with-React[⬜]

REACT:     Components[⬜]  useState[⬜]  useEffect[⬜]  Forms[⬜]

NEXT.JS:   AppRouter[⬜]  APIRoutes[⬜]  ServerComponents[⬜]  Middleware[⬜]

DATABASE:  SQL-basics[⬜]  PostgreSQL[⬜]  Prisma-schema[⬜]  Prisma-queries[⬜]

AUTH:      NextAuth[⬜]  Sessions[⬜]  ProtectedRoutes[⬜]  bcrypt[⬜]

DEPLOY:    Vercel[⬜]  EnvVars-production[⬜]

GITHUB:    Branching[⬜]  PullRequests[⬜]  OpenSource-contributions[⬜]
```

*(Replace ⬜ with 🟡 / 🟠 / 🟢 / ✅ as you progress)*

---

## 📈 PROGRESS SNAPSHOT

> Update this every 2 weeks to see your growth.

| Checkpoint | 🟢 Can Do | ✅ Confident | Projects Done | PRs Merged |
|------------|-----------|------------|---------------|------------|
| Start | 0 | 0 | 0 | 0 |
| Week 4 | | | | |
| Week 8 | | | | |
| Week 12 | | | | |
| Week 16 | | | | |
| Week 20 | | | | |
| Week 26 | | | | |

---

## 🏷️ RESUME SKILLS LIST

> When a skill reaches ✅ Confident, add it here. This becomes your resume skills section.

**Languages:** TypeScript, JavaScript
*(add more as you reach ✅)*

**Frameworks & Libraries:**
*(add as you reach ✅ — e.g., Next.js, React, Prisma, NextAuth.js, Tailwind CSS)*

**Tools:** Git, GitHub
*(add more as you reach ✅)*

**Databases:**
*(add as you reach ✅ — e.g., PostgreSQL, Prisma ORM)*

**Deployment:**
*(add as you reach ✅ — e.g., Vercel)*

---

## 🎓 SKILLS TO MENTION IN INTERVIEWS

When a skill reaches 🟢 or ✅, you can honestly claim it. Here's what to aim for:

- [ ] React.js
- [ ] Next.js (App Router)
- [ ] TypeScript
- [ ] Tailwind CSS
- [ ] REST API design
- [ ] PostgreSQL + Prisma ORM
- [ ] Authentication (NextAuth.js, JWT, sessions)
- [ ] Git & GitHub (including branching and PRs)
- [ ] Vercel deployment
- [ ] Real-time features (WebSockets / Pusher)
- [ ] Stripe payments
- [ ] Open source contribution (at least 1 merged PR)
- [ ] AI-assisted development (vibe coding)

---

*This file is a living document. The goal is to move every ⬜ to ✅ by Month 6.*
*Last updated: [DATE]*
