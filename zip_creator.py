import zipfile
import pathlib


def make_archive(filepaths, dest_dir):
    dest_path = pathlib.Path(dest_dir, "compressed.zip")
    with zipfile.ZipFile(dest_path, 'w') as archive:
        for fp in filepaths:
            # print('raw:', fp)
            # print('parsed:', pathlib.Path(fp))
            fp = pathlib.Path(fp)
            archive.write(fp, arcname=fp.name)


if __name__ == "__main__":
    dest_path = pathlib.Path('dest', "compressed.zip")
    print('dest_path', dest_path)
    make_archive(filepaths=['dest/a.txt', 'dest/b.txt', 'dest/c.txt'], dest_dir='dest')
