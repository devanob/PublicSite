import "../sass/project_listing.scss";

class MyComponent extends HTMLElement {
    constructor(data){
        super();
        
        this.data = this.getAttribute('data');
        console.log(this.data);
        setInterval(()=>{
            this.connectedCallback();
            
        }, 100)
    }
    connectedCallback() {
      this.innerHTML = `<h1>Hello world</h1> ${Math.random() *10 }`;
    }
  }
      
  customElements.define('my-component', MyComponent);
  const fragment = document.getElementById('people-template');
  console.log( fragment);
