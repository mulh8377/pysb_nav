
WINDOW = --win
WEB = --web
CLI = --cli

STRT = start

LANG = python3
TARGET = pysb.py

clean:
	bash bin/clean.sh

build:
	bash bin/build.sh

window:
	$(LANG) $(TARGET) $(WINDOW) $(STRT)
cli:
	$(LANG) $(TARGET) $(CLI) $(STRT)
web:
	$(LANG) $(TARGET) $(WEB) $(STRT)
