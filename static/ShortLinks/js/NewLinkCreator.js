function togglePrivateLink() {
    let className = 'btn-secondary';
    if (privateCheckbox.checked === true) {
        privateCheckboxButton.classList.add(className);
        lockedIcon.hidden = false;
        unlockedIcon.hidden = true;
    }
    else {
        privateCheckboxButton.classList.remove(className);
        unlockedIcon.hidden = false;
        lockedIcon.hidden = true;
    }
}
let lockedIcon;
let unlockedIcon;
let privateCheckbox;
let privateCheckboxButton;
document.addEventListener('DOMContentLoaded', function () {
    privateCheckbox = document.getElementById('privateCheckbox');
    privateCheckboxButton = document.getElementById('privateCheckboxButton');
    if (privateCheckbox === null || privateCheckboxButton === null) {
        return;
    }
    lockedIcon = privateCheckboxButton.getElementsByClassName('fas fa-lock')[0];
    unlockedIcon = privateCheckboxButton.getElementsByClassName('fas fa-lock-open')[0];

    privateCheckboxButton.addEventListener('click', function(e) {
        privateCheckbox.click();
        togglePrivateLink();
    });

    document.getElementById('privateCheckbox').addEventListener('change', function(e) {
        console.log(e.target.checked);
      });
});

