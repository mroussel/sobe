FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN rm -f application.cfg \
 && cp application.cfg.prod application.cfg

CMD [ "flask", "run", "--host=0.0.0.0", "--port=80" ]