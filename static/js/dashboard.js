// les variables du menu
const tbord = document.querySelector(".tboard");
let tclasse = document.querySelector(".tclasse");
const televes = document.querySelector(".televe");
const tsaisi = document.querySelector(".tsaisi");
const tplaniing = document.querySelector(".tplaning");
const parametre = document.querySelector(".parametre");

//les varable du tableau de board
let bord = document.querySelector(".board");
const classe = document.querySelector(".classes");
const planning = document.querySelector(".emploie");
const eleve = document.querySelector(".elev");

tbord.onclick = function(){
    bord.style.display = "block";
    classe.style.display = "none";
    planning.style.display = "none";
    eleve.style.display = "none";
    eleve.classList.remove('animate__animated', 'animate__zoomIn');
    bord.classList.add('animate__animated', 'animate__zoomIn');
    classe.classList.remove('animate__animated', 'animate__zoomIn');
    planning.classList.remove('animate__animated', 'animate__zoomIn');
}
tclasse.onclick = function(){
    bord.style.display = "none";
    classe.style.display = "block";
    planning.style.display = "none";
    eleve.style.display = "none";
    eleve.classList.remove('animate__animated', 'animate__zoomIn');
    classe.classList.add('animate__animated', 'animate__zoomIn');
    bord.classList.remove('animate__animated', 'animate__zoomIn');


}
tplaniing.onclick = function(){
    bord.style.display = "none";
    classe.style.display = "none";
    planning.style.display = "block";
    eleve.style.display = "none";
    eleve.classList.remove('animate__animated', 'animate__zoomIn');
    bord.classList.remove('animate__animated', 'animate__zoomIn');
    classe.classList.remove('animate__animated', 'animate__zoomIn');
    planning.classList.add('animate__animated', 'animate__zoomIn');
}
televes.onclick = function(){
    bord.style.display = "none";
    classe.style.display = "none";
    planning.style.display = "none";
    eleve.style.display = "block";
    eleve.classList.add('animate__animated', 'animate__zoomIn');
    bord.classList.remove('animate__animated', 'animate__zoomIn');
    classe.classList.remove('animate__animated', 'animate__zoomIn');
    planning.classList.remove('animate__animated', 'animate__zoomIn');

    // la partie pour ajouter une classe
    const ajout = document.querySelector('.ajout');
    ajout.innerHTML += `
    <button class="btn btn-primary"
            data-bs-toggle="modal"
            data-bs-target="#ajoutClasse">
        Ajouter une classe
    </button>
`;
    
}
// la partie qui affiche le popup de eleve

