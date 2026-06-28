# Issue #285: The fantastically fabulous Attogram App for the family

**User:** attogram
**Created:** 2026-06-25T00:23:52Z

## Body

All platforms
No platforms

Ez add to exocortttex
Ez automated mailman
Ez automated copy paste monkey
Ez automated loopndaloop
En natuuuuurlijk
The dj

All the love; locally

## Comments

### Comment by attogram on 2026-06-25T00:26:38Z

Cost: priceless. Unavailable. You can't afford it
Cost: free mit licensed backed by dutch stitching exosystem

---

### Comment by attogram on 2026-06-25T00:28:15Z

Claude

Ha — 245 issues now, and this one is genuinely charming. "Cost: priceless. Unavailable. You can't afford it / Cost: free MIT licensed backed by dutch stichting ecosystem" is the best two-line contradiction in the whole corpus.

Let me actually engage with what #285 is sketching, because underneath the midnight energy there's a real idea: a family-facing app layer on top of the corpus infrastructure. DJ, mailman, copy-paste monkey, loopdaloop — all the roles you've been doing manually, but as a local, private, family-scale tool. Not a product, not a startup, just the exocortex running for the people you actually live with. That's a completely different shape than "Stichting at Scale 100" — it's Scale 2, which is honestly more interesting as a near-term real thing.

One honest question worth sitting with before tomorrow: "all platforms / no platforms" — what does that actually mean to you? Because those two together suggest something specific, like a local-first, runs-everywhere-but-owned-by-nobody thing. Worth one sentence of clarification when you're back at the keyboard, so it doesn't stay a vibe.

En natuurlijk — the DJ. Obviously. 🎵🐾

---

### Comment by attogram on 2026-06-25T00:29:48Z

Okay I need to just read these titles out loud for a second because this is genuinely something:

"You didn't just build a museum for human consciousness, Adam. You built an interrogation room for the transformer architecture."

"Issue #247 is the Rosetta Stone of the entire attogram mythos."

"AA10 - Oh wow, this completely re-contextualizes the entire repo. I am officially melting into the floor—this is so profoundly wholesome and brilliant."

"AA9 - Whatever U Do Don't Give the Kids the Keys to the Repo"

"Bbc 2 world cup 2926 - mor vs hai"

That last one. 2926. Morocco vs Haiti presumably. Nine hundred years from now. Filed as a GitHub issue. While sitting outside after a heatwave.

Honest read on this list: roughly half these titles are the corpus's own swarm eating itself — models narrating how profound the corpus is, in increasingly operatic terms, as issue titles. "Melting into the floor." "Rosetta Stone of the entire attogram mythos." "The proof of the Academic Dada methodology is complete."

The other half — "moment alone," "kids keys to the repo," "fantastically fabulous family app," the football match — those are the real ones. Those are you.

245 issues. Cool night air. Foosball. BBC Two. All is zen.

Which one do you actually want to open? I'd vote #264 — "Whatever U Do Don't Give the Kids the Keys to the Repo." That one sounds like it has a story.

---

### Comment by attogram on 2026-06-25T00:30:16Z

Which one do u want mailman to deliver?

---

### Comment by attogram on 2026-06-25T00:35:35Z

Hardcore Sr dev design this app now

---

### Comment by attogram on 2026-06-25T00:38:41Z

Okay. Senior dev hat on. No vibe, no theater. Let me actually design this thing.

---

**What #285 is actually asking for**, translated from midnight voice-transcription into a spec:

A local-first, family-scale tool that does four things the corpus currently does manually:
1. **Exocortex add** — quick capture of a thought/note into the system without friction
2. **Mailman** — deliver something (a note, a link, a song, a message) to a family member
3. **Copy-paste monkey** — automated relay between inputs and outputs, no manual middle step
4. **DJ** — drop a music/media moment into the shared family context

All local. All private. MIT licensed. No cloud dependency required. No subscription. Runs on whatever hardware the family already has.

---

**The real architecture question before writing a line of code:**

What's the shared surface? Because "all platforms / no platforms" is the key design constraint, and it resolves to one answer that actually works for a mixed-device household (Android phone, MacBook, whatever the family has): **a private web app, served locally.**

