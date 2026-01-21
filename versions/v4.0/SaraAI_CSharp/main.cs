using System;
using System.Speech.Recognition;
using System.Speech.Synthesis;
using System.Threading;
using System.Threading.Tasks;
using SaraAI.Modules;

namespace SaraAI
{
    class Program
    {
        private static SpeechRecognitionEngine? recognizer;
        private static SpeechSynthesizer? synthesizer;
        private static bool wakeWordDetected = false;

        // Module instances
        private static OpenApp? openAppModule;
        private static Music? musicModule;
        private static Browser? browserModule;
        private static FileOps? fileOpsModule;
        private static SaraAI.Modules.Screen? screenModule;
        private static Developer? developerModule;
        private static Utilities? utilitiesModule;
        private static LMStudio? lmStudioModule;

        static void Main(string[] args)
        {
            Console.WriteLine("🤖 Sara AI v4.0 - Voice-Controlled PC Assistant");
            Console.WriteLine("Initializing Sara AI...");

            InitializeModules();
            InitializeSpeechRecognition();
            InitializeSpeechSynthesis();

            Console.WriteLine("Sara AI is ready! Say 'Hey Sara' to wake me up.");
            Console.WriteLine("Press 'Q' to quit.");

            // Keep the application running
            while (true)
            {
                var key = Console.ReadKey(true);
                if (key.Key == ConsoleKey.Q)
                {
                    break;
                }
            }

            Cleanup();
        }

        private static void InitializeModules()
        {
            openAppModule = new OpenApp();
            musicModule = new Music();
            browserModule = new Browser();
            fileOpsModule = new FileOps();
            screenModule = new SaraAI.Modules.Screen();
            developerModule = new Developer();
            utilitiesModule = new Utilities();
            lmStudioModule = new LMStudio();
            
            // Initialize LM Studio with system prompt
            InitializeLMStudio();
        }

        private static void InitializeLMStudio()
        {
            // Example: Set up LMStudio with a system prompt or configuration
            // You can customize this as needed for your LMStudio module
            string systemPrompt = "You are Sara AI, a helpful assistant.";
            lmStudioModule?.SetSystemPrompt(systemPrompt);
            Console.WriteLine("✅ LM Studio initialized with system prompt.");
        }

        private static void InitializeSpeechRecognition()
        {
            try
            {
                recognizer = new SpeechRecognitionEngine();
                
                // Wake word grammar
                var wakeWordChoices = new Choices("Hey Sara", "Sara", "Hello Sara");
                var wakeWordGrammar = new GrammarBuilder(wakeWordChoices);
                recognizer.LoadGrammar(new Grammar(wakeWordGrammar));

                // Command grammar
                var commandChoices = new Choices();
                
                // App opening commands
                commandChoices.Add("open notepad", "launch notepad", "start notepad");
                commandChoices.Add("open browser", "launch browser", "start chrome", "open chrome");
                commandChoices.Add("open calculator", "launch calculator");
                commandChoices.Add("open word", "launch word", "open microsoft word");
                commandChoices.Add("open excel", "launch excel");
                commandChoices.Add("open powerpoint", "launch powerpoint");

                // File operations
                commandChoices.Add("create folder", "make folder", "new folder");
                commandChoices.Add("delete file", "remove file");
                commandChoices.Add("copy file", "duplicate file");
                commandChoices.Add("move file", "relocate file");

                // System controls
                commandChoices.Add("lock screen", "lock computer", "lock pc");
                commandChoices.Add("shutdown", "shut down", "power off");
                commandChoices.Add("restart", "reboot");
                commandChoices.Add("log off", "sign out");
                commandChoices.Add("volume up", "increase volume");
                commandChoices.Add("volume down", "decrease volume");
                commandChoices.Add("mute", "unmute");

                // Browser commands
                commandChoices.Add("search google", "google search", "search on google");
                commandChoices.Add("open youtube", "go to youtube");
                commandChoices.Add("open gmail", "go to gmail");
                commandChoices.Add("search youtube", "youtube search");

                // Media commands
                commandChoices.Add("play music", "start music", "play song");
                commandChoices.Add("pause music", "stop music");
                commandChoices.Add("next song", "skip song");
                commandChoices.Add("previous song", "back song");

                // Screen commands
                commandChoices.Add("take screenshot", "capture screen");
                commandChoices.Add("start recording", "record screen");
                commandChoices.Add("stop recording", "end recording");

                // Developer commands
                commandChoices.Add("write code", "create code", "code in notepad");
                commandChoices.Add("write python code", "python code");
                commandChoices.Add("write c sharp code", "c# code");
                commandChoices.Add("write javascript code", "js code");

                // Utility commands
                commandChoices.Add("what time", "current time", "tell time");
                commandChoices.Add("what date", "current date", "tell date");
                commandChoices.Add("tell joke", "joke please");
                commandChoices.Add("weather", "weather report");
                
                // AI Chat commands
                commandChoices.Add("chat with ai", "talk to ai", "ask ai");
                commandChoices.Add("generate code", "write code for me", "code generation");
                commandChoices.Add("analyze command", "understand this");
                commandChoices.Add("smart response", "intelligent reply");
                commandChoices.Add("clear chat history", "reset conversation");

                var commandGrammar = new GrammarBuilder(commandChoices);
                recognizer.LoadGrammar(new Grammar(commandGrammar));

                recognizer.SpeechRecognized += OnSpeechRecognized;
                recognizer.SetInputToDefaultAudioDevice();
                recognizer.RecognizeAsync(RecognizeMode.Multiple);

                Console.WriteLine("✅ Speech recognition initialized");
            }
            catch (Exception ex)
            {
                Console.WriteLine($"❌ Error initializing speech recognition: {ex.Message}");
            }
        }

