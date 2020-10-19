/******/ (function(modules) { // webpackBootstrap
/******/ 	// The module cache
/******/ 	var installedModules = {};
/******/
/******/ 	// The require function
/******/ 	function __webpack_require__(moduleId) {
/******/
/******/ 		// Check if module is in cache
/******/ 		if(installedModules[moduleId]) {
/******/ 			return installedModules[moduleId].exports;
/******/ 		}
/******/ 		// Create a new module (and put it into the cache)
/******/ 		var module = installedModules[moduleId] = {
/******/ 			i: moduleId,
/******/ 			l: false,
/******/ 			exports: {}
/******/ 		};
/******/
/******/ 		// Execute the module function
/******/ 		modules[moduleId].call(module.exports, module, module.exports, __webpack_require__);
/******/
/******/ 		// Flag the module as loaded
/******/ 		module.l = true;
/******/
/******/ 		// Return the exports of the module
/******/ 		return module.exports;
/******/ 	}
/******/
/******/
/******/ 	// expose the modules object (__webpack_modules__)
/******/ 	__webpack_require__.m = modules;
/******/
/******/ 	// expose the module cache
/******/ 	__webpack_require__.c = installedModules;
/******/
/******/ 	// define getter function for harmony exports
/******/ 	__webpack_require__.d = function(exports, name, getter) {
/******/ 		if(!__webpack_require__.o(exports, name)) {
/******/ 			Object.defineProperty(exports, name, { enumerable: true, get: getter });
/******/ 		}
/******/ 	};
/******/
/******/ 	// define __esModule on exports
/******/ 	__webpack_require__.r = function(exports) {
/******/ 		if(typeof Symbol !== 'undefined' && Symbol.toStringTag) {
/******/ 			Object.defineProperty(exports, Symbol.toStringTag, { value: 'Module' });
/******/ 		}
/******/ 		Object.defineProperty(exports, '__esModule', { value: true });
/******/ 	};
/******/
/******/ 	// create a fake namespace object
/******/ 	// mode & 1: value is a module id, require it
/******/ 	// mode & 2: merge all properties of value into the ns
/******/ 	// mode & 4: return value when already ns object
/******/ 	// mode & 8|1: behave like require
/******/ 	__webpack_require__.t = function(value, mode) {
/******/ 		if(mode & 1) value = __webpack_require__(value);
/******/ 		if(mode & 8) return value;
/******/ 		if((mode & 4) && typeof value === 'object' && value && value.__esModule) return value;
/******/ 		var ns = Object.create(null);
/******/ 		__webpack_require__.r(ns);
/******/ 		Object.defineProperty(ns, 'default', { enumerable: true, value: value });
/******/ 		if(mode & 2 && typeof value != 'string') for(var key in value) __webpack_require__.d(ns, key, function(key) { return value[key]; }.bind(null, key));
/******/ 		return ns;
/******/ 	};
/******/
/******/ 	// getDefaultExport function for compatibility with non-harmony modules
/******/ 	__webpack_require__.n = function(module) {
/******/ 		var getter = module && module.__esModule ?
/******/ 			function getDefault() { return module['default']; } :
/******/ 			function getModuleExports() { return module; };
/******/ 		__webpack_require__.d(getter, 'a', getter);
/******/ 		return getter;
/******/ 	};
/******/
/******/ 	// Object.prototype.hasOwnProperty.call
/******/ 	__webpack_require__.o = function(object, property) { return Object.prototype.hasOwnProperty.call(object, property); };
/******/
/******/ 	// __webpack_public_path__
/******/ 	__webpack_require__.p = "";
/******/
/******/
/******/ 	// Load entry module and return exports
/******/ 	return __webpack_require__(__webpack_require__.s = "./PersonalSite/static/backup/js/carousel.js");
/******/ })
/************************************************************************/
/******/ ({

/***/ "./PersonalSite/static/backup/js/carousel.js":
/*!***************************************************!*\
  !*** ./PersonalSite/static/backup/js/carousel.js ***!
  \***************************************************/
/*! no static exports found */
/***/ (function(module, exports) {

//fetch data from an api using get
let fetchHTTP =  (urlLink)=>{ 
    return new Promise((resolve, reject)=>{
        var xhr = new XMLHttpRequest();
        var url = urlLink;

        xhr.open("GET", url, true);
        xhr.setRequestHeader("Content-Type", "application/json");

        xhr.onreadystatechange = function () 
        {
            if (xhr.readyState === 4 && xhr.status === 200) 
            {
                var data = JSON.parse(xhr.responseText);
                resolve(data);

                
            }
            else if (xhr.readyState === 4 && xhr.status == 404){
                reject(JSON.parse(xhr.responseText));
            }
                 
        };
      xhr.send();
    });
}

let  setAttributes =(el, attrs) => {
    for(var key in attrs) {
      el.setAttribute(key, attrs[key]);
    }
  }

function truncate(input, maxlength) {
    if (input.length > maxlength)
       return input.substring(0,maxlength) + '...';
    else
       return input;
 };
//inserts each project to html element to be added to the homepage
let projectInsert =(projectArray) =>{
    projectArray = projectArray.results.filter((element)=>{
        if (element.image != null){
            return true;
        }
    })
    if (projectArray.length == 0){
        return;
    }
    let carousel_items= projectArray.map( (project,index) =>{
        //map all api-request to div to be displayed in the hompage carousel 
        let inner_item = document.createElement('div');
        if (index == 0){
            inner_item.className="carousel-item active";
        }
        else {
            inner_item.className="carousel-item";
        }
        //img main slide 
        var img = new Image();
        var imageContainer = document.createElement('div');
        imageContainer.className="imageContainer";
        imageContainer.appendChild(img)
        inner_item.appendChild(imageContainer);
        img.src=project.image.url;
        img.alt=project.image.alt;
        img.className="img-fluid";
        //project-img-end
        //create clickable link and item_text
        let link= document.createElement('a');
        inner_item.appendChild(link);
        link.href= project.project_link;
        let carousel_caption = document.createElement('div');
        carousel_caption.className = "carousel-caption";
        link.appendChild(carousel_caption);
        //Title 
        let title= document.createElement('h1');
        title.innerText = project.project_name;
        //Description
        let description = document.createElement('p');
        description.innerText = truncate(project.description,100);
        carousel_caption.appendChild(title);
        carousel_caption.appendChild(description);
        return inner_item;

 
    })
    //Add indicator To items 
    let indicator_container = document.getElementById('carousel-indicators-id');
    let inner_container = document.getElementById('carousel-inner-id');
    carousel_items.forEach((element,index) => {
        "<li data-target='#carouselHeader' data-slide-to='1'></li>"
        let li = document.createElement('li');
        if (index == 0 ){
            setAttributes(li, { "data-target":"#carouselHeader","data-slide-to":index , 'class': 'active'});
        }
        else {
            setAttributes(li, { "data-target":"#carouselHeader","data-slide-to":index });
        }
        indicator_container.appendChild(li);
        inner_container.appendChild(element);
        
    });
}
document.addEventListener("DOMContentLoaded", ()=>{

    let httpURl = "/api/v2/projects/";
    fetchHTTP(httpURl).then((data)=>{
        projectInsert(data);
    }).catch(error=>{
        console.log(error);
    })
})



/***/ })

/******/ });
//# sourceMappingURL=compiled_carousel.js.map