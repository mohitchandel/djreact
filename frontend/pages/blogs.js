import React from 'react';
import Navigation from '../components/Nav'
import { Container, Row, Col } from 'react-bootstrap';

export default function blogs({posts, author}){
    return (
        <div>
            <Navigation></Navigation>
            <Container>
                {posts.map((post) => (
                    <Row key="main-row">
                        <Col key="main-col">
                            <h2 key={post.Id}>{post.title}</h2>
                            <div key="desc" className="" >{post.description}</div>
                            {author.map((author) => (
                                author.authorId == post.authorId ? <p key={author.authorId} value={author.Id}>{author.name}</p> : <p key=""></p>
                            ))}
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
    
    const authores = await fetch('http://localhost:8000/author-api/')
    const author = await authores.json()

    return {
      props: {
        posts,
        author
      },
    }
}