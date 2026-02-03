<h1 align="center">🧠 AI Multi-Agent Research & Content Creation System</h1>

<p align="center">
  A Python-based AI application demonstrating how multiple autonomous agents
  collaborate to perform research, generate images, and produce high-quality
  written content using OpenAI’s API.
</p>

<hr />

<h2>🚀 Why This Project Exists</h2>

<p>
  Many AI demos stop at <em>“call the API, get a response.”</em>
  This project goes further by modelling how <strong>intelligent agents can collaborate</strong>,
  each with a clear responsibility, similar to real-world production AI systems.
</p>

<ul>
  <li><strong>Research Agent</strong> — gathers and synthesizes web-based information</li>
  <li><strong>Writer Agent</strong> — converts research into structured, professional writing</li>
  <li><strong>Extensible design</strong> — additional agents can be added with minimal changes</li>
</ul>

<hr />

<h2>✨ Key Highlights</h2>

<ul>
  <li>🤖 <strong>Multi-Agent Architecture</strong><br />
      Clear separation of concerns between independent agents</li>
  <li>🔍 <strong>Research Agent</strong><br />
      Produces synthesized research instead of raw information dumps</li>
  <li>✍️ <strong>Writer Agent</strong><br />
      Generates polished, publication-ready content</li>
  <li>🎨 <strong>Text-to-Image Generation</strong><br />
      Uses OpenAI’s image API to generate visuals from natural language prompts</li>
  <li>🧩 <strong>Production-Minded Design</strong><br />
      Environment-based configuration and clean project structure</li>
</ul>

<hr />

<h2>🏗️ System Architecture</h2>

<pre>
User Prompt
     │
     ▼
Research Agent
(Web research & synthesis)
     │
     ▼
Writer Agent
(Structured, professional writing)
     │
     ▼
Final Output
(Text content + generated images)
</pre>

<p>
  Each agent operates independently, making the system easy to reason about,
  test, and extend.
</p>

<hr />

<h2>🛠️ Tech Stack</h2>

<ul>
  <li><strong>Python 3.9+</strong></li>
  <li><strong>OpenAI API</strong>
    <ul>
      <li>Text generation</li>
      <li>Image generation</li>
    </ul>
  </li>
  <li><strong>python-dotenv</strong> for secure environment configuration</li>
  <li>Modular, agent-based design pattern</li>
</ul>

<hr />

<h2>📂 Project Structure</h2>

<pre>
.
├── agents/
│   ├── research_agent.py   # Information gathering & synthesis
│   └── writer_agent.py     # Content generation & formatting
├── main.py                 # Agent orchestration
├── requirements.txt
├── .env                    # API keys (not committed)
└── README.md
</pre>

<hr />

<h2>🔐 Setup & Installation</h2>

<h3>1. Clone the Repository</h3>

<pre>
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
</pre>

<h3>2. Create a Virtual Environment (Recommended)</h3>

<pre>
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
</pre>

<h3>3. Install Dependencies</h3>

<pre>
pip install -r requirements.txt
</pre>

<hr />

<h2>🔑 Environment Variables</h2>

<p>Create a <code>.env</code> file in the project root:</p>

<pre>
OPENAI_API_KEY=your_api_key_here
</pre>

<p><strong>⚠️ Never commit API keys to source control.</strong></p>

<hr />

<h2>▶️ Running the Applications</h2>

<pre>
python research_and_write_agent.py
python image_generation.py
</pre>

<p>You can:</p>

<ul>
  <li>Provide a topic or prompt</li>
  <li>Trigger automated research</li>
  <li>Generate professional written content</li>
  <li>Create images from text prompts</li>
</ul>

<hr />

<h2>💡 Example Use Cases</h2>

<ul>
  <li>Automated research & article drafting</li>
  <li>AI-assisted blogging or content pipelines</li>
  <li>Experimenting with agent-based LLM systems</li>
  <li>Prototyping AI workflows for startups or internal tools</li>
</ul>

<hr />

<h2>🔮 Future Enhancements</h2>

<ul>
  <li>🧠 Editor / Reviewer Agent</li>
  <li>✅ Fact-Checking Agent</li>
  <li>📈 SEO Optimization Agent</li>
  <li>🗂️ Persistent memory between runs</li>
  <li>🌐 Web UI or API interface</li>
</ul>

<hr />

<h2>📌 What This Project Demonstrates</h2>

<ul>
  <li>Strong understanding of <strong>LLM workflows</strong></li>
  <li>Practical <strong>agent orchestration patterns</strong></li>
  <li>Clean, readable Python architecture</li>
  <li>Awareness of <strong>production concerns</strong> (security, modularity, extensibility)</li>
</ul>

<hr />

<h2>📄 License</h2>

<p>
  This project is licensed under the <strong>MIT License</strong> —
  free to use, modify, and build upon.
</p>
