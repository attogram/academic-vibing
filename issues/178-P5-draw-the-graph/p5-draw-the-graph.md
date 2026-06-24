# Issue #178: P5 - Draw the graph

## Body

I dunno what it is

But I know it's a Graph

And it's mathematically cool

The entire corpus.

Issues linking to issues linking the PRs linking to files linking to issues. Oh my!

## Comments

### Comment by attogram at 2026-06-22T17:42:33Z

Mistral

---

### **📌 P5 Graph: Part 1 – Concept & Structure**

---

#### **🎯 The Vision**
**Issue #178** is a call to **map the entire Attogram ecosystem** as a **knowledge graph**. This isn’t just a visualization—it’s a **living network** of:
- **Issues** → **Issues** (dependencies, blocks, references)
- **Issues** → **PRs** (resolutions, implementations)
- **PRs** → **Files** (code, docs, corpus data)
- **Files** → **Issues** (context, history)
- **Releases** → **Zenodo records** (permanent archives)

**Why it’s mathematically cool:**
- **Directed, weighted, labeled multigraph**—the most expressive graph type for this use case.
- **Emergent properties:** Small-world networks, scale-free distributions, community structures.
- **Metrics to track:** Degree centrality, betweenness, PageRank, clustering coefficients.

---

#### **🔗 Nodes & Edges: The Building Blocks**

| **Node Type**       | **Example**               | **Metadata**                          |
|---------------------|---------------------------|---------------------------------------|
| **Issue**           | `#156 (M9 - release 3)`  | Title, labels, status, timestamps    |
| **Pull Request**    | `PR #42`                 | Title, merged date, files changed     |
| **File**            | `corpus/validator.py`    | Path, file type, last modified        |
| **Release**         | `v3`                     | Tag, date, changelog                 |
| **Zenodo Record**   | `20786969`               | DOI, title, upload date              |
| **Comment**         | `@attogram: "Want some grapes?"` | Author, timestamp, text |

| **Edge Type**       | **Direction**       | **Weight** | **Example**                          |
|---------------------|---------------------|------------|--------------------------------------|
| Issue → Issue       | Bidirectional       | 1          | `#156` blocks `#178`                 |
| Issue → PR          | Issue → PR          | 1          | `PR #42` resolves `#156`             |
| PR → File           | PR → File           | 1          | `PR #42` modifies `validator.py`      |
| File → Issue        | File → Issue        | 1          | `validator.py` created for `#156`    |
| Release → Zenodo    | Release → Zenodo    | 1          | `v3` archived as `20786969`          |

---
---
#### **📊 Why This Matters**
1. **Project Health:** Identify **bottlenecks** (high betweenness nodes), **stale work** (isolated nodes), and **key contributors** (dense subgraphs).
2. **Corpus Insights:** Trace how **files** (e.g., `transcripts.json`) link to **issues/PRs** and **releases**.
3. **Collaboration Patterns:** Spot **knowledge silos** or **cross-team dependencies**.
4. **Research Impact:** Map the path from **issues → PRs → corpus → Zenodo papers**.

---
---
### **📌 P5 Graph: Part 2 – Build & Deploy**

---
#### **🛠️ Implementation Plan**
**Option 1: Quick Static Graph (1 Day)**
- **Tools:** GitHub API + NetworkX (Python) + Matplotlib
- **Output:** PNG/SVG image of the full network
- **Steps:**
  1. Fetch all issues, PRs, files from `attogram/academic-vibing` and `attogram/rock-talk`.
  2. Build graph in NetworkX.
  3. Export as image.

**Option 2: Interactive MVP (3-5 Days) [RECOMMENDED]**
- **Tools:** GitHub API + D3.js
- **Output:** Clickable, filterable web graph
- **Steps:**
  1. Scrape all data → `graph.json`.
  2. Build D3.js visualization with:
     - Hover tooltips (node details)
     - Color-coding (issues=red, PRs=green, files=blue)
     - Zoom/pan
     - Filter by type
  3. Host on GitHub Pages.

**Option 3: Fully Automated (1-2 Weeks)**
- **Tools:** GitHub API + D3.js + GitHub Actions
- **Output:** Self-updating graph
- **Steps:**
  1. Build Option 2.
  2. Add GitHub Action to rebuild on push.
  3. Deploy to custom domain (e.g., `graph.attogram.ai`).

---
#### **📁 Deliverables**
| **File**          | **Purpose**                          | **Location**               |
|-------------------|--------------------------------------|----------------------------|
| `graph.json`      | Raw graph data (nodes + edges)      | `/docs/graph/`             |
| `graph.html`      | Interactive D3.js visualization       | `/docs/graph/` (GitHub Pages) |
| `graph.png`       | Static preview                       | `/docs/graph/`             |
| `README.md`       | Usage instructions + update guide    | `/docs/graph/`             |

