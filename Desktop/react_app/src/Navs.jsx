import {Container,Nav, Navbar, Button, Card } from 'react-bootstrap';

function Navs(){
    return(
    <Navbar bg="dark" variant="dark">
        <Container>
        <Navbar.Brand href="#home">Math.edu</Navbar.Brand>
        <Nav className="me-auto">
          <Nav.Link href="#home">Home</Nav.Link>
          <Nav.Link href="#chatting">1:1채팅</Nav.Link>
          <Nav.Link href="/community">게시판</Nav.Link>
          <Nav.Link href="#show">영상과외</Nav.Link>
        </Nav>
        </Container>
      </Navbar>
    );
  }
  
  export default Navs;