FROM node

ENV NODEDIR=/frontend
ENV PATH /frontend/node_modules/.bin:$PATH
RUN mkdir $NODEDIR
WORKDIR $NODEDIR

COPY frontend/package.json $NODEDIR
COPY frontend/package-lock.json $NODEDIR
RUN npm install --silent
RUN npm install react-scripts -g --silent

COPY . $NODEDIR

CMD [ "npm","run","build" ]