# Software Engineering Lab: PES2UG24CS667

A collection of all Software Engineering lab submissions, covering UML modelling, project management, refactoring, static analysis, test coverage and software testing.

## Student Details

| | |
|---|---|
| **Name** | Vidya Sri Ganesh |
| **SRN** | PES2UG24CS667 |
| **Section** | K |
| **Course** | Software Engineering Lab |
| **University** | PES University |

## Lab Index

| Lab | Topic | Contents |
|-----|-------|----------|
| [Lab 1](PES2UG24CS667_LAB1.pdf) | UML Diagrams | Report PDF |
| [Lab 2](PES2UG24CS667_LAB2.pdf) | JIRA | Report PDF |
| [Lab 3](PES2UG24CS667_LAB3.pdf) | Component Diagram | Report PDF |
| [Lab 4](PES2UG24CS667_LAB4) | Game code refactoring (Fruit Ninja) | Python code, before/after videos, chat history |
| [Lab 5](PES2UG24CS667_LAB5) | Static analysis (Pylint, Flake8, Bandit) | Original and fixed code, before/after reports, reflection |
| [Lab 6](PES2UG24CS667_LAB6) | Commits and test coverage | Code and branch coverage tests, screenshots, PDFs |
| [Lab 7](PES2UG24CS667_Lab%207) | Testing (laundry service) | Code, tests, buggy and fixed versions, report PDF |

---

## Lab Details

### Lab 1: UML Diagrams
- **Objective:** Model a software system using standard UML diagrams.
- **Deliverable:** Report PDF with the diagrams and explanations.
- **File:** `PES2UG24CS667_LAB1.pdf`

### Lab 2: JIRA
- **Objective:** Use JIRA for project and issue tracking.
- **Deliverable:** Report PDF documenting the JIRA setup and workflow.
- **File:** `PES2UG24CS667_LAB2.pdf`

### Lab 3: Component Diagram
- **Objective:** Design a component diagram showing the modules of a system and how they interact.
- **Deliverable:** Report PDF with the component diagram.
- **File:** `PES2UG24CS667_LAB3.pdf`

### Lab 4: Game Code Refactoring (Fruit Ninja)
- **Objective:** Refactor a Python Fruit Ninja game to improve structure, readability and maintainability without changing its behaviour.
- **Contents:**
  - `main.py`: game entry point
  - `game/`: game modules (`fruit.py`, `game_engine.py`, `sounds.py`)
  - `Lab-4/`: before and after demo videos and the chat history PDF
  - `requirements.txt` and `README.md`
- **Folder:** [`PES2UG24CS667_LAB4`](PES2UG24CS667_LAB4)

### Lab 5: Static Code Analysis
- **Objective:** Run static analysis tools on a loan eligibility program, find issues and fix them.
- **Tools:** Pylint (code quality), Flake8 (style and PEP 8), Bandit (security).
- **Contents:** Original and fixed code, before/after tool reports, an issues table and a short reflection.
- **Folder:** [`PES2UG24CS667_LAB5`](PES2UG24CS667_LAB5)

### Lab 6: Commits and Test Coverage
- **Objective:** Practise meaningful commits and measure test coverage on a laundry service module.
- **Contents:**
  - `laundry_service.py`: code under test
  - `test_laundry_service.py`: unit tests
  - `CodeCoverageTest_laundry_service.py` and `BranchCoverageTest_laundry_service.py`: statement and branch coverage tests
  - `CODECOVERAGE_41.png` and `BRANCHCOVERAGE_41.png`: coverage screenshots
  - `Lab6_Commits_PES2UG24CS667.pdf`: commit history report
- **Folder:** [`PES2UG24CS667_LAB6`](PES2UG24CS667_LAB6)

### Lab 7: Software Testing
- **Objective:** Test the laundry service, find the bugs in it and fix them.
- **Contents:**
  - `laundry_service_buggy_backup.py`: version with the bugs
  - `laundry_service_fixed.py`: corrected version
  - `laundry_service.py`: working version
  - `test_laundry_service.py`: test suite
  - `Lab7_Laundry_Report.pdf`: final report
- **Folder:** [`PES2UG24CS667_Lab 7`](PES2UG24CS667_Lab%207)

---

## Tools and Technologies

| Area | Tools |
|------|-------|
| Language | Python 3 |
| Testing | pytest, coverage |
| Static analysis | Pylint, Flake8, Bandit |
| Project management | JIRA |
| Version control | Git, GitHub |
| Diagrams | UML, component diagrams |

## How to Run

Clone the repository:

```bash
git clone https://github.com/vidyasriganesh/PES2UG24CS667_SE_LAB.git
cd PES2UG24CS667_SE_LAB
```

**Lab 4 (Fruit Ninja game):**

```bash
cd PES2UG24CS667_LAB4
pip install -r requirements.txt
python main.py
```

**Lab 6 and Lab 7 (tests):**

```bash
pip install pytest coverage
cd PES2UG24CS667_LAB6
pytest
coverage run -m pytest
coverage report -m
```

Use the same `pytest` command inside `PES2UG24CS667_Lab 7` to run the Lab 7 tests.

**Lab 5 (static analysis):**

```bash
pip install pylint flake8 bandit
pylint <file>.py
flake8 <file>.py
bandit <file>.py
```

## Repository Structure

```
PES2UG24CS667_SE_LAB/
├── README.md
├── PES2UG24CS667_LAB1.pdf
├── PES2UG24CS667_LAB2.pdf
├── PES2UG24CS667_LAB3.pdf
├── PES2UG24CS667_LAB4/    Game refactoring
├── PES2UG24CS667_LAB5/    Static analysis
├── PES2UG24CS667_LAB6/    Test coverage
└── PES2UG24CS667_Lab 7/   Testing
```

## Author

**Vidya Sri Ganesh**
SRN: PES2UG24CS667 | Section K
GitHub: [@vidyasriganesh](https://github.com/vidyasriganesh)
