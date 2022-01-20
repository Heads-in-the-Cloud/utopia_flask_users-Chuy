FROM python
COPY . /app
WORKDIR /app
RUN pip3 install -r requirements.txt
EXPOSE 5002
ENTRYPOINT [ "python3" ]
CMD [ "run.py" ]