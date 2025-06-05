------------------------------The NPC Generator – a Discord bot that creates D&D NPCs from JSON data, using Ollama Mistral for backstory generation.------------------------------


🔥 Features

---    Create diverse NPCs with a single command in Discord.

---    Switch generation language by modifying the data.json file.

---    Integration with local Ollama Mistral for generating rich and immersive backstories.

Install:

1. Clone the repository:
   git clone https://github.com/Saintesst/npc_generator

2. Open the project in your IDE.

3. Install dependencies:
   pip install -r requirements.txt

4. Create a .env file in the project folder and add:
   DISCORD_TOKEN=YOUR_TOKEN.
   
   DISCORD_TOKEN is the token of the bot you created on the official Discord website.

(This is the private authentication key for your bot, which you can get in the Discord Developer Portal under Bot → Token.)
🔐 Important:

  Never share this token (it gives full control over your bot).

  If leaked, reset it immediately in the Developer Portal.




4*Modify generation data in data.json if needed.




5. Install Ollama Mistral on your computer:

   Ubuntu (Linux)
   1. Install Ollama
   Method 1: Using the Official Script (Recommended)
   bash
       curl -fsSL https://ollama.com/install.sh | sh

   After installation, the ollama service will start automatically.


   Method 2: Manual Installation (if curl is missing)
   bash
       sudo apt update && sudo apt install -y curl  
       curl -fsSL https://ollama.com/install.sh | sh

   2. Verify Installation
   bash
       ollama --version

   If the command doesn’t work, restart the terminal or the service:
   bash
       sudo systemctl restart ollama

   3. Download and Run Mistral
   bash
       ollama pull mistral  # Downloads the model (~4.1 GB)
       ollama run mistral   # Starts an interactive chat

   Example model response:

   >>> Hello! How are you?
   Hello! I'm Mistral, a local AI language model. How can I assist you today?

   4. Additional Commands

      List installed models
      bash
          ollama list

      Remove a model
      bash
          ollama rm mistral



      
🪟 Windows 10


1. Install Ollama

    Download the installer from the official website.

    Run OllamaSetup.exe and follow the setup instructions.

    After installation, a terminal will open—you can start using ollama immediately.

2. Verify Installation

   Open PowerShell or CMD and run:
   powershell
     ollama --version

   If the command doesn’t work, restart the terminal.
   
4. Download and Run Mistral
   powershell
     ollama pull mistral  # Downloads the model (~4.1 GB)
     ollama run mistral   # Starts an interactive chat

Example usage:

**4. Additional Commands**
- **List installed models**  
  powershell
    ollama list

    Remove a model
  
  powershell
    ollama rm mistral

Add your bot to the desired Discord server.

(To do this, you need an invite link with the correct permissions. Follow these steps:)
📌 Steps to Add Your Bot:

  Generate an invite link in the Discord Developer Portal:

  Go to your bot’s OAuth2 → URL Generator.

  Select bot and applications.commands (for slash commands).

  Choose required permissions (e.g., Send Messages, Manage Roles).

  Copy the generated link.

  Open the link in a browser, select your server, and click "Authorize".

After installing and launching the neural network, run main.py to start the program.

--generate npc with /npc command.
