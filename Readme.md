# Airflow Docker in Docker

This is a sample docker-compose file extended from [Airflow's how to section](https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html), adding Docker in Docker and the DockerOperator as well as the Sendgrid Provider.


## Running

If you want to create your own environment file.

```bash
echo -e "AIRFLOW_UID=$(id -u)" > .env
echo -e "AIRFLOW_IMAGE_NAME=yourname/airflow:2.4.0" >> .env
```

Source the environmental variables

```bash
. .env
```

or

```bash
source .env
```

Then build the image

```bash
docker-conmpose build
```

Do the init

```bash
docker-compose up airflow-init
```

Finally, run it

```bash
docker-compose up
```

You should be able to login with
`airflow` and `airflow` and run the docker_test DAG


To clean up

```bash
docker-compose down --volumes --remove-orphans
```