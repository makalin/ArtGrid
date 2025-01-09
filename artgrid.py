#!/usr/bin/env python3

import argparse
import os
from PIL import Image

class ArtGrid:
    def __init__(self, pixel_size=32, palette_size=16):
        self.pixel_size = pixel_size
        self.palette_size = palette_size

    def reduce_colors(self, image):
        """Reduce the number of colors in the image."""
        # Convert to RGB if image is in RGBA
        if image.mode == 'RGBA':
            background = Image.new('RGB', image.size, (255, 255, 255))
            background.paste(image, mask=image.split()[3])
            image = background

        # Convert to P mode with limited palette
        return image.convert('P', palette=Image.Palette.ADAPTIVE, colors=self.palette_size)

    def pixelize(self, input_path, output_path):
        """Convert image to pixel art."""
        try:
            # Open and verify the image
            with Image.open(input_path) as img:
                # Calculate new dimensions
                width = img.size[0]
                height = img.size[1]
                
                # Calculate new dimensions based on pixel size
                new_width = width // self.pixel_size
                new_height = height // self.pixel_size

                # Resize down and back up to create pixel effect
                small = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
                result = small.resize((width, height), Image.Resampling.NEAREST)

                # Reduce colors
                result = self.reduce_colors(result)

                # Save the result
                result.save(output_path)
                print(f"Successfully converted {input_path} to pixel art!")
                return True

        except Exception as e:
            print(f"Error processing image: {str(e)}")
            return False

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description='Convert images to pixel art')
    parser.add_argument('input', help='Input image path')
    parser.add_argument('-o', '--output', help='Output image path')
    parser.add_argument('-p', '--pixel-size', type=int, default=32,
                        help='Pixel size (default: 32)')
    parser.add_argument('-c', '--colors', type=int, default=16,
                        help='Number of colors in palette (default: 16)')

    args = parser.parse_args()

    # Generate output path if not specified
    if not args.output:
        filename, ext = os.path.splitext(args.input)
        args.output = f"{filename}_pixel{ext}"

    # Create converter and process image
    converter = ArtGrid(args.pixel_size, args.colors)
    success = converter.pixelize(args.input, args.output)

    if not success:
        parser.print_help()
        exit(1)

if __name__ == "__main__":
    main()
