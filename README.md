# AlvExif
This is a program meant to automate the task of outputing the details of the EXIF data through a CLI-interface.

### Future features

- Capability to remove certain EXIF tags
- Capability to select the precise picture you want to remove the tag from
- Remove a tag from all selected pictures or inside a folder
- Read all common tags from all selected pictures

#### Disclaimer

You'll need to install `Pillow` library on `pip` for this program to run.

```
pip install Pillow
```

####

In order to run this thing you'll have to run

```
py main.py
```

It will process the picture added, which has been edited with `exiftool` to add metadata, you'll see that all metadata added will show up on the outuput once you add it there.