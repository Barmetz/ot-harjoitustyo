from invoke import task

@task
def start(ctx):
	ctx.run("python3 src/GUI.py")

@task
def test(ctx):
	ctx.run("pytest")

@task
def coverage(ctx):
	ctx.run("coverage run --branch -m pytest")

@task
def coverage_report(ctx):
	ctx.run("coverage html")