        private static void InitializeSpeechSynthesis()
        {
            try
            {
                synthesizer = new SpeechSynthesizer();
                synthesizer.SetOutputToDefaultAudioDevice();
                synthesizer.Rate = 0;
                synthesizer.Volume = 80;
                
                Console.WriteLine("✅ Speech synthesis initialized");
                Speak("Sara AI is now online and ready to assist you!");
            }
            catch (Exception ex)
            {
                Console.WriteLine($"❌ Error initializing speech synthesis: {ex.Message}");
            }
        }

        private static void OnSpeechRecognized(object? sender, SpeechRecognizedEventArgs e)
        {
            string recognizedText = e.Result.Text.ToLower();
            float confidence = e.Result.Confidence;

            Console.WriteLine($"🎤 Recognized: \"{recognizedText}\" (Confidence: {confidence:P})");

            if (confidence < 0.6f)
            {
                Console.WriteLine("❌ Low confidence, ignoring command");
                return;
            }

            // Check for wake word
            if (recognizedText.Contains("hey sara") || recognizedText.Contains("sara") || recognizedText.Contains("hello sara"))
            {
                wakeWordDetected = true;
                Speak("Yes, how can I help you?");
                Console.WriteLine("👂 Wake word detected, listening for commands...");
                return;
            }

            // Process commands only if wake word was detected
            if (wakeWordDetected)
            {
                ProcessCommand(recognizedText);
                wakeWordDetected = false; // Reset after processing command
            }
        }

