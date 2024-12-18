# YouTube Video Downloader

## Overview

A simple Python-based YouTube video and audio downloader that allows you to easily download YouTube videos in MP4 or MP3 format.

## Features

- Download YouTube videos in MP4 format
- Extract audio and save as MP3
- Simple command-line interface
- Robust error handling
- Filename sanitization

## Prerequisites

- Python 3.7+
- pip (Python package manager)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Mwantech/youtube-video-downloader.git
cd youtube-video-downloader
```

2. Create a virtual environment (optional but recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

3. Install required dependencies:
```bash
pip install -r requirements.txt
```

## Requirements File (requirements.txt)
```
pytube
requests
```

## Usage

Run the script and follow the prompts:

```bash
python youtubedownloader.py
```

1. When prompted, paste the YouTube video link
2. Choose the download format (mp4 or mp3)

### Example
```
Welcome to the YouTube Downloader!
Paste the YouTube video link: https://youtu.be/example-video
Choose format to download (mp4/mp3): mp4
```

## Troubleshooting

- Ensure you have a stable internet connection
- Verify the video is publicly accessible
- Update pytube to the latest version if issues persist

## Known Limitations

- Some protected or region-restricted videos may not download
- Requires periodic updates due to YouTube's changing website structure

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Disclaimer

This tool is for personal and educational purposes. Always respect YouTube's terms of service and copyright regulations.

## Contact

Your Name - mwantech005@gmail.com

Project Link: [https://github.com/Mwantech/youtube-video-downloader](https://github.com/Mwantech/youtube-video-downloader)