FROM python:3.7.5

WORKDIR /app

COPY requirements.txt requirements.txt
# RUN apt install apturl
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]