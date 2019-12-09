function readFile() {
    var client = new XMLHttpRequest();
    client.open('GET', "https://raw.githubusercontent.com/emscb/Sleeptionary/master/Web/data.txt");
    client.onreadystatechange = function() {
        if (client.responseText != '') {
            var txt = client.responseText.split('\n');
            document.getElementById("1ago").innerHTML = txt[6];
            document.getElementById("2ago").innerHTML = txt[5];
            document.getElementById("3ago").innerHTML = txt[4];
            document.getElementById("4ago").innerHTML = txt[3];
            document.getElementById("5ago").innerHTML = txt[2];
            document.getElementById("6ago").innerHTML = txt[1];
            document.getElementById("7ago").innerHTML = txt[0];
            document.getElementById("temperature").innerHTML = txt[7];
            document.getElementById("humidity").innerHTML = txt[8];
        }
    };
    client.send();
}
function setDate() {
    var today = new Date();
    var d = String(today.getDate()).padStart(2, '0');
    var m = String(today.getMonth() + 1).padStart(2, '0');
    var y = today.getFullYear();

    today = y + '/' + m + '/' + d;
}