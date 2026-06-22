// les variables pour les checkbox
let int_1=document.querySelector(".it1");
let int_2=document.querySelector(".it2");
let int_3=document.querySelector(".it3");
let int_4=document.querySelector(".it4");
let devoir=document.querySelector(".dv");
let compo=document.querySelector(".cp");

// les variables pour les champs de saisie
let int1=document.querySelectorAll(".int1");
let int2=document.querySelectorAll(".int2");
let int3=document.querySelectorAll(".int3");
let int4=document.querySelectorAll(".int4");
let dev=document.querySelectorAll(".devoir");
let comp=document.querySelectorAll(".compo");

// la variable pour le bouton de soumission
let submitBtn=document.querySelector(".submit-btn");

// les fonctions pour afficher ou cacher les champs de saisie
function showInt1(){
    if(int_1.checked){
        for(let i=0;i<int1.length;i++){
            int1[i].innerHTML="<input type='number' value='' class='int1' >";
        }
    }else{
        for(let i=0;i<int1.length;i++){
            int1[i].innerHTML="";
        }
    }
}
function showInt2(){
    if(int_2.checked){
        for(let i=0;i<int2.length;i++){
            int2[i].innerHTML="<input type='number' value='' class='int2' >";
        }
    }else{
        for(let i=0;i<int2.length;i++){
            int2[i].innerHTML="";
        }
    }
}
function showInt3(){
    if(int_3.checked){
        for(let i=0;i<int3.length;i++){
            int3[i].innerHTML="<input type='number' value='' class='int3' >";
        }
    }else{
        for(let i=0;i<int3.length;i++){
            int3[i].innerHTML="";
        }
    }
}
function showInt4(){
    if(int_4.checked){
        for(let i=0;i<int4.length;i++){
            int4[i].innerHTML="<input type='number' value='' class='int4' >";
        }
    }else{
        for(let i=0;i<int4.length;i++){
            int4[i].innerHTML="";
        }
    }
}
function showDevoir(){
    if(devoir.checked){
        for(let i=0;i<dev.length;i++){
            dev[i].innerHTML="<input type='number' value='' class='devoir' >";
        }
    }else{
        for(let i=0;i<dev.length;i++){
            dev[i].innerHTML="";
        }
    }
}
function showCompo(){
    if(compo.checked){
        for(let i=0;i<comp.length;i++){
            comp[i].innerHTML="<input type='number' value='' class='compo' >";
        }
    }else{
        for(let i=0;i<comp.length;i++){
            comp[i].innerHTML="";
        }
    }
}

// les événements pour les checkbox
int_1.addEventListener("change",showInt1);
int_2.addEventListener("change",showInt2);
int_3.addEventListener("change",showInt3);
int_4.addEventListener("change",showInt4);
devoir.addEventListener("change",showDevoir);
compo.addEventListener("change",showCompo);

// la fonction pour reccuperer les champs selectionnes
function getSelectedFields() {
    const prenom= [];
    const selectedFields = [];
    if (int_1.checked){
        for(let i=0;i<int1.length;i++){
            selectedFields.push(int1[i]);
            prenom.push("{{e.prenom}}");
        }
        
    }
    if (int_2.checked){
        for(let i=0;i<int2.length;i++){
            selectedFields.push(int2[i]);
            prenom.push("{{e.prenom}}");
        }
    }
    if (int_3.checked){
        for(let i=0;i<int3.length;i++){
            selectedFields.push(int3[i]);
            prenom.push("{{e.prenom}}");
        }
    }
    if (int_4.checked){
        for(let i=0;i<int4.length;i++){
            selectedFields.push(int4[i]);
            prenom.push("{{e.prenom}}");
        }
    }
    if (devoir.checked){
        for(let i=0;i<dev.length;i++){
            selectedFields.push(dev[i]);
            prenom.push("{{e.prenom}}");
        }
    }
    if (compo.checked){
        for(let i=0;i<comp.length;i++){
            selectedFields.push(comp[i]);
            prenom.push("{{e.prenom}}");
        }
    }
    return { fields: selectedFields, names: prenom };
}

// les événements pour récupérer les champs apres la saisie
for(let i=0;i<int1.length;i++){
    int1[i].addEventListener("blur", getSelectedFields);
}
for(let i=0;i<int2.length;i++){
    int2[i].addEventListener("blur", getSelectedFields);
}
for(let i=0;i<int3.length;i++){
    int3[i].addEventListener("blur", getSelectedFields);
}
for(let i=0;i<int4.length;i++){
    int4[i].addEventListener("blur", getSelectedFields);
}
for(let i=0;i<dev.length;i++){
    dev[i].addEventListener("blur", getSelectedFields);
}
for(let i=0;i<comp.length;i++){
    comp[i].addEventListener("blur", getSelectedFields);
}

// l'evenement pour la soumission du formulaire
submitBtn.addEventListener("click", function(event) {
    event.preventDefault();
    const { fields, names } = getSelectedFields();
    const values = fields.map(field => field.querySelector("input").value);
    console.log("Selected fields:", fields);
    console.log("Values:", values);
    console.log("Names:", names);
    let data={values,names};
    fetch('/enregistrer_note/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': '{{ csrf_token }}'
        },
        body: JSON.stringify(data)
    }).then(response => response.json()).then(data => { console.log(data) });
});
