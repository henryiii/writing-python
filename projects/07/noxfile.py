import nox

nox.options.default_venv_backend = "uv|virtualenv"

@nox.session
def hello(session):
    session.run("python", "-c", "print('hello world')")
