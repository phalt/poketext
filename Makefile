VIRTUALENV = $(shell which virtualenv)

ifeq ($(strip $(VIRTUALENV)),)
  VIRTUALENV = /usr/local/python/bin/virtualenv
endif

venv:
	$(VIRTUALENV) venv

install: venv
	. venv/bin/activate; pip install -r requirements.txt

serve: venv
	. venv/bin/activate; python manage.py runserver

test: venv
	. venv/bin/activate; python manage.py test

clean:
	rm -rf *.pyc

uninstall: clean
	rm -rf venv
