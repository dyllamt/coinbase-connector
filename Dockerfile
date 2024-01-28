FROM python:3.11

COPY requirements.txt ./
RUN pip install -r ./requirements.txt

COPY src/coinbase/main.py ./
CMD [ "python", "-u", "./main.py" ]