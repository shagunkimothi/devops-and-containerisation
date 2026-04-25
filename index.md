<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>Containerization & DevOps Lab</title>
  <style>
    :root {
      --bg: #0d1117;
      --surface: #161b22;
      --border: #30363d;
      --text: #c9d1d9;
      --muted: #8b949e;
      --accent: #58a6ff;
      --accent2: #3fb950;
      --heading: #f0f6fc;
    }
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      background: var(--bg);
      color: var(--text);
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
      font-size: 15px;
      line-height: 1.7;
      padding: 2rem 1rem;
    }
    .container {
      max-width: 860px;
      margin: 0 auto;
    }
    h1 {
      font-size: 2rem;
      color: var(--heading);
      border-bottom: 2px solid var(--accent);
      padding-bottom: 0.5rem;
      margin-bottom: 0.5rem;
    }
    h2 {
      font-size: 1.3rem;
      color: var(--heading);
      margin: 2rem 0 0.75rem;
      border-bottom: 1px solid var(--border);
      padding-bottom: 0.3rem;
    }
    h3 {
      font-size: 1rem;
      color: var(--accent2);
      margin: 1.25rem 0 0.5rem;
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }
    .tagline {
      color: var(--muted);
      font-style: italic;
      margin-bottom: 1.5rem;
    }
    .meta-box {
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: 8px;
      padding: 1rem 1.5rem;
      margin: 1rem 0 1.5rem;
      display: flex;
      flex-wrap: wrap;
      gap: 1rem 2.5rem;
    }
    .meta-box div { font-size: 0.9rem; }
    .meta-box span { color: var(--muted); font-size: 0.8rem; display: block; }
    .meta-box strong { color: var(--heading); }
    hr { border: none; border-top: 1px solid var(--border); margin: 1.5rem 0; }
    table {
      width: 100%;
      border-collapse: collapse;
      margin: 0.5rem 0 1rem;
      font-size: 0.92rem;
    }
    th {
      background: var(--surface);
      color: var(--muted);
      text-align: left;
      padding: 0.5rem 0.75rem;
      border: 1px solid var(--border);
      font-weight: 600;
      font-size: 0.8rem;
      text-transform: uppercase;
      letter-spacing: 0.04em;
    }
    td {
      padding: 0.45rem 0.75rem;
      border: 1px solid var(--border);
      vertical-align: middle;
    }
    tr:nth-child(even) td { background: #0d1117; }
    tr:nth-child(odd) td { background: var(--surface); }
    a { color: var(--accent); text-decoration: none; }
    a:hover { text-decoration: underline; }
    ul { padding-left: 1.4rem; }
    ul li { margin-bottom: 0.3rem; }
    pre {
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: 6px;
      padding: 1rem 1.25rem;
      overflow-x: auto;
      font-size: 0.85rem;
      color: var(--accent2);
      margin: 0.5rem 0;
    }
    .badge {
      display: inline-block;
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: 4px;
      padding: 0.1rem 0.5rem;
      font-size: 0.78rem;
      color: var(--muted);
      margin: 0.1rem;
    }
    .exp-num {
      color: var(--accent);
      font-weight: 700;
      font-size: 0.9rem;
    }
    footer {
      margin-top: 3rem;
      padding-top: 1rem;
      border-top: 1px solid var(--border);
      color: var(--muted);
      font-size: 0.85rem;
      text-align: center;
    }
  </style>
</head>
<body>
<div class="container">

  <h1>🐳 Containerization &amp; DevOps Lab</h1>
  <p class="tagline">Master Repository for All Experiments</p>

  <div class="meta-box">
    <div><span>Course</span><strong>Containerization and DevOps</strong></div>
    <div><span>Focus</span><strong>Virtualization · Containers · CI/CD · Cloud-Native</strong></div>
    <div><span>Name</span><strong>Shagun Kimothi</strong></div>
    <div><span>SAP ID</span><strong>500120283</strong></div>
    <div><span>Program</span><strong>BTech. CSE (CCVT) — Batch 2</strong></div>
  </div>

  <h2>About This Repository</h2>
  <p>This repository serves as the <strong>master lab and class repository</strong> for the subject <strong>Containerization and DevOps</strong>. It follows real-world DevOps repository structure where infrastructure, automation, and documentation coexist in a clean, scalable manner.</p>

  <hr/>

  <h2>Class Sessions</h2>

  <h3>January</h3>
  <table>
    <tr><th>Date</th><th>Link</th></tr>
    <tr><td>22 January</td><td><a href="https://shagunkimothi.github.io/devops-and-containerisation/class/22jan/">View Notes</a></td></tr>
    <tr><td>23 January</td><td><a href="https://shagunkimothi.github.io/devops-and-containerisation/class/23jan/">View Notes</a></td></tr>
    <tr><td>27 January</td><td><a href="https://shagunkimothi.github.io/devops-and-containerisation/class/27jan/">View Notes</a></td></tr>
    <tr><td>28 January</td><td><a href="https://shagunkimothi.github.io/devops-and-containerisation/class/28jan/">View Notes</a></td></tr>
  </table>

  <h3>February</h3>
  <table>
    <tr><th>Date</th><th>Link</th></tr>
    <tr><td>4 February</td><td><a href="https://shagunkimothi.github.io/devops-and-containerisation/class/4feb/">View Notes</a></td></tr>
    <tr><td>5 February</td><td><a href="https://shagunkimothi.github.io/devops-and-containerisation/class/5feb/">View Notes</a></td></tr>
    <tr><td>6 February</td><td><a href="https://shagunkimothi.github.io/devops-and-containerisation/class/6feb/">View Notes</a></td></tr>
    <tr><td>10 February</td><td><a href="https://shagunkimothi.github.io/devops-and-containerisation/class/10feb/">View Notes</a></td></tr>
    <tr><td>11 February</td><td><a href="https://shagunkimothi.github.io/devops-and-containerisation/class/11feb/">View Notes</a></td></tr>
    <tr><td>12 February</td><td><a href="https://shagunkimothi.github.io/devops-and-containerisation/class/12feb/">View Notes</a></td></tr>
    <tr><td>18 February</td><td><a href="https://shagunkimothi.github.io/devops-and-containerisation/class/18feb/">View Notes</a></td></tr>
    <tr><td>20 February</td><td><a href="https://shagunkimothi.github.io/devops-and-containerisation/class/20feb/">View Notes</a></td></tr>
    <tr><td>25 February</td><td><a href="https://shagunkimothi.github.io/devops-and-containerisation/class/25feb/">View Notes</a></td></tr>
    <tr><td>26 February</td><td><a href="https://shagunkimothi.github.io/devops-and-containerisation/class/26feb/">View Notes</a></td></tr>
  </table>

  <h3>March</h3>
  <table>
    <tr><th>Date</th><th>Link</th></tr>
    <tr><td>17 March</td><td><a href="https://shagunkimothi.github.io/devops-and-containerisation/class/17march/">View Notes</a></td></tr>
    <tr><td>18 March</td><td><a href="https://shagunkimothi.github.io/devops-and-containerisation/class/18march/">View Notes</a></td></tr>
    <tr><td>19 March</td><td><a href="https://shagunkimothi.github.io/devops-and-containerisation/class/19%20march/">View Notes</a></td></tr>
    <tr><td>25 March</td><td><a href="https://shagunkimothi.github.io/devops-and-containerisation/class/25%20march/">View Notes</a></td></tr>
  </table>

  <hr/>

  <h2>Experiments</h2>
  <p>Each experiment is organized in its own folder containing experiment-specific source files, individual README documentation, commands, configurations, outputs, and observations.</p>
  <br/>
  <table>
    <tr><th>#</th><th>Experiment</th><th>Link</th></tr>
    <tr><td class="exp-num">1</td><td>Virtual Machines vs Containers</td><td><a href="https://shagunkimothi.github.io/devops-and-containerisation/lab/exp1/">View</a></td></tr>
    <tr><td class="exp-num">2</td><td>Docker Installation &amp; Container Lifecycle</td><td><a href="https://shagunkimothi.github.io/devops-and-containerisation/lab/exp2/">View</a></td></tr>
    <tr><td class="exp-num">3</td><td>Deploying NGINX Using Different Base Images</td><td><a href="https://shagunkimothi.github.io/devops-and-containerisation/lab/exp3/">View</a></td></tr>
    <tr><td class="exp-num">4</td><td>Docker Optimization, Inspection &amp; Publishing</td><td><a href="https://shagunkimothi.github.io/devops-and-containerisation/lab/exp4/">View</a></td></tr>
    <tr><td class="exp-num">5</td><td>Docker Volumes, Environment Variables, Monitoring &amp; Networks</td><td><a href="https://shagunkimothi.github.io/devops-and-containerisation/lab/exp5/">View</a></td></tr>
    <tr><td class="exp-num">6</td><td>Docker Compose</td><td><a href="https://shagunkimothi.github.io/devops-and-containerisation/lab/exp6/">View</a></td></tr>
    <tr><td class="exp-num">9</td><td>Ansible</td><td><a href="https://shagunkimothi.github.io/devops-and-containerisation/lab/exp9/">View</a></td></tr>
    <tr><td class="exp-num">10</td><td>SonarQube</td><td><a href="https://shagunkimothi.github.io/devops-and-containerisation/lab/sonarqube-exp10/">View</a></td></tr>
  </table>

  <hr/>

  <h2>Projects</h2>
  <table>
    <tr><th>#</th><th>Project</th><th>Description</th><th>Link</th></tr>
    <tr>
      <td class="exp-num">1</td>
      <td>Containerized Web App with PostgreSQL</td>
      <td>FastAPI + PostgreSQL + Docker Compose + Macvlan/Ipvlan networking</td>
      <td><a href="https://shagunkimothi.github.io/devops-and-containerisation/project1/">View</a></td>
    </tr>
  </table>

  <hr/>

  <h2>Technologies &amp; Tools</h2>
  <pre>Operating Systems       Ubuntu Linux, Windows (Host)
Virtualization          Oracle VirtualBox, Vagrant
Containerization        Docker Engine, Docker CLI
Networking & Services   Nginx, PostgreSQL, Redis
DevOps Concepts         IaC, Automation, CI/CD, Cloud-Native Architecture</pre>

  <hr/>

  <h2>Learning Outcomes</h2>
  <p>By completing all experiments in this repository, the learner will be able to:</p>
  <ul>
    <li>Understand differences between VMs and containers</li>
    <li>Deploy applications in isolated environments</li>
    <li>Automate infrastructure provisioning</li>
    <li>Use Docker for container-based deployment</li>
    <li>Manage persistent data, environment variables, and networks</li>
    <li>Monitor containers using Docker stats, logs, and events</li>
    <li>Follow DevOps-style repository organization and practices</li>
  </ul>

  <hr/>

  <h2>How to Use This Repository</h2>
  <pre># Clone repository
git clone https://github.com/shagunkimothi/devops-and-containerisation.git

# Navigate to an experiment
cd lab/exp5

# Read experiment-specific documentation
cat README.md

# Navigate to project
cd project1
cat README.md</pre>

  <hr/>

  <h2>Future Enhancements</h2>
  <ul>
    <li>GitHub Actions CI/CD pipelines</li>
    <li>Docker image versioning strategies</li>
    <li>Kubernetes basics and deployment</li>
    <li>Cloud deployment (AWS / Azure / GCP)</li>
    <li>Monitoring and logging integration (Prometheus, Grafana)</li>
  </ul>

  <hr/>

  <h2>Author</h2>
  <div class="meta-box">
    <div><span>Name</span><strong>Shagun Kimothi</strong></div>
    <div><span>Program</span><strong>B.Tech Computer Science Engineering</strong></div>
    <div><span>Specialization</span><strong>Cloud Computing &amp; Virtualization Technology</strong></div>
    <div><span>Focus Areas</span><strong>DevOps · Cloud · Automation · Linux</strong></div>
  </div>

  <footer>
    <a href="https://github.com/shagunkimothi/devops-and-containerisation">View the Complete Repository on GitHub →</a>
  </footer>

</div>
</body>
</html>