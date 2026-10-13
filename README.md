\# GymFlow CI/CD — ACEest Fitness \& Gym



\## 1. Project Overview



GymFlow CI/CD is a Flask-based web application developed for the ACEest Fitness \& Gym DevOps assignment. It demonstrates how Git, GitHub, Pytest, Docker, Jenkins, and GitHub Actions can be used together to implement a Continuous Integration and Continuous Delivery (CI/CD) workflow.



The application provides basic fitness program information, a health-check endpoint, and simple member registration functionality.



\## 2. Features



\- Flask REST API

\- Application health-check endpoint

\- Fitness program listing

\- Member registration and listing

\- Automated unit testing using Pytest

\- Code quality checks using Ruff

\- Docker image creation

\- Jenkins-based CI build

\- GitHub Actions workflow triggered by pushes and pull requests



\## 3. Technology Stack



\- \*\*Language:\*\* Python

\- \*\*Web framework:\*\* Flask

\- \*\*Testing:\*\* Pytest

\- \*\*Linting:\*\* Ruff

\- \*\*Containerization:\*\* Docker

\- \*\*Source control:\*\* Git and GitHub

\- \*\*CI/CD:\*\* Jenkins and GitHub Actions



\## 4. Application Endpoints



| Method | Endpoint | Description |

|---|---|---|

| GET | `/` | Application welcome message |

| GET | `/health` | Application health status |

| GET | `/programs` | List available fitness programs |

| GET | `/members` | List registered members |

| POST | `/members` | Register a member using JSON |



\### Example member registration



Request:



```json

{

&#x20; "name": "Harsha"

}

```



Send this JSON body with a `POST` request to `/members`. A successful registration returns HTTP status `201`.



> Note: Member records are stored in memory and are reset when the application restarts.



\## 5. Prerequisites



Install the following tools:



\- Python 3.13 or a compatible Python version

\- Git

\- Docker Desktop

\- A GitHub account



Jenkins is required to reproduce the local Jenkins CI workflow.



\## 6. Run Locally



Clone the repository:



```bash

git clone https://github.com/Sriharsh001/GymFlow-CI-CD.git

cd GymFlow-CI-CD

```



Create and activate a virtual environment.



On Windows:



```cmd

python -m venv .venv

.venv\\Scripts\\activate

```



Install dependencies:



```bash

python -m pip install -r requirements.txt

python -m pip install ruff

```



Start the application:



```bash

python app.py

```



Open `http://localhost:5000` in a browser to access the application.



\## 7. Run Quality Checks and Tests



Run Ruff:



```bash

python -m ruff check app.py tests

```



Run the unit tests:



```bash

python -m pytest -v

```



The current test suite contains five tests covering the home endpoint, health endpoint, fitness programs, successful member registration, and validation of a missing member name.



\## 8. Docker



Build the Docker image:



```bash

docker build -t gymflow-ci-cd:latest .

```



Run the application container:



```bash

docker run --rm -p 5000:5000 gymflow-ci-cd:latest

```



Open `http://localhost:5000` to access the application.



Run the test suite inside the Docker image:



```bash

docker run --rm gymflow-ci-cd:latest python -m pytest -v

```



The Docker image includes the application, dependencies, and test files.



\## 9. GitHub Actions



The workflow is defined in `.github/workflows/main.yml`.



It runs on pushes and pull requests and performs the configured CI checks:



1\. Check out the repository.

2\. Set up Python.

3\. Install dependencies.

4\. Compile Python files and run Ruff lint checks.

5\. Run unit tests.

6\. Build the Docker image.



Workflow results are available in the \*\*Actions\*\* tab of the GitHub repository.



\## 10. Jenkins CI



A Jenkins Freestyle project named `GymFlow-CI-CD` is configured to pull source code from:



https://github.com/Sriharsh001/GymFlow-CI-CD.git



The configured Windows batch build performs these stages:



1\. Install Python dependencies.

2\. Install Ruff.

3\. Run lint checks.

4\. Run unit tests on Windows.

5\. Build the Docker image.

6\. Run the same unit tests inside the Docker container.



The build should be considered successful only when all stages pass. Build logs are available through Jenkins \*\*Console Output\*\*.



\## 11. Repository Structure



```text

GymFlow-CI-CD/

├── .github/

│   └── workflows/

│       └── main.yml

├── tests/

│   └── test\_app.py

├── .gitignore

├── app.py

├── Dockerfile

├── requirements.txt

└── README.md

```



\## 12. Conclusion



This project demonstrates a basic CI/CD workflow for a Flask application. GitHub provides source control and automated workflow execution, Pytest validates application behavior, Ruff checks code quality, Docker packages the application, and Jenkins independently builds and tests the project.



The workflow helps identify code issues early and makes application builds more repeatable.