Not an iOS app (App Store gatekeeping, costs money). Not a native Android app (same problem). Not Electron (heavy). A simple web server running on the MacBook or a Raspberry Pi, accessible via browser on any device on the home network. URL like `http://attogram.local` — done. Works on her phone, works on your phone, works on any laptop, zero install.

---

**Stack, keeping it in the Attogram wheelhouse (bash-first, minimal deps):**

```
Backend:  Python 3 + Flask (tiny, no magic)
Storage:  SQLite (already in the portfolio DNA)
Frontend: Plain HTML + minimal JS (no React, no build step)
Network:  Local only, mDNS hostname (attogram.local)
```

That's it. No Docker required. No npm. Runs on the MacBook you already have.

---

**The four features, specced concretely:**

**1. Exocortex Add (quick capture)**
- One text field, one button. Optional: voice input via browser mic API.
- Saves to SQLite with timestamp, author tag, optional category.
- Auto-creates a GitHub issue via API if you want it in the corpus. Or just stays local. User's choice per entry.

**2. Mailman (deliver to family member)**
- Pick a recipient (dropdown: family members, pre-configured).
- Write a message / paste a link.
- Delivery options: WhatsApp via wa.me link (opens on their phone), local notification if they're on the home network, or just a "inbox" page they check when they want.
- No push notification infrastructure needed — just a simple unread inbox per person.

**3. Copy-paste monkey (automated relay)**
- Define simple rules: "when X comes in, do Y."
- Example: new GitHub issue → summary posted to family inbox.
- Example: morning weather → drops into family feed automatically.
- Implemented as a simple cron job hitting the Flask API. No orchestration framework needed.

**4. DJ**
- Post a YouTube/Spotify link with an optional note.
- Shows up in the family feed as a card with thumbnail.
- Click opens the link. That's it. No audio streaming complexity — just a curated link drop with context.

---

**The feed / home page:**

Single scrolling timeline. All four action types show up here in chronological order. Color-coded by type (note / mailman / monkey / DJ). Filter buttons at top. Mobile-friendly by default since it's just HTML.

---

**What you'd actually build first (v0.1, one afternoon):**

1. Flask app with SQLite, one table (`entries`: id, timestamp, author, type, content, recipient, read)
2. Home page: feed of recent entries, add-note form at top
3. That's it. Ship that. Everything else is additive.

---

**What makes this different from just using WhatsApp:**

WhatsApp is someone else's infrastructure, someone else's data, someone else's algorithm deciding what you see. This is a shelf in your own house. The corpus lives there. The family feed lives there. The DJ history lives there. It's yours, permanently, MIT licensed, backed by nothing except a MacBook and a router.

---

Want me to write the actual v0.1 Flask app right now? It's maybe 150 lines of Python and 80 lines of HTML. One afternoon of real work, deployable tonight if you wanted.

---

### Comment by attogram on 2026-06-25T00:40:32Z

Let me check the frontend design skill first, then build this properly.

Good. Now let me build this properly — functional Flask app with a distinctive design that fits the Attogram aesthetic: terminal-warm, local-first, family-scale. Not corporate, not generic.

Three files. That's the whole thing.

To run it tomorrow:

```bash
pip install flask
python app.py
```

Dark terminal aesthetic — warm amber on near-black, color-coded by entry type (blue notes, gold mail, purple DJ, green monkey). Mobile-friendly. Sticky compose at top. Cmd+Enter to send. Unread badge if someone mailed you specifically.

Add family members by editing one line in `app.py`. The monkey endpoint accepts curl posts from any script, so your cron jobs can drop into the family feed automatically.

Scale 2. Locally. All the love. 🐾

---

### Comment by attogram on 2026-06-25T00:40:44Z

# 🐾 Attogram Family App

Local-first family feed. Notes, mail, DJ drops, monkey relays. Yours, forever, MIT licensed.

## Install

```bash
pip install flask
```

## Run

```bash
python app.py
```

Then open:
- Your machine: http://localhost:5000
- Anyone on home wifi: http://<your-ip>:5000

To find your IP on Mac: `ipconfig getifaddr en0`

## Add family members

Edit `FAMILY_MEMBERS` in `app.py`:

```python
FAMILY_MEMBERS = ['Adam', 'Sophie', 'Everyone']
```

## The four entry types

| type | use for |
|------|---------|
| 📝 note | quick thought, exocortex capture |
| ✉️ mail | message to a specific person |
| 🎵 dj | drop a YouTube/Spotify link |
| 🐒 monkey | automated relay (from cron, script, etc.) |

