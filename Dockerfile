FROM python:3.9

#RUN /usr/local/bin/python -m pip install --upgrade pip

ADD app /opt/app
WORKDIR /opt/app

RUN pip install -r requirements.txt

EXPOSE 5001

ENTRYPOINT ["python", "main.py"]
