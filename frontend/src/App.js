import React from "react";
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";
import Login from "./components/login";
import Employee from "./components/employee";
import Admin from "./components/admin";
import Customer from "./components/customer";

function App() {
  return (
    <div className="App">
      <Router>
        <Switch>
          <Route path="/" exact component={() => <Login />} />
          <Route path="/employee" exact component={() => <Employee />} />
          <Route path="/admin" exact component={() => <Admin />} />
          <Route path="/customer" exact component={() => <Customer />} />
        </Switch>
      </Router>
    </div>
  );
}

export default App;