import os

def create_github_workflow_files():
    """
    Create essential GitHub Actions workflow YAML files with basic introductory content.

    This function ensures the '.github/workflows' directory exists and then populates it
    with a set of predefined workflow files containing minimal identifying comments.
    """
    base_path = ".github/workflows"
    os.makedirs(base_path, exist_ok=True)

    workflows = {
        "python-app.yml": "# Python/Flask CI workflow\n",
        "bandit-scan.yml": "# Bandit scan workflow (security)\n",
        "codeql.yml": "# CodeQL analysis workflow\n",
        "pages-deploy.yml": "# Deploy static HTML to GitHub Pages\n",
        "docker-build.yml": "# Build Docker image and publish to GitHub Packages\n",
        "manual-tasks.yml": "# Manually triggered workflow\n",
        "greetings.yml": "# Welcome message for new contributors\n",
        "labeler.yml": "# Automatically label pull requests\n",
        "stale.yml": "# Auto-close stale issues and PRs\n"
    }

    for filename, content in workflows.items():
        file_path = os.path.join(base_path, filename)
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(content)

    print("All essential GitHub Actions files have been created successfully.")


if __name__ == "__main__":
    create_github_workflow_files()
