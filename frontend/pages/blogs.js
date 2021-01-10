import React from 'react';
import Navigation from '../components/Nav'
import { Container, Row, Col } from 'react-bootstrap';

export default function blogs({posts}){
    return (
        <div>
            <Navigation></Navigation>
            <Container>
                {posts.map((post) => (
                    <Row>
                        <Col md='6'>
                            <img/>
                        </Col>
                        <Col md='6'>
                            <h1>{post.title}</h1>
                            <div className="" dangerouslySetInnerHTML={{__html: post.discription}}></div>
                            <p>{post.category}</p>
                        </Col>
                    </Row>
                ))}
            </Container>
        </div>
    )
}


export async function getStaticProps() {
    const res = await fetch('http://localhost:8000/blogs-api/')
    const posts = await res.json()

    console.log(posts)
    
    return {
      props: {
        posts,
      },
    }
}