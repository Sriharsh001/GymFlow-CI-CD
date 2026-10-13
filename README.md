# GymFlow CI/CD

A fitness and gym management application built with Flask, integrated with automated testing, Docker containerization, GitHub Actions, and Jenkins.

**Project Overview**

GymFlow demonstrates how DevOps practices can automate application validation and build processes. The project uses Git for version control, Pytest for testing, Docker for containerization, GitHub Actions for continuous integration, and Jenkins for automated builds.

**Technology Stack**

- Python and Flask
- Pytest
- Ruff for code linting
- Git and GitHub
- Docker
- GitHub Actions
- Jenkins

**Project Structure**

```text
GymFlow-CI-CD/
├── .github/
│   └── workflows/
│       └── main.yml
├── tests/
│   └── test_app.py
├── app.py
├── requirements.txt
├── Dockerfile
├── .gitignore
└── README.md
```

**Application Features**

- Welcome endpoint
- Health-check endpoint
- Fitness program listing
- Member listing and registration
- Automated API tests

**Getting Started**

Prerequisites: Python, Git, and Docker if you want to run the containerized version.

1. Clone the repository.

   ```bash
   git clone https://github.com/Sriharsh001/GymFlow-CI-CD.git
   cd GymFlow-CI-CD
   ```

2. Install the dependencies.

   ```bash
   python -m pip install -r requirements.txt
   ```

3. Start the application.

   ```bash
   python app.py
   ```

4. Open `http://localhost:5000` in your browser.

**Testing and Code Quality**

Run the automated tests:

```bash
python -m pytest -v
```

Check code quality with Ruff:

```bash
python -m pip install ruff
python -m ruff check app.py tests
```

**Docker**

Build the application image:

```bash
docker build -t gymflow-ci-cd:latest .
```

Run the application:

```bash
docker run --rm -p 5000:5000 gymflow-ci-cd:latest
```

Run the tests inside the Docker image:

```bash
docker run --rm gymflow-ci-cd:latest python -m pytest -v
```

**GitHub Actions**

The workflow is defined in `.github/workflows/main.yml` and runs on pushes and pull requests.

The pipeline performs the following steps:

1. Checks out the repository.
2. Installs the Python dependencies.
3. Compiles the Python files and checks code quality.
4. Runs the automated tests.
5. Builds the Docker image.
6. Runs the automated tests inside the Docker container.

Workflow results are available in the repository's **Actions** tab.

**Jenkins**

The Jenkins job checks out the latest source code from GitHub and automates the following operations:

- Dependency installation
- Code linting
- Automated testing
- Docker image building
- Test execution inside the Docker container

A successful build confirms that the configured pipeline stages have completed without errors.

**Learning Outcomes**

This project demonstrates practical implementation of:

- Version control and meaningful Git commits
- Automated testing with Pytest
- Code quality checks
- Docker image creation and containerized testing
- CI workflow automation using GitHub Actions
- Automated builds using Jenkins

**Repository**

[GymFlow CI/CD on GitHub](https://github.com/Sriharsh001/GymFlow-CI-CD)
