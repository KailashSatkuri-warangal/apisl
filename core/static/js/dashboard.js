function toggleMode() {
    document.body.classList.toggle("light");
}

function showLoader() {
    document.getElementById("loader").style.display = "block";
}

function hideLoader() {
    document.getElementById("loader").style.display = "none";
}

function exportPDF() {
    window.print();
}