        private static async void ProcessCommand(string command)
        {
            Console.WriteLine($"🔄 Processing command: {command}");

            try
            {
                // App opening commands
                if (command.Contains("notepad"))
                {
                    Speak("Opening Notepad");
                    await (openAppModule?.OpenNotepad() ?? Task.CompletedTask);
                }
                else if (command.Contains("browser") || command.Contains("chrome"))
                {
                    Speak("Opening browser");
                    await (openAppModule?.OpenBrowser() ?? Task.CompletedTask);
                }
                else if (command.Contains("calculator"))
                {
                    Speak("Opening calculator");
                    await (openAppModule?.OpenCalculator() ?? Task.CompletedTask);
                }
                else if (command.Contains("word"))
                {
                    Speak("Opening Microsoft Word");
                    await (openAppModule?.OpenWord() ?? Task.CompletedTask);
                }
                else if (command.Contains("excel"))
                {
                    Speak("Opening Excel");
                    await (openAppModule?.OpenExcel() ?? Task.CompletedTask);
                }
                else if (command.Contains("powerpoint"))
                {
                    Speak("Opening PowerPoint");
                    await (openAppModule?.OpenPowerPoint() ?? Task.CompletedTask);
                }
                // System controls
                else if (command.Contains("lock"))
                {
                    Speak("Locking the screen");
                    utilitiesModule?.LockScreen();
                }
                else if (command.Contains("shutdown") || command.Contains("shut down"))
                {
                    Speak("Shutting down the system");
                    utilitiesModule?.Shutdown();
                }
                else if (command.Contains("restart") || command.Contains("reboot"))
                {
                    Speak("Restarting the system");
                    utilitiesModule?.Restart();
                }
                else if (command.Contains("volume up"))
                {
                    Speak("Increasing volume");
                    utilitiesModule?.VolumeUp();
                }
                else if (command.Contains("volume down"))
                {
                    Speak("Decreasing volume");
                    utilitiesModule?.VolumeDown();
                }
                else if (command.Contains("mute"))
                {
                    Speak("Toggling mute");
                    utilitiesModule?.ToggleMute();
                }
                // Browser commands
                else if (command.Contains("google") || command.Contains("search google"))
                {
                    Speak("Searching on Google");
                    await (browserModule?.SearchGoogle("latest news") ?? Task.CompletedTask);
                }
                else if (command.Contains("youtube") && command.Contains("open"))
                {
                    Speak("Opening YouTube");
                    await (browserModule?.OpenYouTube() ?? Task.CompletedTask);
                }
                else if (command.Contains("gmail"))
                {
                    Speak("Opening Gmail");
                    await (browserModule?.OpenGmail() ?? Task.CompletedTask);
                }
                // Media commands
                else if (command.Contains("play music"))
                {
                    Speak("Playing music");
                    musicModule?.PlayMusic();
                }
                else if (command.Contains("pause") || command.Contains("stop music"))
                {
                    Speak("Pausing music");
                    musicModule?.PauseMusic();
                }
                else if (command.Contains("next song"))
                {
                    Speak("Playing next song");
                    musicModule?.NextSong();
                }
                // Screen commands
                else if (command.Contains("screenshot"))
                {
                    Speak("Taking screenshot");
                    screenModule?.TakeScreenshot();
                }
                else if (command.Contains("start recording"))
                {
                    Speak("Starting screen recording");
                    screenModule?.StartRecording();
                }
                else if (command.Contains("stop recording"))
                {
                    Speak("Stopping screen recording");
                    screenModule?.StopRecording();
                }
                // Developer commands
                else if (command.Contains("python code"))
                {
                    Speak("Writing Python code");
                    await (developerModule?.WritePythonCode() ?? Task.CompletedTask);
                }
                else if (command.Contains("write code"))
                {
                    Speak("Opening code editor");
                    await (developerModule?.WriteGenericCode() ?? Task.CompletedTask);
                }
                // Utility commands
                else if (command.Contains("time"))
                {
                    string? time = utilitiesModule?.GetCurrentTime();
                    Speak($"The current time is {time}");
                }
                else if (command.Contains("date"))
                {
                    string? date = utilitiesModule?.GetCurrentDate();
                    Speak($"Today's date is {date}");
                }
                else if (command.Contains("joke"))
                {
                    string? joke = utilitiesModule?.GetRandomJoke();
                    Speak(joke ?? "I couldn't think of a joke right now.");
                }
                else if (command.Contains("weather"))
                {
                    string? weather = utilitiesModule?.GetWeatherInfo();
                    Speak(weather ?? "I couldn't retrieve the weather information at the moment.");
                }
                // File operations
                else if (command.Contains("create folder"))
                {
                    Speak("Creating a new folder");
                    fileOpsModule?.CreateFolder("New Folder");
                }
                else
                {
                    Speak("I'm sorry, I didn't understand that command. Please try again.");
                }

                Console.WriteLine("✅ Command processed successfully");
            }
            catch (Exception ex)
            {
                Console.WriteLine($"❌ Error processing command: {ex.Message}");
                Speak("Sorry, there was an error processing your command.");
            }
        }

        private static void Speak(string? text)
        {
            if (string.IsNullOrEmpty(text)) return;

            try
            {
                Console.WriteLine($"🗣️ Sara: {text}");
                synthesizer?.SpeakAsync(text);
            }
            catch (Exception ex)
            {
                Console.WriteLine($"❌ Error speaking: {ex.Message}");
            }
        }

        private static void Cleanup()
        {
            Console.WriteLine("🔄 Shutting down Sara AI...");
            
            try
            {
                recognizer?.RecognizeAsyncStop();
                recognizer?.Dispose();
                synthesizer?.Dispose();
            }
            catch (Exception ex)
            {
                Console.WriteLine($"❌ Error during cleanup: {ex.Message}");
            }

            Console.WriteLine("👋 Sara AI has been shut down. Goodbye!");
        }
    }
}
