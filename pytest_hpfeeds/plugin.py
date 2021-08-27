from pytest_docker_tools import container, fetch

hpfeeds_broker_image = fetch(repository="hpfeeds/hpfeeds-broker:latest")

hpfeeds_broker = container(
    image="{hpfeeds_broker_image.id}",
    environment={
        "HPFEEDS_TEST_SECRET": "test",
        "HPFEEDS_TEST_SUBCHANS": "test",
        "HPFEEDS_TEST_PUBCHANS": "test",
    },
    command=[
        "/app/bin/hpfeeds-broker",
        "--bind=0.0.0.0:20000",
        # Read user creds from environment variables
        "--auth=env",
    ],
    ports={
        "20000/tcp": None,
    },
)
