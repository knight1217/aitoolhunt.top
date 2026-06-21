// ===== AI Tools Directory - Main JS =====

// Google Analytics 4
(function() {
  var script = document.createElement('script');
  script.async = true;
  script.src = 'https://www.googletagmanager.com/gtag/js?id=G-HNVS8KTTEE';
  document.head.appendChild(script);

  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  window.gtag = gtag;
  gtag('js', new Date());
  gtag('config', 'G-HNVS8KTTEE');
})();

// Google AdSense
(function() {
  var ads = document.createElement('script');
  ads.async = true;
  ads.src = 'https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-1693165095863269';
  ads.crossOrigin = 'anonymous';
  document.head.appendChild(ads);
})();

// App state
let appData = null;
let currentCategory = null;
let currentTool = null;
let searchTimeout = null;

// ===== Init =====
document.addEventListener('DOMContentLoaded', () => {
  initMobileMenu();
  loadData().then(() => {
    const page = detectPage();
    try {
      switch(page) {
        case 'home': renderHome(); break;
        case 'category': renderCategory(); break;
        case 'tool': renderToolDetail(); break;
        case 'compare': renderCompare(); break;
        case 'guide': break;  // static page, no JS rendering needed
        case 'blog': initBlogArticleNav(); break;  // add back link on article pages
        case 'about': break;
        case 'static': break; // unknown static page, do nothing
      }
    } catch(e) {
      console.error('Page render error (' + page + '):', e.message, e.stack);
      // Target main content area only, never the header
      const mainContent = document.querySelector('main .container') || document.querySelector('main');
      if (mainContent) {
        mainContent.innerHTML = '<div class="empty-state" style="padding:40px"><div class="emoji">🔧</div><p>Something went wrong loading this page. Please try again.</p></div>';
      }
    }
  });
});

// ===== Data Loading =====
async function loadData() {
  try {
    // Use embedded data if available (avoids fetch CORS on file://)
    if (window.__TOOLS_DATA__) {
      appData = window.__TOOLS_DATA__;
      if (!appData.tools) appData.tools = [];
      return appData;
    }
    // Fallback: fetch from file (works on HTTP server)
    const res = await fetch('data/tools.json');
    appData = await res.json();
    if (!appData.tools) appData.tools = [];
    return appData;
  } catch(e) {
    console.error('Failed to load data:', e);
    appData = { categories: [], tools: [] };
    return appData;
  }
}

// ===== Page Detection =====
function detectPage() {
  const path = window.location.pathname.toLowerCase();
  if (path.includes('category')) return 'category';
  if (path.includes('tool')) return 'tool';
  if (path.includes('compare')) return 'compare';
  if (path.includes('about')) return 'about';
  if (path.includes('guide')) return 'guide';
  if (path.includes('blog')) return 'blog';
  if (path.includes('privacy')) return 'static';
  // Default: check if page has home-specific elements, otherwise treat as static
  if (document.getElementById('catGrid') || document.getElementById('featuredTools')) return 'home';
  return 'static';  // unknown static page, do nothing
}

// ===== Blog Article Navigation =====
function initBlogArticleNav() {
  // Only inject back link on article pages, not blog index
  const path = window.location.pathname.toLowerCase();
  const isIndex = path.endsWith('/blog/') || path.endsWith('/blog') || path.endsWith('/blog/index.html');
  if (isIndex) return;

  const main = document.querySelector('main');
  if (!main) return;

  // Inject back button
  const backHTML = `
    <div class="blog-back-nav" style="max-width:800px;margin:0 auto 16px;padding:12px 0;">
      <a href="index.html" style="display:inline-flex;align-items:center;gap:8px;color:var(--accent);font-weight:600;font-size:0.95rem;text-decoration:none;padding:8px 16px;border-radius:8px;background:var(--bg-card);border:1px solid var(--border);transition:all 0.2s;">
        ← Back to All Articles
      </a>
    </div>`;
  main.querySelector('.container').insertAdjacentHTML('afterbegin', backHTML);

  // Ensure header nav is visible (in case CSS failed to load header)
  const header = document.querySelector('.header');
  if (!header || header.offsetHeight === 0) {
    const fallbackNav = document.createElement('div');
    fallbackNav.className = 'blog-fallback-nav';
    fallbackNav.innerHTML = `
      <a href="../index.html">Home</a>
      <a href="../index.html#categories">Categories</a>
      <a href="index.html">Blog</a>
      <a href="../about.html">About</a>`;
    fallbackNav.style.cssText = 'display:flex;gap:20px;padding:12px 20px;background:var(--bg-secondary);border-bottom:1px solid var(--border);flex-wrap:wrap;justify-content:center;';
    document.body.insertBefore(fallbackNav, document.body.firstChild);
  }
}

