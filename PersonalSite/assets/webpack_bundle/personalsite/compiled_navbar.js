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
/******/ 	return __webpack_require__(__webpack_require__.s = "./PersonalSite/static/js/navbar.js");
/******/ })
/************************************************************************/
/******/ ({

/***/ "./PersonalSite/static/js/navbar.js":
/*!******************************************!*\
  !*** ./PersonalSite/static/js/navbar.js ***!
  \******************************************/
/*! no static exports found */
/***/ (function(module, exports) {


let viewableItem= (element) =>{

        let elemTop = element.offsetTop;
        let elemBottom = elemTop + element.offsetHeight;
        let viewportTop = window.scrollY;
        let viewportBottom = viewportTop + window.innerHeight;
        return elemBottom <= viewportBottom && elemTop >= viewportTop ;
}
let headerViewableBefore = true;// True By Default
let helperScrollEventHandlier = (element)=>{
    let headerViewable = viewableItem(element);
    if (headerViewable && headerViewableBefore == false){ //We'll Need To Chnage Styling
        headerViewableBefore = true;
        let navibar  = document.getElementById("navbarTop");
        navibar.classList.add("navbar-custom");
        navibar.classList.remove("navbar-dark-custom", "solid");
        return false;
    }
    else if (!headerViewable && headerViewableBefore == true){ //We'll Need To chnage styling back
        headerViewableBefore = false;
        let navibar  = document.getElementById("navbarTop");
        navibar.classList.add("navbar-dark-custom", "solid");
        navibar.classList.remove("navbar-custom");
        return true;
    }
    
    
}
let scrollEventHandlier = () =>{
    let viewAbles = document.getElementsByClassName("viewables");
    for (let i = 0 ; i < viewAbles.length; i++){
      if (helperScrollEventHandlier(viewAbles[i])){
        return;
      }
    }
    hideNavScroll();
}
document.addEventListener("scroll",scrollEventHandlier);

let setViewAvaibility = (element)=>{
    let isViewable = viewableItem(element);
    if (!isViewable){
        let navibar  = document.getElementById("navbarTop");
        navibar.classList.add("navbar-dark-custom", "solid");
        navibar.classList.remove("navbar-custom");
        return false;
    }
    return true;
}

let loadNav = ()=>{
    let allViewable = document.getElementsByClassName("viewables");
    console.log(allViewable);
    for (let i = 0 ; i < allViewable.length; i++){
      if(setViewAvaibility(allViewable[i])){
        return; // if any viewable item is in the view port then return 
      }
    }
    let navibar  = document.getElementById("navbarTop");
    navibar.classList.add("navbar-dark-custom", "solid");
    navibar.classList.remove("navbar-custom");
    


}

if(document.readyState === 'loading'){

  document.addEventListener('DOMContentLoaded',loadNav );

}
else{

  loadNav()
}
//Nav Bar Interaction 
var prevScrollpos = window.pageYOffset;
let hideNavScroll =()=>{
  var currentScrollPos = window.pageYOffset;
  let navibar  = document.getElementById("navbarTop");
  if (navibar.classList.contains('navbar-dark-custom')){
    if (prevScrollpos > currentScrollPos) {
      
      navibar.classList.add("solid");
      navibar.classList.remove("light");
      
    } else {
      navibar.classList.add("light");
      navibar.classList.remove("solid");
      
    }
  }
  prevScrollpos = currentScrollPos;
}



/***/ })

/******/ });
//# sourceMappingURL=compiled_navbar.js.map