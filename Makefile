# Determine the command used to start Python.  This will be the
# shell's Python unless the variable ${PYTHON} is set.
ifndef PYTHON
	PYTHON=python
endif

# Command for running management tool.
MANAGE=${PYTHON} manage.py

# List all installed applications
APPS=$(notdir $(shell find apps -mindepth 1 -maxdepth 1 -type d -print))

# Clean up.
clean : tidy

# Prepares existing .po for localizations and compiles them
# Public domain
# To make first time localization (for example for de_DE) run
# $ python manage.py makemessages -e ".html,.txt" -l de_DE
int :
	${MANAGE} makemessages -e ".html,.txt,.py" --all
	${MANAGE} compilemessages

# Handle schema migration for all applications.
schemamigration :
	@for i in ${APPS}; do ${MANAGE} schemamigration $$i --auto; done

# Display the settings.
settings :
	@echo "PYTHON:" ${PYTHON}
	@echo "APPS:" ${APPS}

# Synchronize the database.
syncdb :
	@${PYTHON} manage.py syncdb --noinput --migrate

# Runs pep8 and pyflakes
check_code :
	@-pep8 --exclude migrations .
	@pyflakes apps/ |grep -v migrations

# Tidy up by removing .pyc files.
tidy :
	@rm -rf htmlcov `find . -name '*.pyc'` `find . -name '*~'`
