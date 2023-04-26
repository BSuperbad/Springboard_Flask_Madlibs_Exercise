form = document.getElementById('story_form');

form.addEventListener('submit', function (e) {
    let hasError = false;

    for (i = 0; i < form.elements.length; i++) {
        if (form.elements[i].value === '') {
            hasError = true;
            break;
        }

    }

    if (hasError) {
        e.preventDefault();
        alert('PLEASE FILL OUT ALL FIELDS');
    } else {
        form.submit()
    }
})