# Whisper Audio Transcriber

A Python script for transcribing `.wav` audio files in the current directory using OpenAI's Whisper model. This tool automatically converts selected audio files into text and saves the transcription to a file.

## Features
- Lists all `.wav` files in the current directory.
- Allows user selection of a specific audio file for transcription.
- Transcribes the selected file and saves the text output to `transcription.txt`.

## Prerequisites
- **Python 3.7+** required.
- **Whisper** by OpenAI. Install it via pip:

  ```bash
  pip install -U openai-whisper
  ```

## Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/its-cutie-valerie/whisper-audio-transcriber.git
   cd whisper-audio-transcriber
   ```

2. Place your `.wav` files in the same directory as the script.

3. Run the script:

   ```bash
   python transcribe.py
   ```

4. Follow the on-screen instructions to select the file to transcribe. The script will display all `.wav` files in the directory with an index to select from:

   ```
   Available .wav files:
   0: audio_sample1.wav
   1: audio_sample2.wav
   Enter the index of the file to transcribe:
   ```

5. The transcription will be saved to `transcription.txt` in the same directory.

## Example Output

```plaintext
Transcribing audio file: /path/to/your/audio_sample.wav
Transcription saved to transcription.txt
```

## Notes
Ensure you have the `.wav` files you wish to transcribe in the same directory as the script. This script uses OpenAI's Whisper `base` model; other models can be substituted by modifying the script.

