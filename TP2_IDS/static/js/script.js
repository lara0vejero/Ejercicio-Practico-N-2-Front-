const leer_mas = document.getElementById("texto_oculto")
const boton_ver_mas =document.getElementById("leer-mas")

boton_ver_mas.onclick = function(){
    if (leer_mas.style.display == "none"){
        leer_mas.style.display = "block"
        boton_ver_mas.textContent = "leer menos"
    } else {
        leer_mas.style.display = "none"
        boton_ver_mas.textContent = "leer mas" 
    }
};


