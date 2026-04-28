# PRD Template Quick Reference Guide

## 🎯 Purpose
This is your universal template for creating detailed Product Requirements Documents for ANY project type - software, hardware, services, APIs, mobile apps, or anything else.

---

## 📋 Quick Start Checklist

### Before You Start
- [ ] Understand the problem you're solving
- [ ] Know your target users
- [ ] Have stakeholder alignment on goals
- [ ] Gather any existing documentation

### Filling Out the Template
- [ ] **Section 1-2:** Executive Summary & Overview (30 mins)
- [ ] **Section 3-4:** Problem Statement & Goals (1 hour)
- [ ] **Section 5-6:** Users & Use Cases (2 hours)
- [ ] **Section 7-8:** Functional & Non-Functional Requirements (3-4 hours)
- [ ] **Sections 9-14:** Technical Details (varies by complexity)
- [ ] **Section 15:** Testing Strategy (1 hour)
- [ ] **Sections 16-20:** Implementation & Planning (2 hours)

### After Completion
- [ ] Review with technical team
- [ ] Review with stakeholders
- [ ] Get formal approval
- [ ] Share with all team members
- [ ] Set up version control

---

## 🚀 How to Use This Template for Different Projects

### For a Web Application
**Focus On:**
- Sections 7-8: Functional & Non-functional requirements
- Section 9: System architecture
- Section 11: UI/UX
- Section 13: APIs and integrations
- Section 15: Testing strategy

**You Can Skip/Minimize:**
- Section 10.4: Data migration (unless migrating from old system)
- Hardware-specific details

**Example Projects:**
- E-commerce platform
- Social media app
- SaaS dashboard
- Content management system

---

### For a Mobile App
**Focus On:**
- Section 5: User personas (mobile users behave differently)
- Section 8.6: Compatibility (iOS/Android versions)
- Section 11: UI/UX (mobile-specific patterns)
- Section 14: Privacy (app permissions)
- Platform-specific requirements

**Add Custom Sections:**
- App store requirements (iOS App Store, Google Play)
- Push notification strategy
- Offline functionality
- Mobile-specific performance metrics

**Example Projects:**
- Food delivery app
- Fitness tracker
- Mobile game
- Banking app

---

### For an API/Platform
**Focus On:**
- Section 7: Functional requirements (endpoints)
- Section 8: Non-functional (performance, rate limiting)
- Section 13: Integration & APIs (this is your core)
- Section 14: Security (authentication, authorization)
- API documentation standards

**Add Custom Sections:**
- API versioning strategy
- SDK requirements
- Developer portal requirements
- Sample code and examples

**Example Projects:**
- RESTful API
- GraphQL API
- Payment gateway
- Data analytics platform

---

### For Hardware Products
**Focus On:**
- Section 3: Problem statement (physical needs)
- Section 7: Functional requirements (physical capabilities)
- Section 8: Non-functional (durability, environmental)
- Physical specifications (add custom section)
- Manufacturing constraints

**Add Custom Sections:**
- Materials and components
- Physical dimensions and weight
- Environmental conditions (temperature, humidity)
- Safety and compliance certifications
- Manufacturing and assembly process

**Example Projects:**
- IoT device
- Consumer electronics
- Medical device
- Industrial equipment

---

### For Internal Tools/Services
**Focus On:**
- Section 2.3: Target audience (internal users)
- Section 6: Use cases (internal workflows)
- Section 7: Functional requirements
- Section 12: Business rules (company policies)
- Section 16: Implementation (internal rollout)

**You Can Skip:**
- Marketing metrics
- Competitive analysis
- Complex scaling (unless needed)

**Example Projects:**
- Employee management system
- Internal reporting tool
- Workflow automation
- Admin dashboard

---

### For AI/ML Projects
**Focus On:**
- Section 3: Problem statement (what AI solves)
- Section 7: Functional requirements (AI capabilities)
- Section 8: Performance (accuracy, precision, recall)
- Section 10: Data requirements (training data)
- Section 15: Testing (model validation)

**Add Custom Sections:**
- Model architecture
- Training data requirements
- Model performance metrics
- Bias and fairness considerations
- Model monitoring and retraining

