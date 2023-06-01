import React from "react";
import { Container, Row, Col, Form, Button } from "react-bootstrap";

const Search = () => {
  return (
    <Container>
      <Row>
        <Col>
          <Form>
            <Row>
              <Col>
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
