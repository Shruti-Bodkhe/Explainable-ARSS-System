# ARSS System – Explainable AI-Based Automated Resume Screening System

## Overview

The Automated Resume Screening System (ARSS) is an Explainable AI-powered recruitment support platform designed to automate the initial stages of candidate screening. The system evaluates uploaded resumes against selected job roles using semantic similarity analysis, skill matching, and explainable scoring techniques.

Traditional resume screening is time-consuming, subjective, and difficult to scale when recruiters receive hundreds of applications for a single position. ARSS addresses this challenge by automatically ranking candidates based on their relevance to job requirements while providing transparent explanations for each recommendation.

The system combines Natural Language Processing (NLP), BERT-based semantic understanding, skill extraction, and interactive visual analytics to assist recruiters in making faster and more informed hiring decisions.

---

# Problem Statement

Organizations often receive a large number of resumes for a single job opening. Manual screening requires significant time and effort and may lead to inconsistencies or human bias.

The objective of this project is to develop an automated and explainable resume screening system that:

* Processes resumes automatically.
* Extracts candidate skills and information.
* Compares candidate profiles with job requirements.
* Generates candidate rankings.
* Provides explainable recommendations.
* Visualizes recruitment insights through an interactive dashboard.

---

# Objectives

* Automate resume screening and ranking.
* Reduce recruiter workload.
* Improve candidate shortlisting efficiency.
* Implement semantic matching using BERT.
* Provide explainable AI-based recommendations.
* Generate visual analytics for hiring decisions.
* Create a professional recruiter dashboard.

---

# Key Features

### Resume Processing

* PDF Resume Upload
* Resume Parsing
* Text Extraction
* Skill Extraction
* Candidate Information Processing

### Intelligent Matching

* Job Role Selection
* Skill-Based Matching
* Semantic Similarity Matching
* BERT Embedding Comparison
* Resume Ranking

### Explainable AI

* Match Percentage Calculation
* Matched Skills Identification
* Missing Skills Detection
* Recommendation Generation
* Candidate Score Explanation

### Interactive Dashboard

* Candidate Ranking Table
* Top Candidate Profile
* KPI Flashcards
* Match Distribution Charts
* Skill Coverage Analytics
* Candidate Comparison Visualizations
* Downloadable Reports

---

# System Architecture

Resume Upload
↓
Resume Parsing
↓
Text Extraction
↓
Skill Extraction
↓
Job Description Processing
↓
BERT Semantic Similarity
↓
Skill Matching Engine
↓
Score Calculation
↓
Explainability Layer
↓
Candidate Ranking
↓
Interactive Dashboard

---

# Technologies Used

## Programming Language

* Python 3.x

## Machine Learning & NLP

* BERT (Bidirectional Encoder Representations from Transformers)
* Sentence Transformers
* Scikit-learn

## Data Processing

* Pandas
* NumPy

## Resume Parsing

* PDFMiner
* PyResParser
* Docx2txt
* OCR Support

## Visualization

* Plotly
* Matplotlib

## Web Framework

* Streamlit

## Version Control

* Git
* GitHub

---

# Methodology

## Phase 1: Dataset Collection

A collection of resumes from multiple domains was gathered for experimentation and evaluation.

The dataset included resumes from:

* Data Science
* Machine Learning
* Software Development
* Web Development
* Artificial Intelligence
* General Technical Profiles

---

## Phase 2: Resume Parsing

Resumes were processed to extract textual information.

Extracted information includes:

* Skills
* Experience
* Education
* Projects
* Certifications

---

## Phase 3: Job Role Definition

Job role requirements were manually defined.

Examples:

* Data Scientist
* Machine Learning Engineer
* Web Developer

Each role contains:

* Required Skills
* Preferred Skills
* Domain Keywords

---

## Phase 4: Semantic Matching using BERT

Traditional keyword matching often fails when candidates use different wording.

Example:

"Machine Learning" and "Predictive Analytics"

may represent similar concepts but contain different keywords.

BERT embeddings were used to capture semantic meaning and measure similarity between:

Resume Content ↔ Job Requirements

This improves candidate relevance assessment.

---

## Phase 5: Skill Matching

The system identifies:

### Matched Skills

Skills present in both:

* Resume
* Job Requirement

### Missing Skills

Skills required by the role but absent in the resume.

---

## Phase 6: Score Generation

The final score is calculated using:

### Semantic Similarity Score

Measures contextual relevance using BERT.

### Skill Match Score

Measures overlap between candidate skills and job requirements.

### Combined Score

Used to rank candidates.

---

## Phase 7: Explainability Layer

To ensure transparency, the system generates:

* Match Percentage
* Matched Skills
* Missing Skills
* Recommendation
* Explanation Statement

This enables recruiters to understand why a candidate received a particular ranking.

---

# Evaluation Metrics

The project supports evaluation using:

* Accuracy
* Precision
* Recall
* F1 Score
* Confusion Matrix

These metrics help validate the effectiveness of the screening system.

---

# Dashboard Analytics

The recruiter dashboard provides:

### Candidate Overview

* Total Candidates
* Top Match Percentage
* Average Match Score
* Selection Rate

### Visual Insights

* Match Score Distribution
* Candidate Ranking Analysis
* Skill Coverage Charts
* Recommendation Breakdown

### Candidate Profile

* Resume Name
* Match Score
* Matched Skills
* Missing Skills
* Recommendation

---

# Project Structure

Explainable_ARSS_Project/

├── dataset/

├── notebooks/

├── ui_dashboard/

│ ├── app.py

│ ├── process.py

│ ├── auth.py

│ ├── styles.py

│ └── bert_utils.py

├── results/

├── evaluation.py

├── requirements.txt

├── README.md

└── .gitignore

---

# Challenges Faced

### Resume Format Variability

Different resume templates required robust parsing logic.

### Skill Standardization

Candidates often describe identical skills using different terminology.

### Semantic Understanding

Keyword matching alone was insufficient.

BERT-based embeddings were introduced to improve contextual understanding.

### Explainability

Generating transparent recommendations required additional logic beyond simple ranking.

### Dashboard Design

Building a recruiter-focused interface required balancing usability, analytics, and professional presentation.

---

# Future Enhancements

* Multi-Industry Job Roles
* Advanced Resume Classification
* Interview Recommendation Engine
* Candidate Skill Gap Analysis
* Real-Time Recruitment Analytics
* Cloud Deployment
* Recruiter Authentication System
* Generative AI Feedback Module

---

# Results

The ARSS system successfully:

* Automates resume screening.
* Ranks candidates effectively.
* Provides explainable recommendations.
* Reduces manual recruiter effort.
* Delivers interactive recruitment analytics.

The integration of BERT-based semantic matching significantly improves candidate-job relevance assessment compared to traditional keyword matching approaches.

---
**Complete UI Demonstration and Screenshots:**

[View Projects_Screenshots.pdf](Projects_Screenshots.pdf)

---
# Team Members

- Shruti Bodkhe
- Mayuri Jagtap
- Shreya Madne
- Jayant Deshmukh

Bachelor of Technology (Computer Science Engineering)

Specialization: Artificial Intelligence & Analytics

MIT School of Computing, Pune

---

