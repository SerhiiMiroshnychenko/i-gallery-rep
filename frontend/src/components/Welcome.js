import React from 'react';
import { Jumbotron, Button } from 'react-bootstrap';

const jumbotronStyle = {
  backgroundColor: 'aliceblue',
  color: 'steelblue',
  fontSize: '1.25rem',
  display: 'flex',
  flexDirection: 'column',
  alignItems: 'center',
  justifyContent: 'center',
  textAlign: 'center',
};

const buttonContainerStyle = {
  display: 'flex',
  justifyContent: 'center',
};

const buttonStyle = {
  margin: '10px',
};

const headingStyleBottom = {
  marginBottom: '50px',
};

const headingStyleTop = {
  marginTop: '25px',
};

const Welcome = () => (
  <Jumbotron style={jumbotronStyle}>
    <h3 style={headingStyleBottom}>
      <i>
        <b>I - gallery</b>
      </i>
    </h3>
    <p>Це простий додаток, який отримує фотографії за допомогою Unspash API.</p>
    <p>Щоб почати, введіть будь-який пошуковий термін у поле пошуку.</p>
    <div>
      <h5 style={headingStyleTop}>
        <i>
          <b>Контакти:</b>
        </i>
      </h5>
      <div style={buttonContainerStyle}>
        <p>
          <Button
            variant="primary"
            href="https://github.com/SerhiiMiroshnychenko/i-gallery-rep"
            target="_blank"
            style={buttonStyle}
          >
            GitHub додатку
          </Button>
          <Button
            variant="primary"
            href="https://www.linkedin.com/in/serhii-miroshnychenko-mariupol/"
            target="_blank"
            style={buttonStyle}
          >
            LinkedIn автора
          </Button>
        </p>
      </div>
    </div>
  </Jumbotron>
);

export default Welcome;
