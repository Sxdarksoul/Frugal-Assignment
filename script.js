const countryStateCity = {
    USA: { states: ["New York", "California"], cities: { "New York": ["NYC", "Buffalo"], "California": ["LA", "SF"] } },
    India: { states: ["Maharashtra", "Karnataka"], cities: { "Maharashtra": ["Mumbai", "Pune"], "Karnataka": ["Bangalore", "Mysore"] } }
};

function loadStates() {
    const country = document.getElementById("country").value;
    const stateSel = document.getElementById("state");
    stateSel.innerHTML = "<option value=''>Select State</option>";
    if (country && countryStateCity[country]) {
        countryStateCity[country].states.forEach(s => {
            stateSel.innerHTML += `<option value='${s}'>${s}</option>`;
        });
    }
}

function loadCities() {
    const country = document.getElementById("country").value;
    const state = document.getElementById("state").value;
    const citySel = document.getElementById("city");
    citySel.innerHTML = "<option value=''>Select City</option>";
    if (state && countryStateCity[country].cities[state]) {
        countryStateCity[country].cities[state].forEach(c => {
            citySel.innerHTML += `<option value='${c}'>${c}</option>`;
        });
    }
}

function checkStrength() {
    const val = document.getElementById("password").value;
    const meter = document.getElementById("strengthMessage");
    if (val.length < 5) { meter.innerText = "Weak"; meter.className = "weak"; }
    else if (val.length < 8) { meter.innerText = "Medium"; meter.className = "medium"; }
    else { meter.innerText = "Strong"; meter.className = "strong"; }
    validateForm();
}

function validateForm() {
    const email = document.getElementById("email").value;
    const pass = document.getElementById("password").value;
    const confirm = document.getElementById("confirmPassword").value;
    const btn = document.getElementById("submitBtn");
    
    // Disposable email check [cite: 99]
    if (email.includes("@tempmail.com")) {
        document.getElementById("emailError").innerText = "No disposable emails!";
        btn.disabled = true;
        return;
    } else {
        document.getElementById("emailError").innerText = "";
    }

    // Password Match
    if (pass !== confirm) {
        document.getElementById("matchError").innerText = "Passwords do not match";
    } else {
        document.getElementById("matchError").innerText = "";
    }
    
    // Enable submit only if form is roughly valid
    const isValid = document.getElementById("firstName").value && document.getElementById("lastName").value && email && pass && (pass === confirm);
    btn.disabled = !isValid;
}

document.getElementById("regForm").addEventListener("change", validateForm);
document.getElementById("regForm").addEventListener("keyup", validateForm);

document.getElementById("regForm").addEventListener("submit", function(e) {
    e.preventDefault();
    document.getElementById("successMessage").style.display = "block";
    alert("Registration Successful!");
});