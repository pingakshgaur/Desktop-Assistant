# Desktop-Assistant - SCAI
A comprehensive voice-controlled desktop assistant built with Python that responds to voice commands and automates various computer tasks through speech recognition and text-to-speech technology.

## 🚀 Features :-

- **Voice Recognition**: Responds to natural voice commands in English.
- **Text-to-Speech**: Provides audio feedback with customizable voice options.
- **Web Automation**: Opens websites, performs Google/YouTube searches.
- **Application Control**: Launches apps like VS Code, WhatsApp, Discord, Spotify, etc.
- **System Management**: Clears temp files, manages Recycle Bin.
- **Email Integration**: Automated email sending through Gmail.
- **Music Control**: Spotify playlist management and playback.
- **Wikipedia Integration**: Fetches and reads Wikipedia summaries.
- **Time & Weather**: Real-time information and weather reports.
- **Sound Effects**: Interactive audio feedback for enhanced user experience.

## 🛠️ Technologies Used :-

- **Python 3.6+**
- **speech_recognition** - Voice command processing
- **pyttsx3** - Text-to-speech conversion
- **pyautogui** - GUI automation and control
- **webbrowser** - Web browser automation
- **wikipedia** - Wikipedia API integration
- **datetime** - Time and date management
- **winsound** - Sound effects playback
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
├── scai-d.py                    # Main assistant script
├── SFX/                         # Sound effects folder
│   └── Named/                   # Named sound files
├── README.md                    # Project documentation
└── requirements.txt             # Python dependencies
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

**Your Name**
- GitHub: [@pingakshgaur](https://github.com/pingakshgaur)
- LinkedIn: [Pingaksh Gaur](https://linkedin.com/in/pingakshgaur)
- Email: pingakshgaur@gmail.com

## 🙏 Acknowledgments :-

- Thanks to the Python community for excellent libraries.
- Inspired by AI assistants like JARVIS and Alexa.
