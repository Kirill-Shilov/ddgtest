FROM python:buster
WORKDIR /tmp/test
RUN apt install wget
RUN pip install --no-cache-dir selenium
RUN pip install --no-cache-dir pytest
RUN wget --no-check-certificate --content-disposition https://raw.githubusercontent.com/Kirill-Shilov/ddgtest/blob/master/test_1.py
CMD python -m pytest test_1.py
