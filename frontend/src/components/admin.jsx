import React, { Component, useState } from 'react';
import axios from 'axios';
const uniqueRandom = require('unique-random');
 
const random = uniqueRandom(10, 1000000);
	
class Admin extends Component {
  constructor(props){
    super(props);
    this.state = {
      activeForm: false,
      formElement: <div></div>,
      content: <div></div>,
      rooms:{},
      roomForm: {
        RoomID: 0,
        Price: 0,
        Amenities: "",
        Extendable: "",
        Mountainview: "",
        Seaview: "",
        Capacity: 1,
        Available: "",
        HotelID: ""
      },
      hotelForm:{
        HotelID: 0,
        StarCategory: 0,
        NumOfRooms: 1,
        PhoneNumber: "",
        Address: "",
        ContactEmail: "",
        ParentHotelID: 0,
        Name: ""
      },
      employeeForm: {
        EmpID: 0,
        FullName: "",
        Address: "",
        Salary: 0,
        Role: "",
        ParentHotelID: 0,
        SIN: ""
      },
      customerForm: {
        CusID: 0,
        FullName: "",
        Address: "",
        DateOfReg: "",
        SIN: "",
        Phone: ""
      },
      hotels:{},
      employees:{},
      customers:{}
    };

    //Customers handling functions
    this.handleUpdateCustomers = this.handleUpdateCustomers.bind(this);
    this.handleDeleteCustomer = this.handleDeleteCustomer.bind(this);
    this.handleEditCustomer = this.handleEditCustomer.bind(this);
    this.handleInsertCustomer = this.handleInsertCustomer.bind(this);
    this.getCustomerForm = this.getCustomerForm.bind(this);

    //Employee handling functions
    this.handleUpdateEmployees = this.handleUpdateEmployees.bind(this);
    this.handleDeleteEmployee = this.handleDeleteEmployee.bind(this);
    this.handleEditEmployee = this.handleEditEmployee.bind(this);
    this.handleInsertEmployee = this.handleInsertEmployee.bind(this);
    this.getEmployeeForm = this.getEmployeeForm.bind(this);

    //Hotels handling functions
    this.handleUpdateHotels = this.handleUpdateHotels.bind(this);
    this.handleDeleteHotel = this.handleDeleteHotel.bind(this);
    this.handleEditHotel = this.handleEditHotel.bind(this);
    this.handleInsertHotel = this.handleInsertHotel.bind(this);
    this.getHotelForm = this.getHotelForm.bind(this);

    //Rooms handling functions
    this.handleUpdateRooms = this.handleUpdateRooms.bind(this);
    this.handleDeleteRoom = this.handleDeleteRoom.bind(this);
    this.handleEditRoom = this.handleEditRoom.bind(this);
    this.getRoomForm = this.getRoomForm.bind(this);
    this.handleInsertRoom = this.handleInsertRoom.bind(this);
  }


//Customers functions
  handleUpdateCustomers(event){
    axios.get("http://localhost:5000/api/customer").then((response) =>{
      let data = response.data;
      let contents =[];
      contents.push(<button onClick={this.getCustomerForm}>Insert</button>)
      contents.push(<tr className="titles"><th className="tabC">Customer ID</th><th className="tabC">Fullname</th><th className="tabC">Address</th><th className="tabC">Date of Registration</th><th className="tabC">SIN</th><th className="tabC">Phone</th><th className="tabC">Options</th></tr>)
      for(let i = 0; i< data.length; i++){
        this.state.customers[data[i][0]] = data[i];
        let button1 = <button onClick={this.getCustomerForm} className="optionsB">Edit</button>;
        let button2 = <button onClick={this.handleDeleteCustomer} className="optionsB">Delete</button>
        contents.push(<tr id={data[i][0]}><td className="tabC">{data[i][0]}</td><td className="tabC">{data[i][1]}</td><td className="tabC">{data[i][2]}</td><td className="tabC">{data[i][3]}</td><td className="tabC">{data[i][4]}</td><td className="tabC">{data[i][5]}</td><td className="tabC">{button1}{button2}</td></tr>)
      }

      let element = React.createElement("table", {className: "table", id:"table"}, contents);
      this.setState({
        activeForm: false,
        content: element
      })
      
    });
  }

