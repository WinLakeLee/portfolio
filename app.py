from flask import Flask, render_template, abort
from projects_data import (
    PROJECTS,
    get_all_projects_summary,
    get_project_by_id,
    get_profile_data,
)

app = Flask(__name__)


@app.context_processor
def inject_metadata():
    return {
        "site_name": "Developer Portfolio",
        "developer_name": "WinLakeLee",  # To be customized by user
        "github_url": "https://github.com/WinLakeLee",
    }


@app.route("/")
def home():
    projects = get_all_projects_summary()
    profile = get_profile_data()
    return render_template("index.html", projects=projects, profile=profile)


@app.route("/projects")
def projects_list():
    projects = get_all_projects_summary()
    return render_template("projects.html", projects=projects)


@app.route("/project/<project_id>")
def project_detail(project_id):
    project = get_project_by_id(project_id)
    if not project:
        abort(404)
    return render_template("project_detail.html", project=project)


if __name__ == "__main__":
    app.run(debug=True)
