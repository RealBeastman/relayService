import socket
import asyncio

# Docker config
DOCKER_HOST = "host.docker.internal"
PORT = 5000

# Discord/Server config
SERVER_HOST = "0.0.0.0"

# Message queue
message_queue = asyncio.Queue()

# Send message to listener server
def send_message_to_server(message):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.connect((DOCKER_HOST, PORT))
            client_socket.sendall(message.encode())
            print(f"Message sent to bot: {message}")
    except Exception as e:
        print(f"Error sending message: {str(e)}")

# Start listener server on defined host and port
async def start_server():
    server = await asyncio.start_server(handle_messenger, SERVER_HOST, PORT)
    async with server:
        print(f"Server listening on {SERVER_HOST}:{PORT}")
        await server.serve_forever()

# Read messages as they are sent
async def handle_messenger(reader, writer):
    while True:
        try:
            # Read message from sender
            data = await reader.read()
            if not data:
                break
            message = data.decode()
            print(f"Received message: {message}")

            # Place message into queue
            await message_queue.put(message)
        except Exception as e:
            print(f"Error in message handler: {e}")
            break

    writer.close()
    await writer.wait_closed()