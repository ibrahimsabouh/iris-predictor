# Iris Flower Predictor

A machine learning web application that predicts Iris flower species based on flower measurements. Built with FastAPI, scikit-learn, and Docker.

## Features

- Machine learning model trained on the classic Iris dataset
- Clean and intuitive web interface
- Real-time predictions with confidence scores
- Containerized application for easy deployment

## Tech Stack

- FastAPI (Backend & API)
- scikit-learn (Machine Learning)
- HTML/JavaScript (Frontend)
- Tailwind CSS (Styling)
- Docker (Containerization)

## Quick Start

### Running Locally with Docker

1. Clone the repository:
```bash
git clone https://github.com/ibrahimsabouh/iris-predictor.git
cd iris-predictor
```

2. Build and run with Docker Compose:
```bash
docker-compose up --build
```

3. Access the application at `http://localhost:8000`

### Running with Docker Hub Image

```bash
docker pull ibrahimsabouh/iris-predictor
docker run -p 8000:8000 ibrahimsabouh/iris-predictor
```

## Usage

1. Open the web interface at `http://localhost:8000`
2. Enter the following measurements:
   - Sepal Length
   - Sepal Width
   - Petal Length
   - Petal Width
3. Click "Predict" to see the results

## Project Structure

```
.
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
└── app
    ├── main.py          # FastAPI application
    ├── model.py         # Data models
    ├── train.py         # ML model training
    └── templates
        └── index.html   # Frontend interface
```

## Development

To modify the project:

1. Clone the repository
2. Make your changes
3. Rebuild the Docker container:
```bash
docker-compose up --build
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

MIT License
