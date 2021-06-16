FROM python:3

# set a directory for the app
WORKDIR /usr/src/app

# copy all the files to the container
COPY . .

# install dependencies
RUN pip install --no-cache-dir -r requirements.txt

#Install git
RUN apt-get install git
# download the git repo
RUN git clone https://github.com/pe-st/garmin-connect-export

# tell the port number the container should expose
EXPOSE 5000

# run the command
CMD ["python", "./app.py"]
