import React from "react";
import { Container, Row, Col, Form, Button } from "react-bootstrap";

const Search = ({handleSubmit}) => {
  return (
    <Container className="mt-4">
      <Row className="justify-content-center">
        <Col xs={12} md={8}>
          <Form onSubmit={handleSubmit}>
            <Form.Row>
              <Col xs={8}>
                <Form.Control placeholder="Пошук нового зображення..." />
              </Col>
              <Col>
                <Button variant="primary" type="submit">ПОШУК</Button>
              </Col>
            </Form.Row>
          </Form>
        </Col>
      </Row>
    </Container>
  );
};

export default Search;
