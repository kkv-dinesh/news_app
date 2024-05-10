

# News App

This project consists of a web application and a React component for displaying the latest news headlines fetched from the News API.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Setup](#setup)
- [Usage](#usage)
- [Dependencies](#dependencies)
- [Contributing](#contributing)
- [License](#license)

## Overview

The News App provides a simple interface to view the latest news headlines from various sources. It includes a Streamlit-based Python application for the web and a React component for integration into web pages.

## Features

- Fetches and displays the latest news headlines from the News API.
- Displays headlines with details such as title, source, and publication date.
- Caches data for 1 hour to improve performance using Streamlit's caching mechanism.
- Responsive layout for viewing headlines on different screen sizes.

## Setup

To set up the project, follow these steps:

1. Clone the repository:

   ```
   git clone <repository_url>
   ```

2. Navigate to the project directory:

   ```
   cd news_app
   ```

3. Install the necessary dependencies:

   ```
   pip install -r requirements.txt
   ```

4. Run the Streamlit web application:

   ```
   streamlit run news_app.py
   ```

5. Run the React component:

   ```
   npm install
   npm start
   ```

## Usage

Once the application is running, you can view the latest news headlines by visiting the provided URL for the Streamlit web application. For the React component, you can integrate it into your web page by importing and using the `NewsComponent` as needed.

## Dependencies

- **Streamlit**: For building the web application in Python.
- **React**: For building the React component in JavaScript.
- **Axios**: For making HTTP requests in the React component.
- **Pandas**: For data manipulation in the Python application.

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests to contribute to the project.

## License

This project is licensed under the [MIT License](LICENSE).

