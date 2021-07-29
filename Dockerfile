FROM python:latest
COPY . /all
WORKDIR /all
RUN pip install -r "requirements.txt"
CMD python arpita_app.py
