from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    # A simple page verifying the system is live
    return """
    <html>
        <body>
            <h1>Target System Online</h1>
            <p>Status: Live</p>
            <!-- TODO: Remove debug info before production -->
        </body>
    </html>
    """, 200

if __name__ == '__main__':
    # host='0.0.0.0' is REQUIRED for Docker/Sandboxes
    app.run(host='0.0.0.0', port=5000)
