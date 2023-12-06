import runpod
from Text2Speech import Text2Speech
import re
import gdown
import base64

def extract_file_id(link):
    # Try to find the file ID in the given Google Drive link
    match = re.search(r'/file/d/([a-zA-Z0-9_-]+)', link)
    if match:
        return match.group(1)
    else:
        print(f"Error: Unable to extract File ID from the link.")
        return None

def downloadAudio(link, output_file='temp_audio.wav'):
    file_id = extract_file_id(link)
    
    if file_id:
        download_url = f'https://drive.google.com/uc?id={file_id}'
        gdown.download(download_url, output_file, quiet=False)
        print(f'The audio file has been downloaded and saved as {output_file}')

def handler(event):
    '''
    This is the handler function that will be called by the serverless.
    '''
    # print(event)
    print("###***")
    # return "hello world, this just is pain in the ass"
    
    referenceFile = event["input"]["reference"]
    text = event["input"]["text"]
    temp_audio_path = 'temp_audio.wav'
    print("before audio download")

    # temp_audio_path = 'temp_audio.wav'
    # referenceFile.save(temp_audio_path)
    downloadAudio(referenceFile,temp_audio_path)
    print("After audio download")

    tts = Text2Speech(temp_audio_path)
    print("TTS init done")

    outputPath = tts.t2s(text)
    print("output attained")

    print(outputPath)
    # Load the output file content
    # try:
    output_content = ""
    with open(outputPath, 'rb') as output_file:
        output_content = output_file.read()
    data_to_serialize = base64.b64encode(output_content).decode('utf-8')
    # except Exception as e:
        # return f"Error loading output file: {str(e)}"
    print("File read")
    return data_to_serialize
    
runpod.serverless.start({"handler": handler})
# {
#   "input": {
#     "reference": "https://drive.google.com/file/d/16aCs0MaIqtLGH7lpkHT97JXAxX8oEg9A/view?usp=sharing",
#     "text":"H, how are you ?"

#   }
# }
# mydockersadaf/tts_runpod:0.4