  getCustomerForm(event){
    let id = event.target.parentNode.parentNode.id;
    let customer =  this.state.customers[id];
    let operation = this.handleEditCustomer;
    let operationName = "Edit";
    if(customer === undefined){
      id = random();
      this.state.customerForm = {
        CusID: id,
        FullName: "",
        Address: "",
        DateOfReg: "",
        SIN: "",
        Phone: ""
      }
      operation = this.handleInsertCustomer;
      operationName = "Insert"
    } else{
      this.state.customerForm={
        CusID: id,
        FullName: customer[1],
        Address: customer[2],
        DateOfReg: customer[3],
        SIN: customer[4],
        Phone: customer[5]
      }
    }

    const form = this.state.customerForm;
    const FormElement = () => {
      const [v, setValue] = useState(0);
      function handleValueChange(event) {
        const field = event.target.parentNode.innerText;
        form[field] = event.target.value;
        setValue((value) => value +1);
      }
  
      return (
        <div>
          <form onSubmit={operation}>
            <label><p>CusID: {id}</p></label>
            <label>
              FullName
              <input type="text" value={form.FullName} onChange={handleValueChange} required></input>
            </label>
            <label>
              Address
              <input type="text" value={form.Address} onChange={handleValueChange} required></input>
            </label>
            <label>
              DateOfReg
              <input type="date" value={form.DateOfReg} onChange={handleValueChange} required></input>
            </label>
            <label>
              SIN
              <input type="text" value={form.SIN} onChange={handleValueChange} required></input>
            </label>
            <label>
              Phone
              <input type="text" value={form.Phone} onChange={handleValueChange} required></input>
            </label>
            <button type="Submit" className="bookRoomSubmit">{operationName}</button>
          </form>
        </div>
      )
  }
    this.setState({activeForm: true, formElement: FormElement});
  }

  handleEditCustomer(event){
    event.preventDefault();
    axios.patch("http://localhost:5000/api/customer", {
      ...this.state.customerForm
    }, {
      headers:{
        "content-type": "application/json"
      }
    
    }).then(()=>{
      this.handleUpdateCustomers();
    });
  }


  handleInsertCustomer(event){
    event.preventDefault();
    axios({
      method: 'post',
      url: 'http://localhost:5000/api/customer',
      data: this.state.customerForm
    }).then(()=>{
      this.handleUpdateCustomers();
    })
  }

  handleDeleteCustomer(event){
    let id = event.target.parentNode.parentNode.id;
    axios({
      method: 'delete',
      url: 'http://localhost:5000/api/customer',
      data: {
        CusID: id
      }
    }).then(()=>{
      this.handleUpdateCustomers();
    });
  }

  //employees functions
  handleUpdateEmployees(event){
    axios.get("http://localhost:5000/api/employee").then((response) =>{
      let data = response.data;
      let contents =[];
      contents.push(<button onClick={this.getEmployeeForm}>Insert</button>)
      contents.push(<tr className="titles"><th className="tab">Employee ID</th><th className="tab">Fullname</th><th className="tab">Address</th><th className="tab">Salary</th><th className="tab">Role</th><th className="tab">Parent hotel ID</th><th className="tab">SIN</th><th className="tab">Options</th></tr>)
      for(let i = 0; i< data.length; i++){
        this.state.employees[data[i][0]] = data[i];
        let button1 = <button onClick={this.getEmployeeForm} className="optionsB">Edit</button>;
        let button2 = <button onClick={this.handleDeleteEmployee} className="optionsB">Delete</button>
        contents.push(<tr id={data[i][0]}><td className="tab">{data[i][0]}</td><td className="tab">{data[i][1]}</td><td className="tab">{data[i][2]}</td><td className="tab">{data[i][3]}</td><td className="tab">{data[i][4]}</td><td className="tab">{data[i][5]}</td><td className="tab">{data[i][6]}</td><td className="tab">{button1}{button2}</td></tr>)
      }

      let element = React.createElement("table", {className: "table", id:"table"}, contents);
      this.setState({
        activeForm: false,
        content: element
      })
      
    });

  }

