

const infinityContainer = document.querySelector(".infinityContainer")
const URL = "https://source.unsplash.com/random/"


function getRandNum(){
    return Math.floor(Math.random() * 100)
}

function loadImages(numImages = 4){
    let i = 0;
    while(i < numImages){
        const img = document.createElement("img")
        img.src = `${URL}${getRandNum()}`
        infinityContainer.appendChild(img)
        i++

    }
}

loadImages()


window.addEventListener("scroll", () =>{
    if(window.scrollY + window.innerHeight > document.documentElement.scrollHeight){
        loadImages()
    }

})