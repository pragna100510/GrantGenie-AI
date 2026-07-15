# 🚀 GrantGenie-AI

## Agentic AI-Based Startup Grant Recommendation and Proposal Generation System

GrantGenie-AI is an Agentic AI application that helps startups identify suitable funding opportunities, analyze eligibility requirements, and generate AI-powered funding proposals.

The system uses multiple AI agents powered by **IBM watsonx.ai** to automate the grant discovery and application preparation process.

---

# 📌 Problem Statement

Startups often face difficulties in:

- Finding relevant government and private funding opportunities
- Understanding complex grant eligibility criteria
- Determining whether they qualify for a grant
- Preparing professional funding proposals

GrantGenie-AI solves this problem by providing an intelligent AI assistant that analyzes startup details and recommends suitable grants.

---

# 💡 Solution Overview

GrantGenie-AI follows an Agentic AI workflow where multiple specialized agents collaborate:

```
                Startup Information
                        |
                        ↓
              Startup Profile Agent
                        |
                        ↓
              Grant Recommendation Agent
                        |
                        ↓
             Eligibility Verification Agent
                        |
                        ↓
             Proposal Generation Agent
                        |
                        ↓
             AI Funding Proposal
```

---

# 🤖 AI Agents

## 1. Startup Profile Agent

**Purpose:**
Extracts important startup information from user input.

Extracts:

- Domain
- Country
- Startup stage
- Technologies
- Funding requirement


---

## 2. Grant Recommendation Agent

**Purpose:**
Finds suitable grants based on startup characteristics.

Provides:

- Grant name
- Sector
- Funding amount
- Deadline
- Website
- Match score
- Recommendation reason


---

## 3. Eligibility Verification Agent

**Purpose:**
Evaluates startup eligibility for recommended grants.

Generates:

- Eligibility percentage
- Matched requirements
- Missing requirements
- Recommendations


---

## 4. Proposal Generation Agent

**Purpose:**
Creates an AI-generated funding proposal.

Generates:

- Problem statement
- Solution overview
- Technical approach
- Budget requirements
- Expected impact


---

# 🛠️ Technology Stack

## Frontend

- React.js
- Vite
- CSS

## Backend

- Python
- FastAPI

## Artificial Intelligence

- IBM watsonx.ai
- Meta Llama 3.3 70B Instruct Model

## Deployment

- Render / IBM Code Engine

---

# ☁️ IBM watsonx.ai Integration

GrantGenie-AI uses IBM watsonx.ai foundation models for intelligent reasoning and content generation.

Model used:

```
meta-llama/llama-3-3-70b-instruct
```

IBM watsonx.ai provides:

- Large Language Model inference
- AI-powered decision support
- Natural language generation

---

# ✨ Features

✅ AI startup profile extraction  
✅ Intelligent grant recommendation  
✅ Grant match scoring  
✅ Eligibility verification  
✅ Missing requirement detection  
✅ AI-generated funding proposal  
✅ Modern dashboard interface  
✅ Interactive proposal generation  

---

# 📂 Project Structure

```
GrantGenie-AI
│
├── backend
│   │
│   ├── app.py
│   ├── agents
│   ├── routes
│   ├── services
│   ├── utils
│   └── requirements.txt
│
├── frontend
│   │
│   ├── src
│   ├── package.json
│   └── vite.config.js
│
├── app.json
├── README.md
├── yourproblemstatement.pdf
└── projectpresentation.pptx
```

---

# ⚙️ Installation and Setup

## Clone Repository

```bash
git clone https://github.com/pragna100510/GrantGenie-AI.git

cd GrantGenie-AI
```

---

# Backend Setup

Navigate to backend:

```bash
cd backend
```

Create virtual environment:

```bash
python -m venv venv
```

Activate:

Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create environment variables:

```
IBM_API_KEY=your_api_key
IBM_PROJECT_ID=your_project_id
IBM_URL=https://us-south.ml.cloud.ibm.com
```

Run backend:

```bash
uvicorn app:app --reload
```

Backend runs at:

```
http://localhost:8000
```

API documentation:

```
http://localhost:8000/docs
```

---

# Frontend Setup

Navigate:

```bash
cd frontend
```

Install packages:

```bash
npm install
```

Run:

```bash
npm run dev
```

Frontend runs at:

```
http://localhost:5173
```

---

# 📊 Application Workflow

1. User enters startup description

2. Startup Profile Agent analyzes the idea

3. Grant Agent recommends suitable funding opportunities

4. Eligibility Agent evaluates requirements

5. Proposal Agent generates a funding proposal

6. User can review and export the proposal

---

# 🎯 Use Cases

- Early-stage startups
- Student entrepreneurs
- Innovation teams
- Research organizations
- Government grant applicants

---

# 🔮 Future Enhancements

- Real-time grant database integration
- Multi-language support
- Automated grant application submission
- More specialized funding agents
- Document-based eligibility verification

---

# 👩‍💻 Team

**GrantGenie-AI Team**

Agentic AI Project  
IBM SkillsBuild Internship

---

# 📄 License

This project is developed for educational purposes as part of the IBM SkillsBuild Internship Program.