# Phishing Mail Detector

A beginner-friendly phishing email detection system built using Python, designed to identify suspicious language patterns and malicious links in email content.  
The project is developed phase-by-phase to build a strong understanding of cybersecurity fundamentals and Python programming concepts.

---

## Goals
- Detect phishing emails using rule-based content analysis  
- Identify suspicious keywords and extract embedded links  
- Assign a simple risk level based on detected indicators  

---

## Project Structure
- `detector.py` — Main phishing detection script  
- `README.md` — Project documentation and phase-wise progress  

---

## Detection Phases

### Phase 1: Email Input & Preprocessing
- Accept email content from user input  
- Normalize text using lowercase conversion  

### Phase 2: Suspicious Keyword Detection
- Identify common phishing-related keywords  
- Count occurrences of suspicious language  

### Phase 3: Risk-Based Decision Logic
- Assign risk levels based on keyword thresholds  
- Classify emails as safe or likely phishing  

### Phase 4: Code Modularization
- Refactor logic into reusable Python functions  
- Improve readability and control flow  

### Phase 5: Link Detection & URL Extraction
- Detect presence of links in email content  
- Extract and clean URLs from text  
- Separate detection logic from reporting logic  

---

## Status
Phase 5 completed:
- Suspicious keyword detection  
- Risk-based decision logic  
- URL extraction and link detection  

Phase 6: Domain-level analysis (planned)

---

## Tech Stack
- Python (core logic and detection)
- Git & GitHub (version control and project hosting)
- VS Code & PowerShell (development environment)

---

## How to Run

1. Clone the repository  
2. Navigate to the project directory  
3. Run the detector script:

```bash
python detector.py
