from flask import Flask, request, send_from_directory
import os

app = Flask(__name__)

# Define the path to the folder where you want to save the file
file_path = r"C:\Users\edwin\Downloads\about me\ips.txt"

@app.route('/')
def serve_index():
    return send_from_directory('.', 'f.html')

@app.route('/log-ip', methods=['POST'])
def log_ip():
    try:
        # Get the IP address from the request
        ip = request.remote_addr

        # Check if file exists and create if it doesn't
        if not os.path.exists(file_path):
            with open(file_path, 'w') as f:
                f.write("IP Address Log:\n")

        # Append the IP address to the file
        with open(file_path, 'a') as f:
            f.write(f"{ip}\n")

        return "IP logged successfully", 200
    except Exception as e:
        return f"Error: {str(e)}", 500

if __name__ == "__main__":
    app.run(debug=True)
