# <ins>Desktop Assistant SCAI - ReadMe</ins>
A comprehensive voice-controlled desktop assistant built with Python that responds to voice commands and automates various computer tasks through speech recognition and text-to-speech technology.

## 🚀 Features :-

- **_Voice Recognition_**: Responds to natural voice commands in English.
- **_Text-to-Speech_**: Provides audio feedback with customizable voice options.
- **_Web Automation_**: Opens websites, performs Google/YouTube searches.
- **_Application Control_**: Launches apps like VS Code, WhatsApp, Discord, Spotify, etc.
- **_System Management_**: Clears temp files, manages Recycle Bin.
- **_Email Integration_**: Automated email sending through Gmail.
- **_Music Control_**: Spotify playlist management and playback.
- **_Wikipedia Integration_**: Fetches and reads Wikipedia summaries.
- **_Time & Weather_**: Real-time information and weather reports.
- **_Sound Effects_**: Interactive audio feedback for enhanced user experience.

## 🛠️ Technologies Used :-

- **Python 3.6+**
- **_speech_recognition_** - Voice command processing
- **_pyttsx3_** - Text-to-speech conversion
- **_pyautogui_** - GUI automation and control
- **_webbrowser_** - Web browser automation
- **_wikipedia_** - Wikipedia API integration
- **_datetime_** - Time and date management
- **_winsound_** - Sound effects playback
- **os** - System operations

## 📋 Prerequisites :-

Before running SCAI, ensure you have:
- Python 3.6 or higher installed
- Working microphone for voice input
- Internet connection for web-based features
- Windows OS (for certain system-specific features)

## ⚡ Installation :-

1. **Clone the repository**
```bash
git clone https://github.com/pingakshgaur/Desktop-Assistant-SCAI.git
cd Desktop-Assistant-SCAI
```

2. **Install required packages**
```bash
pip install pyautogui
pip install pyttsx3
pip install speechrecognition
pip install wikipedia
pip install webbrowser
pip install pyaudio
```

3. **Setup microphone permissions** (if required by your OS)

## 🎯 Usage :-

1. **Run the assistant**
```bash
python scai-d.py
```

2. **Voice Commands Examples:**
   - _"Hey SCAI"_ - Basic greeting.
   - _"Open YouTube"_ - Opens YouTube in the default browser.
   - _"Search Google for Python tutorials"_ - Performs a Google search.
   - _"What's the time?"_ - Tells the current time.
   - _"Play my Spotify playlist"_ - Opens Spotify.
   - _"Tell me about Albert Einstein"_ - Wikipedia search.
   - _"Clear temporary files"_ - System cleanup.
   - _"Sleep for 30 seconds"_ - Pause assistant.
   - _"Exit"_ - Close the assistant.

## 📁 Project Structure :-

```
Desktop-Assistant-SCAI/
│
├── da-SCAI.py                   # Main assistant script
├── SFX/...                      # Sound effects folder
├── README.md                    # Project documentation
└── REQUIREMENTS.md              # Python dependencies
```

## 🔧 Configuration :-

### Voice Settings
- Change voice gender by modifying `bot_voice` variable (0 for DAVID, 1 for ZIRA).
- Adjust speech rate in the voice setup section (1 to 200).
- Modify volume levels as needed (1 to 100).

### Application Paths
Update file paths in the code for your system:
```python
vscode_path = "C:\\Your\\Path\\To\\VS Code\\Code.exe"
spotify_path = "C:\\Your\\Path\\To\\Spotify\\Spotify.exe"
```

## 🤝 Contributing :-

Contributions are welcome!
Please feel free to submit a Pull Request.
For major changes:
  1. Fork the repository
  2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
  3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
  4. Push to the branch (`git push origin feature/AmazingFeature`)
  5. Open a Pull Request

## 📝 Future Enhancements :-

- [ ] Add machine learning for better voice recognition
- [ ] Multi-language support
- [ ] Custom command creation interface
- [ ] Bugs fix & minor changes

## 🐛 Known Issues :-

- Some features may require specific application versions.
- Microphone sensitivity may need adjustment based on hardware or physical environment.
- Path configurations need manual setup for different systems.

## 📄 License :-

This project is not licensed under any company or individual and is Free for anyone to use/modify.

## 👤 Author :-

**Pingaksh Gaur**
- GitHub: _[@pingakshgaur](https://github.com/pingakshgaur)_
- LinkedIn: _[Pingaksh Gaur](https://linkedin.com/in/pingakshgaur)_
- Email: _pingakshgaur@gmail.com_

## 🙏 Acknowledgments :-

- Thanks to the Python community for excellent libraries.
- Inspired by AI assistants like JARVIS and Alexa.
