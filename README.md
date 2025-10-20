🐍 Step 1: Install Anaconda

Anaconda is a free and open-source distribution of Python that simplifies package management and deployment.

🔗 Download Anaconda

👉 Download Anaconda for your OS

💻 Installation Instructions

Windows:

Run the downloaded .exe installer.

Follow the on-screen instructions and check “Add Anaconda to PATH environment variable” (recommended).

Open Anaconda Prompt from the Start Menu after installation.

macOS:

Open the .pkg file you downloaded and follow the prompts.

Once installed, open the Terminal and type:

conda --version


to verify installation.

Linux:

Open a terminal and run:

bash ~/Downloads/Anaconda3-*-Linux-x86_64.sh


Follow the prompts and restart your terminal.

Verify installation:

conda --version

🧱 Step 2: Clone the Repository

If you haven’t already cloned your project repository:

git clone https://github.com/<your-username>/<your-repo-name>.git
cd <your-repo-name>


Replace <your-username> and <your-repo-name> with your actual GitHub repository details.

🧬 Step 3: Create and Activate a Conda Environment (Python 3.9)

Create a new environment named flask_env (you can rename it as you like):

conda create -n flask_env python=3.9 -y


Activate the environment:

On Windows:

conda activate flask_env


On macOS/Linux:

source activate flask_env


Verify your Python version:

python --version


It should show something like:

Python 3.9.x

📋 Step 4: Install Dependencies

Install all required Python packages listed in requirements.txt:

pip install -r requirements.txt


If you see any dependency errors, try updating pip first:

pip install --upgrade pip


and then rerun the installation command.

🔥 Step 5: Run the Flask App

Make sure you are inside your project directory and your virtual environment is activated.

Run your Flask app using one of the following commands (depending on how your app is structured):

Option 1: If your app entry file is app.py
python app.py

Option 2: If using Flask CLI

If you’ve set your Flask app via environment variable:

Windows (PowerShell):

$env:FLASK_APP = "app.py"
flask run


macOS/Linux (bash/zsh):

export FLASK_APP=app.py
flask run

🌐 Step 6: Access the Application

Once the Flask server is running, open your browser and go to:

👉 http://127.0.0.1:5000

You should see your Flask application running locally!
