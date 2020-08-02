FROM python:buster
CMD apt install wget
CMD pip install -U selenium && pip install -U pytest
CMD wget https://github.com/kirill-shilov/ducktest/test_1.py 
CMD python test_1.py
