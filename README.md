# MemoryMuppets

MemoryMuppets is a straightforward, yet entertaining, memory game based on The Muppets.
Please, remember to turn on the sound in your device to have better user experience.

<p align="center">
  <img src="/img/memorymuppets.PNG">
</p>

## Getting Started & Installing

Please, either clone the repository or use incuded tar/wheels.

### For playing

* go to [releases](https://github.com/harper25/MemoryMuppets/releases) and download a last release
* create a virtual environment for the game (ex. `virtualenv .venv`) and activate it
* run `pip install <last-release-name>`
* run `python -m memorymuppets`
* have fun!

### For development

The project was developed with [Poetry](https://poetry.eustace.io/). Therefore you have to:

* install Poetry: [GitHub](https://github.com/sdispater/poetry)
* git clone the repository
* create a virtual environment for development (ex. `virtualenv .venv`) and activate it
* cd to main folder and run: `poetry update` to get all dependencies from `pyproject.toml` installed to your virtual environment
* run `python -m memorymuppets`
* modify and have fun!

The project uses common Python packages. No special prerequisites required.

Build your own resources:

`pyside2-rcc -o memorymuppets/resources.py resources.qrc`

Build app with pyinstaller:

`pyinstaller --onefile --windowed --version-file file_version_info.txt --name MemoryMuppets memorymuppets/__main__.py`

## Authors

* [harper25](https://github.com/harper25)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgments

Thanks to:

* [Miroslaw Zelent](https://miroslawzelent.pl/) for inspiration
* [PurpleBooth](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2) for a Readme template

## Sources

Idea & sounds:
* [Miroslaw Zelent - C++](https://miroslawzelent.pl/kurs-obiektowy-c++/dzwieki-wav-mp3-wlasna-gra/)

Images:
* [background](https://www.ravelry.com/patterns/library/yip-yips-crochet/slideshow?fullscreen=1&start=80427358)
* [icon](https://www.google.com/imgres?imgurl=http%3A%2F%2Fwdmpi-0.vo.llnwd.net%2Fd1%2FthemuppetsDatastore%2Fresponsivesite%2Fimages%2Ficons-avatars%2Fanimal-icon-125x125.jpg&imgrefurl=http%3A%2F%2Fwdmpi-0.vo.llnwd.net%2Fd1%2FthemuppetsDatastore%2Fresponsivesite%2Fdownloads.html&docid=p8O7kJPYb7XhPM&tbnid=1d1-vVRZhzp5AM%3A&vet=12ahUKEwiP7MeM7priAhUDEVAKHRZvC3c4yAEQMygSMBJ6BAgBEBM..i&w=125&h=125&bih=946&biw=1920&q=icon%20muppet&ved=2ahUKEwiP7MeM7priAhUDEVAKHRZvC3c4yAEQMygSMBJ6BAgBEBM&iact=mrc&uact=8#h=125&imgdii=1d1-vVRZhzp5AM:&vet=12ahUKEwiP7MeM7priAhUDEVAKHRZvC3c4yAEQMygSMBJ6BAgBEBM..i&w=125)
* buzzer based on: [buzzer](http://chittagongit.com/icon/buzzer-icon-16.html)
