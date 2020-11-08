import React, {Component} from "react";
import * as blobs2 from "blobs/v2";
import * as blobs2Animate from "blobs/v2/animate";
//Project Instance
class ProjectInstance extends Component{
    //
    state ={current_icon_index : 0};
    constructor(props){
        super(props);
        this.setIconChange();
        
    }

    setIconChange = ()=>{
       
        setInterval(()=>{
           
            //console.log(numm);
            let number = this.state.current_icon_index;
            //console.log(random_number);
            this.setState({current_icon_index: number + 1 });
        },3000);
        
    }
    
    //
    render(){
        const {project  = null} = this.props;
        let _categories = project._categories;
        
        //console.log(current_index);
        _categories = _categories.filter((cat)=>{
        //console.log(cat)
        return cat.icon !== null;
        })
        //
        
        //console.log( this.state.current_icon_index);
        current_index = 0;
        if (_categories.length){
            current_index = this.state.current_icon_index % _categories.length;
        }
        console.log(_categories);
        console.log(current_index);
        return (

        <div className="project col-lg-4 col-md-6 d-flex align-items-stretch" data-aos="zoom-in" data-aos-delay="100">
            <div className="icon-box">
             <div className="icon-wrapper">
                 {_categories.map((value,index)=>{
                    let addtional_classname=  index === current_index  ?  "active" : "";
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
            <div className={"icon " + addtional_classname + " " + value.name } key={"icon_"+ value.id} >
               <div className='blob' dangerouslySetInnerHTML={{ __html:svgString }}></div>
               <div className={'category-icon '} dangerouslySetInnerHTML={{ __html:value.icon }}></div>
            </div>  
          );
        })}
      </div>
        <h4><a href={project.project_link}>{project.project_name}</a></h4>
        <p>{project.description}</p>
      </div>
    </div>
        );
    }
}

export default ProjectInstance;