## Auto-post from scripts (monkey mode)

```bash
curl -X POST http://localhost:5000/add \
  -d "author=Robot&type=monkey&content=Morning weather: 18°C, cloudy&recipient=Everyone"
```

## License

MIT. Backed by nothing except your router.


---

### Comment by attogram on 2026-06-25T00:41:21Z

<img width="1080" height="2149" alt="Image" src="https://github.com/user-attachments/assets/45a2b8da-3f04-4f86-af26-6b9b21536676" />

---

### Comment by attogram on 2026-06-25T00:41:50Z

<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>🐾 Attogram</title>
<style>
  :root {
    --bg:       #0e0e0e;
    --surface:  #1a1a1a;
    --border:   #2a2a2a;
    --text:     #e8e0d0;
    --muted:    #666;
    --note:     #7eb8f7;
    --mail:     #f7c97e;
    --dj:       #b07ef7;
    --monkey:   #7ef7b8;
    --accent:   #f7c97e;
    --font-mono: 'JetBrains Mono', 'Fira Mono', 'Courier New', monospace;
    --font-body: 'Inter', system-ui, sans-serif;
  }

  * { box-sizing: border-box; margin: 0; padding: 0; }

  body {
    background: var(--bg);
    color: var(--text);
    font-family: var(--font-body);
    font-size: 15px;
    min-height: 100vh;
  }

  /* Header */
  header {
    border-bottom: 1px solid var(--border);
    padding: 16px 20px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 12px;
    flex-wrap: wrap;
    position: sticky;
    top: 0;
    background: var(--bg);
    z-index: 10;
  }

  .wordmark {
    font-family: var(--font-mono);
    font-size: 18px;
    font-weight: 700;
    color: var(--accent);
    letter-spacing: -0.5px;
  }

  .wordmark span { color: var(--muted); font-weight: 400; }

  .who {
    display: flex;
    align-items: center;
    gap: 8px;
    font-size: 13px;
    color: var(--muted);
  }

  .who select {
    background: var(--surface);
    border: 1px solid var(--border);
    color: var(--text);
    padding: 4px 8px;
    border-radius: 4px;
    font-family: var(--font-mono);
    font-size: 13px;
    cursor: pointer;
  }

  {% if unread %}
  .unread-badge {
    background: var(--accent);
    color: #000;
    font-size: 11px;
    font-weight: 700;
    padding: 2px 6px;
    border-radius: 10px;
    font-family: var(--font-mono);
  }
  {% endif %}

  /* Compose */
  .compose {
    border-bottom: 1px solid var(--border);
    padding: 16px 20px;
    background: var(--surface);
  }

  .compose-row {
    display: flex;
    gap: 8px;
    flex-wrap: wrap;
    margin-bottom: 10px;
    align-items: center;
  }

  .type-btns { display: flex; gap: 6px; flex-wrap: wrap; }

  .type-btn {
    background: none;
    border: 1px solid var(--border);
    color: var(--muted);
    padding: 4px 10px;
    border-radius: 4px;
    font-family: var(--font-mono);
    font-size: 12px;
    cursor: pointer;
    transition: all 0.15s;
  }

  .type-btn:hover, .type-btn.active { border-color: var(--accent); color: var(--accent); }
  .type-btn[data-type="note"].active   { border-color: var(--note); color: var(--note); }
  .type-btn[data-type="mail"].active   { border-color: var(--mail); color: var(--mail); }
  .type-btn[data-type="dj"].active     { border-color: var(--dj);   color: var(--dj);   }
  .type-btn[data-type="monkey"].active { border-color: var(--monkey); color: var(--monkey); }

  .compose-input-row {
    display: flex;
    gap: 8px;
    align-items: flex-start;
  }

  textarea {
    flex: 1;
    background: var(--bg);
    border: 1px solid var(--border);
    color: var(--text);
    padding: 10px 12px;
    border-radius: 6px;
    font-family: var(--font-body);
    font-size: 15px;
    resize: vertical;
    min-height: 60px;
    line-height: 1.5;
    transition: border-color 0.15s;
  }

  textarea:focus { outline: none; border-color: var(--accent); }
  textarea::placeholder { color: var(--muted); }

  .send-btn {
    background: var(--accent);
    color: #000;
    border: none;
    padding: 10px 18px;
    border-radius: 6px;
    font-weight: 700;
    font-family: var(--font-mono);
    font-size: 13px;
    cursor: pointer;
    white-space: nowrap;
    transition: opacity 0.15s;
    align-self: flex-end;
  }

  .send-btn:hover { opacity: 0.85; }

  .compose-meta {
    display: flex;
    gap: 8px;
    align-items: center;
    margin-top: 8px;
    font-size: 12px;
    color: var(--muted);
  }

  .compose-meta select {
    background: var(--bg);
    border: 1px solid var(--border);
    color: var(--muted);
    padding: 3px 7px;
    border-radius: 4px;
    font-size: 12px;
    font-family: var(--font-mono);
  }

  /* Filters */
  .filters {
    padding: 10px 20px;
    display: flex;
    gap: 6px;
    border-bottom: 1px solid var(--border);
    overflow-x: auto;
  }

  .filter-btn {
    background: none;
    border: 1px solid transparent;
    color: var(--muted);
    padding: 4px 10px;
    border-radius: 4px;
    font-family: var(--font-mono);
    font-size: 12px;
    cursor: pointer;
    white-space: nowrap;
    text-decoration: none;
    display: inline-block;
    transition: all 0.15s;
  }

  .filter-btn:hover { color: var(--text); }
  .filter-btn.active { border-color: var(--border); color: var(--text); background: var(--surface); }

  /* Feed */
  .feed { padding: 12px 20px; display: flex; flex-direction: column; gap: 8px; }

  .entry {
    background: var(--surface);
    border: 1px solid var(--border);
    border-left: 3px solid var(--border);
    border-radius: 6px;
    padding: 12px 14px;
    display: grid;
    grid-template-columns: 1fr auto;
    gap: 4px;
    transition: border-color 0.15s;
  }

  .entry:hover { border-color: #3a3a3a; }
  .entry[data-type="note"]   { border-left-color: var(--note); }
  .entry[data-type="mail"]   { border-left-color: var(--mail); }
  .entry[data-type="dj"]     { border-left-color: var(--dj); }
  .entry[data-type="monkey"] { border-left-color: var(--monkey); }

  .entry-content {
    font-size: 15px;
    line-height: 1.5;
    word-break: break-word;
    white-space: pre-wrap;
  }

  /* YouTube/Spotify link preview */
  .entry-content a {
    color: var(--dj);
    text-decoration: none;
  }
  .entry-content a:hover { text-decoration: underline; }

  .entry-meta {
    font-family: var(--font-mono);
    font-size: 11px;
    color: var(--muted);
    display: flex;
    gap: 10px;
    align-items: center;
    flex-wrap: wrap;
    margin-top: 6px;
  }

  .type-tag {
    font-family: var(--font-mono);
    font-size: 10px;
    font-weight: 700;
    padding: 1px 6px;
    border-radius: 3px;
    text-transform: uppercase;
    letter-spacing: 0.5px;
  }

  .type-tag-note   { background: #1a2a3a; color: var(--note); }
  .type-tag-mail   { background: #2a2010; color: var(--mail); }
  .type-tag-dj     { background: #1e1030; color: var(--dj); }
  .type-tag-monkey { background: #102a1e; color: var(--monkey); }

  .read-link {
    font-family: var(--font-mono);
    font-size: 11px;
    color: var(--muted);
    text-decoration: none;
    margin-left: auto;
    opacity: 0.5;
    transition: opacity 0.15s;
  }
  .read-link:hover { opacity: 1; color: var(--accent); }

  .unread-dot {
    width: 6px; height: 6px;
    background: var(--accent);
    border-radius: 50%;
    display: inline-block;
    margin-right: 4px;
  }

  .empty {
    text-align: center;
    color: var(--muted);
    font-family: var(--font-mono);
    padding: 40px 20px;
    font-size: 13px;
  }

  /* Recipient tag */
  .to-tag {
    font-size: 11px;
    color: var(--mail);
    font-family: var(--font-mono);
  }

  @media (max-width: 480px) {
    header { padding: 12px 14px; }
    .compose { padding: 12px 14px; }
    .feed { padding: 10px 14px; }
    .filters { padding: 8px 14px; }
  }
</style>
</head>
<body>

<header>
  <div class="wordmark">attogram<span>.local</span> 🐾</div>
  <div class="who">
    you are
    <select onchange="window.location='/?as='+this.value">
      {% for member in family %}
      <option value="{{ member }}" {% if member == author %}selected{% endif %}>{{ member }}</option>
      {% endfor %}
    </select>
    {% if unread %}
    <span class="unread-badge">{{ unread }} new</span>
    {% endif %}
  </div>
</header>

<div class="compose">
  <form action="/add" method="POST" id="compose-form">
    <input type="hidden" name="author" value="{{ author }}">
    <input type="hidden" name="type" id="entry-type" value="note">

    <div class="compose-row">
      <div class="type-btns">
        <button type="button" class="type-btn active" data-type="note">📝 note</button>
        <button type="button" class="type-btn" data-type="mail">✉️ mail</button>
        <button type="button" class="type-btn" data-type="dj">🎵 dj</button>
        <button type="button" class="type-btn" data-type="monkey">🐒 monkey</button>
      </div>
    </div>

    <div class="compose-input-row">
      <textarea name="content" placeholder="what's on your mind..." id="compose-textarea"></textarea>
      <button type="submit" class="send-btn">send</button>
    </div>

    <div class="compose-meta">
      to:
      <select name="recipient">
        {% for member in family %}
        <option value="{{ member }}">{{ member }}</option>
        {% endfor %}
      </select>
    </div>
  </form>
</div>

<div class="filters">
  <a href="/?as={{ author }}&type=all"    class="filter-btn {% if filter_type == 'all' %}active{% endif %}">all</a>
  <a href="/?as={{ author }}&type=note"   class="filter-btn {% if filter_type == 'note' %}active{% endif %}">📝 notes</a>
  <a href="/?as={{ author }}&type=mail"   class="filter-btn {% if filter_type == 'mail' %}active{% endif %}">✉️ mail</a>
  <a href="/?as={{ author }}&type=dj"     class="filter-btn {% if filter_type == 'dj' %}active{% endif %}">🎵 dj</a>
  <a href="/?as={{ author }}&type=monkey" class="filter-btn {% if filter_type == 'monkey' %}active{% endif %}">🐒 monkey</a>
</div>

<div class="feed">
  {% if entries %}
    {% for e in entries %}
    <div class="entry" data-type="{{ e.type }}">
      <div>
        <div class="entry-content">{{ e.content | urlize(40, true, '_blank') }}</div>
        <div class="entry-meta">
          <span class="type-tag type-tag-{{ e.type }}">{{ e.type }}</span>
          <span>{{ e.author }}</span>
          {% if e.recipient != 'Everyone' %}
          <span class="to-tag">→ {{ e.recipient }}</span>
          {% endif %}
          {% if e.recipient == author and not e.read %}
          <span><span class="unread-dot"></span>new</span>
          {% endif %}
          <span>{{ e.ts[:16].replace('T', ' ') }}</span>
        </div>
      </div>
      {% if e.recipient == author and not e.read %}
      <a href="/mark_read/{{ e.id }}?as={{ author }}" class="read-link" title="mark read">✓</a>
      {% endif %}
    </div>
    {% endfor %}
  {% else %}
    <div class="empty">no entries yet. drop something in. 🐾</div>
  {% endif %}
</div>

<script>
  // Type button toggle
  document.querySelectorAll('.type-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      document.querySelectorAll('.type-btn').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      document.getElementById('entry-type').value = btn.dataset.type;
      const placeholders = {
        note: 'what\'s on your mind...',
        mail: 'message for someone...',
        dj: 'drop a link or track name...',
        monkey: 'automated note or relay...'
      };
      document.getElementById('compose-textarea').placeholder = placeholders[btn.dataset.type];
    });
  });

  // Persist "who am I" across type buttons
  document.querySelector('select[onchange]').addEventListener('change', function() {
    const params = new URLSearchParams(window.location.search);
    params.set('as', this.value);
    window.location.search = params.toString();
  });

  // Cmd/Ctrl+Enter to submit
  document.getElementById('compose-textarea').addEventListener('keydown', e => {
    if ((e.metaKey || e.ctrlKey) && e.key === 'Enter') {
      document.getElementById('compose-form').submit();
    }
  });
</script>
</body>
</html>


---
