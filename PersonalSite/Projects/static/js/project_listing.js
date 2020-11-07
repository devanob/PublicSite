import "../sass/project_listing.scss";

import * as blobs2 from "blobs/v2";
import * as blobs2Animate from "blobs/v2/animate";
const axios = require('axios');
import React from 'react';
import ReactDOM from 'react-dom';
import ReactDOMServer from 'react-dom/server';

class ProjectListing{
  isBusy =false;
  next_page_link = null;
  project_container = null;
  ap_url = null;
  svgStringGenerator = null;
  constructor(){
    this.init();
  }

  //toggles the busy flag
  toggleBusy(){
    this.isBusy = this.isBusy  ? false: true;
  }

  setDomBusy= ()=>{

  }
  
  init = ()=>{
    this.setUpContainersIntial();
    this.setUpEventsInitial();
    this.get_init_data();
    
  }
  handleData = (response)=>{
    this.filteredProject(response.data);
  }
  
  filteredProject =(data)=>{
    this.next_page_link = data.next;
    let inner_project = this.project_container.querySelector(".row.projects");
    let projects = data.results;
    projects.forEach(project=>{
      project_html = this.generateProjectHTML(project);
      inner_project.insertAdjacentHTML('beforeend', project_html);
      

    })


  }
  generateProjectHTML=(element_json)=>{
    let _categories = element_json._categories;
    _categories = _categories.filter((cat)=>{
      //console.log(cat)
      return cat.icon !== null;
    })
    return ReactDOMServer.renderToStaticMarkup(
    <div className="col-lg-4 col-md-6 d-flex align-items-stretch" data-aos="zoom-in" data-aos-delay="100">
      <div className="icon-box">
      <div className="icon-wrapper">

        {_categories.map((value,index)=>{
          let addtional_classname=  index === 0 ?  "active" : "";
          let category = value.name;
          const svgString = blobs2.svg(
            {
                seed: Math.random(),
                extraPoints: 8,
                randomness: 4,
                size: 100,
            },
            {
                fill: "white", // 🚨 NOT SANITIZED
                stroke: "black", // 🚨 NOT SANITIZED
                strokeWidth: 1,
            },
        );
          return(
            <div className={"icon " + addtional_classname + " " + value.name } >
               <div className='blob' dangerouslySetInnerHTML={{ __html:svgString }}></div>
               <div className={'category-icon '} dangerouslySetInnerHTML={{ __html:value.icon }}></div>
            </div>  
          );
        })}
      </div>
        <h4><a href={element_json.project_link}>{element_json.project_name}</a></h4>
        <p>{element_json.description}</p>
      </div>
  </div>
    
    )
  } 
  get_init_data = ()=>{
    this.get_data("GET",this.ap_url,null,this.handleData)
  }
  get_data = (type,url,data=null,call_back=null)=>{
    if (type.toLowerCase() === 'get'){
      axios.get(url).then(call_back);
    }
  }


  setBusy = (flag = null) =>{
    this.flag = flag;
    
  }
  setUpContainersIntial = ()=>{
    this.project_container  = document.querySelector(".projects.container");
    this.ap_url = this.project_container.getAttribute("data-url-project");

  }
  //set all the event for the project listing 
  setUpEventsInitial = ()=>{
    //query for all buttons 
    let filter_buttons = document.querySelectorAll(".projects .filters .filter-button");
    filter_buttons.forEach(dom_element=>{
      dom_element.addEventListener("click", this.filterButtonHanldierGenerator(dom_element));
    })
  }
  //returns a handle than handles the clicking event for each filter button
  filterButtonHanldierGenerator =(dom_object)=>{
    return ()=>{
      console.log(dom_object);
    }
  }

}


window.addEventListener('DOMContentLoaded', (event) => {
  new ProjectListing();
})








