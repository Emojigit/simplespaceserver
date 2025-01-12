import flask
import subprocess

page = """
<!DOCTYPE HTML>
<html style="height: 100%" lang="zh">
<body style="height: 100%" ontouchstart="send();">
<p style="font-size: 6em;">
按白色處翻頁<br />
按鍵盤上的 PageUp <br >回到上一頁
</p>
</body>
<script>
    function send() {
        var xhr = new XMLHttpRequest();
        xhr.open("POST", "/submit", true);
        xhr.send("HELLO");
    }
</script> 
</html>
"""

if __name__ == "__main__":
    app = flask.Flask(__name__)

    @app.route('/', methods=['GET'])
    def index():
        return page

    @app.route("/submit", methods=['POST'])
    def submit():
        subprocess.run(["xdotool", "key", "space"])
        return "Ok"

    app.run(host="0.0.0.0")