// ===== Mobile Menu =====
function initMobileMenu() {
  const toggle = document.querySelector('.mobile-toggle');
  const nav = document.querySelector('.nav-links');
  if (!toggle || !nav) return;
  toggle.addEventListener('click', () => {
    nav.classList.toggle('open');
  });
}

// ===== Stats Counter =====
function animateStats() {
  const stats = document.querySelectorAll('.stat-number');
  stats.forEach(stat => {
    const target = parseInt(stat.textContent);
    if (isNaN(target)) return;
    let current = 0;
    const duration = 1500;
    const step = target / (duration / 16);
    const timer = setInterval(() => {
      current += step;
      if (current >= target) {
        stat.textContent = target;
        clearInterval(timer);
      } else {
        stat.textContent = Math.floor(current);
      }
    }, 16);
  });
}

// ===== HOME PAGE =====
function renderHome() {
  if (!appData) return;
  
  const featured = appData.tools.filter(t => t.featured);
  const totalTools = appData.tools.length;
  
  // Stats — read from dynamic data
  const statEls = document.querySelectorAll('.stat-number');
  if (statEls.length >= 4) {
    statEls[0].textContent = totalTools;
    statEls[1].textContent = appData.categories.length;
    // Blog & Compare stats are set in HTML, not in data.js
    // Keep HTML values (statEls[2] and statEls[3] untouched)
  }
  
  // Search
  initSearch();
  
  // Categories (skip empty ones)
  const catGrid = document.getElementById('catGrid');
  if (catGrid) {
    catGrid.innerHTML = appData.categories
      .filter(cat => appData.tools.some(t => t.category === cat.id))
      .map(cat => {
        const count = appData.tools.filter(t => t.category === cat.id).length;
        return `
          <a href="category.html?id=${cat.slug}" class="cat-card">
            <span class="cat-icon">${cat.icon}</span>
            <div class="cat-info">
              <h3>${cat.name}</h3>
              <span>${count} tools</span>
            </div>
          </a>
        `;
      }).join('');
  }
  
  // Featured tools
  const featuredGrid = document.getElementById('featuredTools');
  if (featuredGrid) {
    featuredGrid.innerHTML = featured.slice(0, 6).map(t => toolCardHTML(t, true)).join('');
  }
  
  // Recently Added (last 6 tools by order)
  const recentGrid = document.getElementById('recentTools');
  if (recentGrid) {
    const recent = [...appData.tools].reverse().slice(0, 6);
    recentGrid.innerHTML = recent.map(t => toolCardHTML(t, false)).join('');
  }
  
  // Coming Soon — click to expand/collapse
  const upcomingList = document.getElementById('upcomingList');
  if (upcomingList && appData.upcoming) {
    upcomingList.innerHTML = appData.upcoming.map((u, i) => `
      <div class="upcoming-item" onclick="toggleUpcoming(this)" role="button" tabindex="0" aria-expanded="false">
        <span class="upcoming-dot"></span>
        <div class="upcoming-body">
          <div class="upcoming-header">
            <strong>${u.name}</strong>
            <span class="upcoming-cat">${u.category}</span>
          </div>
          <p class="upcoming-desc">${u.desc || ''}</p>
          <div class="upcoming-details">
            <p>${u.details || ''}</p>
          </div>
        </div>
        <span class="upcoming-eta">${u.eta}</span>
        <span class="upcoming-arrow">▾</span>
      </div>
    `).join('');
  }
  
  // All tools
  const allGrid = document.getElementById('allToolsGrid');
  if (allGrid) {
    allGrid.innerHTML = appData.tools.map(t => toolCardHTML(t, t.featured)).join('');
  }
  
  animateStats();
}

