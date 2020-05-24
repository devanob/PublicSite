require("../sass/about.scss");require("../css/about.css");document.addEventListener('DOMContentLoaded',()=>{});(function($){"use strict";$('a.js-scroll-trigger[href*="#"]:not([href="#"])').click(function(){if(location.pathname.replace(/^\//,'')==this.pathname.replace(/^\//,'')&&location.hostname==this.hostname){var target=$(this.hash);target=target.length?target:$('[name='+this.hash.slice(1)+']');if(target.length){$('html, body').animate({scrollTop:(target.offset().top-30)},1000,"easeInOutExpo");return false;}}});$('.js-scroll-trigger').click(function(){$('.navbar-collapse').collapse('hide');});$('body').scrollspy({target:'#mainNav',offset:0});})(jQuery);;let convertToLocaltime=(domObjectTime)=>{}
let timeStamp=()=>{let timeObjects=document.getElementsByClassName("timeLocal");for(let i=0;i<timeObjects.length;i++){let timeConvert=new Date(timeObjects[i].innerText.trim());timeObjects[i].innerText=timeConvert.toLocaleDateString("en-US",options);}}
var options={weekday:'long',year:'numeric',month:'long',day:'numeric',hour:'numeric',minute:'numeric'};document.addEventListener("DOMContentLoaded",timeStamp);;let fetchHTTP=(urlLink)=>{return new Promise((resolve,reject)=>{var xhr=new XMLHttpRequest();var url=urlLink;xhr.open("GET",url,true);xhr.setRequestHeader("Content-Type","application/json");xhr.onreadystatechange=function()
{if(xhr.readyState===4&&xhr.status===200)
{var data=JSON.parse(xhr.responseText);resolve(data);}
else if(xhr.readyState===4&&xhr.status==404){reject(JSON.parse(xhr.responseText));}};xhr.send();});}
let setAttributes=(el,attrs)=>{for(var key in attrs){el.setAttribute(key,attrs[key]);}}
function truncate(input,maxlength){if(input.length>maxlength)
return input.substring(0,maxlength)+'...';else
return input;};let projectInsert=(projectArray)=>{projectArray=projectArray.results.filter((element)=>{if(element.image!=null){return true;}})
if(projectArray.length==0){return;}
let carousel_items=projectArray.map((project,index)=>{let inner_item=document.createElement('div');if(index==0){inner_item.className="carousel-item active";}
else{inner_item.className="carousel-item";}
var img=new Image();var imageContainer=document.createElement('div');imageContainer.className="imageContainer";imageContainer.appendChild(img)
inner_item.appendChild(imageContainer);img.src=project.image.url;img.alt=project.image.alt;img.className="img-fluid";let link=document.createElement('a');inner_item.appendChild(link);link.href=project.project_link;let carousel_caption=document.createElement('div');carousel_caption.className="carousel-caption";link.appendChild(carousel_caption);let title=document.createElement('h1');title.innerText=project.project_name;let description=document.createElement('p');description.innerText=truncate(project.description,100);carousel_caption.appendChild(title);carousel_caption.appendChild(description);return inner_item;})
let indicator_container=document.getElementById('carousel-indicators-id');let inner_container=document.getElementById('carousel-inner-id');carousel_items.forEach((element,index)=>{"<li data-target='#carouselHeader' data-slide-to='1'></li>"
let li=document.createElement('li');if(index==0){setAttributes(li,{"data-target":"#carouselHeader","data-slide-to":index,'class':'active'});}
else{setAttributes(li,{"data-target":"#carouselHeader","data-slide-to":index});}
indicator_container.appendChild(li);inner_container.appendChild(element);});}
document.addEventListener("DOMContentLoaded",()=>{let httpURl="/api/v2/projects/";fetchHTTP(httpURl).then((data)=>{projectInsert(data);}).catch(error=>{console.log(error);})});AOS.init();;