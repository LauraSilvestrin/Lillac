var Form1 = document.getElementById("Form1");
var Form2 = document.getElementById("Form2");
var Form3 = document.getElementById("Form3");

var Step1 = document.getElementById("Step1");
var Step2 = document.getElementById("Step2");
var Step3 = document.getElementById("Step3");


var progress = document.getElementById("progress");

Step1.onclick = () => {
    Form1.style.left = "40px";
    Form2.style.left = "440px";
    Form3.style.left = "440px";

    progress.style.width = "33%";
    Step2.style.color = "#333";
    Step3.style.color = "#333";
}

Step2.onclick = () => {
    Form2.style.left = "40px";
    Form1.style.left = "440px";
    Form3.style.left = "440px";

    progress.style.width = "66%";
    Step2.style.color = "var(--first-color-lighten)";
    Step3.style.color = "#333";
}

Step3.onclick = () => {
    Form3.style.left = "40px";
    Form1.style.left = "440px";
    Form2.style.left = "440px";

    progress.style.width = "100%";
    Step2.style.color = "var(--first-color-lighten)";
    Step3.style.color = "var(--first-color-lighten)";
}

/*
Back1.onclick = function() {
    Form1.style.left = "40px";
    Form2.style.left = "450px";
    progress.style.width = "120px";
    Step2.style.color = "#333";
}

Next2.onclick = function() {
    Form2.style.left = "-450px";
    Form3.style.left = "45px";
    progress.style.width = "360px";
    Step3.style.color = "var(--first-color-lighten)";
}

Back2.onclick = function() {
    Form2.style.left = "40px";
    Form3.style.left = "450px";
    progress.style.width = "240px";
    Step3.style.color = "#333";
}

*/