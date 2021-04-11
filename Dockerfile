# Use the LTS release.
FROM python:3.7-slim-stretch

# RUN useradd --user-group --create-home --shell /bin/false app 
  
ENV HOME=/home/app

WORKDIR $HOME/tact_chart

ADD requirements.txt $HOME/tact_chart/

ADD app.py $HOME/tact_chart/

RUN pip install -r requirements.txt

# USER app