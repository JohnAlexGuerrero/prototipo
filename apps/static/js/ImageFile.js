
const resizeImageToFitContainer = (img, container) => {
    const originalWidth = img.naturalWidth;
    const originalHeight = img.naturalHeight;

    const containerWidth = container.clientWidth;
    const containerHeight = container.clientHeight;

    
    const widthRatio = containerWidth / originalWidth;
    const heightRatio = containerHeight / originalHeight;
    
    const scale = Math.min(widthRatio, heightRatio);

    const newWidth = originalWidth * scale;
    const newHeight = originalHeight * scale;

    img.style.width = `${newWidth}px`;
    img.style.height = `${newHeight}px`;
    container.style.height = `${newHeight + 100}px`;
}

const selectedFile = (imgEl, helpText, env) =>{
    helpText.textContent = env.target.files[0].name
    
    if(env.target.files[0]){
        deleteBtn.disabled = false;
        
        const reader = new FileReader()
        reader.onload = (env)=>{
            imgEl.src = env.target.result
        }
        reader.readAsDataURL(env.target.files[0])
    }
}

const deleteFile = (imgEl, helpText)=>{
    imgEl.src = ''
    helpText.textContent = "No hay un archivo"

}