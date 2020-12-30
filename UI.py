import PySimpleGUI as gui
from PIL import Image
import imager

print("UI Loaded")

#initialize global var window with no content
window = gui.Window('Loading Screen', [[]], location=(0, 0))

#create layout for UI

#two images side by side
#text var and crop vars
#save button
normalImageEl = gui.Image('images\\blankWhite.png', size=(600, 600))
editedImageEl = gui.Image('images\\blankBlack.png', size=(600, 600))
layout = [
    [normalImageEl, editedImageEl], 
    [gui.InputText('Add text to image', key='textImage', size=(25, 240)),  gui.InputText('left crop', key='leftCrop', size=(25, 240)),  gui.InputText('right crop', key='rightCrop', size=(25, 240)), gui.InputText('top crop', key='topCrop', size=(25, 240)), gui.InputText('bottom crop', key='bottomCrop', size=(25, 240)), gui.InputText('font size', key='fontSize', size=(25, 50))],
    [gui.Input(key='chosenFile',  change_submits=True), gui.FileBrowse('Choose image'), gui.Button('Submit image'), gui.Button('Edit')], 
    [gui.Input(key='chosenFolder',  change_submits=True), gui.FolderBrowse('Choose folder'), gui.Button('Save')]
    ]

def loadUI ():
    gui.theme('darkAmber')
    global window 
    window = gui.Window('Image Editor', layout, size=(1300, 700), location=(0, 0))
    while True:
        event, values = window.read()
        if event == gui.WIN_CLOSED : 
            break
        elif event == 'Submit image':
            imager.loadImage(values['chosenFile'], 'normal')
            normalImageEl.update('images\\normal.png')
        elif event == 'Edit' :
            imager.edit(values['chosenFile'], values['textImage'],
                        int(values['leftCrop']), int(values['rightCrop']), int(
                            values['topCrop']), int(values['bottomCrop']), int(values['fontSize']))
            imager.loadImage('images\\edited.png', 'editedThumbnail')
            editedImageEl.update('images\\editedThumbnail.png')
        elif event == 'Save':
            imager.saveImage(values['chosenFolder'], values['textImage'])
            
