let copy_btn = document.querySelectorAll('.copy_btn');
let position = 0;
const slaidesToShow = 3;
const slaidesToScroll = 3;
const container = document.querySelector('.flex-wrapper');
const track = document.querySelector('.slaider-wrapper');
const slaides = document.querySelectorAll('.slaider');
const btnPrev = document.querySelector('.btnPrev');
const btnNext = document.querySelector('.btnNext');
const slaidesCount = slaides.length;
const slaidesWidth = container.clientWidth / slaidesToShow;
const movePosition = slaidesToScroll * slaidesWidth;


slaides.forEach((slaide) => {
    slaide.style.minwidth = `${slaidesWidth}px`
})

btnNext.addEventListener('click',() =>{
    const slaidesLeft = slaidesCount - (Math.abs(position) + slaidesToShow * slaidesWidth) / slaidesWidth;
    position -= slaidesLeft >= slaidesToScroll ? movePosition : slaidesLeft * slaidesWidth
    setPosition();
    checkBtn();
})

btnPrev.addEventListener('click',() =>{
    const slaidesLeft = Math.abs(position) / slaidesWidth;
    position += slaidesLeft >= slaidesToScroll ? movePosition : slaidesLeft * slaidesWidth
    setPosition();
    checkBtn();
})

for (let i of copy_btn){
    i.addEventListener('click', function(){
        let input = i.previousElementSibling
        input.select()
        document.execCommand('copy')
    })
}

const setPosition = () =>{
    track.style.transform = `translateX(${position}px)`
}

const checkBtn = () =>{
    btnPrev.disabled = position === 0;
    btnPrev.disabled ? btnPrev.classList.add('btnDisable') : btnPrev.classList.remove('btnDisable');

    btnNext.disabled = position === -(container.clientWidth * (slaidesCount/slaidesToShow) - container.clientWidth);
    btnNext.disabled ? btnNext.classList.add('btnDisable') : btnNext.classList.remove('btnDisable');    
}

checkBtn();

function replacePosition (){
    if (position === 0 || position === -container.clientWidth){
        const slaidesLeft = slaidesCount - (Math.abs(position) + slaidesToShow * slaidesWidth) / slaidesWidth;
        position -= slaidesLeft >= slaidesToScroll ? movePosition : slaidesLeft * slaidesWidth;
        setPosition();
        checkBtn();
    }else{
        position = 0;
        setPosition();
        checkBtn();
    }
}

setInterval(replacePosition, 6000);

