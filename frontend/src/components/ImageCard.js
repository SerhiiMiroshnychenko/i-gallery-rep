import React from 'react';
import { Card, Button } from 'react-bootstrap';

const ImageCard = ({ image, deleteImage }) => {
  try {
    return (
      <Card style={{ width: '18rem' }}>
        <Card.Img variant="top" src={image.urls.small} />
        <Card.Body>
          <Card.Title>{image.title?.toUpperCase()}</Card.Title>
          <Card.Text>{image.description || image.alt_description}</Card.Text>
          <Button variant="primary" onClick={() => deleteImage(image.id)}>
            Delete
          </Button>
        </Card.Body>
      </Card>
    );
  } catch (error) {
    console.error(error);
    return (
      <Card style={{ width: '18rem' }}>
        <Card.Body>
          <Card.Title>ERROR</Card.Title>
          <Card.Text>Картинка не знайдена</Card.Text>
          <Button variant="warning" onClick={() => deleteImage(image.id)}>
            Delete
          </Button>
        </Card.Body>
      </Card>
    );
  }
};

export default ImageCard;