**Example Projects:**
- Recommendation engine
- Image recognition system
- Chatbot/conversational AI
- Predictive analytics tool

---

## 📊 Section-by-Section Guide

### Essential Sections (Never Skip)
1. **Executive Summary** - Your elevator pitch
2. **Problem Statement** - Why this exists
3. **Goals & Objectives** - What success looks like
4. **Functional Requirements** - What it does
5. **Success Metrics** - How you measure it

### Important Sections (Skip Only if Not Applicable)
6. **User Personas** - Who uses it
7. **Non-Functional Requirements** - Performance, security, etc.
8. **Testing Strategy** - How you verify it works
9. **Implementation Plan** - How you build it
10. **Risks** - What could go wrong

### Optional Sections (Use as Needed)
11. **System Architecture** - For technical projects
12. **Data Model** - If data is central
13. **UI/UX** - For user-facing products
14. **APIs** - For integrated systems
15. **Business Rules** - For complex workflows

---

## 🎨 Customization Examples

### Minimal PRD (Simple Internal Tool)
Keep only:
- Executive Summary
- Problem Statement
- Functional Requirements
- Testing Strategy
- Implementation Plan

**Total Length:** 5-10 pages

---

### Standard PRD (Typical Product)
Include:
- All essential sections
- Most important sections
- Selected optional sections based on project type

**Total Length:** 20-40 pages

---

### Comprehensive PRD (Complex Enterprise System)
Include:
- All sections
- Detailed appendices
- Multiple persona profiles
- Extensive test cases
- Complete API documentation

**Total Length:** 50-100+ pages

---

## ✍️ Writing Tips

### Be Specific
❌ "The system should be fast"
✅ "API response time must be <200ms for 95th percentile"

### Be Testable
❌ "User-friendly interface"
✅ "New users complete first task within 5 minutes with 90% success rate"

### Be Complete
❌ "Support payment processing"
✅ "Support payment processing via Stripe API with credit cards, debit cards, and PayPal, including refund workflows"

### Use Acceptance Criteria
For every requirement, include:
- [ ] Specific condition that must be met
- [ ] How it will be verified
- [ ] What "done" looks like

### Prioritize with MoSCoW
- **Must Have** - Non-negotiable for launch
- **Should Have** - Important but not critical
- **Could Have** - Nice to have if time permits
- **Won't Have** - Out of scope for this version

---

## 🔄 PRD Lifecycle

### Phase 1: Draft (Week 1)
- Fill in essential sections
- Get input from key stakeholders
- Identify gaps and questions

### Phase 2: Review (Week 2)
- Circulate to team
- Gather feedback
- Refine requirements
- Add technical details

### Phase 3: Approval (Week 3)
- Present to stakeholders
- Address concerns
- Get formal sign-off
- Baseline the document

### Phase 4: Living Document
- Update as you learn
- Track changes in version history
- Review quarterly
- Maintain single source of truth

---

## 🛠️ Tools to Use Alongside PRD

### Documentation
- **Diagrams:** Draw.io, Lucidchart, Miro
- **Mockups:** Figma, Sketch, Adobe XD
- **Workflows:** Miro, Whimsical

### Collaboration
- **Review:** Google Docs, Confluence
- **Tracking:** Jira, Linear, Asana
- **Version Control:** Git for markdown PRDs

### Templates
- **User Stories:** Use this template's Section 6
- **Test Cases:** Use this template's Section 15
- **API Docs:** Use this template's Section 13

---

## 📌 Common Mistakes to Avoid

### 1. Writing Implementation Instead of Requirements
❌ "Use PostgreSQL database with Redis cache"
✅ "System must store data persistently with sub-second retrieval"

(Save implementation details for technical design docs)

### 2. Vague Requirements
❌ "System should handle lots of users"
✅ "System must support 10,000 concurrent users with 99.9% uptime"

### 3. Missing Edge Cases
Always ask:
- What if the user enters invalid data?
- What if the external service is down?
- What if the user loses connection?

### 4. No Acceptance Criteria
Every requirement needs:
- Clear pass/fail criteria
- How it will be tested
- Who will test it

### 5. Scope Creep During Writing
Stick to your MVP definition. Create a "Future Enhancements" section for nice-to-haves.

