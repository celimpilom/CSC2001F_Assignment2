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

docs:
	javadoc -d doc/ src/*.java

run:
	java -cp bin AccessAVLApp $(stdN)

experiment:
	$(PYTHON) script/test.py
data:
	$(PYTHON) script/data.py
graphs:
	$(PYTHON) script/graphs.py