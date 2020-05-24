//import scripts 
import {$,jQuery} from 'jquery';
import "./carousel.js";
import "./jqBootstrapValidation.js"
import "./navbar";
import "./time.js";
import "./scrolling-nav";
import "./carousel.js";
//import scripts to style

import "../sass/animationFix.scss";
import "../sass/buttonStyling.scss";
import "../sass/carousel.scss";
import "../sass/generalNavBar.scss";
import "../sass/personals.scss";
import "../sass/scrolling-nav.scss";
import "../sass/base.scss";
import 'bootstrap';

import cssVars from 'css-vars-ponyfill';

cssVars({
    // Options...
  });

let nav_height_var = ()=>{
let nav_bar = document.querySelector(".padded-top #navbarTop");
    if (nav_bar){
        let nav_bar_height = nav_bar.offsetHeight;
        console.log(nav_bar_height);
        //
        document.documentElement.style.setProperty('--navHeight', "".concat(nav_bar_height, "px"));
        window.addEventListener('resize', function () {
            // We execute the same script as before
            let nav_bar_height = nav_bar.offsetHeight;
            console.log(nav_bar_height);
            document.documentElement.style.setProperty('--navHeight', "".concat(nav_bar_height, "px"));
        });
    }
}


if (document.readyState !== 'loading') {
    nav_height_var()
  } else {
    window.addEventListener("DOMContentLoaded", function () {
        nav_height_var();
    });
  }