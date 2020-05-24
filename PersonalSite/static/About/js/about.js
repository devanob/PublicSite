
import "../sass/about.scss";
console.log("Hello Worldi");
document.addEventListener('DOMContentLoaded', () =>{
    let box  = document.getElementById("test-slider-one");
    let innerBox  = box.querySelector("ul");
    let boxArrowRight = box.querySelector(".right.slider-control");
    let boxArrowLeft = box.querySelector(".left.slider-control");
    let childLi = box.querySelector("ul>li");
    console.log(childLi);
    console.log(boxArrowRight);
    console.log(innerBox);
    boxArrowRight.addEventListener("click", ()=>{
        let lastScrollPosition =  Math.max(innerBox.scrollLeft);
        console.log(lastScrollPosition);
        innerBox.scrollLeft += (childLi.clientWidth + 2)*2;
        if (lastScrollPosition === innerBox.scrollLeft){
            console.log("EndReach");
        }
        
    console.log("Lemon")
    console.log(innerBox.scrollLeft);
    console.log(innerBox.clientWidth);
    })
    boxArrowLeft.addEventListener("click", ()=>{
        let lastScrollPosition =  Math.max(innerBox.scrollLeft);
        console.log(lastScrollPosition);
        innerBox.scrollLeft -= (childLi.clientWidth + 2)*2;
        if (lastScrollPosition === innerBox.scrollLeft){
            console.log("EndReach");
        }
        
    
    console.log(innerBox.scrollLeft);
    console.log(innerBox.clientWidth);
    })
})