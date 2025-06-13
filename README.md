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

## Prerequisites

- Git
- Python 3.10+
  - python3-pip
  - python3-venv

## Setup

1. Create an account and get a free API key from [weatherapi.com](https://www.weatherapi.com). This is required for the Local Weather & Temperature feature.
2. Download the [scripts](scripts).
3. Run [setup.sh](sripts/setup.sh) and follow its instructions.
4. Prepare your Weekly Announcements within a DOCX file.
5. Make a slideshow with the dimensions 1920x810px for the Club Advertisements and export it as a PDF document. Each slide should be placed on a separate page.

> [!NOTE]  
> To change the Weekly Announcements or Club Advertisements on screen, simply insert your new DOCX file and PDF document into the "documents" folder. Highland Highlights will update its display with your new documents automatically without a restart.

## Usage

- To run Highland Highlights, run [run.sh](scripts/run.sh).
- To restore/repair Highland Highlights, run [setup.sh](scripts/setup.sh) again.

## Customization

To customize Highland Highlights, modify the values of the constants in [settings.py](src/settings.py).

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
