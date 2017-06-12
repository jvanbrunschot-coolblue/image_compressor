import os
import imghdr  # https://docs.python.org/3.5/library/imghdr.html
import click
from PIL import Image

supported_image_formats = ['jpeg', 'png']


def get_image_size(image_path):
    return os.stat(image_path).st_size


def compress_image(original_image_path, compressed_image_path, quality):
    raw_image = Image.open(original_image_path)
    raw_image.save(compressed_image_path, quality=quality, optimize=True)
    raw_image_size = get_image_size(original_image_path)
    compressed_image_size = get_image_size(compressed_image_path)
    compress_ratio = (raw_image_size / compressed_image_size)
    return 'Image: {} compressed {:.2f} times'.format(
        original_image_path,
        compress_ratio
    )


@click.command()
@click.option('--entrypoint', required=True, help='Full path to image directory')
@click.option('--output', default='compressed', help='Output directory')
@click.option('--quality', default=80, help='Quality of the compression')
@click.option('--force', default=False, help='Forces the application to compress already compressed files')
def cli(entrypoint, output, quality, force):
    absolute_entrypoint_path = os.path.abspath(entrypoint)
    for parent_dir, child_dir, files in os.walk(absolute_entrypoint_path):

        # Duplicate directory structure for compressed images
        if not os.path.exists(output + parent_dir):
            os.makedirs(output + parent_dir)

        # Iterate the files and check if they already exist and are in supported format
        for file in files:
            original_image_path = parent_dir + '/' + file
            compressed_image_path = output + parent_dir + '/' + file
            if imghdr.what(original_image_path) in supported_image_formats and \
               not os.path.isfile(compressed_image_path):
                print(compress_image(
                    original_image_path,
                    compressed_image_path,
                    quality
                ))


if __name__ == '__main__':
    cli()
