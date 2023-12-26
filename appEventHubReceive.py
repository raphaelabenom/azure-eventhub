# Description: Receives events from an Azure Event Hub and saves them to a blob storage container.
# Baseado em: https://docs.microsoft.com/pt-br/azure/event-hubs/event-hubs-python-get-started-send
# Libraries:
import asyncio

from dotenv import load_dotenv
import logging
import json
import os

from azure.eventhub.extensions.checkpointstoreblobaio import BlobCheckpointStore
from azure.eventhub.aio import EventHubConsumerClient
from azure.storage.blob import BlobServiceClient
from azure.eventhub import EventData


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

load_dotenv()

# Event Hub connection string
EVENT_HUB_CONNECTION_STR = os.getenv("EVENT_HUB_CONNECTION_STR")
EVENT_HUB_NAME = os.getenv("EVENT_HUB_NAME")

# Blob storage connection string
BLOB_STORAGE_CONNECTION_STRING = os.getenv("BLOB_STORAGE_CONNECTION_STRING")
BLOB_CONTAINER_NAME = os.getenv("BLOB_CONTAINER_NAME")


async def on_event(partition_context, event):
    try:
        print(
            'Received event: "{}" from partition ID: "{}"'.format(
                event.body_as_str(encoding="UTF-8"), partition_context.partition_id
            )
        )

        # Convert the event data to a JSON object
        event_data = json.loads(event.body_as_str(encoding="UTF-8"))

        try:
            # Convert the JSON data to a formatted JSON string
            json_str = json.dumps(event_data, indent=2)

            blob_service_client = BlobServiceClient.from_connection_string(
                BLOB_STORAGE_CONNECTION_STRING
            )
            container_client = blob_service_client.get_container_client(
                BLOB_CONTAINER_NAME
            )

            blob_client = container_client.get_blob_client(str(event.sequence_number))
            blob_client.upload_blob(json_str, overwrite=True)

        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")

        except Exception as error:
            logger.error(f"Error processing event: {str(error)}")

    except Exception as error:
        logger.error(f"Error processing event: {str(error)}")


async def receive_events():
    # checkpoint_store = BlobCheckpointStore.from_connection_string(
    #     BLOB_STORAGE_CONNECTION_STRING, BLOB_CONTAINER_NAME
    # )

    client = EventHubConsumerClient.from_connection_string(
        EVENT_HUB_CONNECTION_STR,
        consumer_group="$Default",
        eventhub_name=EVENT_HUB_NAME,
        # checkpoint_store=checkpoint_store,
    )

    async with client:
        await client.receive(
            on_event=on_event, starting_position="-1"
        )  # "-1" is the beginning of the partition.


def main():
    try:
        loop = asyncio.get_event_loop()
        loop.run_until_complete(receive_events())
    except Exception as error:
        logger.error(f"Error in main: {str(error)}")


if __name__ == "__main__":
    main()