// ===== CATEGORY PAGE =====
function renderCategory() {
  const params = new URLSearchParams(window.location.search);
  const slug = params.get('id') || params.get('cat');
  const cat = appData.categories.find(c => c.slug === slug);
  
  if (!cat) {
    document.querySelector('.container').innerHTML = '<div class="empty-state"><div class="emoji">🔍</div><p>Category not found</p></div>';
    return;
  }
  
  document.title = `${cat.name} AI Tools | AI Tool Directory`;
  document.getElementById('catTitle').textContent = cat.name + ' AI Tools';
  document.getElementById('catDesc').textContent = cat.desc;
  document.getElementById('breadcrumbCat').textContent = cat.name;
  document.getElementById('breadcrumbCat').href = `category.html?id=${cat.slug}`;
  
  const tools = appData.tools.filter(t => t.category === cat.id);
  const grid = document.getElementById('catToolGrid');
  
  if (tools.length === 0) {
    grid.innerHTML = '<div class="empty-state"><div class="emoji">📦</div><p>No tools in this category yet.</p></div>';
  } else {
    grid.innerHTML = tools.map(t => toolCardHTML(t, false)).join('');
  }
  
  // Filter buttons
  const pricingTypes = [...new Set(tools.map(t => t.pricing))];
  const filterBar = document.getElementById('filterBar');
  filterBar.innerHTML = `
    <button class="filter-btn active" onclick="filterCategory('all', this)">All</button>
    ${pricingTypes.map(p => `<button class="filter-btn" onclick="filterCategory('${p}', this)">${p}</button>`).join('')}
    <select class="filter-sort" onchange="sortCategory(this.value)">
      <option value="name">Name A-Z</option>
      <option value="rating">Highest Rated</option>
      <option value="featured">Featured First</option>
    </select>
  `;
}

function filterCategory(pricing, btn) {
  document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
  btn.classList.add('active');
  
  const params = new URLSearchParams(window.location.search);
  const slug = params.get('id');
  const cat = appData.categories.find(c => c.slug === slug);
  let tools = appData.tools.filter(t => t.category === cat.id);
  
  if (pricing !== 'all') {
    tools = tools.filter(t => t.pricing === pricing);
  }
  
  const grid = document.getElementById('catToolGrid');
  grid.innerHTML = tools.length ? tools.map(t => toolCardHTML(t, false)).join('') 
    : '<div class="empty-state"><div class="emoji">📦</div><p>No tools match this filter.</p></div>';
}

function sortCategory(sortBy) {
  const params = new URLSearchParams(window.location.search);
  const slug = params.get('id');
  const cat = appData.categories.find(c => c.slug === slug);
  let tools = appData.tools.filter(t => t.category === cat.id);
  
  if (sortBy === 'name') tools.sort((a, b) => a.name.localeCompare(b.name));
  else if (sortBy === 'rating') tools.sort((a, b) => b.rating - a.rating);
  else if (sortBy === 'featured') tools.sort((a, b) => (b.featured ? 1 : 0) - (a.featured ? 1 : 0));
  
  document.getElementById('catToolGrid').innerHTML = tools.map(t => toolCardHTML(t, false)).join('');
}

