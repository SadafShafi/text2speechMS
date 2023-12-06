from flask import Flask, request, jsonify, send_file
import io
from Text2Speech import Text2Speech
from unittest.mock import patch

app = Flask(__name__)

# Initialize the Text2Speech instance
text_to_speech = None


@app.route('/initialize_tts', methods=['POST'])
def initialize_tts():
    try:
        global text_to_speech

        # Check if the global instance already exists
        if text_to_speech is not None:
            return jsonify({'status': 'success', 'message': 'Text2Speech is already initialized'})

        # Handle the incoming audio file
        audio_file = request.files['file']
        temp_audio_path = 'temp_audio.wav'
        audio_file.save(temp_audio_path)

        # Use unittest.mock to simulate 'y' input during initialization
        with patch('builtins.input', return_value='y'):
            text_to_speech = Text2Speech(referenceAudiopth=temp_audio_path)

        return jsonify({'status': 'success', 'message': 'Text2Speech clone ready'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})


@app.route('/generate_audio', methods=['GET'])
def generate_audio():
   try:
        global text_to_speech

        # Check if Text2Speech is initialized
        if text_to_speech is None:
            return jsonify({'status': 'error', 'message': 'Text2Speech is not initialized'})

        # Handle the incoming text for audio generation
        text = request.args.get('text')
        generated_audio_path = text_to_speech.t2s(text)

        # Return the audio file as a response
        return send_file(generated_audio_path, mimetype='audio/wav', as_attachment=True, download_name='generated_audio.wav')

   except Exception as e:
       return jsonify({'status': 'error', 'message': str(e)})


if __name__ == '__main__':
    app.run(debug=True)

