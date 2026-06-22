let eleveSection = document.querySelector('.eleve');
let personnelSection = document.querySelector('.personnel');
let personnels = document.querySelector('.personnels');
let eleves = document.querySelector('.eleves');

eleves.onclick = function(){
    eleveSection.style.display = 'block';
    personnelSection.style.display = 'none';
    eleveSection.classList.add('animate__animated', 'animate__backInUp');
    personnelSection.classList.remove('animate__animated', 'animate__backInUp');
}
personnels.onclick = function(){
    personnelSection.style.display = 'block';
    eleveSection.style.display = 'none';
    personnelSection.classList.add('animate__animated', 'animate__backInUp');
    eleveSection.classList.remove('animate__animated', 'animate__backInUp');
}
window.onload = function(){
    eleveSection.style.display = 'block';
    personnelSection.style.display = 'none';
    eleveSection.classList.add('animate__animated', 'animate__backInUp');
    personnelSection.classList.remove('animate__animated', 'animate__backInUp');
}