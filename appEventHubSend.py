import asyncio
from azure.eventhub import EventData
from azure.eventhub.aio import EventHubProducerClient
from dotenv import load_dotenv
import os
import logging
import json

logging.basicConfig(level=logging.INFO)

load_dotenv()

EVENT_HUB_CONNECTION_STR = os.getenv("EVENT_HUB_CONNECTION_STR")
EVENT_HUB_NAME = os.getenv("EVENT_HUB_NAME")


async def run():
    # Create a producer client to send messages to the event hub.
    # Specify a connection string to your event hubs namespace and
    # the event hub name.
    producer = EventHubProducerClient.from_connection_string(
        conn_str=EVENT_HUB_CONNECTION_STR, eventhub_name=EVENT_HUB_NAME
    )
    async with producer:
        # Create a batch.
        event_data_batch = await producer.create_batch()

        # Add events to the batch.
        messages = [
            {
            "timestamp": "2023-12-26T10:00:00",
            "temperatura": 2.5,
            "unidade": "Celsius"
            },
            {
            "timestamp": "2023-12-26T11:00:00",
            "temperatura": 2.8,
            "unidade": "Celsius"
            },
            {
            "timestamp": "2023-12-26T12:00:00",
            "temperatura": 3.2,
            "unidade": "Celsius"
            },
            {
            "timestamp": "2023-12-26T13:00:00",
            "temperatura": 3.0,
            "unidade": "Celsius"
            },
            {
            "timestamp": "2023-12-26T17:00:00",
            "temperatura": 2.6,
            "unidade": "Celsius"
            }
        ]

        logging.info("Sending messages")
        for message in messages:
            event_data_batch.add(EventData(message))

        # Send the batch of events to the event hub.
        await producer.send_batch(event_data_batch)


asyncio.run(run())
logging.info("Send sucessfully")
