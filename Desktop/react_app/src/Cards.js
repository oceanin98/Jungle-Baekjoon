
import {Container,Nav, Navbar, Button, Card } from 'react-bootstrap';
import axios from 'axios';

function Cards() {
  



    return (
      <Card>
      <Card.Header>Featured</Card.Header>
      <Card.Body>
        <Card.Title>Special title treatment</Card.Title>
        <Card.Text>
          With supporting text below as a natural lead-in to additional content.
        </Card.Text>
        <Button onClick={()=>{
      axios.get('https://codingapple1.github.io/shop/data2.json').then((결과)=>{
        console.log(결과.data)

      })
      .catch(()=>{
        console.log('실패함')
      })
    }}>버튼</Button> 
{/* ajax 데이터 가져옴 서버에서 가져온 데이터 */}

      </Card.Body>
    </Card>
    );
  }
  export default Cards;