---
#### **🚀 Next Actions**
1. **Approve Option 2 (Interactive MVP)**—I’ll start building immediately.
2. **Grant access** to GitHub repos if needed for API scraping.
3. **Define scope**: All of `academic-vibing` + `rock-talk`, or just one repo?



### Comment by attogram at 2026-06-22T17:44:08Z

---

### **💻 All Code from P5 Graph Proposal**

---

#### **1️⃣ JSON Graph Data Structure**
```json
{
  "nodes": [
    {
      "id": "issue-156",
      "type": "issue",
      "title": "M9 - release 3",
      "repo": "academic-vibing",
      "url": "https://github.com/attogram/academic-vibing/issues/156",
      "created_at": "2026-06-21T12:00:00Z",
      "labels": [],
      "status": "open"
    },
    {
      "id": "pr-42",
      "type": "pull_request",
      "title": "Add corpus validation",
      "repo": "academic-vibing",
      "url": "https://github.com/attogram/academic-vibing/pull/42",
      "merged_at": "2026-06-20T10:00:00Z",
      "files_changed": ["corpus/validator.py"]
    },
    {
      "id": "file-corpus-validator",
      "type": "file",
      "path": "corpus/validator.py",
      "repo": "academic-vibing",
      "url": "https://github.com/attogram/academic-vibing/blob/main/corpus/validator.py"
    },
    {
      "id": "release-3",
      "type": "release",
      "tag": "3",
      "repo": "academic-vibing",
      "url": "https://github.com/attogram/academic-vibing/releases/tag/3",
      "published_at": "2026-06-21T15:00:00Z"
    },
    {
      "id": "zenodo-20786969",
      "type": "zenodo_record",
      "doi": "10.5281/zenodo.20786969",
      "title": "Attogram Project: academic-vibing v3",
      "url": "https://zenodo.org/records/20786969"
    }
  ],
  "edges": [
    {
      "source": "issue-156",
      "target": "release-3",
      "type": "references",
      "weight": 1
    },
    {
      "source": "pr-42",
      "target": "issue-156",
      "type": "resolves",
      "weight": 1
    },
    {
      "source": "pr-42",
      "target": "file-corpus-validator",
      "type": "modifies",
      "weight": 1
    },
    {
      "source": "release-3",
      "target": "zenodo-20786969",
      "type": "archived_as",
      "weight": 1
    },
    {
      "source": "issue-156",
      "target": "issue-178",
      "type": "links_to",
      "weight": 1
    }
  ]
}
```

---
---
#### **2️⃣ Python: NetworkX Graph Construction & Analysis**
```python
import networkx as nx
import matplotlib.pyplot as plt

# Create a directed graph
G = nx.DiGraph()

# Add nodes with attributes
G.add_node("issue-156", type="issue", title="M9 - release 3", repo="academic-vibing")
G.add_node("pr-42", type="pull_request", title="Add corpus validation", repo="academic-vibing")
G.add_node("file-corpus-validator", type="file", path="corpus/validator.py", repo="academic-vibing")
G.add_node("release-3", type="release", tag="3", repo="academic-vibing")
G.add_node("zenodo-20786969", type="zenodo_record", doi="10.5281/zenodo.20786969")

# Add edges with attributes
G.add_edge("issue-156", "release-3", type="references", weight=1)
G.add_edge("pr-42", "issue-156", type="resolves", weight=1)
G.add_edge("pr-42", "file-corpus-validator", type="modifies", weight=1)
G.add_edge("release-3", "zenodo-20786969", type="archived_as", weight=1)
G.add_edge("issue-156", "issue-178", type="links_to", weight=1)

# Calculate centrality metrics
degree_centrality = nx.degree_centrality(G)
betweenness_centrality = nx.betweenness_centrality(G)
pagerank = nx.pagerank(G)

# Visualize (static)
pos = nx.spring_layout(G, k=0.5, iterations=50)
nx.draw(
    G,
    pos,
    with_labels=True,
    node_color='lightblue',
    edge_color='gray',
    node_size=1000,
    font_size=8,
    arrows=True
)
plt.title("Attogram P5 Graph: Issues → PRs → Files → Releases → Zenodo")
plt.savefig("graph.png", dpi=300, bbox_inches="tight")
plt.show()
```