  getEmployeeForm(event){
    let id = event.target.parentNode.parentNode.id;
    let employee =  this.state.employees[id];
    console.log(employee);
    console.log(this.state.employees);
    let operation = this.handleEditEmployee;
    let operationName = "Edit";
    if(employee === undefined){
      id = random();
      this.state.employeeForm = {
        EmpID: id,
        FullName: "",
        Address: "",
        Salary: 0,
        Role: "",
        ParentHotelID: 0,
        SIN: ""
      }
      operation = this.handleInsertEmployee;
      operationName = "Insert"
    } else{
      this.state.employeeForm={
        EmpID: id,
        FullName: employee[1],
        Address: employee[2],
        Salary: employee[3],
        Role: employee[4],
        ParentHotelID: employee[5],
        SIN: employee[6]
      }
    }

    const form = this.state.employeeForm;
    const FormElement = () => {
      const [v, setValue] = useState(0);
      function handleValueChange(event) {
        const field = event.target.parentNode.innerText;
        form[field] = event.target.value;
        setValue((value) => value +1);
      }
  
      return (
        <div>
          <form onSubmit={operation}>
            <label><p>EmpID: {id}</p></label>
            <label>
              FullName
              <input type="text" value={form.FullName} onChange={handleValueChange} required></input>
            </label>
            <label>
              Address
              <input type="text" value={form.Address} onChange={handleValueChange} required></input>
            </label>
            <label>
              Salary
              <input type="number" min="0" value={form.Salary} onChange={handleValueChange} required></input>
            </label>
            <label>
              Role
              <input type="text" value={form.Role} onChange={handleValueChange} required></input>
            </label>
            <label>
              ParentHotelID
              <input type="number" value={form.ParentHotelID} onChange={handleValueChange} required></input>
            </label>
            <label>
              SIN
              <input type="text" value={form.SIN} onChange={handleValueChange} required></input>
            </label>
            <button type="Submit" className="bookRoomSubmit">{operationName}</button>
          </form>
        </div>
      )
  }
    this.setState({activeForm: true, formElement: FormElement});
  }

  handleEditEmployee(event){
    event.preventDefault();
    axios.patch("http://localhost:5000/api/employee", {
      ...this.state.employeeForm
    }, {
      headers:{
        "content-type": "application/json"
      }
    
    }).then(()=>{
      this.handleUpdateEmployees();
    });
  }

  handleInsertEmployee(event){
    event.preventDefault();
    axios({
      method: 'post',
      url: 'http://localhost:5000/api/employee',
      data: this.state.employeeForm
    }).then(()=>{
      this.handleUpdateEmployees();
    })
  }


  handleDeleteEmployee(event){
    let id = event.target.parentNode.parentNode.id;
    axios({
      method: 'delete',
      url: 'http://localhost:5000/api/employee',
      data: {
        EmpID: id
      }
    }).then(()=>{
      this.handleUpdateEmployees();
    });

  }


