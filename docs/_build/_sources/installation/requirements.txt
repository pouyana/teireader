========================
TEIReader Requirements
========================
TEIReader can work with bare python library installed on Linux/Mac/Windows system. Some features are not availbe. If you want to extend the classifier with your own corpus, you should have the optimal requirements ready.

Minimum Requirements
----------------------
- Python 2.7/3.x

Optimal Requirements
----------------------
- Ubuntu Linux 12.4/14.4
    - `Ubuntu 12.04/14.04 <http://www.ubuntu.com/download/desktop/install-desktop-long-term-support>`_
- Python 2.7/3.x
    - `Python 2.7 <http://docs.python.org/2.7/>`_ , `Python 3.x <http://docs.python.org/3/>`_
- NLTK
    - `For Python 2.7 <http://www.nltk.org/install.html>`_ , `For Python 3.x <http://www.nltk.org/nltk3-alpha/>`_
- Numpy
    - `Numpy <http://www.numpy.org/>`_
- Scikit
    - `Scikit Download <http://scikit-learn.org/stable/>`_
- Java 6/7 (For Stanford Parser)
    - `Download Java <https://www.java.com/de/download/>`_
- Stanford Pos_Tagger
    - `Download PosTagger <http://nlp.stanford.edu/software/tagger.shtml>`_
- NLTK Trainer
    - `Nltk Trainer Documention <http://nltk-trainer.readthedocs.org/en/latest/>`_

Hardware requirements
----------------------
If you run Stanford pos_tagger server parallel to TEIReader on the same computer, you will need at least 2Gb of memory. If you only run TEIReader the memory footprint of the application it self is less tahn 200Mb at most.
