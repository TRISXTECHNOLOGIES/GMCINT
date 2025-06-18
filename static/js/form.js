
document.addEventListener('DOMContentLoaded', function () {
    const nextBtns = document.querySelectorAll('.nextBtn');
    const prevBtns = document.querySelectorAll('.prevBtn');
    const formSteps = document.querySelectorAll('.form-step');
    const progressSteps = document.querySelectorAll('.step');
    const progressLine = document.querySelector('.line');

    let formStepsNum = 0;

    nextBtns.forEach((btn, index) => {
        btn.addEventListener('click', () => {

            if (index === formStepsNum) {
                formStepsNum++;
                console.log("index" + index)
                updateFormSteps();
                updateProgressBar();
            }
        });
    });

    prevBtns.forEach((btn, index) => {
        btn.addEventListener('click', () => {
  
            if (index === formStepsNum - 1) {
                formStepsNum--;
                updateFormSteps();
                updateProgressBar();
            }
        });
    });

    function updateFormSteps() {
        formSteps.forEach((formStep, idx) => {
            formStep.classList.toggle('active', idx === formStepsNum);
        });
    }

    function updateProgressBar() {

       // const validIndices = [0,2,6,7];
        validityState=[1,2,3,4]
        progressSteps.forEach((progressStep, idx) => {
            if (validIndices.includes(idx)) {
                progressStep.classList.toggle('completed', idx <= formStepsNum);
            } else {
                progressStep.classList.remove('completed');
            }
        });
    }
});