  //Hotels Functions
  handleUpdateHotels(event){
    axios.get("http://localhost:5000/api/hotelChain").then((response) =>{
      let data = response.data;
      let contents =[];
      contents.push(<button onClick={this.getHotelForm}>Insert</button>)
      contents.push(<tr className="titles"><th className="tab">Hotel ID</th><th className="tab">Star Category</th><th className="tab">Number of rooms</th><th className="tab">Phone number</th><th className="tab">Address</th><th className="tab">Email</th><th className="tab">Parent hotel ID</th><th className="tab">Name</th><th className="tab">Options</th></tr>)
      for(let i = 0; i< data.length; i++){
        this.state.hotels[data[i][0]] = data[i];
        let button1 = <button onClick={this.getHotelForm} className="optionsB">Edit</button>;
        let button2 = <button onClick={this.handleDeleteHotel} className="optionsB">Delete</button>
        contents.push(<tr id={data[i][0]}><td className="tab">{data[i][0]}</td><td className="tab">{data[i][1]}</td><td className="tab">{data[i][2]}</td><td className="tab">{data[i][3]}</td><td className="tab">{data[i][4]}</td><td className="tab">{data[i][5]}</td><td className="tab">{data[i][6]}</td><td className="tab">{data[i][7]}</td><td className="tab">{button1}{button2}</td></tr>)
      }

      let element = React.createElement("table", {className: "table", id:"table"}, contents);
      this.setState({
        activeForm: false,
        content: element
      })
      
    });

  }
  getHotelForm(event){
    let id = event.target.parentNode.parentNode.id;
    let hotel =  this.state.hotels[id];
    let operation = this.handleEditHotel;
    let operationName = "Edit";
    if(hotel === undefined){
      id = random();
      this.state.hotelForm = {
        HotelID: id,
        StarCategory: 0,
        NumOfRooms: 0,
        PhoneNumber: "",
        Address: "",
        ContactEmail: "",
        ParentHotelID: 0,
        Name: ""
      }
      operation = this.handleInsertHotel;
      operationName = "Insert"
    } else{
      this.state.hotelForm={
        HotelID: id,
        StarCategory: hotel[1],
        NumOfRooms: hotel[2],
        PhoneNumber: hotel[3],
        Address: hotel[4],
        ContactEmail: hotel[5],
        ParentHotelID: hotel[6],
        Name: hotel[7]
      }
    }

    const form = this.state.hotelForm;
    const FormElement = () => {
      const [v, setValue] = useState(0);
      function handleValueChange(event) {
        const field = event.target.parentNode.innerText;
        form[field] = event.target.value;
        setValue((value) => value +1);
      }
  
      return (
        <div>
          <form onSubmit={operation}>
            <label><p>HotelID: {id}</p></label>
            <label>
              StarCategory
              <input type="number" min="0" value={form.StarCategory} onChange={handleValueChange} required></input>
            </label>
            <label>
              NumOfRooms
              <input type="number" min="1" value={form.NumOfRooms} onChange={handleValueChange} required></input>
            </label>
            <label>
              PhoneNumber
              <input type="text" value={form.PhoneNumber} onChange={handleValueChange} required></input>
            </label>
            <label>
              Address
              <input type="text" value={form.Address} onChange={handleValueChange} required></input>
            </label>
            <label>
              ContactEmail
              <input type="text" value={form.ContactEmail} onChange={handleValueChange} required></input>
            </label>
            <label>
              ParentHotelID
              <input type="number" value={form.ParentHotelID} onChange={handleValueChange} required></input>
            </label>
            <label>
              Name
              <input type="text" value={form.Name} onChange={handleValueChange} required></input>
            </label>
            <button type="Submit" className="bookRoomSubmit">{operationName}</button>
          </form>
        </div>
      )
  }
    this.setState({activeForm: true, formElement: FormElement});
  }


  handleEditHotel(event){
    event.preventDefault();
    axios.patch("http://localhost:5000/api/hotelChain", {
      ...this.state.hotelForm
    }, {
      headers:{
        "content-type": "application/json"
      }
    
    }).then(()=>{
      this.handleUpdateHotels();
    });
  }

  handleInsertHotel(event){
    event.preventDefault();
    axios({
      method: 'post',
      url: 'http://localhost:5000/api/hotelChain',
      data: this.state.hotelForm
    }).then(()=>{
      this.handleUpdateHotels();
    })
  }

  handleDeleteHotel(event){
    let id = event.target.parentNode.parentNode.id;
    axios({
      method: 'delete',
      url: 'http://localhost:5000/api/hotelChain',
      data: {
        HotelID: id
      }
    }).then(()=>{
      this.handleUpdateHotels();
    });
  }


  // rooms functions
  handleUpdateRooms(event){
    axios.get("http://localhost:5000/api/room").then((response) =>{
      let data = response.data;
      let contents =[];
      contents.push(<button onClick={this.getRoomForm}>Insert</button>)
      contents.push(<tr className="titles"><th className="tab">Room ID</th><th className="tab">Price</th><th className="tab">Amenities</th><th className="tab">Extendable</th><th className="tab">Mountain view</th><th className="tab">Sea view</th><th className="tab">Capacity</th><th className="tab">Available</th><th className="tab">Hotel ID</th><th className="tab">Options</th></tr>)
      for(let i = 0; i< data.length; i++){
        this.state.rooms[data[i][0]] = data[i];
        let button1 = <button onClick={this.getRoomForm} className="optionsB">Edit</button>;
        let button2 = <button onClick={this.handleDeleteRoom} className="optionsB">Delete</button>
        contents.push(<tr id={data[i][0]}><td className="tab">{data[i][0]}</td><td className="tab">{data[i][1]}</td><td className="tab">{data[i][2]}</td><td className="tab">{data[i][3]}</td><td className="tab">{data[i][4]}</td><td className="tab">{data[i][5]}</td><td className="tab">{data[i][6]}</td><td className="tab">{data[i][7]}</td><td className="tab">{data[i][8]}</td><td className="tab">{button1}{button2}</td></tr>)
      }

      let element = React.createElement("table", {className: "table", id:"table"}, contents);
      this.setState({
        activeForm: false,
        content: element
      })
      
    });
  }


