import PySimpleGUI as sg
from zip_creator import make_archive

sg.theme("LightGreen5")

select_file_label = sg.Text('Select file(s) to compress:')
select_file_input = sg.Input(key='file_input')
choose_file_button = sg.FilesBrowse('Choose', key='files', tooltip='Choose file(s) to be included in the archive',
                                    target='file_input')

select_dest_label = sg.Text('Select destination folder:')
select_dest_input = sg.Input(key='dest_input')
choose_dest_button = sg.FolderBrowse('Choose', key='folder',
                                     tooltip='Choose destination folder in which the archive will be created',
                                     target='dest_input')

left_col = sg.Column([[select_file_label], [select_dest_label]])
mid_col = sg.Column([[select_file_input], [select_dest_input]])
right_col = sg.Column([[choose_file_button], [choose_dest_button]])

compress_button = sg.Button('Compress')
output_label = sg.Text(key='output', text_color='green')

window = sg.Window('File(s) Archive Maker',
                   layout=[
                       [left_col, mid_col, right_col],
                       [compress_button, output_label]
                   ])
while True:
    event, values = window.read()
    print(event, values)
    try:
        filepaths = values['files'].split(';')
        folder = values['folder']
        try:
            make_archive(filepaths=filepaths, dest_dir=folder)
            window['output'].update(value='Compression succeeded!')
        except:
            print('Failed to create an archive.')
    except:
        print('Failed to create an archive.')

    match event:
        case sg.WINDOW_CLOSED:
            print('Thanks for choosing us, shutting down...')
            break

window.close()
