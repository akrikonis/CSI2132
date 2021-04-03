import React, { Component } from 'react';
import axios from 'axios';
const uniqueRandom = require('unique-random');
 
const random = uniqueRandom(10, 1000000);
	
class Customer extends Component {
  constructor(props){
    super(props);
    this.state = {
      loading: true,
      content: <div></div>,
      rooms: {},
      book: false,
      booking: {}
    };
    this.handleBook = this.handleBook.bind(this);
    this.update = this.update.bind(this);
    this.handleBookRoom = this.handleBookRoom.bind(this);
  }

  handleBook(event){
    let id = event.target.parentNode.parentNode.id;
    // axios.patch("http://localhost:5000/api/room/book", {
    //   RoomID: id
    // }).then(()=>{
    //   this.update();
    // });
    this.setState({book: true, booking:{
      RoomID: id
    }});
    
  }
  update(){
    axios.get("http://localhost:5000/api/room").then((response) =>{
      let data = response.data;
      let contents =[];
      contents.push(<tr className="titles"><th className="tab">Price</th><th className="tab">Amenities</th><th className="tab">Extendable</th><th className="tab">Mountain view</th><th className="tab">Sea view</th><th className="tab">Capacity</th><th className="tab">Available</th><th className="tab">Book</th></tr>)
      for(let i = 0; i< data.length; i++){
        this.state.rooms[data[i][0]] = data[i];
        let button = <p></p>;
        if(data[i][7] === "free"){
          button = <button onClick={this.handleBook}>Book</button>
        }
        contents.push(<tr id={data[i][0]}><td className="tab">{data[i][1]}</td><td className="tab">{data[i][2]}</td><td className="tab">{data[i][3]}</td><td className="tab">{data[i][4]}</td><td className="tab">{data[i][5]}</td><td className="tab">{data[i][6]}</td><td className="tab">{data[i][7]}</td><td className="tab">{button}</td></tr>)
      }

      let element = React.createElement("table", {className: "table", id:"table"}, contents);
      this.setState({
        loading: false,
        content: element
      })
      
    });
  }

  handleBookRoom(event){
    event.preventDefault();
    this.state.booking={
      ...this.state.booking,
      Occupants: event.target.children[4].children[0].value,
      StartDate: event.target.children[5].children[0].value
    }
    let customer = {
      CusID: this.state.booking.CusID,
      FullName: event.target.children[0].children[0].value,
      Address: event.target.children[1].children[0].value,
      DateOfReg: '2021-04-03',
      SIN: event.target.children[2].children[0].value,
      Phone: event.target.children[3].children[0].value
    }
    axios({
      method: 'post',
      url: 'http://localhost:5000/api/customer',
      data: customer
    }).then(()=>{
      axios({
        method: 'post',
        url: 'http://localhost:5000/api/booking',
        data: this.state.booking
      }).then(()=>{
        axios.patch("http://localhost:5000/api/room/book", {
          RoomID: this.state.booking.RoomID
        }).then(()=>{
            this.setState({
              book: false,
              booking: {}
            })
            this.update();
        });
      });
    });
  }

  getBookingElement(){
    let room =  this.state.rooms[this.state.booking.RoomID]
    let hotelID =room[8];
    let maxOccupants = room[6];
    this.state.booking ={
      ...this.state.booking,
      BookingID: random(),
      CusID: random(),
      HotelID: hotelID
    }
    return (
      <div>
        <form onSubmit={this.handleBookRoom}>
          <label>
            Full Name: 
            <input type="text" id="fullname" required></input>
          </label>
          <label>
            Address: 
            <input type="text" id="address" required></input>
          </label>
          <label>
            SIN: 
            <input type="text" id="sin" required></input>
          </label>
          <label>
            Phone number: 
            <input type="text" id="phone" required></input>
          </label>
          <label>
            Number of Occupants: 
            <input type="number" id="occupants" min="1" max={maxOccupants} required></input>
          </label>
          <label>
            Date: 
            <input type="date" id="date" required></input>
          </label>
          <button type="Submit" className="bookRoomSubmit">Book room</button>
        </form>
      </div>
    )
  }

  componentDidMount(){
    this.update();
  }
  
  render() {
    let content = <div></div>
    if(this.state.loading){
      content = (
        <div>
          Loading...
        </div>
      )
    } else{
      content = this.state.content;
    }
    let bookingForm = <div></div>;
    if(this.state.book){
      bookingForm = this.getBookingElement();
    }
    return (
      <div className="container">
        <h1>Customer</h1>
        {content}
        {bookingForm}
      </div>
      
    );
  }
}
export default Customer;