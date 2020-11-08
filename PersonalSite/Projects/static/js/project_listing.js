import "../sass/project_listing.scss";


const axios = require('axios');
import React, {Component} from "react";
import ReactDOMServer from 'react-dom/server';
import ProjectInstance from "./ProjectInstance";
import ReactDOM from 'react-dom';
class ProjectListing extends Component {
  isBusy =false;
  next_page_link = null;
  project_container = null;
  ap_url = null;
  svgStringGenerator = null;
  state = { projects: [] }
  constructor(props){
    super(props);
    this.init();
  } 

  //toggles the busy flag
  toggleBusy(){
    this.isBusy = this.isBusy  ? false: true;
  }

  setDomBusy= ()=>{

  }
  
  init = ()=>{
    this.isBusy = true;
    this.setUpContainersIntial();
    this.setUpEventsInitial();
    this.get_init_data();
    
  }
  handleData = (response)=>{
    console.log(response);
    this.setState({ projects: response.data.results });
  }
  
  render(){
    if (this.isBusy === false  ){
      return (<div> Loading </div>);
    }
    else if(!this.state.projects.length){
      return (<div> No Projects  </div>)
    }
    else{
      return (this.state.projects.map((project,value)=>{
        return <ProjectInstance key={"project_" + project.id} project={project}/>
      }));
    }
      
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

export default ProjectListing

window.addEventListener('DOMContentLoaded', (event) => {
  let inner_project = document.querySelector(".projects.container .row.projects");
  ReactDOM.render(
    <ProjectListing/>,
    inner_project);
})








