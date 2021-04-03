import React, { Component } from 'react';
import "../styles/style.css";

	
class Login extends Component {

  constructor(props){
    super(props);
    this.state = {
      username: '',
      password: '',
      wrongCred: false,
    };

    this.handleUsernameChange = this.handleUsernameChange.bind(this);
    this.handlePasswordChange = this.handlePasswordChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleUsernameChange(event){
    this.setState({username: event.target.value});
  }

  handlePasswordChange(event){
    this.setState({password: event.target.value});
  }

  handleSubmit(event) {
    if(this.state.username === "admin" && this.state.password === "admin"){
      window.location.assign("./admin");
    } else if(this.state.username ==="customer" && this.state.password === "customer"){
      window.location.assign("./customer");
    } else if(this.state.username ==="employee" && this.state.password === "employee"){
      window.location.assign("./employee");
    } else{
      this.setState({wrongCred:true});
    }
    event.preventDefault();
  }
  

  render() {
    let msg = <div></div>;
    if(this.state.wrongCred){
      msg = <p>Wrong username or password please try again</p>
    }
    return (
      <div className="loginContainer">
        <h1>Login</h1>
        <form onSubmit={this.handleSubmit} >
          {msg}
          <label>
            Username:<br/>
            <input type="text" value={this.state.username} onChange={this.handleUsernameChange} required/>
          </label>
          <br/>
          <label>
            Password:<br/>
            <input type="password" value={this.state.password} onChange={this.handlePasswordChange} required/>
          </label>
          <br/>
          <button type="submit" >Login</button>
        </form>
        
      </div>
      
    );
  }
}
export default Login;