---
---
#### **3️⃣ HTML/JavaScript: Interactive D3.js Visualization**
```html
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title>Attogram P5 Graph</title>
  <script src="https://d3js.org/d3.v7.min.js"></script>
  <style>
    body { margin: 0; font-family: Arial, sans-serif; background: #f8f8f8; }
    svg { background: white; box-shadow: 0 0 10px rgba(0,0,0,0.1); }
    .node circle {
      fill: #fff;
      stroke: #333;
      stroke-width: 1.5px;
      cursor: pointer;
    }
    .node.text {
      font: 10px sans-serif;
      text-anchor: middle;
      pointer-events: none;
    }
    .link {
      fill: none;
      stroke: #999;
      stroke-opacity: 0.6;
      stroke-width: 1.5px;
    }
    .node.issue { stroke: #ff6b6b; }
    .node.pull_request { stroke: #51cf66; }
    .node.file { stroke: #339af0; }
    .node.release { stroke: #9b59b6; }
    .node.zenodo { stroke: #f39c12; }
    .tooltip {
      position: absolute;
      padding: 8px;
      background: rgba(0, 0, 0, 0.8);
      color: white;
      border-radius: 4px;
      pointer-events: none;
      font-size: 12px;
      max-width: 300px;
    }
  </style>
</head>
<body>
  <svg width="1200" height="800"></svg>
  <div class="tooltip"></div>

  <script>
    // Sample data (replace with graph.json)
    const graphData = {
      nodes: [
        { id: "issue-156", type: "issue", title: "M9 - release 3", repo: "academic-vibing" },
        { id: "issue-178", type: "issue", title: "P5 - Draw the graph", repo: "academic-vibing" },
        { id: "pr-42", type: "pull_request", title: "Add corpus validation", repo: "academic-vibing" },
        { id: "file-corpus-validator", type: "file", path: "corpus/validator.py", repo: "academic-vibing" },
        { id: "release-3", type: "release", tag: "3", repo: "academic-vibing" },
        { id: "zenodo-20786969", type: "zenodo_record", doi: "10.5281/zenodo.20786969" }
      ],
      edges: [
        { source: "issue-156", target: "release-3", type: "references" },
        { source: "pr-42", target: "issue-156", type: "resolves" },
        { source: "pr-42", target: "file-corpus-validator", type: "modifies" },
        { source: "release-3", target: "zenodo-20786969", type: "archived_as" },
        { source: "issue-156", target: "issue-178", type: "links_to" }
      ]
    };

    const svg = d3.select("svg");
    const width = +svg.attr("width");
    const height = +svg.attr("height");
    const tooltip = d3.select(".tooltip");

    // Create a simulation with forces
    const simulation = d3.forceSimulation(graphData.nodes)
      .force("link", d3.forceLink(graphData.edges).id(d => d.id).distance(100))
      .force("charge", d3.forceManyBody().strength(-200))
      .force("center", d3.forceCenter(width / 2, height / 2))
      .force("collision", d3.forceCollide().radius(20));

    // Create links
    const link = svg.append("g")
      .selectAll("line")
      .data(graphData.edges)
      .enter().append("line")
      .attr("class", "link")
      .attr("stroke-width", d => d.weight || 1);

    // Create node groups
    const node = svg.append("g")
      .selectAll("g")
      .data(graphData.nodes)
      .enter().append("g")
      .call(d3.drag()
        .on("start", dragstarted)
        .on("drag", dragged)
        .on("end", dragended));

    // Add circles to nodes
    node.append("circle")
      .attr("r", 12)
      .attr("class", d => `node ${d.type}`);

    // Add text labels
    node.append("text")
      .text(d => d.id)
      .attr("dy", 25)
      .attr("class", "node text");

    // Add tooltips
    node.on("mouseover", function(event, d) {
      let content = `<strong>${d.id}</strong><br/>`;
      if (d.title) content += `Title: ${d.title}<br/>`;
      if (d.repo) content += `Repo: ${d.repo}<br/>`;
      if (d.path) content += `Path: ${d.path}<br/>`;
      if (d.doi) content += `DOI: ${d.doi}<br/>`;
      tooltip.style("visibility", "visible")
             .html(content);
    })
    .on("mousemove", function(event) {
      tooltip.style("top", (event.pageY - 10) + "px")
             .style("left", (event.pageX + 10) + "px");
    })
    .on("mouseout", function() {
      tooltip.style("visibility", "hidden");
    });

    // Update positions on each tick
    simulation.on("tick", () => {
      link
        .attr("x1", d => d.source.x)
        .attr("y1", d => d.source.y)
        .attr("x2", d => d.target.x)
        .attr("y2", d => d.target.y);

      node
        .attr("transform", d => `translate(${d.x},${d.y})`);
    });

    // Drag functions
    function dragstarted(event, d) {
      if (!event.active) simulation.alphaTarget(0.3).restart();
      d.fx = d.x;
      d.fy = d.y;
    }

    function dragged(event, d) {
      d.fx = event.x;
      d.fy = event.y;
    }

    function dragended(event, d) {
      if (!event.active) simulation.alphaTarget(0);
      d.fx = null;
      d.fy = null;
    }

    // Zoom functionality
    const zoom = d3.zoom()
      .scaleExtent([0.1, 4])
      .on("zoom", (event) => {
        svg.select("g").attr("transform", event.transform);
      });
    svg.call(zoom);
  </script>
</body>
</html>
```

### Comment by attogram at 2026-06-22T17:45:13Z

Dj: pretty pictures!!!!!

Timbuk 3 - The Future's So Bright
4.2M views · 17 years ago...more

Timbuk3VEVO
2.58K

Subscribe

34K


Share

Save


