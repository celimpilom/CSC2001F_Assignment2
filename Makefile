# assignment 2 make file
# Celimpilo manqele
# 19 April 2021

JAVAC=/usr/bin/javac
.SUFFIXES: .java .class
SRCDIR=src
BINDIR=bin
FILESDIR=files
PYTHON=/usr/bin/python3

$(BINDIR)/%.class:$(SRCDIR)/%.java
	$(JAVAC) -d $(BINDIR)/ -cp $(BINDIR) $<

CLASSES=BinaryTreeNode.class BTQueueNode.class \
	 BTQueue.class BinaryTree.class \
	 AVLTree.class ReadFile.class AccessAVLApp.class

CLASS_FILES=$(CLASSES:%.class=$(BINDIR)/%.class)

default: $(CLASS_FILES)

run:
	java -cp bin AccessAVLApp $(stdN) $(file)

docs:
	javadoc -d docs/ src/*.java

experiment:
	make clean
	$(PYTHON) script/test.py

clean:
	rm -f files/data/*
	rm -f files/inputs/*
	rm -f files/cases/*
graphs:
	$(PYTHON) script/graphs.py
