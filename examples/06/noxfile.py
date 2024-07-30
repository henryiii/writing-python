import nox


@nox.session
def format(session):
    session.install("ruff")
    session.run("ruff", "format", "noxfile.py")
