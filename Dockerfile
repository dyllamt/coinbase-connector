FROM python:3.10

COPY requirements.txt ./
RUN pip install -r ./requirements.txt

COPY src/coinbase/main.py ./
CMD [ "python", "./main.py" ]