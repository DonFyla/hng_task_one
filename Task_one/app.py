from flask import Flask, request, jsonify
import datetime
import pytz

app = Flask(__name__)

@app.route("/", methods =["GET"])
def information():
    slack_name = request.args.get("slack_name")
    track = request.args.get("track")

    current_time = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)
    current_time_str = current_time.strftime('%Y-%m-%d, %H:%M')
    current_day = current_time.strftime('%A')
    github_file_url = "https://github.com/DonFyla/hng_task_one/blob/f24145a0a379555817ff0bcb63568bea05926a64/Task_one/app.py"
    github_repo_url = "https://github.com/DonFyla/hng_task_one.git"


    response = {
    'slack_name': slack_name,
    'current_day': current_day,
    'utc_time': current_time_str,
    'track': track,
    'github_file_url': github_file_url,
    'github_repo_url': github_repo_url,
    'status_code': 200
}

    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
