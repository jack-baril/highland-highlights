<header align="center">
  <h1>
    <img src="assets/img/title.png" alt="Title">
  </h1>
  <img src="assets/img/screenshot.png" alt="Screenshot of Highland Highlights">
</header>

## About

**Connecting us together through the power of information.**

Highland Highlights is a digital signage application I developed as a student at Highland. Built for the Raspberry Pi using the Qt for Python framework, it was designed to replace the outdated TV system with a more modern look and feel, along with additional convenient [features](#features) to better serve our community.

## Features

- **Digital Clock & Date:** Shows the current time and date
- **Local Weather & Temperature:** Provides real-time weather updates
- **Weekly Announcements:** Scrolls through school news
- **Club Advertisements:** Promotes extracurricular activities in a slideshow format

## Prerequisites

- Git
- Python 3.10+

## Setup

1. Create an account and get a free API key from [weatherapi.com](https://www.weatherapi.com). This is needed for the Local Weather & Temperature feature.
2. Clone Highland Highlights.
3. Run [setup.sh](sripts/setup.sh) in the terminal and follow its instructions.
4. Download the Weekly Announcements Microsoft Word file shared with you by Desiree Chavez from your Google Drive.
5. Prepare a slideshow with the dimensions 1920x810px for the Club Advertisements and export it as a PDF document. Each slide should be placed on a separate page.
6. Put the Microsoft Word and PDF files into the "documents" folder inside `highland-highlights/assets`.

## Usage

- To run Highland Highlights, run [run.sh](scripts/run.sh).
- To change the Weekly Announcements or Club Advertisements on screen, insert your new Microsoft Word file and PDF document into the documents folder. The display will update automatically without a restart of the application.

## Customization

To customize the appearance and behavior of Highland Highlights, modify the values of the constants in [config.py](highland-highlights/config.py).

> [!NOTE]
> Sizes, widths, heights, and spacing are measured in pixels; intervals are measured in milliseconds.
