FROM python:3
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/

EXPOSE 8000

RUN python ./covid19casebycase/manage.py migrate
CMD ["python", "./covid19casebycase/manage.py", "runserver", "0.0.0.0:8000"]