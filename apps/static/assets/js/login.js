const fieldUser = document.getElementById("username_login");
const fieldPassword = document.getElementById("pwd_login");
const showPassword = document.querySelector(".show"),
    pwd = document.querySelector("#pwd_login");

showPassword.addEventListener("click", () => {
    if (pwd.type === "password") {
        pwd.type = "text";
        showPassword.classList.replace("fa-eye-slash", "fa-eye");
    } else {
        pwd.type = "password";
        showPassword.classList.replace("fa-eye", "fa-eye-slash");
    }
});

if (window.history.replaceState) {
    window.history.replaceState(null, null, window.location.href);
}