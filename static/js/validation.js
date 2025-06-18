document.addEventListener('DOMContentLoaded', function () {
    const formSteps = document.querySelectorAll('.form-step');
    const nextButtons = document.querySelectorAll('.nextBtn');
    const prevButtons = document.querySelectorAll('.prevBtn');
    let currentStep = 0;

    // Initialize the form by showing the first step and hiding others
    showStep(currentStep);
    updateProgressBar(currentStep); // Initialize progress bar

    // Add event listeners to all Next buttons
    nextButtons.forEach((button, index) => {
        button.addEventListener('click', function () {
            // Special handling for Step 5's multiple Next buttons
            if (currentStep === 4) { // Step 5 (0-based index)
                if (button.classList.contains('nextBtn1')) {

                    currentStep++;
                    showStep(currentStep);
                    updateProgressBar(currentStep);
                } else {
                    currentStep++;
                    showStep(currentStep);
                    updateProgressBar(currentStep);
                }
            } else {
                if (validateStep(currentStep)) {
                    currentStep++;
                    showStep(currentStep);
                    updateProgressBar(currentStep);
                }
            }

            // Handle saving signature data before moving from Step 9
            if (currentStep === 8) { // Step 9 (0-based index)
                if (signaturePad) {
                    displayError(formSteps[8], ['Please provide your signature.']);
                } else {
                    const dataURL = signaturePad.toDataURL();
                    document.getElementById('signature_data').value = dataURL;
                    hideError(formSteps[8]);
                }
            }
        });
    });

    // Add event listeners to all Back buttons
    prevButtons.forEach((button, index) => {
        button.addEventListener('click', function () {
            currentStep--;
            showStep(currentStep);
            updateProgressBar(currentStep);
        });
    });

    // Add input event listeners for real-time validation
    formSteps.forEach((step, index) => {
        const inputs = step.querySelectorAll('input, textarea, select');
        inputs.forEach(input => {
            input.addEventListener('input', () => {
                toggleNextButton(step, index);
            });

            // For radio buttons and checkboxes
            if (input.type === 'radio' || input.type === 'checkbox') {
                input.addEventListener('change', () => {
                    toggleNextButton(step, index);
                });
            }
        });
    });

    // Function to show a specific step
    function showStep(stepIndex) {
        formSteps.forEach((step, index) => {
            step.classList.remove('active');
            if (index === stepIndex) {
                step.classList.add('active');
            }
        });
        toggleNextButton(formSteps[stepIndex], stepIndex);
    }

    // Function to toggle the Next button based on validation
    function toggleNextButton(step, index) {
        const nextBtn = step.querySelector('.nextBtn');
        if (validateStep(index, false)) {
            nextBtn.disabled = false;
            nextBtn.classList.remove('opacity-50');
            nextBtn.classList.add('opacity-90');
            hideError(step);
        } else {
            nextBtn.disabled = true;
            nextBtn.classList.remove('opacity-90');
            nextBtn.classList.add('opacity-50');
        }
    }

    // Function to validate a specific step
    function validateStep(stepIndex, showError = true) {
        const step = formSteps[stepIndex];
        let valid = true;
        let messages = [];

        // Select all required inputs in the current step
        const requiredInputs = step.querySelectorAll('[required]');
        requiredInputs.forEach(input => {
            if (input.type === 'radio') {
                const radioGroup = step.querySelectorAll(`input[name="${input.name}"]`);
                const isChecked = Array.from(radioGroup).some(radio => radio.checked);
                if (!isChecked) {
                    valid = false;
                    messages.push(`Please select an option for "${getLabel(input)}".`);
                }
            } else if (input.type === 'checkbox') {
                if (!input.checked) {
                    valid = false;
                    messages.push(`Please check the "${getLabel(input)}" box.`);
                }
            } else if (input.type === 'file') {
                if (input.files.length === 0) {
                    valid = false;
                    messages.push(`Please upload a file for "${getLabel(input)}".`);
                }
            } else {
                if (input.value.trim() === '') {
                    valid = false;
                    messages.push(`Please fill out the "${getLabel(input)}" field.`);
                } else {
                    // Additional validations can be added here (e.g., email format)
                    if (input.type === 'email' && !validateEmail(input.value.trim())) {
                        valid = false;
                        messages.push(`Please enter a valid email address.`);
                    }
                }
            }
        });

        // Handle optional fields (e.g., Passenger 2 details in Step 7)
        if (stepIndex === 6) { // Step 7 (0-based index)
            const passenger2FirstName = document.getElementById('passenger2FirstName');
            const passenger2LastName = document.getElementById('passenger2LastName');
            const passenger2Email = document.getElementById('passenger2Email');

            // if (passenger2FirstName.value.trim() !== '' ||
            //     passenger2LastName.value.trim() !== '' ||
            //     passenger2Email.value.trim() !== '') {

                
            //     if (passenger2FirstName.value.trim() === '') {
            //         valid = false;
            //         messages.push('Please fill out the "Passenger 2 First Name" field or leave all Passenger 2 fields empty.');
            //     }

            //     if (passenger2LastName.value.trim() === '') {
            //         valid = false;
            //         messages.push('Please fill out the "Passenger 2 Last Name" field or leave all Passenger 2 fields empty.');
            //     }

            //     if (passenger2Email.value.trim() !== '' && !validateEmail(passenger2Email.value.trim())) {
            //         valid = false;
            //         messages.push('Please enter a valid email address for "Passenger 2 Email".');
            //     }
            // }
        }

        // Special validation for signature pad in Step 9
        // if (stepIndex === 8) { // Step 9 (0-based index)
        //     const signatureData = document.getElementById('signature_data').value;
        //     if (signatureData.trim() === '') {
        //         valid = false;
        //         messages.push('Please provide your signature.');
        //     }
        // }

        // // Special validation for file uploads in Step 10
        // if (stepIndex === 9) { // Step 10 (0-based index)
        //     const uploadDocuments = document.getElementById('uploadDocuments');
        //     if (uploadDocuments.files.length === 0) {
        //         valid = false;
        //         messages.push('Please upload at least one document.');
        //     } else {
        //         const allowedTypes = ['image/png', 'image/jpg', 'image/jpeg', 'application/pdf'];
        //         const maxSize = 15 * 1024 * 1024; // 15MB
        //         for (let file of uploadDocuments.files) {
        //             if (!allowedTypes.includes(file.type)) {
        //                 valid = false;
        //                 messages.push(`File type not allowed: ${file.name}`);
        //             }
        //             if (file.size > maxSize) {
        //                 valid = false;
        //                 messages.push(`File size exceeds 15MB: ${file.name}`);
        //             }
        //         }
        //     }
        // }

        // Display error messages if validation fails and showError is true
        if (!valid && showError) {
            displayError(step, messages);
        } else {
            hideError(step);
        }

        return valid;
    }

    // Function to get the label text for an input
    function getLabel(input) {
        // Try to find a label associated with the input
        let label = input.closest('.form-group') ?.querySelector('label');
        if (!label) {
            // For radio buttons and checkboxes, find the nearest label
            label = input.closest('label');
        }
        return label ? label.innerText.replace('*', '').trim() : 'This field';
    }

    // Function to display error messages
    function displayError(step, messages) {
        let errorContainer = step.querySelector('.error-message');
        if (!errorContainer) {
            errorContainer = document.createElement('div');
            errorContainer.classList.add('error-message', 'text-red-500', 'mt-2');
            // Insert the error container above the navigation buttons
            const navButtons = step.querySelector('.flex.flex-row.justify-end, .flex.flex-row.justify-between');
            if (navButtons) {
                step.insertBefore(errorContainer, navButtons);
            } else {
                step.appendChild(errorContainer);
            }
        }
        errorContainer.innerHTML = messages.map(msg => `<p>${msg}</p>`).join('');
        errorContainer.style.display = 'block';
    }

    // Function to hide error messages
    function hideError(step) {
        const errorContainer = step.querySelector('.error-message');
        if (errorContainer) {
            errorContainer.style.display = 'none';
            errorContainer.innerHTML = '';
        }
    }

    // Function to validate email format
    function validateEmail(email) {
        const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return re.test(String(email).toLowerCase());
    }

    // Initialize SignaturePad for Step 9
    const canvas = document.getElementById('signaturePad');
    const signaturePad = new SignaturePad(canvas);

    // // Function to clear the signature
    // window.clearSignature = function () {
    //     signaturePad.clear();
    //     document.getElementById('signature_data').value = '';
    //     toggleNextButton(formSteps[8], 8);
    // };

    // // Resize the canvas to fit its container
    // function resizeCanvas() {
    //     const ratio = Math.max(window.devicePixelRatio || 1, 1);
    //     canvas.width = canvas.offsetWidth * ratio;
    //     canvas.height = canvas.offsetHeight * ratio;
    //     canvas.getContext("2d").scale(ratio, ratio);
    //     signaturePad.clear(); // Otherwise isEmpty() might return incorrect value
    // }

    // window.addEventListener("resize", resizeCanvas);
    // resizeCanvas();
// Handle file upload click
const uploadDocuments = document.getElementById('uploadDocuments');
const documentsContainer = document.getElementById('documents');

// Create a list to display uploaded files
const uploadedFilesList = document.createElement('ul');
uploadedFilesList.style.paddingLeft = '20px';
uploadedFilesList.style.marginTop = '10px';

// Create a paragraph to display file count message
const filesCountMessage = document.createElement('p');
filesCountMessage.style.fontWeight = 'bold';
filesCountMessage.style.marginTop = '10px';

// Append the count message and file list to the documents container
documentsContainer.appendChild(filesCountMessage);
documentsContainer.appendChild(uploadedFilesList);

// Handle file upload click event
documentsContainer.addEventListener('click', () => {
    uploadDocuments.click(); // Trigger file input click
});

// Handle file upload change event
uploadDocuments.addEventListener('change', () => {
    const files = Array.from(uploadDocuments.files); // Convert FileList to array
    const allowedTypes = ['image/png', 'image/jpg', 'image/jpeg', 'application/pdf'];
    const maxSize = 15 * 1024 * 1024; // 15MB per file
    let valid = true;
    let messages = [];

    // Clear the previous file list and file count message
    uploadedFilesList.innerHTML = '';
    filesCountMessage.textContent = '';

    if (files.length === 0) {
        valid = false;
        messages.push('Please upload at least one document.');
    } else {
        // Display the number of uploaded files
        filesCountMessage.textContent = `You have uploaded ${files.length} file(s).`;

        files.forEach(file => {
            // Validate file type and size
            if (!allowedTypes.includes(file.type)) {
                valid = false;
                messages.push(`File type not allowed: ${file.name}`);
            }
            if (file.size > maxSize) {
                valid = false;
                messages.push(`File size exceeds 15MB: ${file.name}`);
            }

            // Show the uploaded file in the list
            const listItem = document.createElement('li');
            listItem.textContent = file.name; // Show file name

            // If it's an image, create a preview
            if (file.type.startsWith('image/')) {
                const imgPreview = document.createElement('img');
                imgPreview.src = URL.createObjectURL(file); // Create URL for image preview
                imgPreview.style.width = '100px'; // Set image size for preview
                imgPreview.style.marginTop = '5px';
                listItem.appendChild(imgPreview);
            }

            if (file.type === 'application/pdf') {
                const pdfIcon = document.createElement('span');
                pdfIcon.textContent = '📄'; // Use an icon to represent the PDF file
                listItem.prepend(pdfIcon); // Show the PDF icon
            }

            // Append file details or image preview to the list
            uploadedFilesList.appendChild(listItem);
        });
    }

    const step = formSteps[9]; // Assuming step 10 in your formSteps array
    if (!valid) {
        displayError(step, messages); // Custom function to show error messages
    } else {
        hideError(step); // Custom function to hide error messages
    }

    toggleNextButton(step, 9); // Enable or disable the Next button based on validity
});


   

    // Optional: Handle Add Passenger button in Step 7
    // const addPassengerBtn = document.querySelector('.addtBtn');
    // const passengerDetailsContainer = document.getElementById('passengerDetails');

    // addPassengerBtn.addEventListener('click', () => {
  
    //     const passengerCount = passengerDetailsContainer.querySelectorAll('.passenger').length + 2; 
    //     const newPassenger = document.createElement('div');
    //     newPassenger.classList.add('passenger', 'mt-4', 'border', 'p-4', 'rounded');

    //     newPassenger.innerHTML = `
    //             <h3 class="text-lg font-semibold">Passenger ${passengerCount} <span class="text-gray-400 italic text-sm">(Optional)</span></h3>
    //             <label for="passenger${passengerCount}FirstName">First Name</label>
    //             <input type="text" id="passenger${passengerCount}FirstName" name="first_name_passenger_${passengerCount}" class="!w-full lg:!w-1/2" placeholder="Enter First name as per your ID">
                
    //             <label for="passenger${passengerCount}LastName" class="mt-2">Last Name</label>
    //             <input type="text" id="passenger${passengerCount}LastName" name="last_name_passenger_${passengerCount}" class="!w-full lg:!w-1/2" placeholder="Enter Last name as per your ID">
                
    //             <label for="passenger${passengerCount}Email" class="mt-2">Email</label>
    //             <input type="email" id="passenger${passengerCount}Email" name="email_passenger_${passengerCount}" class="!w-full lg:!w-1/2 py-[15px] px-[20px]" placeholder="abc@example.com">
    //         `;

    //     passengerDetailsContainer.appendChild(newPassenger);

    //     const newInputs = newPassenger.querySelectorAll('input');
    //     newInputs.forEach(input => {
    //         input.addEventListener('input', () => {
    //             toggleNextButton(formSteps[6], 6); 
    //         });

    //         if (input.type === 'radio' || input.type === 'checkbox') {
    //             input.addEventListener('change', () => {
    //                 toggleNextButton(formSteps[6], 6); 
    //             });
    //         }
    //     });
    // });

    // Handle form submission in Step 10
    const submitButton = formSteps[9].querySelector('.nextBtn');
    submitButton.addEventListener('click', function () {
        if (validateStep(9)) {
            // Collect all form data
            const formData = new FormData();

            formSteps.forEach(step => {
                const inputs = step.querySelectorAll('input, textarea, select');
                inputs.forEach(input => {
                    if (input.type === 'file') {
                        for (let file of input.files) {
                            formData.append(input.name, file);
                        }
                    } else if (input.type === 'radio' || input.type === 'checkbox') {
                        if (input.checked) {
                            formData.append(input.name, input.value);
                        }
                    } else {
                        formData.append(input.name, input.value);
                    }
                });
            });

            // Example: Send the form data via Fetch API
            fetch('YOUR_FORM_SUBMISSION_ENDPOINT', {
                    method: 'POST',
                    body: formData
                })
                .then(response => response.json())
                .then(data => {
                    alert('Form submitted successfully!');
                })
                .catch(error => {
                    // alert('An error occurred while submitting the form.');
                    console.error(error);
                });
        } else {
            displayError(formSteps[9], ['Please fix the errors before submitting.']);
        }
    });

    function updateProgressBar(currentStep) {
        const progressSteps = document.querySelectorAll('.progress-indicator .step');
        let completedSteps = 1;

        if (currentStep >= 0 && currentStep <= 3) {
            completedSteps = 1;
        } else if (currentStep === 4) {
            completedSteps = 2;
        } else if (currentStep === 5) {
            completedSteps = 3;
        } else if (currentStep >= 6 && currentStep <= 9) {
            completedSteps = 4;
        }

        progressSteps.forEach((step, index) => {
            if (index < completedSteps) {
                step.classList.add('completed');
            } else {
                step.classList.remove('completed');
            }
        });
    }
});