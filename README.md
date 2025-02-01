# ArtGrid

ArtGrid is a command-line tool for macOS that converts images to pixel art. It features customizable pixel sizes and color palettes, making it perfect for creating retro-style graphics or preparing sprites for pixel art games.

![ArtGrid Banner](screen2.png)

## Features

- Convert any image to pixel art while maintaining aspect ratio
- Customizable pixel size for different levels of pixelation
- Adjustable color palette size for that authentic retro look
- Support for common image formats (PNG, JPG, JPEG, GIF)
- Simple command-line interface
- Handles transparency in PNG images

## Installation

### Prerequisites

- Python 3.6 or higher
- pip (Python package installer)

### Steps

1. Clone the repository:
```bash
git clone https://github.com/makalin/ArtGrid.git
cd ArtGrid
```

2. Install the required dependencies:
```bash
pip install Pillow
```

3. Make the script executable:
```bash
chmod +x artgrid.py
```

## Usage

Basic usage:
```bash
./artgrid.py input_image.jpg
```

### Options

- `-o, --output`: Specify output file path
- `-p, --pixel-size`: Set pixel size (default: 32)
- `-c, --colors`: Set number of colors in palette (default: 16)

### Examples

Convert an image with default settings:
```bash
./artgrid.py my_photo.jpg
```

Specify an output file:
```bash
./artgrid.py my_photo.jpg -o pixelated.png
```

Create highly pixelated art with limited colors:
```bash
./artgrid.py my_photo.jpg -p 64 -c 8
```

## Examples

| Original | Pixelated (32px) | Pixelated (16px) |
|----------|------------------|------------------|
| [Original Image] | [32px Example] | [16px Example] |

## How It Works

ArtGrid uses a two-step process to create pixel art:

1. **Downscaling**: The image is first reduced to a smaller size using the Lanczos algorithm for high-quality results.
2. **Upscaling**: The image is then scaled back up using nearest-neighbor interpolation to create sharp, distinct pixels.
3. **Color Reduction**: Finally, the color palette is reduced using adaptive color quantization.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Pillow (PIL Fork) library for image processing
- Inspired by classic pixel art from retro games

## Support

If you encounter any problems or have suggestions, please [open an issue](https://github.com/makalin/artgrid/issues) on GitHub.

## Future Plans

- [ ] Add custom color palette support
- [ ] Implement dithering options
- [ ] Add batch processing for multiple images
- [ ] Create a simple GUI interface
- [ ] Add animation support for GIFs
