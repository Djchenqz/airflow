FROM apache/airflow:2.3.3

RUN pip3 install openpyxl

COPY ./dags  /opt/airflow/dags/

USER airflow

