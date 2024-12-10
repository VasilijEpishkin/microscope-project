# Microscope Project
This project provides an interactive platform for exploring high-resolution tile-based images, emulating the experience of a digital microscope.

## Features
Tile-based Image Management: Efficiently handles large images by breaking them into smaller, manageable tiles for faster processing and viewing.
Zoom and Pan: Allows users to zoom in on detailed areas and pan across images, ideal for exploring microscopic details.
Image Stitching: Combines multiple tiles into a coherent, seamless high-resolution image for comprehensive analysis.
Interactive Interface: A user-friendly interface for navigating complex image data with options for annotating or measuring.
Real-time Rendering: Quickly loads and renders high-resolution image tiles for a smooth viewing experience.
Customizable Layers: Users can overlay different layers of data (e.g., staining, annotations) on the image tiles for enhanced analysis.
## Getting Started
### Prerequisites
Python 3.8+
Docker
Docker Compose
## Installation
1. Clone the repository:
git clone https://github.com/VasilijEpishkin/microscope-project.git
2. Navigate to the project directory:
cd microscope-project
3. Install dependencies:
pip install -r requirements.txt
## Running the Application
1. Build and start the application using Docker Compose:
docker-compose up --build
2. Access the application in your web browser at http://localhost.
## File Structure
manage.py - Entry point for the application.
Dockerfile - Configuration for containerizing the application.
docker-compose.yml - Orchestrates multi-container setup.
requirements.txt - Lists project dependencies.

License
This project is licensed under the MIT License. See LICENSE for details.