  handleEditRoom(event){
    event.preventDefault();
    axios.patch("http://localhost:5000/api/room", {
      ...this.state.roomForm
    }, {
      headers:{
        "content-type": "application/json"
      }
    
    }).then(()=>{
      this.handleUpdateRooms();
    });
  }

  handleInsertRoom(event){
    event.preventDefault();
    axios({
      method: 'post',
      url: 'http://localhost:5000/api/room',
      data: this.state.roomForm
    }).then(()=>{
      this.handleUpdateRooms();
    })
  }

  getRoomForm(event){
    let id = event.target.parentNode.parentNode.id;
    let room =  this.state.rooms[id];
    let operation = this.handleEditRoom;
    let operationName = "Edit";
    if(room === undefined){
      id = random();
      this.state.roomForm = {
        RoomID: 0,
        Price: 0,
        Amenities: "",
        Extendable: "",
        Mountainview: "",
        Seaview: "",
        Capacity: 0,
        Available: "",
        HotelID: ""
      };
      operation = this.handleInsertRoom;
      operationName = "Insert"
    } else{
      this.state.roomForm={
        ...this.state.roomForm,
        Price: room[1],
        Amenities: room[2],
        Extendable: room[3],
        Mountainview: room[4],
        Seaview: room[5],
        Capacity: room[6],
        Available: room[7],
        HotelID: room[8]
      }
    }
    this.state.roomForm ={
      ...this.state.roomForm,
      RoomID: id
    }

    const form = this.state.roomForm;
    const FormElement = () => {
      const [v, setValue] = useState(0);
      function handleValueChange(event) {
        const field = event.target.parentNode.innerText;
        form[field] = event.target.value;
        setValue((value) => value +1);
      }
  
      return (
        <div>
          <form onSubmit={operation}>
            <label><p>Room ID: {id}</p></label>
            <label>
              Price
              <input type="number" min="0" value={form.Price} onChange={handleValueChange} required></input>
            </label>
            <label>
              Amenities 
              <input type="text" value={form.Amenities} onChange={handleValueChange} required></input>
            </label>
            <label>
              Extendable
              <input type="text" value={form.Extendable} onChange={handleValueChange} required></input>
            </label>
            <label>
              Mountainview
              <input type="text" value={form.Mountainview} onChange={handleValueChange} required></input>
            </label>
            <label>
              Seaview
              <input type="text" value={form.Seaview} onChange={handleValueChange} required></input>
            </label>
            <label>
              Capacity
              <input type="number" min="1" value={form.Capacity} onChange={handleValueChange} required></input>
            </label>
            <label>
              Available
              <input type="text" value={form.Available} onChange={handleValueChange} required></input>
            </label>
            <label>
              HotelID
              <input type="number" value={form.HotelID} onChange={handleValueChange} required></input>
            </label>
            <button type="Submit" className="bookRoomSubmit">{operationName}</button>
          </form>
        </div>
      )
  }
    this.setState({activeForm: true, formElement: FormElement});
  }

  handleDeleteRoom(event){
    let id = event.target.parentNode.parentNode.id;
    axios({
      method: 'delete',
      url: 'http://localhost:5000/api/room',
      data: {
        RoomID: id
      }
    }).then(()=>{
      this.handleUpdateRooms();
    });
  }



  //Render component
  render() {
    let content = this.state.content;
    let Form = () => {
      return <div></div>;
    };
    if(this.state.activeForm){
      Form = this.state.formElement;
    }
    return (
      <div className="container">
        <h1>Admin</h1>
        <button onClick={this.handleUpdateCustomers} className="adminB">Customers</button>
        <button onClick={this.handleUpdateEmployees} className="adminB">Employees</button>
        <button onClick={this.handleUpdateHotels} className="adminB">Hotels</button>
        <button onClick={this.handleUpdateRooms} className="adminB">Rooms</button>
        {content}
        <Form></Form>
      </div>
      
    );
  }
}
export default Admin;