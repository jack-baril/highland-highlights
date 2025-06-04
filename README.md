<header align="center">
  <h1>
    <img src="assets/images/title.png" alt="Title">
  </h1>
  <img src="assets/images/screenshot.png" alt="Screenshot of Highland Highlights">
</header>

## About

<p><strong>Connecting us through the power of information.</strong></p>
Highland Highlights is a modern digital bulletin board application I made as a student at Highland, for Highland. Developed for the Raspberry Pi using the Qt for Python framework, it was designed to replace the old and outdated one on the TVs with a cleaner look and feel, together along with additional convenient features to better serve our community.

## Features

- **Digital Clock & Date:** Shows the current time and date
- **Local Weather & Temperature:** Provides real-time weather updates
- **Weekly Announcements:** Scrolls through important school news
- **Club Advertisements:** Promotes extracurricular activities in a slideshow format
- **Easy Updates:** Update weekly announcements via a DOCX file and club advertisements through a PDF file

## Getting Started

### Prerequisites

- Git
- Python 3.10+

### Download

1. In the terminal, clone the GitHub repository and navigate into its directory:

   ```bash
   git clone https://github.com/jack-baril/highland-highlights.git
   cd highland-highlights
   ```

2. Create and activate a virtual environment:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. Install the required packages and dependencies:

   ```bash
   python3 -m pip install -r requirements.txt
   ```

### Setup & Usage

1. Sign in and get a free API key from [WeatherAPI](https://www.weatherapi.com).
2. Enter your API key into [config.py](src/config.py) inside the quotation marks within the line shown below:

   ```python
   API_KEY = ""
   ```

3. Prepare your Weekly Announcements within a DOCX file.
4. Make a slideshow in your software of choice with the dimensions 1920x810px for the Club Advertisements, placing each on a separate page of the PDF document.
5. Create a folder inside the "assets" folder and name it "documents."
6. Put both your DOCX file and PDF document into the "documents" folder.
7. Run [main.py](src/main.py):

   ```bash
   python3 main.py
   ```

> [!NOTE]  
> To update the Weekly announcements or Club Advertisements on screen, insert your new DOCX file and PDF document into the "documents" folder. The application will then update its display with your new documents automatically without a restart.

## Configuration & Customization

To configure and customize the application, modify the values of the constants in the following files:

| File                          | Description                                                      |
| ----------------------------- | ---------------------------------------------------------------- |
| [config.py](src/config.py)    | Contains settings that control the behavior of the application   |
| [styles.py](src/ui/styles.py) | Contains settings that control the appearance of the application |

> [!NOTE]
> Intervals are measured in milliseconds. Sizes, widths, and heights are measured in pixels.

## License

Copyright (c) 2025 Jack Baril  
Highland Highlights is licensed under the [MIT License](LICENSE.txt).

## Author

<a href="https://github.com/jack-baril/highland-highlights/graphs/contributors">
   <img src="https://contrib.rocks/image?repo=jack-baril/highland-highlights" />
</a>

## Contact

Email: [jack.r.baril@gmail.com](mailto:jack.r.baril@gmail.com)
