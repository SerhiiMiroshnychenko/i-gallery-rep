import React from 'react';
import { Navbar, Container } from 'react-bootstrap';
import { ReactComponent as Logo } from '../images/logo.svg';

const navbarStyle = {
  backgroundColor: 'steelblue',
  color: 'lightblue',
  fontSize: '1.25rem',
  fontStyle: 'italic',
  fontWeight: 'bold',
};

const Header = ({ title }) => {
  return (
    <Navbar style={navbarStyle} variant="light">
      <Container>
        <Logo alt={title} style={{ maxWidth: '20rem', maxHeight: '4rem' }} />
        by Serhii Miroshnychenko
      </Container>
    </Navbar>
  );
};

export default Header;
