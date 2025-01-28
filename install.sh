curl -fsSL https://ollama.com/install.sh | sh
sh ./start.sh &
ollama pull deepseek-r1:1.5b
pip install ollama
python main.py