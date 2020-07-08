/**
 *
 */
function locationSelector() {
    var content = document.getElementById("selections")
    var buttons = content.getElementsByClassName("loc")

    for (var i = 0; i < buttons.length; i++) {
        deselect_option = false
        buttons[i].onclick = function () {
            // Toggle the location type selection.
            this.classList.toggle("active");
        }
    }
}
