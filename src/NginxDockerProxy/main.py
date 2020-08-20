import os
from flask import Flask
from healthcheck import HealthCheck, EnvironmentDump

app = Flask(__name__)
health = HealthCheck()
envdump = EnvironmentDump()

# health.add_check()

@app.route("/status/health")
def status_health():
    return health.run()

if __name__ == "__main__":
    app.run(debug=False, port=80)

