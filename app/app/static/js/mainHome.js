/* CHANGE BACKGROUND COLOR */
function scrollHeader() {
    const header = document.getElementById('header')

    if (this.scrollY >= 50) {
        header.style.backgroundColor = ''; 
        header.classList.add('scroll-header') 
    }
    
    else {
        header.style.backgroundColor = 'transparent';
        header.classList.remove('scroll-header')
    }
                       
}

window.addEventListener('scroll', scrollHeader)

/* SWIPER */
var swiperItens = new Swiper(".itens__container", {
    spaceBetween: 32,
    grabCursor: true,
    slidesPerView: 'auto',
    centeredSlides: true,
    navigation: {
        nextEl: ".swiper-button-next",
        prevEl: ".swiper-button-prev",
    }
})

/* VALUE ACCORDION */
const accordionItens = document.querySelectorAll('.value__accordion-item')

accordionItens.forEach((item) => {
    const accordionHeader = item.querySelector('.value__accordion-header')

    accordionHeader.addEventListener('click', () => {
        const openItem = document.querySelector('.accordion-open')
        
        toggleItem(item)

        if (openItem && openItem !== item) {
            toggleItem(openItem)
        }
    })
})

const toggleItem = (item) => {
    const accordionContent = item.querySelector('.value__accordion-content')

    if (item.classList.contains('accordion-open')) {
        accordionContent.removeAttribute('style')
        item.classList.remove('accordion-open')
    }

    else {
        accordionContent.style.height = accordionContent.scrollHeight + 'px'
        item.classList.add('accordion-open')
    }
}

/* SECTION ACTIVE LINK */
const sections = document.querySelectorAll('section[id]')
    
const scrollActive = () =>{
  	const scrollY = window.pageYOffset

	sections.forEach(current =>{
		const sectionHeight = current.offsetHeight,
			  sectionTop = current.offsetTop - 58,
			  sectionId = current.getAttribute('id'),
			  sectionsClass = document.querySelector('.nav__menu a[href*=' + sectionId + ']')

		if(scrollY > sectionTop && scrollY <= sectionTop + sectionHeight){
			sectionsClass.classList.add('active-link')
		}else{
			sectionsClass.classList.remove('active-link')
		}                                                    
	})
}
window.addEventListener('scroll', scrollActive)

/* SCROLL UP */
const scrollUp = () =>{
	const scrollUp = document.getElementById('scroll-up')
	this.scrollY >= 350 ? scrollUp.classList.add('show-scroll')
						: scrollUp.classList.remove('show-scroll')
}
window.addEventListener('scroll', scrollUp)

/* DARK / LIGHT THEME */
const themeButton = document.getElementById('theme-button')

const darkTheme = 'dark-theme'
const iconTheme = 'bx-sun'

const selectedTheme = localStorage.getItem('selected-theme')
const selectedIcon = localStorage.getItem('selected-icon')

const getCurrentTheme = () => document.body.classList.contains(darkTheme) ? 'dark' : 'light'
const getCurrentIcon = () => themeButton.classList.contains(iconTheme) ? 'bx bx-moon' : 'bx bx-sun'

if (selectedTheme) {
  document.body.classList[selectedTheme === 'dark' ? 'add' : 'remove'](darkTheme)
  themeButton.classList[selectedIcon === 'bx bx-moon' ? 'add' : 'remove'](iconTheme)
}

themeButton.addEventListener('click', () => {
    document.body.classList.toggle(darkTheme)
    themeButton.classList.toggle(iconTheme)

    localStorage.setItem('selected-theme', getCurrentTheme())
    localStorage.setItem('selected-icon', getCurrentIcon())
})