// ===== TOOL DETAIL PAGE =====
function renderToolDetail() {
  const params = new URLSearchParams(window.location.search);
  const id = params.get('id');
  const tool = appData.tools.find(t => t.id === id);
  
  if (!tool) {
    document.querySelector('.container').innerHTML = '<div class="empty-state"><div class="emoji">🔍</div><p>Tool not found</p></div>';
    return;
  }
  
  document.title = `${tool.name} Review & Rating | AI Tool Directory`;
  
  const cat = appData.categories.find(c => c.id === tool.category);
  
  document.getElementById('toolContent').innerHTML = `
    <div class="breadcrumb">
      <a href="index.html">Home</a> <span class="sep">/</span>
      <a href="category.html?id=${cat.slug}">${cat.name}</a> <span class="sep">/</span>
      <span>${tool.name}</span>
    </div>
    
    <div class="tool-hero">
      <div class="tool-hero-icon">${getToolEmoji(tool)}</div>
      <div class="tool-hero-info">
        <h1>${tool.name}</h1>
        <span class="pricing-badge pricing-${tool.pricing.toLowerCase().replace(' ', '-')}">${tool.pricing}</span>
        <p class="tool-hero-summary">${tool.summary}</p>
        <div class="tool-actions">
          <a href="${tool.url}" target="_blank" rel="noopener" class="btn btn-primary">Visit ${tool.name} →</a>
          ${tool.alternatives && tool.alternatives.length >= 2 ? 
            `<a href="compare.html?t1=${tool.id}&t2=${tool.alternatives[0]}" class="btn btn-secondary">${tool.name} vs ${getToolName(tool.alternatives[0])}</a>` : ''}
        </div>
        <div style="margin-top:16px; color: var(--text-muted); font-size: 0.9rem;">
          Pricing: ${tool.price_detail} | Rating: ${'★'.repeat(Math.round(tool.rating/2))} ${tool.rating}/10
        </div>
      </div>
    </div>
    
    <div class="detail-section">
      <h2>What is ${tool.name}?</h2>
      <p style="color: var(--text-secondary); line-height: 1.8;">${tool.description}</p>
    </div>

    ${tool.tutorial ? `
    <div class="detail-section tutorial-box">
      <h2>🚀 Quick Start Guide</h2>
      <div class="tutorial-content" style="color: var(--text-secondary); line-height: 1.9; background: var(--bg-card); padding: 24px; border-radius: 12px; border-left: 4px solid var(--accent);">
        <p>${tool.tutorial.replace(/\.\s+(?=\d+\.)/g, '.</p><p>')}</p>
      </div>
    </div>
    ` : ''}

    ${tool.affiliate ? `
    <div class="detail-section affiliate-box">
      <h2>🎯 Try ${tool.name}</h2>
      <p style="color: var(--text-secondary); margin-bottom: 12px;">Ready to get started? Click below to visit ${tool.name}.</p>
      <a href="${tool.affiliate}" target="_blank" rel="noopener sponsored" class="btn btn-primary" style="font-size: 1.1rem; padding: 14px 32px;">🚀 Try ${tool.name} Now →</a>
      <p style="color: var(--text-muted); font-size: 0.8rem; margin-top: 8px;">We may earn a commission if you sign up, at no extra cost to you.</p>
    </div>
    ` : ''}

    <div class="detail-section">
      <div class="pros-cons">
        <div class="pro-list">
          <h3>👍 Pros</h3>
          <ul>${(tool.pros || []).map(p => `<li>${p}</li>`).join('')}</ul>
        </div>
        <div class="con-list">
          <h3>👎 Cons</h3>
          <ul>${(tool.cons || []).map(c => `<li>${c}</li>`).join('')}</ul>
        </div>
      </div>
    </div>
    
    <div class="detail-section">
      <h2>Best For</h2>
      <p style="color: var(--text-secondary);">${tool.best_for}</p>
    </div>
    
    <div class="detail-section">
      <h2>Pricing</h2>
      <p style="color: var(--text-secondary); font-size: 1.05rem;">${tool.price_detail}</p>
    </div>
    
    ${tool.alternatives && tool.alternatives.length > 0 ? `
    <div class="detail-section">
      <h2>Alternatives to ${tool.name}</h2>
      <div class="alt-tools">
        ${tool.alternatives.map(altId => {
          const alt = appData.tools.find(t => t.id === altId);
          if (!alt) return '';
          return `
            <a href="tool.html?id=${alt.id}" class="alt-card">
              <h4>${getToolEmoji(alt)} ${alt.name}</h4>
              <p>${alt.summary.substring(0, 80)}...</p>
              <span style="color: var(--accent); font-size: 0.85rem;">Compare →</span>
            </a>
          `;
        }).join('')}
      </div>
    </div>
    ` : ''}
    
    <div class="detail-section">
      <h2>Tags</h2>
      <div class="tool-card-tags">
        ${(tool.tags || []).map(tag => `<span class="tool-tag">${tag}</span>`).join('')}
      </div>
    </div>
  `;
}

// ===== COMPARE PAGE =====
function renderCompare() {
  const params = new URLSearchParams(window.location.search);
  const t1Id = params.get('t1');
  const t2Id = params.get('t2');
  
  const tool1 = appData.tools.find(t => t.id === t1Id);
  const tool2 = appData.tools.find(t => t.id === t2Id);
  
  const compareEl = document.getElementById('compareContent');
  if (!compareEl) return; // static compare article page, skip JS rendering
  
  // Only render when t1/t2 params are present; otherwise keep static HTML content
  if (!tool1 || !tool2) return;
  
  document.title = `${tool1.name} vs ${tool2.name} | AI Tool Directory`;
  
  compareEl.innerHTML = `
    <div class="breadcrumb">
      <a href="index.html">Home</a> <span class="sep">/</span>
      <span>${tool1.name} vs ${tool2.name}</span>
    </div>
    
    <h1 style="font-size: 2rem; margin-bottom: 8px;">${tool1.name} vs ${tool2.name}</h1>
    <p style="color: var(--text-secondary); margin-bottom: 32px;">Detailed comparison to help you choose the right AI tool.</p>
    
    <table class="compare-table">
      <tr><th>Feature</th><td style="font-weight:700;font-size:1.1rem">${getToolEmoji(tool1)} ${tool1.name}</td><td style="font-weight:700;font-size:1.1rem">${getToolEmoji(tool2)} ${tool2.name}</td></tr>
      <tr><th>Rating</th><td>${'★'.repeat(Math.round(tool1.rating/2))} ${tool1.rating}/10</td><td>${'★'.repeat(Math.round(tool2.rating/2))} ${tool2.rating}/10</td></tr>
      <tr><th>Pricing</th><td>${tool1.price_detail}</td><td>${tool2.price_detail}</td></tr>
      <tr><th>Category</th><td>${tool1.category}</td><td>${tool2.category}</td></tr>
      <tr><th>Summary</th><td>${tool1.summary}</td><td>${tool2.summary}</td></tr>
      <tr><th>Pros</th><td>${(tool1.pros || []).map(p => '✓ '+p).join('<br>')}</td><td>${(tool2.pros || []).map(p => '✓ '+p).join('<br>')}</td></tr>
      <tr><th>Cons</th><td>${(tool1.cons || []).map(c => '✗ '+c).join('<br>')}</td><td>${(tool2.cons || []).map(c => '✗ '+c).join('<br>')}</td></tr>
      <tr><th>Best For</th><td>${tool1.best_for}</td><td>${tool2.best_for}</td></tr>
      <tr><th>Link</th><td><a href="${tool1.url}" target="_blank" class="btn btn-primary" style="font-size:0.85rem">Visit →</a></td><td><a href="${tool2.url}" target="_blank" class="btn btn-primary" style="font-size:0.85rem">Visit →</a></td></tr>
    </table>
  `;
}

