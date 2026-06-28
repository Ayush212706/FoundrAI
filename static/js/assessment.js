let currentStep = 1;

function updateProgress() {
    const progress = document.getElementById("progressBar");
    progress.style.width = (currentStep * 25) + "%";
}

function showStep(step) {

    document.querySelectorAll(".step").forEach(s => {
        s.style.display = "none";
    });

    document.getElementById("step" + step).style.display = "block";

    updateProgress();
}

function nextStep() {

    if(currentStep < 4){
        currentStep++;
        showStep(currentStep);
    }

}

function previousStep(){

    if(currentStep > 1){
        currentStep--;
        showStep(currentStep);
    }

}

window.onload = function(){
    showStep(1);
}