function runCode() {
    var code = document.getElementById("code").value;
    var outputDiv = document.getElementById("output");
    outputDiv.innerHTML = "Output:<br>";

    var xhr = new XMLHttpRequest();
    xhr.open("POST", "http://localhost:8000/run_python_script", true);
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            outputDiv.innerHTML += xhr.responseText;
        }
    };
    xhr.send(JSON.stringify({ code: code }));
}

function clearOutput() {
    document.getElementById("output").innerHTML = "";
}
