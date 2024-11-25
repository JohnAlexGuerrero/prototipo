const inputUpperCase = (e)=>{
    let x = e.target

    if(x.value.length === 1){
        x.value = x.value.charAt(0).toUpperCase();
    }
    else{
        x.value = x.value;
    }
}

//transforma un texto a mayusculas
const textChanceUpper = e => {
    let el = e.target;

    el.value = el.value.toUpperCase()
    el.textContent = el.value
}

//conteo de caracteres en inputs
const textCount = (el, maxLength, e) => {
    let strSize = e.target.value.length
    el.textContent = maxLength - strSize
    console.log(el.target)
}