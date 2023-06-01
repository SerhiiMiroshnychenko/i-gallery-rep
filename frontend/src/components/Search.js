import React from "react";
import { Container, Row, Col, Form, Button } from "react-bootstrap";

const Search = () => {
  return (
    <Container className="mt-4">
      <Row className="justify-content-center">
        <Col xs={12} md={8}>
          <Form>
            <Row>
              <Col xs={8}>
                <Form.Control placeholder="Пошук нового зображення..." />
              </Col>
              <Col>
                <Button variant="primary" type="submit">ПОШУК</Button>
              </Col>
            </Row>
          </Form>
        </Col>
      </Row>
    </Container>
  );
};

export default Search;
