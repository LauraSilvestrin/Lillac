window.addEventListener('load', () => {    
    document.body.style.setProperty('--body-color', '#FFF'); 
})

button = document.getElementById('theme-button');
buttonMobile = document.getElementById('theme-button');

button.addEventListener("click", changeTheme)
buttonMobile.addEventListener("click", changeTheme)

function changeTheme() {
    if (document.body.style.getPropertyValue('--body-color') === '#FFF') {
        document.body.style.setProperty('--body-color', '#1F1F1F');
        document.body.style.setProperty('--title-color', 'hsl(228, 66%, 47%)');
        document.body.style.setProperty('--text-color', 'hsl(228, 12%, 75%)');
        
        button.classList.remove("bx-moon");
        button.classList.add("bx-sun");

        buttonMobile.classList.remove("bx-moon");
        buttonMobile.classList.add("bx-sun");
    }

    else {
        document.body.style.setProperty('--body-color', '#FFF');
        document.body.style.setProperty('--title-color', 'hsl(228, 57%, 28%)');
        document.body.style.setProperty('--text-color', 'hsl(228, 15%, 50%)');
        
        button.classList.remove("bx-sun");
        button.classList.add("bx-moon");

        buttonMobile.classList.remove("bx-sun");
        buttonMobile.classList.add("bx-moon");
    }
}

// MOBILE SELECT
selectBtns = document.getElementsByClassName("header-item");
pages = document.getElementsByClassName("results");

for (let i = 0; i < selectBtns.length; i++) {
    selectBtns[i].addEventListener("click", () => {
        selectBtns[i].classList.add("active");
        deactivate(i);

        pages[i].classList.add("active-page");
        deactivatePage(i);
    })
}

function deactivate(index) {
    for (let i = 0; i < selectBtns.length; i++) {
        if (i != index) {
            selectBtns[i].classList.remove("active");
        }
    }
}

function deactivatePage(index) {
    for (let i = 0; i < selectBtns.length; i++) {
        if (i != index) {
            pages[i].classList.remove("active-page");
        }
    }
}