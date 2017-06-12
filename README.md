## Image compressor

A simple tool written in Python3 to compress a given directory tree. Currently only `jpeg` and `png` are supported image formats.
Default compression ratio is 80%.

### Usage

`python app.py --help`

The tool works with both absolute as non-absolute paths

`python app.py --entrypoint /Users/example/Picures`  
`python app.py --entrypoint ~/Picures`  
`python app.py --entrypoint Picures`  

Change compression ratio (default = 80)
`python app.py --entrypoint ~/Picures --quality 50`

Compress images are stored in `compressed/`

### TODO
- [ ] enable `force` option to recompress images
- [x] able to change output directory
- [ ] automatically archive compressed images to AWS S3 Glacier
