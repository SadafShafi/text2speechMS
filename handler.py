import runpod
from Text2Speech import Text2Speech
import base64

def handler(event):
    '''
    This is the handler function that will be called by the serverless.
    '''
    # print(event)
    print("###***")
    # return "hello world, this just is pain in the ass"
    
    prompt = event["input"]["prompt"]
    language = event["input"]["language"]
    speaker = event["input"]["speaker"]

    temp_audio_path = 'temp_audio.wav'
    
    print("before audio download")

    tts = Text2Speech(prompt = prompt,speaker = speaker,language = language)
    print("TTS init done")

    outputPath = tts.t2s()
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
#     "prompt": "Hello There, How are you?",
#     "speaker":"male-en-2",
#     "language":"en"
    

#   }
# }