// ===== Search =====
function initSearch() {
  const input = document.getElementById('searchInput');
  const results = document.getElementById('searchResults');
  if (!input || !results) return;
  
  input.addEventListener('input', () => {
    clearTimeout(searchTimeout);
    searchTimeout = setTimeout(() => {
      const query = input.value.trim().toLowerCase();
      if (query.length < 1) {
        results.classList.remove('active');
        return;
      }
      
      const matches = appData.tools.filter(t => 
        t.name.toLowerCase().includes(query) ||
        (t.tags || []).some(tag => tag.includes(query)) ||
        t.category.includes(query) ||
        t.summary.toLowerCase().includes(query)
      ).slice(0, 8);
      
      if (matches.length === 0) {
        results.innerHTML = '<div class="search-result-item"><span style="color:var(--text-muted)">No tools found</span></div>';
      } else {
        results.innerHTML = matches.map(t => `
          <a href="tool.html?id=${t.id}" class="search-result-item">
            <span class="tool-icon">${getToolEmoji(t)}</span>
            <span class="tool-name">${t.name}</span>
            <span class="tool-cat">${t.category}</span>
          </a>
        `).join('');
      }
      results.classList.add('active');
    }, 200);
  });
  
  document.addEventListener('click', (e) => {
    if (!e.target.closest('.search-box')) {
      results.classList.remove('active');
    }
  });
}

// ===== Tool Card HTML =====
function toolCardHTML(tool, isFeatured) {
  return `
    <a href="tool.html?id=${tool.id}" class="tool-card ${isFeatured ? 'featured' : ''}">
      <div class="tool-card-header">
        <div class="tool-card-icon">${getToolEmoji(tool)}</div>
        <div class="tool-card-meta">
          <div class="tool-card-name">${tool.name}</div>
          <div class="tool-card-pricing">${tool.pricing} · ${(tool.price_detail || '').split(' / ')[0]}</div>
        </div>
      </div>
      <p class="tool-card-summary">${tool.summary}</p>
      <div class="tool-card-footer">
        <div class="tool-rating">
          <span class="stars">${'★'.repeat(Math.round(tool.rating/2))}</span>
          <span class="score">${tool.rating}</span>
        </div>
        <div class="tool-card-tags">
          ${(tool.tags || []).slice(0, 2).map(t => `<span class="tool-tag">${t}</span>`).join('')}
        </div>
      </div>
    </a>
  `;
}

// ===== Helpers =====
function getToolEmoji(tool) {
  const emojis = {
    chatbot: '🤖', writing: '✍️', image: '🎨', video: '🎬', coding: '💻',
    audio: '🎵', design: '🖌️', marketing: '📈', productivity: '⚡', education: '📚',
    search: '🔍', music: '🎶', text: '📝', default: '🛠️'
  };
  if (tool.tags) {
    for (const tag of tool.tags) {
      if (emojis[tag]) return emojis[tag];
    }
  }
  return emojis[tool.category] || emojis.default;
}

function getToolName(id) {
  const tool = appData.tools.find(t => t.id === id);
  return tool ? tool.name : id;
}

// ===== Upcoming expand/collapse =====
function toggleUpcoming(item) {
  const wasExpanded = item.classList.contains('expanded');
  // Close all
  document.querySelectorAll('.upcoming-item.expanded').forEach(el => el.classList.remove('expanded'));
  // Toggle clicked one
  if (!wasExpanded) {
    item.classList.add('expanded');
    item.setAttribute('aria-expanded', 'true');
  } else {
    item.setAttribute('aria-expanded', 'false');
  }
}
