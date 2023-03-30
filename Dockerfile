FROM python:3.10
WORKDIR /tool
COPY ./scanner.py /tool/scanner.py
COPY ./requirements.txt /tool/requirements.txt
RUN apt-get update
RUN apt-get install -y python
RUN pip install -r requirements.txt
EXPOSE 8081
ENTRYPOINT ["python3"]
CMD ["./scanner.py"]
