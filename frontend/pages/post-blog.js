import React, {useState} from 'react';
import  { Redirect } from 'react-router-dom';
import { Container, Form, Row, Col, Button } from 'react-bootstrap';

export default function postBlog({author}){

    const [title, setTitle] = useState('')
    const [description, setDescription] = useState('')
    const [authorid, setAuthorid] = useState('')
    console.log(authorid)

    const postBlog = async (e) =>{
        e.preventDefault()
        try {
            const postres = await fetch('http://localhost:8000/blogs-api/', {
                method: 'post',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    title: title,
                    description: description,
                    authorId: authorid 
                })
            })

            if (postres.status === 200) {
                return <Redirect to='/blogs'  />
            } else {
                alert('Sorry, something went wrong.')
            }
            
        }catch(err) { 

        }
    }

    return(
        <div>
            <Container>
                <Form className="py-3 my-3">
                    <Row className="my-3">
                        <Col>
                            <Form.Control id="title" name="title" placeholder="Title" value={title} onChange={e => setTitle(e.target.value)}/>
                        </Col>
                    </Row>
                    <Row className="my-3">    
                        <Col>
                        <Form.Control id="authorId" as="select" name="authorId" value={authorid} onChange={e => setAuthorid(e.target.value)}>
                            <option key='select' >-- Select Author --</option>
                            {author.map((author) => (
                                <option key={author.authorId} value={author.authorId}>{author.name}</option>
                            ))}
                        </Form.Control>
                        </Col>
                    </Row>
                    <Row className="my-3">    
                        <Col>
                            <Form.Control value={description} onChange={e => setDescription(e.target.value)} id="description" name="description" as="textarea" rows={3} placeholder="Description"/>
                        </Col>
                    </Row>
                    <Row>
                        <Col>
                            <Button variant="primary" type="submit" onClick={postBlog}>
                                Submit
                            </Button>
                        </Col>
                    </Row>
                </Form>
            </Container>
        </div>
    )
}



export async function getStaticProps() {
    const res = await fetch('http://localhost:8000/author-api/')
    const author = await res.json()

    return {
      props: {
        author,
      },
    }
}


