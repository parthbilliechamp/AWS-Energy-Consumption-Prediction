FROM python:3.9

WORKDIR /usr/app

COPY . .

RUN pip3 install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python3", "-m", "flask", "run","--host=0.0.0.0"]
