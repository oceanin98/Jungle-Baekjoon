import logo from './logo.svg';
import './App.css';
import { useState } from 'react';
import { useEffect } from 'react';

import 'bootstrap/dist/css/bootstrap.min.css';
import {Container,Nav, Navbar, Button, Card } from 'react-bootstrap';
import { Routes, Route, Link, useNavigate } from 'react-router-dom';
import Cards from './Cards';
import styled from 'styled-components';
import detail from './detail';
import Navs from './Navs';
import axios from 'axios';

//css파일 안쓰고 사용하기 
let Yellowbtn = styled.button`
  background: ${props => props.bg =='blue' ? 'white' : 'black'};
  color: black;
  padding: 10px;
  `
let Box = styled.div`
  padding: 20px;
  background: grey;
  `
  



function Header(props){

  useEffect(() => {
    console.log('useEffect')
  })
let [count, setCount] = useState(0);


  console.log('props',props,props.title);
  return <header>
    <h1>{props.title}</h1>
      <h4><a href="/">java</a></h4>

      {count} 
      <button onClick={()=>{setCount(count+1 )}}>👍좋아요</button>
      {/* //카운트와 아래 버튼 같이 사용해야함  */}

    </header>
}
function Top(props){
  
  const lis = []
  for (let i=0; i<props.topics.length; i++){
    let t = props.topics[i];
   
    lis.push(<li key={t.id}>
      <a id={t.id} href={'/read/'+t.id} onClick={event=>{
        event.preventDefault();
        props.onChangeMode(Number(event.target.id)); //문자를 숫자로 
      }}>{t.title}</a>
      </li>)
  }
  return <nav>
    <ol>{lis}</ol>
  </nav>
}

function Article(props){
  return <article>
    <h2>{props.title}</h2>
    <h3>{props.body}</h3>
  </article>
  
}

function Create(props){

return <article>
<h2>create</h2>
<form onSubmit={event=>{
  event.preventDefault();
  const title= event.target.title.value;
  const body= event.target.body.value;
  props.onCreate(title,body);
}}>
  <p><input type="text" name="title" placeholder="title"/></p>
  <p><textarea name="body" placeholder="body"></textarea></p>
  <p><input type= "submit" value="Create"></input></p>
 
  </form>
</article>

}

function Update(props){
  const[title, setTitle] = useState(props.title); //react hook
  const [body,setBody]= useState(props.body);
  return <article>
  <h2>Update</h2>
  <form onSubmit={event=>{
    event.preventDefault();
    const title= event.target.title.value;
    const body= event.target.body.value;
    props.onUpdate(title,body); //onUpdate를 호출하면서 title과 body를 전달
  }}>
    <p><input type="text" name="title" placeholder="title" value={title} onChange={event=>{
      console.log(event.target.value);
      setTitle(event.target.value); 
    }}/></p>
    <p><textarea name="body" placeholder="body" value={body} onChange={event=>{
      setBody(event.target.value);
    }}></textarea></p>
    <p><input type= "submit" value="Update"></input></p>
    </form>
  </article>
}

function App() {
  // const _mode = useState('WELCOME');
  // const mode = _mode[0];
  // const setMode = _mode[1];

  let [shoes] = useState()
  let navigate = useNavigate();
  
  const [ mode,setMode] = useState('WELCOME');
  const[id,  setId]= useState(null);
  const[nextId, setNextId]=useState(3);

  const [topics, setTopics]= useState([
    {id:1, title:'html', body:'html is ...'},
    {id:2, title:'css', body:'css is ...'}
  ]);
  let content = null;
  let contextControl = null; // 얘 없으면 왜 안나와?
  if (mode === 'WELCOME'){
    content =  <Article title="welcome" body="mode is welcome"></Article>
    }else if(mode === 'READ'){  //이게 뭔지 모르겠음
    let title, body= null;
    for (let i= 0; i<topics.length; i++){
      if(topics[i].id === id){
        title = topics[i].title;
        body = topics[i].body;
      }
    }

    content =  <Article title={title} body={body}></Article>
    contextControl = <>
    <li><a href={'/update/'+id} onClick={event=>{
      event.preventDefault();
      setMode('UPDATE');
    }}>Update</a></li>
    <li><input type="button" value="Delete" onClick={()=>{
      const newTopics = []
      for(let i=0; i<topics.length; i++){
        if(topics[i].id !== id){
            newTopics.push(topics[i]);
        }
      }
      setTopics(newTopics);
      setMode('WELCOME');
    }} /></li>
    </>
  } else if (mode ==='CREATE'){
    content = <Create onCreate={(_title, _body)=>{
      const newTopic = {id:nextId, title:_title, body:_body}
      const newTopics=[...topics]

      newTopics.push(newTopic);
      setTopics(newTopics);
      setMode('READ');
      setId(nextId);
      setNextId(nextId+1);
    }}></Create>
  }else if(mode === 'UPDATE'){
    let title, body= null;
    for (let i= 0; i<topics.length; i++){

      if(topics[i].id === id){
        title = topics[i].title;
        body = topics[i].body;
      }
    }
    content= <Update title={title} body ={body} onUpdate={(title, body)=>{
      const newTopics = [...topics]
      const updatedTopic= {id:id, title:title, body:body}
      for(let i=0; i<newTopics.length; i++){
        if(newTopics[i].id === id){
          newTopics[i]=updatedTopic;
          break;
        }
      }
      setTopics(newTopics);
      setMode('READ');
    }}></Update>
  }
  return (
    <div className="App">
      
       
    <Navs/>
    <div className="main-bg"></div>
   <Cards/>

  <Routes>
    <Route path="/community" element={
      <>
     <Header title="WEB" on ChangeMode={()=>{
      setMode('WELCOME');
      }}></Header>
      <Top topics={topics} onChangeMode={(_id)=>{
       setMode('READ');
       setId(_id);
      }}></Top>
      {content}
      <ul>
      <li><a href="/create" onClick={event=>{
       event.preventDefault();
       setMode('CREATE');
      }}>Create</a></li>
      {contextControl}
      </ul>
      </>
    }/>

  </Routes>
  <Box>
  <Yellowbtn bg="blue">qj</Yellowbtn>
  <Yellowbtn bg="orange">qj</Yellowbtn>
  </Box>
    </div>
  );
}


export default App;

