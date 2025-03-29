```javascript
<script>
    const chatSocket = new WebSocket(
        "ws://" + window.location.host + "/ws/battery/",
    );
    chatSocket.onmessage = function (e) {
        const data = JSON.parse(e.data);
        console.log(data);
        setInterval(() => {
            chatSocket.send(
                JSON.stringify({
                    message: "get_battery",
                }),
            );
            document.getElementById("status-display").innerHTML =
                "battery: " + data["battery"] + " %";
        }, 10000);
    };

    chatSocket.onclose = function (e) {
        console.error("Chat socket closed unexpectedly");
    };
</script>
```
#### TODO:
- update urls in index.html
- dockerize
