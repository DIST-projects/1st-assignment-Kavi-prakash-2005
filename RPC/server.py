# ==========================================
# RPC SERVER PROGRAM
# Hosted on: Azure Virtual Machine
# Language: Python
# Communication: HTTP (RPC-style)
# ==========================================

# BaseHTTPRequestHandler -> handles HTTP requests
# HTTPServer -> creates and runs the HTTP server
from http.server import BaseHTTPRequestHandler, HTTPServer

# json module is used to parse and send JSON data
import json


# This class handles incoming RPC requests from client
class RPCHandler(BaseHTTPRequestHandler):

    # This method is automatically called when
    # the client sends an HTTP POST request
    def do_POST(self):

        # Read size of incoming request data
        content_length = int(self.headers['Content-Length'])

        # Read the request body (raw bytes)
        body = self.rfile.read(content_length)

        # Convert JSON data into Python dictionary
        data = json.loads(body)

        # -------- RPC METHOD 1 --------
        # Counts number of words in the text
        if self.path == "/word_count":
            result = len(data["text"].split())

        # -------- RPC METHOD 2 --------
        # Reverses the given text
        elif self.path == "/reverse_text":
            result = data["text"][::-1]

        # -------- RPC METHOD 3 --------
        # Checks if the text is a palindrome
        elif self.path == "/is_palindrome":
            text = data["text"].replace(" ", "").lower()
            result = text == text[::-1]

        # If client calls an invalid RPC method
        else:
            self.send_error(404, "Method not found")
            return

        # Send HTTP success response
        self.send_response(200)

        # Specify response type as JSON
        self.send_header("Content-Type", "application/json")
        self.end_headers()

        # Create response dictionary
        response = {"result": result}

        # Send JSON response back to client
        self.wfile.write(json.dumps(response).encode())


# Function to start the RPC server
def run():

    # Create HTTP server
    # "0.0.0.0" allows external clients to connect
    # 8000 is the port number
    server = HTTPServer(("0.0.0.0", 8000), RPCHandler)

    print("RPC Server running on Azure VM at port 8000")

    # Keep server running continuously
    server.serve_forever()


# Start the server
run()
