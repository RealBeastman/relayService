# relayService

> This was developed to act as a bridge between containerized applications.

---

## Overview

`relayService` allows a user to pass messages between applications being ran in Docker containers. This was initially designed to capture and send messages to a Discord bot for real-time feedback from a containerized application.

## Example:

**Containerized Application:**

*can be run several times in an application, the messages are dumped into a queue*
```
import relayService

relayService.send_message_to_server("Broadcasted Message")
```

**Discord Bot:**

*Start `relayService` server*
```
import relayService

async def on_ready():
  `bot.loop.create_task(relayService.start_server())`
  `bot.loop.create_task(process_message_queue())` # Custom bot loop to handle queue
```

*Process message queue*
```
import relayService

async def process_message_queue():
  while True:
    message = await relayService.message_queue.get()'
    channel = bot.get_channel(CHANNEL_ID)
    channel.send(message)
    asyncio.sleep(0.2) # Throttle to 5 messages/sec
```

---

## Installation:

`pip install git+https://github.com/RealBeastman/relayService.git`

---

## Author

Joshua Eastman — [contact@joshuaeastman.dev](mailto:contact@joshuaeastman.dev)
