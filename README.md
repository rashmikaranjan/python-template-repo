🚀 **Python-Template-Repo**

# Description
This repository serves as a template for Python projects, including:
- **Pre-configured CI/CD pipeline** using CircleCI
- **Strict static analysis & formatting** with `ruff` and `mypy`
- **Comprehensive testing** (Unit, Integration, End-to-End) using `pytest`
- **Test coverage tracking**

📌 Setup & Installation

1️⃣ Clone the Repository
git clone https://github.com/lkyuan233/python-template-repo.git
cd python-template-repo

2️⃣ Install Dependencies
pip install --upgrade pip
uv pip install -r requirements.txt

3️⃣ Run Static Analysis & Formatting
ruff check .
mypy src/
ruff format .

🛠️ Usage
This repository includes three key components: (please refer component.md)
- Calculator – Performs basic arithmetic operations.
- Logger – Records calculator operations.
- Notifier – Sends an alert when results exceed a threshold.

✅ Running Tests

📊 Viewing Coverage Report

CI/CD Pipeline (CircleCI)
Tests are executed on every push to GitHub.
Results are visible in CircleCI’s “Tests” section.
Test coverage report is available via CircleCI artifacts.
To manually trigger a CI/CD run:
- Push a commit or open a PR.
- Check CircleCI dashboard

📏 Code Quality Tools
The repository enforces strict linting and static analysis:
- Code Formatting: ruff format .
- Linting: ruff check .
- Static Analysis: mypy src/
If any check fails, fix issues before committing.

🤝 Contributing
- Fork the repo.
- Create a new branch: git checkout -b feature-name
- Commit changes: git commit -m "Add feature"
- Push and create a PR.

# License
This project is licensed under the MIT License. For more details, see the LICENSE file.
