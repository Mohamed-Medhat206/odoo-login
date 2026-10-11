/* Password reveal toggle on the branded login page.
 * Bound via delegation on `document`: this file ships in a lazily loaded
 * frontend bundle, so DOMContentLoaded has usually already fired by the time
 * it runs, and the form itself is (re)rendered by the user-switch component. */
document.addEventListener("click", function (ev) {
    var toggle = ev.target.closest(".lb_password_toggle");
    if (!toggle) {
        return;
    }
    var input = toggle.parentElement.querySelector("input");
    if (!input) {
        return;
    }
    var hidden = input.type === "password";
    input.type = hidden ? "text" : "password";
    toggle.setAttribute("aria-label", hidden ? "Hide password" : "Show password");
    var icon = toggle.querySelector("i");
    if (icon) {
        icon.classList.toggle("fa-eye", !hidden);
        icon.classList.toggle("fa-eye-slash", hidden);
    }
});
