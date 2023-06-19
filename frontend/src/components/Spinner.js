import React from 'react';
import { Container, Button, Spinner as Loader } from 'react-bootstrap';

const containerStyle = {
  position: 'absolute',
  top: 'calc(40% - 2rem)',
  left: 'calc(40% - 1rem)',
};

const buttonStyle = {
  backgroundColor: 'SteelBlue',
  color: 'white',
  fontSize: '1.5rem',
};

const Spinner = () => {
  return (
    <Container style={containerStyle}>
      <Button style={buttonStyle} disabled>
        <Loader
          as="span"
          animation="border"
          variant="warning"
          role="status"
          aria-hidden="true"
        />
        Завантаження...
      </Button>
    </Container>
  );
};

export default Spinner;
