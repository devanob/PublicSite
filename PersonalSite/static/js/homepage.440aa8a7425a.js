// const elementVisibleInPercent = (element) => {
//     return new Promise((resolve, reject) => {
//         const observer = new Is (entries => {
//             entries.forEach(entry => {
//                 resolve(Math.floor(entry.intersectionRatio * 100));
//                 clearTimeout(timeout);
//                 observer.disconnect();
//             });
//         });

//         observer.observe(element);
//         // Probably not needed, but in case something goes wrong.
//         const timeout = setTimeout(() => {
//             reject();
//         }, 500);
//     });
// };

// document.addEventListener("DOMContentLoaded", (event)=> {
//     let section = document.getElementById("testPage");
//     document.addEventListener("scroll",(event)=>{
//         const percentageVisible = elementVisibleInPercent(section).then(num=>{
//             console.log(num);
//         });
//         console.log(percentageVisible);
//     });
// });