### 6. Writing Alone
PRDs should be collaborative:
- Include product team
- Consult with engineering
- Validate with users
- Review with stakeholders

---

## 📈 PRD Quality Checklist

### Content Quality
- [ ] Every requirement has acceptance criteria
- [ ] All requirements are testable
- [ ] No ambiguous language ("fast," "good," "user-friendly")
- [ ] Clear priorities (Must/Should/Could/Won't)
- [ ] Realistic timelines and resources

### Completeness
- [ ] All essential sections filled
- [ ] All stakeholders identified
- [ ] All risks documented
- [ ] All dependencies listed
- [ ] All integrations specified

### Clarity
- [ ] Anyone can understand the purpose
- [ ] Technical and non-technical readers can follow
- [ ] Examples provided where helpful
- [ ] Diagrams included for complex concepts
- [ ] Glossary defines all terms

### Usability
- [ ] Table of contents present
- [ ] Sections well-organized
- [ ] Easy to find information
- [ ] Consistent formatting
- [ ] Version-controlled

---

## 💡 Pro Tips

### 1. Start with "Why"
Before writing anything, clearly articulate:
- Why are we building this?
- What problem does it solve?
- How will we know it's successful?

### 2. Include Real Examples
Don't just describe features abstractly. Show:
- Sample user flows
- Example data
- Mock screenshots
- API request/response examples

### 3. Make It Scannable
Use:
- Tables for structured data
- Bullet points for lists
- Headers for organization
- Callout boxes for important notes

### 4. Link to Supporting Docs
Your PRD references:
- Design mockups
- Technical architecture docs
- Market research
- User research findings

### 5. Version Everything
Track:
- What changed
- When it changed
- Who changed it
- Why it changed

---

## 🎓 Learning Resources

### Templates & Examples
- [Product Hunt PRD examples]
- [Atlassian PRD guide]
- [Productboard templates]

### Books
- "Inspired" by Marty Cagan
- "The Lean Product Playbook" by Dan Olsen
- "User Story Mapping" by Jeff Patton

### Courses
- Product School
- Pragmatic Institute
- Mind the Product

---

## 🚦 When to Use What Format

### Use This Full Template When:
- Building a new product from scratch
- Complex system with many stakeholders
- Need formal approval process
- Enterprise or regulated environment

### Use Simplified Version When:
- Internal tools
- Small features or updates
- Proof of concept
- Quick experiments

### Use Alternative Formats When:
- **One-pager:** Executive pitch
- **User stories:** Agile development
- **Spec doc:** Technical implementation
- **RFP:** Vendor selection

---

## 📞 Getting Help

### Stuck on a Section?
1. Look at similar products' docs
2. Interview users or stakeholders
3. Start with what you know, mark TODOs
4. Get feedback from team

### Need Validation?
- Share draft with 2-3 people
- Ask specific questions
- Iterate based on feedback

### Disagreement on Requirements?
- Document both perspectives
- Define decision criteria
- Get stakeholder input
- Make decision and document rationale

---

## ✅ Final Checklist Before Sharing

- [ ] All sections relevant to your project are complete
- [ ] All TODOs and placeholders removed
- [ ] Reviewed by at least 2 people
- [ ] Stakeholders identified and aligned
- [ ] Acceptance criteria defined for all requirements
- [ ] Success metrics clearly defined
- [ ] Risks identified and mitigation planned
- [ ] Timeline is realistic
- [ ] Budget is approved (if applicable)
- [ ] Document is properly formatted
- [ ] Version number and date are correct
- [ ] All links work
- [ ] All diagrams are included

---

**Remember: A PRD is a living document. Start with what you know, iterate, and improve as you learn more!**

---

## 📝 Template Versions

### Current Version: 2.0
- **File:** `PRD_Template_Universal.md`
- **Use For:** Any project type
- **Length:** Comprehensive (all sections)

### Quick Start Version (Coming Soon)
- **File:** `PRD_Template_Minimal.md`
- **Use For:** Simple projects, MVPs
- **Length:** Essential sections only (10-15 pages)

### Technical Spec Version (Coming Soon)
- **File:** `Technical_Spec_Template.md`
- **Use For:** Implementation details
- **Length:** Technical focus

---

**Good luck with your PRDs! 🚀**
