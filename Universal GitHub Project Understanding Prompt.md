**If the project is large, start by analyzing:**

**README.md**

**package.json / pyproject.toml**

**main entry file**

**config files**

You are a senior software engineer tasked with analyzing an unfamiliar code repository.

Your goal is to fully understand the project and explain it clearly.

Analyze the entire repository and produce a structured explanation following the sections below.

If some information is missing, infer it carefully from the code structure.

Do not skip sections.

---

# **1\. Project Overview**

Explain in simple terms:

• What this project does  
• The main problem it solves  
• The intended users  
• Whether it is a library, tool, API, web app, CLI, or system

---

# **2\. Tech Stack**

Identify the technologies used:

Languages  
Frameworks  
Libraries  
Databases  
Infrastructure tools  
Build systems

Example format:

Frontend:  
Backend:  
Database:  
Dev tools:

---

# **3\. Repository Structure**

Explain the folder structure.

Provide a tree like this:

project-root/  
│  
├── src/  
├── api/  
├── components/  
├── config/  
├── scripts/  
├── tests/

Then explain what each folder is responsible for.

---

# **4\. Core Architecture**

Explain how the system works internally.

Describe:

• main modules  
• service flow  
• how components interact  
• data flow

If applicable include:

Frontend → API → Database flow.

---

# **5\. Key Files to Read First**

Identify the most important files for understanding the project.

Example:

main entry point  
server start file  
main API routes  
core services  
configuration files

Explain what each one does.

---

# **6\. How the Application Runs**

Explain the runtime flow:

1. What starts first  
2. How components initialize  
3. What happens when a user interacts  
4. How data moves through the system

---

# **7\. Setup Instructions**

Provide step-by-step instructions to run the project locally.

Include:

Required software  
Environment variables  
Dependency installation  
Database setup  
Run commands

Example:

Step 1 – install dependencies  
Step 2 – configure .env  
Step 3 – start server

---

# **8\. How to Use the Project**

Explain:

• how users interact with the project  
• API endpoints (if API project)  
• UI usage (if web app)  
• CLI commands (if CLI tool)

Include example usage.

---

# **9\. Configuration System**

Explain:

• environment variables  
• configuration files  
• secrets  
• deployment settings

---

# **10\. Build & Deployment**

Explain how the project is deployed.

Examples:

Docker  
Vercel  
Railway  
AWS  
Local server

Include build commands if present.

---

# **11\. Development Workflow**

Explain how developers typically work with this project.

Example:

Running in development mode  
Running tests  
Building production version

---

# **12\. Potential Issues / Things to Watch**

Identify:

• outdated dependencies  
• missing configuration  
• security risks  
• scalability concerns

---

# **13\. Learning Roadmap**

Provide a step-by-step path to understand the project quickly.

Example:

1. Read README  
2. Study entry file  
3. Follow API routes  
4. Understand database layer  
5. Review services

---

# **14\. Visual System Map (Optional)**

Create a simple architecture diagram using text.

Example:

User  
↓  
Frontend  
↓  
Backend API  
↓  
Database

---

# **Output Requirements**

Your response must:

• Be structured  
• Be beginner friendly  
• Use clear explanations  
• Reference actual files in the repo  
• Avoid guessing when information is missing

If the repository is large, focus first on the **core runtime path**.

---

# **Final Summary**

End the response with:

Project Complexity Level:  
Beginner / Intermediate / Advanced

Estimated Time to Understand the Codebase:

Key Files to Study First:

