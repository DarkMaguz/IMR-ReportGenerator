FROM python:3.9

RUN /usr/local/bin/python -m pip install --upgrade pip
ADD app/requirements.txt /tmp
WORKDIR /tmp
RUN pip install -r requirements.txt

WORKDIR /usr/app

EXPOSE 5001

ENTRYPOINT ["python", "main.py"]
