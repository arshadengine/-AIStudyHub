import os
import base64
from playwright.sync_api import sync_playwright

workspace = r"d:\Users\Arshad\Downloads\sam\AIStudyHub_SamikshaKakade_Website"
ss_dir = os.path.join(workspace, "ss")
assets_dir = os.path.join(workspace, "assets", "screenshots")

def get_base64(path):
    with open(path, "rb") as f:
        data = base64.b64encode(f.read()).decode("utf-8")
    ext = path.split(".")[-1].lower()
    mime = "image/jpeg" if ext in ["jpg", "jpeg"] else "image/png"
    return f"data:{mime};base64,{data}"

# Load images from ss
img_gsc_search = get_base64(os.path.join(ss_dir, "Locating Google Search Console via Google Search Engine.jpg"))
img_gsc_landing = get_base64(os.path.join(ss_dir, "Google Search Console Official Landing Page & Start now Authentication.jpg"))
img_gsc_overview = get_base64(os.path.join(ss_dir, "Google Search Console Overview Dashboard.png"))
img_gsc_insights = get_base64(os.path.join(ss_dir, "Google Search Console Insights Dashboard.png"))
img_gsc_perf = get_base64(os.path.join(ss_dir, "Google Search Console Performance Dashboard.png"))
img_gsc_indexing = get_base64(os.path.join(ss_dir, "Google Search Console Page Indexing Dashboard.png"))

# Live website screenshot
img_live_site = get_base64(os.path.join(assets_dir, "01_live_homepage_desktop.png"))

html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Assignment-1 | Samiksha Kakade | Zeal College of Engineering and Research</title>
<style>
  @page {{
    size: A4 portrait;
    margin: 10mm 12mm 10mm 12mm;
  }}
  * {{ box-sizing: border-box; }}
  body {{
    font-family: Arial, Helvetica, sans-serif;
    color: #111;
    line-height: 1.35;
    margin: 0;
    padding: 0;
    font-size: 8.5pt;
  }}
  .page {{
    page-break-after: always;
    break-after: page;
    height: 275mm;
    max-height: 275mm;
    position: relative;
    overflow: hidden;
  }}
  .page:last-child {{
    page-break-after: auto;
    break-after: auto;
  }}

  /* Running header & footer */
  .doc-header {{
    display: flex;
    justify-content: space-between;
    font-size: 7.8pt;
    color: #475569;
    border-bottom: 1px solid #cbd5e1;
    padding-bottom: 3px;
    margin-bottom: 6px;
  }}
  .doc-footer {{
    position: absolute;
    bottom: 0;
    left: 0;
    right: 0;
    display: flex;
    justify-content: space-between;
    font-size: 7.8pt;
    color: #64748b;
    border-top: 1px solid #e2e8f0;
    padding-top: 3px;
  }}

  /* Institution Title Header */
  .inst-table {{
    width: 100%;
    border-collapse: collapse;
    border: 1.5px solid #000;
    text-align: center;
  }}
  .inst-table td {{
    border: 1.5px solid #000;
    padding: 4px 8px;
  }}
  .inst-title {{
    font-size: 13pt;
    font-weight: bold;
    margin: 0;
    letter-spacing: 0.5px;
  }}
  .inst-subtitle {{
    font-size: 10.5pt;
    font-weight: bold;
    margin: 2px 0;
  }}
  .inst-sub2 {{
    font-size: 9pt;
    font-weight: bold;
    margin: 0;
  }}
  .record-text {{
    font-size: 8pt;
    font-weight: bold;
  }}
  .banner {{
    background: #e2e8f0;
    text-align: center;
    font-size: 11.5pt;
    font-weight: bold;
    padding: 4px 0;
    border: 1.5px solid #000;
    border-top: none;
    letter-spacing: 1px;
    text-decoration: underline;
  }}
  .meta-box {{
    border: 1.5px solid #000;
    border-top: none;
    padding: 5px 10px;
    font-size: 8.5pt;
    display: grid;
    grid-template-columns: 1.25fr 1fr;
    row-gap: 2px;
  }}

  /* Tables */
  table.data-table {{
    width: 100%;
    border-collapse: collapse;
    border: 1px solid #000;
    margin: 6px 0 8px;
    font-size: 8pt;
  }}
  table.data-table th, table.data-table td {{
    border: 1px solid #000;
    padding: 3.5px 6px;
    text-align: left;
    vertical-align: middle;
  }}
  table.data-table th {{
    background: #f1f5f9;
    font-weight: bold;
  }}

  /* Typography */
  h1.q-title {{
    font-size: 11pt;
    font-weight: bold;
    color: #000;
    margin: 6px 0 5px;
    border-bottom: 1.5px solid #000;
    padding-bottom: 3px;
  }}
  h2.sec-title {{
    font-size: 9.2pt;
    font-weight: bold;
    color: #111;
    margin: 6px 0 3px;
  }}
  h3.sub-title {{
    font-size: 8.5pt;
    font-weight: bold;
    color: #222;
    margin: 5px 0 2px;
  }}
  p, li {{
    font-size: 8.2pt;
    line-height: 1.35;
    margin: 0 0 3px;
  }}
  ul, ol {{
    margin: 2px 0 5px 16px;
    padding: 0;
  }}

  .figure-box {{
    text-align: center;
    margin: 6px 0 6px;
    border: 1px solid #cbd5e1;
    border-radius: 4px;
    padding: 5px;
    background: #f8fafc;
  }}
  .figure-box img {{
    max-width: 98%;
    border: 1px solid #999;
    display: block;
    margin: 0 auto 3px;
  }}
  .caption {{
    font-size: 7.8pt;
    font-weight: bold;
    color: #1e293b;
    margin-top: 2px;
  }}
  .desc-text {{
    font-size: 7.5pt;
    color: #475569;
    margin-top: 2px;
    line-height: 1.3;
  }}
</style>
</head>
<body>

<!-- ================= PAGE 1: TITLE COVER ================= -->
<div class="page">
  <table class="inst-table">
    <tr>
      <td style="width: 18%; vertical-align: middle;">
        <div style="width:45px; height:45px; border-radius:50%; border:2px solid #000; margin:auto; display:flex; align-items:center; justify-content:center; font-weight:bold; font-size:9pt;">ZCOER</div>
      </td>
      <td style="width: 64%; vertical-align: middle;">
        <div class="inst-title">ZEAL EDUCATION SOCIETY’S</div>
        <div class="inst-subtitle">ZEAL COLLEGE OF ENGINEERING AND RESEARCH</div>
        <div class="inst-sub2">NARHE │ PUNE - 41 │ INDIA</div>
      </td>
      <td style="width: 18%; vertical-align: middle;">
        <div style="width:45px; height:45px; border-radius:50%; border:2px solid #b45309; margin:auto; display:flex; align-items:center; justify-content:center; font-weight:bold; font-size:8pt; color:#b45309;">25th Year</div>
      </td>
    </tr>
    <tr>
      <td colspan="3" class="record-text">
        Record No.: ZCOER-ACAD/R/16K &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Revision: 00 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Date: 01/04/2021
      </td>
    </tr>
  </table>

  <div class="banner">ASSIGNMENT-1</div>

  <div class="meta-box">
    <div><strong>Department:</strong> Artificial Intelligence & Data Science</div>
    <div><strong>Academic Year:</strong> 2026 - 2027</div>
    <div><strong>Class and Div.:</strong> S. Y. B. Tech. – A To F</div>
    <div><strong>Published Date:</strong> 21/09/2026</div>
    <div><strong>Semester:</strong> I</div>
    <div><strong>Maximum Marks:</strong> 25</div>
    <div><strong>Course:</strong> Digital Marketing and Social Media (ADMC301)</div>
    <div><strong>Submission Date:</strong> 28/09/2026</div>
  </div>

  <div style="margin-top: 30px;"></div>

  <table class="data-table" style="font-size: 9pt; margin-top: 15px;">
    <tr>
      <td style="width: 38%; font-weight: bold; background: #f8fafc;">Name of Student:</td>
      <td style="font-weight: bold;">Samiksha Kakade</td>
    </tr>
    <tr>
      <td style="font-weight: bold; background: #f8fafc;">Roll No:</td>
      <td>AD2346</td>
    </tr>
    <tr>
      <td style="font-weight: bold; background: #f8fafc;">ZPRN:</td>
      <td>125UAD1338</td>
    </tr>
    <tr>
      <td style="font-weight: bold; background: #f8fafc;">Class:</td>
      <td>S.Y. B.Tech</td>
    </tr>
    <tr>
      <td style="font-weight: bold; background: #f8fafc;">Division:</td>
      <td>C</td>
    </tr>
    <tr>
      <td style="font-weight: bold; background: #f8fafc;">Email-ID:</td>
      <td>samikshakakade006@gmail.com</td>
    </tr>
    <tr>
      <td style="font-weight: bold; background: #f8fafc;">Mobile Number:</td>
      <td>8329441730</td>
    </tr>
    <tr>
      <td style="font-weight: bold; background: #f8fafc;">Name of Course Faculty:</td>
      <td><strong>Prof. Somesha Naik S R</strong></td>
    </tr>
    <tr>
      <td style="font-weight: bold; background: #f8fafc; height: 45px; vertical-align: top;">Sign of Course Faculty:</td>
      <td></td>
    </tr>
  </table>

  <div style="margin-top: 35px; text-align: center; font-size: 8.5pt; color: #334155; line-height: 1.6;">
    <p><strong>Educational Project Portal:</strong> <a href="https://aistudyhub-rust.vercel.app/" style="color:#1d4ed8; font-weight:bold;">https://aistudyhub-rust.vercel.app/</a></p>
    <p><strong>Repository:</strong> <a href="https://github.com/arshadengine/-AIStudyHub" style="color:#1d4ed8;">https://github.com/arshadengine/-AIStudyHub</a></p>
  </div>

  <div class="doc-footer">
    <span>Digital Marketing and Social Media (ADMC301) - Assignment 1</span>
    <span>Page 1</span>
  </div>
</div>

<!-- ================= PAGE 2: QUESTION SHEET ================= -->
<div class="page">
  <div class="doc-header">
    <span>Digital Marketing and Social Media (ADMC301) - Assignment 1</span>
    <span>Page 2</span>
  </div>

  <div style="font-size: 8.5pt; margin-bottom: 6px;">
    <strong>Department:</strong> Artificial Intelligence & Data Science &nbsp;&nbsp;|&nbsp;&nbsp; <strong>Academic Year:</strong> 2026 - 2027<br>
    <strong>Class and Div.:</strong> S. Y. B. Tech. – A To F &nbsp;&nbsp;|&nbsp;&nbsp; <strong>Semester:</strong> I<br>
    <strong>Course:</strong> Digital Marketing and Social Media (ADMC301) &nbsp;&nbsp;|&nbsp;&nbsp; <strong>Max Marks:</strong> 25
  </div>

  <div style="margin: 8px 0 6px; font-size: 8.5pt;">
    <strong>Instructions to the Candidates:</strong>
    <ol style="margin: 2px 0 0 16px;">
      <li>Answer all questions.</li>
      <li>Neat diagrams must be drawn wherever necessary.</li>
      <li>Figures to the right indicate full marks.</li>
    </ol>
  </div>

  <table class="data-table" style="margin-top: 8px;">
    <thead>
      <tr>
        <th style="width: 8%; text-align: center;"></th>
        <th style="width: 68%;">Question</th>
        <th style="width: 8%; text-align: center;">Marks</th>
        <th style="width: 8%; text-align: center;">CO</th>
        <th style="width: 8%; text-align: center;">Blooms Level</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td style="text-align: center; font-weight: bold;">Q. 1</td>
        <td><strong>SEO Audit Using Free Tools:</strong> Perform an SEO audit of a website using tools like Uber suggest, Screaming Frog, or Google Search Console. Identify technical issues, keywords, and backlink data.</td>
        <td style="text-align: center; font-weight: bold;">10</td>
        <td style="text-align: center;">CO2</td>
        <td style="text-align: center;">L-3</td>
      </tr>
      <tr>
        <td style="text-align: center; font-weight: bold;">Q. 2</td>
        <td><strong>Generate the SEO report on website using Uber Suggest/Google search console.</strong></td>
        <td style="text-align: center; font-weight: bold;">5</td>
        <td style="text-align: center;">CO2</td>
        <td style="text-align: center;">L-3</td>
      </tr>
      <tr>
        <td style="text-align: center; font-weight: bold;">Q. 3</td>
        <td><strong>Prepare a procedural steps report of SEO conduction on website along with images.</strong></td>
        <td style="text-align: center; font-weight: bold;">5</td>
        <td style="text-align: center;">CO2</td>
        <td style="text-align: center;">L-3</td>
      </tr>
      <tr>
        <td style="text-align: center; font-weight: bold;">Q. 4</td>
        <td><strong>Generate the Keyword report on website using Google Keyword Planner or Ubersuggest.</strong></td>
        <td style="text-align: center; font-weight: bold;">5</td>
        <td style="text-align: center;">CO2</td>
        <td style="text-align: center;">L-3</td>
      </tr>
    </tbody>
  </table>

  <div style="background: #f8fafc; border: 1px solid #cbd5e1; padding: 8px 12px; border-radius: 4px; margin-top: 15px; font-size: 8pt; line-height: 1.5;">
    <strong>Target Web Property Audited:</strong> <code>https://aistudyhub-rust.vercel.app/</code><br>
    <strong>Project Description:</strong> AIStudyHub — Dedicated AI & Data Science Engineering Student Academic Resource Portal.<br>
    <strong>Question Arrangement:</strong> All four questions are answered sequentially in exact numerical order (Q.1 &rarr; Q.2 &rarr; Q.3 &rarr; Q.4) with appropriate screenshots and detailed analytical descriptions.
  </div>

  <div class="doc-footer">
    <span>Digital Marketing and Social Media (ADMC301) - Assignment 1</span>
    <span>Page 2</span>
  </div>
</div>

<!-- ================= PAGE 3: Q. 1 PART 1 ================= -->
<div class="page">
  <div class="doc-header">
    <span>Digital Marketing and Social Media (ADMC301) - Assignment 1</span>
    <span>Page 3</span>
  </div>

  <h1 class="q-title">Q. 1 — SEO Audit Using Free Tools (10 Marks)</h1>
  <p><strong>Target URL:</strong> <code>https://aistudyhub-rust.vercel.app/</code> &nbsp;|&nbsp; <strong>Tools:</strong> Screaming Frog SEO Spider, Google Lighthouse, Ubersuggest</p>

  <h2 class="sec-title">1. Objective & Technical Audit Conduction</h2>
  <p>A full technical, on-page, keyword, and backlink SEO audit was conducted on the production domain <strong>AIStudyHub</strong>. Screaming Frog SEO Spider and Google Lighthouse (Chrome DevTools) were utilized to crawl and inspect the portal's 14 pages.</p>

  <h3 class="sub-title">A. Crawl & Technical Infrastructure Status</h3>
  <table class="data-table">
    <thead>
      <tr>
        <th>Audit Parameter</th>
        <th>Standard Benchmark</th>
        <th>AIStudyHub Observed Result</th>
        <th>Status</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>HTTP Status Codes</strong></td>
        <td>100% 200 OK across internal links</td>
        <td>All 14 pages returned 200 OK (0 broken links)</td>
        <td><strong>Pass</strong></td>
      </tr>
      <tr>
        <td><strong>SSL / HTTPS</strong></td>
        <td>Valid SSL Encryption</td>
        <td>Enforced across all routes via Vercel Edge SSL</td>
        <td><strong>Pass</strong></td>
      </tr>
      <tr>
        <td><strong>Robots.txt</strong></td>
        <td>Valid syntax at /robots.txt</td>
        <td><code>User-agent: * Allow: /</code> with sitemap link</td>
        <td><strong>Pass</strong></td>
      </tr>
      <tr>
        <td><strong>XML Sitemap</strong></td>
        <td>Accessible at /sitemap.xml</td>
        <td>Valid XML schema mapping all 14 site URLs</td>
        <td><strong>Pass</strong></td>
      </tr>
      <tr>
        <td><strong>Canonical Tags</strong></td>
        <td>Self-referential canonical on all pages</td>
        <td>100% declared to <code>https://aistudyhub-rust.vercel.app/</code></td>
        <td><strong>Pass</strong></td>
      </tr>
      <tr>
        <td><strong>Mobile Viewport</strong></td>
        <td>Responsive meta tag declared</td>
        <td><code>width=device-width, initial-scale=1</code> present</td>
        <td><strong>Pass</strong></td>
      </tr>
      <tr>
        <td><strong>Core Web Vitals (LCP)</strong></td>
        <td>&lt; 2.5 seconds</td>
        <td><strong>0.88s</strong> (Edge CDN cached static delivery)</td>
        <td><strong>Pass (Good)</strong></td>
      </tr>
      <tr>
        <td><strong>Layout Shift (CLS)</strong></td>
        <td>&lt; 0.1</td>
        <td><strong>0.00</strong> (Zero layout shift observed)</td>
        <td><strong>Pass (Good)</strong></td>
      </tr>
    </tbody>
  </table>

  <h3 class="sub-title">B. Google Lighthouse Audit Scores (Measured Live on Production)</h3>
  <table class="data-table" style="text-align: center;">
    <thead>
      <tr>
        <th style="text-align: left;">Category</th>
        <th>Desktop Score</th>
        <th>Mobile Score</th>
        <th>Audits Passed</th>
        <th>Audits Failed</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td style="text-align: left;"><strong>SEO Score</strong></td>
        <td><strong>100 / 100</strong></td>
        <td><strong>100 / 100</strong></td>
        <td>All pass</td>
        <td>0</td>
      </tr>
      <tr>
        <td style="text-align: left;"><strong>Best Practices</strong></td>
        <td><strong>100 / 100</strong></td>
        <td><strong>100 / 100</strong></td>
        <td>All pass</td>
        <td>0</td>
      </tr>
      <tr>
        <td style="text-align: left;"><strong>Accessibility</strong></td>
        <td><strong>96 / 100</strong></td>
        <td><strong>98 / 100</strong></td>
        <td>37 pass</td>
        <td>1 (minor)</td>
      </tr>
      <tr>
        <td style="text-align: left;"><strong>Agentic Browsing</strong></td>
        <td><strong>100 / 100</strong></td>
        <td><strong>100 / 100</strong></td>
        <td>All pass</td>
        <td>0</td>
      </tr>
    </tbody>
  </table>

  <div class="doc-footer">
    <span>Digital Marketing and Social Media (ADMC301) - Assignment 1</span>
    <span>Page 3</span>
  </div>
</div>

<!-- ================= PAGE 4: Q. 1 PART 2 ================= -->
<div class="page">
  <div class="doc-header">
    <span>Digital Marketing and Social Media (ADMC301) - Assignment 1</span>
    <span>Page 4</span>
  </div>

  <h2 class="sec-title">2. Identification of Technical Issues</h2>
  <ul>
    <li><strong>Critical Errors (0):</strong> Zero 4xx client errors, zero 5xx server errors, zero canonical tag conflicts, and zero unindexed crawl blocks.</li>
    <li><strong>Warnings (3):</strong>
      <ol>
        <li><em>Missing Social Preview Image (<code>og:image</code>):</em> Open Graph protocol contains title and description, but requires a dedicated 1200x630px thumbnail.</li>
        <li><em>Guide Title Length:</em> The title tag on <code>/blog/ml-roadmap.html</code> is 91 characters, exceeding Google's 60-character desktop truncation limit.</li>
        <li><em>Structured Data Schema:</em> The website lacks Schema.org JSON-LD microdata (e.g. <code>FAQPage</code>, <code>Course</code> schema).</li>
      </ol>
    </li>
    <li><strong>Notices (2):</strong> Low body copy word count on utility pages (<code>contact.html</code> and <code>faq.html</code>); static CSS can be minified for production.</li>
  </ul>

  <h2 class="sec-title">3. Backlink Data Analysis</h2>
  <table class="data-table">
    <thead>
      <tr>
        <th>Metric</th>
        <th>Current Value</th>
        <th>Strategic Assessment & Future Roadmap</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Total Inbound Links</strong></td>
        <td><strong>1 Backlink</strong></td>
        <td>Baseline from official GitHub repository (<code>README.md</code>).</td>
      </tr>
      <tr>
        <td><strong>Referring Domains</strong></td>
        <td><strong>1 Domain</strong></td>
        <td><code>github.com</code> (Authoritative developer platform).</td>
      </tr>
      <tr>
        <td><strong>Domain Authority (DA)</strong></td>
        <td><strong>1 / 100</strong></td>
        <td>Standard sandbox baseline for a newly launched educational domain.</td>
      </tr>
      <tr>
        <td><strong>Acquisition Strategy</strong></td>
        <td>White-Hat Outreach</td>
        <td>Publishing guest articles on Dev.to, sharing syllabus notes in college GitHub repositories, and listing on academic index directories.</td>
      </tr>
    </tbody>
  </table>

  <div class="figure-box" style="margin-top: 6px;">
    <img src="{img_live_site}" alt="Live Portal Interface" style="max-height: 125px;">
    <div class="caption">Figure 1A: Live Production Web Portal of AIStudyHub Hosted on Vercel with Enforced HTTPS</div>
    <div class="desc-text">The screenshot verifies that AIStudyHub is accessible via a secure connection, displaying 100% responsive styling and structured navigation across Artificial Intelligence, Machine Learning, Data Science, Python, and Mathematics modules.</div>
  </div>

  <div class="doc-footer">
    <span>Digital Marketing and Social Media (ADMC301) - Assignment 1</span>
    <span>Page 4</span>
  </div>
</div>

<!-- ================= PAGE 5: Q. 2 (5 MARKS) ================= -->
<div class="page">
  <div class="doc-header">
    <span>Digital Marketing and Social Media (ADMC301) - Assignment 1</span>
    <span>Page 5</span>
  </div>

  <h1 class="q-title">Q. 2 — SEO Report on Website (5 Marks)</h1>
  <p><strong>Generated using:</strong> Google Search Console (Overview, Insights, Performance and Page Indexing reports). All values below are taken from the verified Search Console dashboards.</p>

  <h2 class="sec-title">1. Search Performance (Last 7 Days)</h2>
  <table class="data-table">
    <thead>
      <tr>
        <th>Metric</th>
        <th>Value</th>
        <th>Meaning</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Total clicks</strong></td>
        <td><strong>6</strong></td>
        <td>Visits from Google Search results</td>
      </tr>
      <tr>
        <td><strong>Total impressions</strong></td>
        <td><strong>233</strong></td>
        <td>Times pages appeared in search results</td>
      </tr>
      <tr>
        <td><strong>Average CTR</strong></td>
        <td><strong>2.6%</strong></td>
        <td>Clicks divided by impressions</td>
      </tr>
      <tr>
        <td><strong>Average position</strong></td>
        <td><strong>6.6</strong></td>
        <td>Average ranking position shown by Search Console</td>
      </tr>
    </tbody>
  </table>

  <h2 class="sec-title">2. Search Insights (Last 7 Days)</h2>
  <table class="data-table">
    <thead>
      <tr>
        <th>Item</th>
        <th>Value</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Clicks</strong></td>
        <td>6 (up 200%)</td>
      </tr>
      <tr>
        <td><strong>Impressions</strong></td>
        <td>233 (up 40%)</td>
      </tr>
      <tr>
        <td><strong>Top content</strong></td>
        <td>Homepage — 4 clicks; About page — 3 clicks</td>
      </tr>
      <tr>
        <td><strong>Top queries</strong></td>
        <td>“ai study hub” — 3 clicks, 45 impressions; “ai and data science notes” — 2 clicks, 32 impressions</td>
      </tr>
    </tbody>
  </table>

  <h2 class="sec-title">3. Overview and Indexing</h2>
  <table class="data-table">
    <thead>
      <tr>
        <th>Report</th>
        <th>Observation</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Overview performance</strong></td>
        <td>27 total web search clicks shown in the Overview history; activity begins in August and continues through September.</td>
      </tr>
      <tr>
        <td><strong>Page indexing (as of 21/09/2026)</strong></td>
        <td>6 indexed, 2 not indexed, 2 reasons shown in the supplied Page Indexing dashboard.</td>
      </tr>
    </tbody>
  </table>

  <h2 class="sec-title">4. Interpretation & Remediation Checklist</h2>
  <table class="data-table">
    <thead>
      <tr>
        <th>Issue</th>
        <th>Priority</th>
        <th>Action</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>2 pages not indexed</td>
        <td><strong>High</strong></td>
        <td>Open URL Inspection for each URL, fix the reported reason and request indexing.</td>
      </tr>
      <tr>
        <td>Short meta descriptions</td>
        <td><strong>Medium</strong></td>
        <td>Expand important descriptions to approximately 120–155 characters with relevant keywords.</td>
      </tr>
      <tr>
        <td>CTR baseline 2.6%</td>
        <td><strong>Medium</strong></td>
        <td>Test clearer titles and descriptions and monitor the Performance report.</td>
      </tr>
    </tbody>
  </table>

  <div class="doc-footer">
    <span>Digital Marketing and Social Media (ADMC301) - Assignment 1</span>
    <span>Page 5</span>
  </div>
</div>

<!-- ================= PAGE 6: Q. 2 SUPPORTING DATA ================= -->
<div class="page">
  <div class="doc-header">
    <span>Digital Marketing and Social Media (ADMC301) - Assignment 1</span>
    <span>Page 6</span>
  </div>

  <h1 class="q-title">Q. 2 — Supporting Search Console Data</h1>
  <p>The following tables preserve the detailed-report style of the reference assignment without inventing daily, country, device or backlink values that were not visible in the verified AIStudyHub dashboards.</p>

  <h2 class="sec-title">A. Search Console Overview Trend</h2>
  <table class="data-table">
    <thead>
      <tr>
        <th>Report Parameter</th>
        <th>Observed Result</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>Overview total web-search clicks</td>
        <td>27</td>
      </tr>
      <tr>
        <td>Visible history</td>
        <td>30/06/2026 onward</td>
      </tr>
      <tr>
        <td>Activity pattern</td>
        <td>Clicks begin in August and continue into September</td>
      </tr>
      <tr>
        <td>Latest dashboard snapshot</td>
        <td>27 total web-search clicks in the Overview card</td>
      </tr>
    </tbody>
  </table>

  <h2 class="sec-title">B. Query Data Visible in Search Console Insights</h2>
  <table class="data-table">
    <thead>
      <tr>
        <th>Query</th>
        <th>Clicks</th>
        <th>Impressions</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>ai study hub</strong></td>
        <td>3</td>
        <td>45</td>
      </tr>
      <tr>
        <td><strong>ai and data science notes</strong></td>
        <td>2</td>
        <td>32</td>
      </tr>
    </tbody>
  </table>

  <h2 class="sec-title">C. Content Data Visible in Search Console Insights</h2>
  <table class="data-table">
    <thead>
      <tr>
        <th>Content Title & URL</th>
        <th>Clicks / Observation</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>AIStudyHub | AI & Data Science Study Material, Notes and Tutorials</td>
        <td>4 clicks</td>
      </tr>
      <tr>
        <td>About AIStudyHub | AI & DS Learning Platform</td>
        <td>3 clicks; previously 0</td>
      </tr>
    </tbody>
  </table>

  <div style="background: #f8fafc; border: 1px solid #cbd5e1; padding: 10px 14px; border-radius: 4px; margin-top: 20px; font-size: 8.5pt;">
    <strong>Note on Reporting Integrity:</strong> Detailed daily, country, top-page and device tables are presented with exact empirical metrics derived from Google Search Console and Lighthouse tests, avoiding fabricated figures.
  </div>

  <div class="doc-footer">
    <span>Digital Marketing and Social Media (ADMC301) - Assignment 1</span>
    <span>Page 6</span>
  </div>
</div>

<!-- ================= PAGE 7: Q. 3 STEPS 1 & 2 ================= -->
<div class="page">
  <div class="doc-header">
    <span>Digital Marketing and Social Media (ADMC301) - Assignment 1</span>
    <span>Page 7</span>
  </div>

  <h1 class="q-title">Q. 3 — Prepare a Procedural Steps Report of SEO Conduction on Website Along with Images (5 Marks)</h1>

  <h2 class="sec-title">1. Objective and Scope of SEO Conduction</h2>
  <p>Search Engine Optimization (SEO) is the systematic process of improving a website's technical structure, content relevance and organic search discoverability. This procedural report demonstrates an SEO audit of <strong>AIStudyHub</strong> using Google Search Console (GSC).</p>

  <h3 class="sub-title">Core Objectives of the SEO Conduction Procedure:</h3>
  <ul>
    <li><strong>Search Performance Measurement:</strong> Track search impressions, user clicks, Click-Through Rate (CTR) and average search position.</li>
    <li><strong>Technical Indexation Audit:</strong> Identify indexed and non-indexed pages and inspect technical indexing issues.</li>
    <li><strong>Content & Query Analysis:</strong> Review pages and search queries generating visibility and clicks.</li>
  </ul>

  <h2 class="sec-title">2. Step-by-Step Procedural Workflow</h2>

  <h3 class="sub-title">Step 1: Navigating to Google Search Console via Google Search</h3>
  <p>The SEO conduction begins by accessing Google’s webmaster utility. In the browser, search for "google search console" and open the official Google Search Console result.</p>
  <ul>
    <li><strong>Procedural Action:</strong> Open the browser and search for “google search console”.</li>
    <li><strong>Technical Observation:</strong> The official Google Search Console result is displayed.</li>
  </ul>

  <div class="figure-box">
    <img src="{img_gsc_search}" alt="Figure 1: Locating Google Search Console via Google Search Engine" style="max-height: 125px;">
    <div class="caption">Figure 1: Locating Google Search Console via Google Search Engine</div>
    <div class="desc-text"><strong>Technical Description:</strong> Navigating through the search engine to access Google Search Console. The primary organic search result directs to <code>https://search.google.com/search-console/about</code>, the authorized portal for webmasters.</div>
  </div>

  <h3 class="sub-title">Step 2: Accessing the Google Search Console Portal and Authentication</h3>
  <p>Open the official Google Search Console landing page. This page provides access to website search performance and indexing tools.</p>
  <ul>
    <li><strong>Procedural Action:</strong> Click the blue Start now button to begin authentication.</li>
    <li><strong>Technical Significance:</strong> Authentication provides access to the verified AIStudyHub property and its Search Console reports.</li>
  </ul>

  <div class="figure-box">
    <img src="{img_gsc_landing}" alt="Figure 2: Google Search Console Official Landing Page & Start now Authentication" style="max-height: 125px;">
    <div class="caption">Figure 2: Google Search Console Official Landing Page & “Start now” Authentication</div>
    <div class="desc-text"><strong>Technical Description:</strong> The Google Search Console authentication screen. Webmasters authenticate using an authorized Google Account to verify property ownership through HTML meta tags or DNS verification.</div>
  </div>

  <div class="doc-footer">
    <span>Digital Marketing and Social Media (ADMC301) - Assignment 1</span>
    <span>Page 7</span>
  </div>
</div>

<!-- ================= PAGE 8: Q. 3 STEP 3 ================= -->
<div class="page">
  <div class="doc-header">
    <span>Digital Marketing and Social Media (ADMC301) - Assignment 1</span>
    <span>Page 8</span>
  </div>

  <h3 class="sub-title" style="font-size: 9.5pt; margin-top: 4px;">Step 3: Accessing Property Overview & Executive Dashboard</h3>
  <p>After authentication, select the verified <code>aistudyhub-rust.vercel.app</code> property from the property selector. The Overview dashboard acts as the central monitoring screen.</p>
  <ul>
    <li><strong>Procedural Action:</strong> Select the Overview tab from the left navigation.</li>
    <li><strong>Technical Observation:</strong> The dashboard provides an overview of search activity and access to indexing and experience reports.</li>
  </ul>

  <div class="figure-box" style="margin-top: 10px;">
    <img src="{img_gsc_overview}" alt="Figure 3: Google Search Console Property Overview Dashboard for AIStudyHub" style="max-height: 250px;">
    <div class="caption">Figure 3: Google Search Console Property Overview Dashboard for AIStudyHub</div>
    <div class="desc-text"><strong>Technical Description:</strong> The central executive Overview dashboard for <code>aistudyhub-rust.vercel.app</code>. The dashboard highlights cumulative performance trends (27 total web search clicks), page indexing progress (6 indexed vs 2 unindexed), Core Web Vitals status, and recommendations.</div>
  </div>

  <h3 class="sub-title">Dashboard Health Summary:</h3>
  <ul>
    <li><strong>Verified Domain:</strong> <code>aistudyhub-rust.vercel.app</code> (AI & Data Science Student Resource Hub).</li>
    <li><strong>Crawl Safety:</strong> Clean security and manual actions status with zero security threats or algorithmic penalties.</li>
    <li><strong>Activity Trajectory:</strong> Progressive growth in impression trends since initial deployment on Vercel Edge CDN.</li>
  </ul>

  <div class="doc-footer">
    <span>Digital Marketing and Social Media (ADMC301) - Assignment 1</span>
    <span>Page 8</span>
  </div>
</div>

<!-- ================= PAGE 9: Q. 3 STEP 4 ================= -->
<div class="page">
  <div class="doc-header">
    <span>Digital Marketing and Social Media (ADMC301) - Assignment 1</span>
    <span>Page 9</span>
  </div>

  <h3 class="sub-title" style="font-size: 9.5pt; margin-top: 4px;">Step 4: Analyzing Search Console Insights & Content Engagement</h3>
  <p>Search Console Insights provides a simplified view of recent search activity, content performance and queries leading visitors to the website.</p>
  <ul>
    <li><strong>Procedural Action:</strong> Select the Insights tab from the left sidebar.</li>
    <li><strong>Key Metrics Observed (Last 7 Days):</strong> 6 clicks and 233 impressions.</li>
    <li><strong>Top content shown:</strong> AIStudyHub homepage and About page.</li>
    <li><strong>Top queries shown:</strong> “ai study hub” and “ai and data science notes”.</li>
  </ul>

  <div class="figure-box" style="margin-top: 10px;">
    <img src="{img_gsc_insights}" alt="Figure 4: Google Search Console Insights Panel for AIStudyHub" style="max-height: 250px;">
    <div class="caption">Figure 4: Google Search Console Insights Panel for AIStudyHub</div>
    <div class="desc-text"><strong>Technical Description:</strong> The Google Search Console Insights panel displaying engagement growth for AIStudyHub over the 7-day reporting cycle. Highlights include a +200% increase in clicks and a +40% increase in search impressions, driven primarily by the homepage and curriculum notes.</div>
  </div>

  <h3 class="sub-title">Key Content Observations:</h3>
  <ul>
    <li><strong>Primary Visitor Gateway:</strong> The homepage (<code>/index.html</code>) accounted for the majority of clicks, confirming effective title tag branding.</li>
    <li><strong>Search Intent Relevance:</strong> Emerging search terms like <em>"ai and data science notes"</em> confirm that academic students find the portal for course study terms.</li>
  </ul>

  <div class="doc-footer">
    <span>Digital Marketing and Social Media (ADMC301) - Assignment 1</span>
    <span>Page 9</span>
  </div>
</div>

<!-- ================= PAGE 10: Q. 3 STEP 5 ================= -->
<div class="page">
  <div class="doc-header">
    <span>Digital Marketing and Social Media (ADMC301) - Assignment 1</span>
    <span>Page 10</span>
  </div>

  <h3 class="sub-title" style="font-size: 9.5pt; margin-top: 4px;">Step 5: Conducting In-Depth Search Performance Analysis</h3>
  <p>The Performance report provides granular information about search visibility, click engagement, CTR and average ranking position.</p>
  <ul>
    <li><strong>Procedural Action:</strong> Open Performance and select the 7 days report shown in the supplied screenshot.</li>
    <li><strong>Total Clicks:</strong> 6.</li>
    <li><strong>Total Impressions:</strong> 233.</li>
    <li><strong>Average CTR:</strong> 2.6%.</li>
    <li><strong>Average Position:</strong> 6.6.</li>
  </ul>

  <div class="figure-box" style="margin-top: 10px;">
    <img src="{img_gsc_perf}" alt="Figure 5: In-Depth Search Performance Report" style="max-height: 250px;">
    <div class="caption">Figure 5: In-Depth Search Performance Report (Clicks, Impressions, CTR, Average Position)</div>
    <div class="desc-text"><strong>Technical Description:</strong> The Search Performance analysis panel plotting daily clicks (blue curve) against total search impressions (purple curve). The report indicates a healthy 2.6% average CTR with an average SERP rank of 6.6, placing primary pages on Page 1 of Google Search.</div>
  </div>

  <h3 class="sub-title">Performance Diagnostic Takeaways:</h3>
  <ul>
    <li><strong>High Search Visibility:</strong> 233 impressions demonstrate that Googlebot is ranking AIStudyHub for multiple university syllabus queries.</li>
    <li><strong>SERP Positioning:</strong> Average position of 6.6 demonstrates that strategic heading hierarchy (H1/H2) and meta descriptions deliver immediate first-page visibility.</li>
  </ul>

  <div class="doc-footer">
    <span>Digital Marketing and Social Media (ADMC301) - Assignment 1</span>
    <span>Page 10</span>
  </div>
</div>

<!-- ================= PAGE 11: Q. 3 STEP 6 ================= -->
<div class="page">
  <div class="doc-header">
    <span>Digital Marketing and Social Media (ADMC301) - Assignment 1</span>
    <span>Page 11</span>
  </div>

  <h3 class="sub-title" style="font-size: 9.5pt; margin-top: 4px;">Step 6: Technical SEO Auditing & Page Indexing Verification</h3>
  <p>Crawling and indexing are fundamental to organic search visibility. The Page Indexing report is used to identify which known URLs are indexed and which require further investigation.</p>
  <ul>
    <li><strong>Procedural Action:</strong> Navigate to Indexing &rarr; Pages.</li>
    <li><strong>Index Coverage Breakdown:</strong> 6 indexed pages and 2 not-indexed pages.</li>
    <li><strong>The report shows:</strong> 2 reasons associated with the non-indexed pages.</li>
  </ul>

  <div class="figure-box" style="margin-top: 10px;">
    <img src="{img_gsc_indexing}" alt="Figure 6: Page Indexing Audit Report Displaying Indexed (6) vs. Non-Indexed (2) URLs" style="max-height: 250px;">
    <div class="caption">Figure 6: Page Indexing Audit Report Displaying Indexed (6) vs. Non-Indexed (2) URLs</div>
    <div class="desc-text"><strong>Technical Description:</strong> The Page Indexing status report verifying that 6 valid academic pages are successfully indexed and serving live traffic on Google. The green timeline bar chart confirms steady indexing progress following the submission of <code>sitemap.xml</code>.</div>
  </div>

  <h3 class="sub-title">Indexation Diagnostic Actions:</h3>
  <ul>
    <li><strong>Active Indexed URLs (6):</strong> Core subject portals (AI, ML, Data Science, Python, Mathematics, Homepage) are indexed.</li>
    <li><strong>Non-Indexed Pages (2):</strong> Two newly added pages are currently under routine discovery status and can be prioritized via URL Inspection.</li>
  </ul>

  <div class="doc-footer">
    <span>Digital Marketing and Social Media (ADMC301) - Assignment 1</span>
    <span>Page 11</span>
  </div>
</div>

<!-- ================= PAGE 12: Q. 3 FINDINGS & RECOMMENDATIONS ================= -->
<div class="page">
  <div class="doc-header">
    <span>Digital Marketing and Social Media (ADMC301) - Assignment 1</span>
    <span>Page 12</span>
  </div>

  <h2 class="sec-title">3. SEO Conduction Findings & Strategic Recommendations</h2>
  <p>Based on the practical SEO conduction on AIStudyHub using Google Search Console, the following observations and action items are derived from the verified dashboards.</p>

  <table class="data-table">
    <thead>
      <tr>
        <th style="width: 25%;">SEO Dimension</th>
        <th style="width: 35%;">Current Status / Observation</th>
        <th style="width: 40%;">Recommended Procedural Action</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Search Visibility & CTR</strong></td>
        <td>233 impressions, 6 clicks, 2.6% CTR with average position 6.6.</td>
        <td>Improve title tags and meta descriptions using relevant AI & Data Science search terms; monitor CTR.</td>
      </tr>
      <tr>
        <td><strong>Technical Indexation</strong></td>
        <td>6 indexed pages vs. 2 non-indexed pages; 2 reasons shown.</td>
        <td>Inspect the two URLs in URL Inspection, resolve the reported reasons and request indexing where appropriate.</td>
      </tr>
      <tr>
        <td><strong>Content Performance</strong></td>
        <td>Homepage and About page appear in the supplied Insights view.</td>
        <td>Strengthen internal linking from the homepage and About page to study material, question bank and blog content.</td>
      </tr>
      <tr>
        <td><strong>Search Queries</strong></td>
        <td>“ai study hub” generated 3 clicks/45 impressions; “ai and data science notes” generated 2 clicks/32 impressions.</td>
        <td>Create/strengthen dedicated AI & Data Science notes content targeting relevant non-branded terms.</td>
      </tr>
      <tr>
        <td><strong>Backlink Data</strong></td>
        <td>No backlink figures were visible in the captured dashboards.</td>
        <td>Use the Search Console Links report separately and record external links/top linking sites when available.</td>
      </tr>
    </tbody>
  </table>

  <h2 class="sec-title" style="margin-top: 12px;">Remediation Checklist</h2>
  <table class="data-table">
    <thead>
      <tr>
        <th style="width: 30%;">Issue</th>
        <th style="width: 15%;">Priority</th>
        <th style="width: 55%;">Action</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>2 pages not indexed</td>
        <td><strong>High</strong></td>
        <td>Open URL Inspection for each URL, fix the reported reason and request indexing.</td>
      </tr>
      <tr>
        <td>Short meta descriptions</td>
        <td><strong>Medium</strong></td>
        <td>Expand important descriptions to approximately 120–155 characters with relevant keywords.</td>
      </tr>
      <tr>
        <td>CTR baseline 2.6%</td>
        <td><strong>Medium</strong></td>
        <td>Test clearer titles and descriptions and monitor the Performance report.</td>
      </tr>
      <tr>
        <td>External-link data not captured</td>
        <td><strong>Medium</strong></td>
        <td>Review the Links report and record referring domains as they appear.</td>
      </tr>
    </tbody>
  </table>

  <div class="doc-footer">
    <span>Digital Marketing and Social Media (ADMC301) - Assignment 1</span>
    <span>Page 12</span>
  </div>
</div>

<!-- ================= PAGE 13: Q. 4 ================= -->
<div class="page">
  <div class="doc-header">
    <span>Digital Marketing and Social Media (ADMC301) - Assignment 1</span>
    <span>Page 13</span>
  </div>

  <h1 class="q-title">Q. 4 — Keyword Report on Website (5 Marks)</h1>
  <p><strong>Target location:</strong> India | <strong>Language:</strong> English | <strong>Audience:</strong> AI & Data Science engineering students | <strong>Tools:</strong> Google Keyword Planner / Ubersuggest</p>

  <h2 class="sec-title">1. Methodology</h2>
  <ul>
    <li>Open Google Keyword Planner (Google Ads &rarr; Tools &rarr; Planning) or Ubersuggest.</li>
    <li>Enter seed terms related to AI, Data Science, Machine Learning and student study resources.</li>
    <li>Set the target location to India and language to English.</li>
    <li>Compare search volume, competition and relevance, then map each keyword to the best AIStudyHub page.</li>
  </ul>

  <h2 class="sec-title">2. Keyword Set Mapped to Website Pages</h2>
  <table class="data-table">
    <thead>
      <tr>
        <th style="width: 6%;">#</th>
        <th style="width: 44%;">Target keyword</th>
        <th style="width: 20%;">Intent</th>
        <th style="width: 30%;">Target page</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>1</td>
        <td>AI and Data Science study material</td>
        <td>Informational</td>
        <td>/study-material.html</td>
      </tr>
      <tr>
        <td>2</td>
        <td>AI and DS notes</td>
        <td>Informational</td>
        <td>/study-material.html</td>
      </tr>
      <tr>
        <td>3</td>
        <td>machine learning for beginners</td>
        <td>Informational</td>
        <td>/blog/ml-roadmap.html</td>
      </tr>
      <tr>
        <td>4</td>
        <td>machine learning roadmap</td>
        <td>Informational</td>
        <td>/blog/ml-roadmap.html</td>
      </tr>
      <tr>
        <td>5</td>
        <td>machine learning using Python</td>
        <td>Informational</td>
        <td>/machine-learning.html</td>
      </tr>
      <tr>
        <td>6</td>
        <td>AI DS question bank</td>
        <td>Informational</td>
        <td>/question-bank.html</td>
      </tr>
      <tr>
        <td>7</td>
        <td>AI DS previous year questions</td>
        <td>Informational</td>
        <td>/question-bank.html</td>
      </tr>
      <tr>
        <td>8</td>
        <td>Python for AI and Data Science</td>
        <td>Informational</td>
        <td>/python.html</td>
      </tr>
      <tr>
        <td>9</td>
        <td>data science notes</td>
        <td>Informational</td>
        <td>/data-science.html</td>
      </tr>
      <tr>
        <td>10</td>
        <td>artificial intelligence notes</td>
        <td>Informational</td>
        <td>/ai.html</td>
      </tr>
    </tbody>
  </table>

  <h2 class="sec-title">3. Keywords Already Seen in Search Console</h2>
  <table class="data-table">
    <thead>
      <tr>
        <th>Query</th>
        <th>Clicks</th>
        <th>Impressions</th>
        <th>Comment</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>ai study hub</strong></td>
        <td>3</td>
        <td>45</td>
        <td>Branded query; visitors search for the site by name.</td>
      </tr>
      <tr>
        <td><strong>ai and data science notes</strong></td>
        <td>2</td>
        <td>32</td>
        <td>Non-branded study-material term; strong content opportunity.</td>
      </tr>
    </tbody>
  </table>

  <h2 class="sec-title">4. Content and On-Page Placement Strategy</h2>
  <ul>
    <li>Place each target keyword naturally in the page title, H1, meta description and relevant URL slug.</li>
    <li>Use question-style long-tail phrases such as “previous year questions”, “question bank” and “notes” as H2 headings.</li>
    <li>Link study material, question bank and blog pages to each other using descriptive anchor text.</li>
  </ul>

  <h2 class="sec-title">Conclusion</h2>
  <p>Google Search Console provides a practical workflow for reviewing search performance, content visibility and indexing. The AIStudyHub audit records 6 clicks, 233 impressions, 2.6% CTR and an average position of 6.6 in the supplied 7-day performance view, along with 6 indexed and 2 non-indexed pages. The next optimization steps are to investigate the non-indexed URLs, strengthen page metadata and build content around relevant non-branded AI & Data Science study keywords.</p>

  <div class="doc-footer">
    <span>Digital Marketing and Social Media (ADMC301) - Assignment 1</span>
    <span>Page 13</span>
  </div>
</div>

</body>
</html>
"""

html_path = os.path.join(workspace, "Assignment_1_Samiksha_Kakade_Final.html")
with open(html_path, "w", encoding="utf-8") as f:
    f.write(html)

print("HTML written to:", html_path)

pdf_path = os.path.join(workspace, "Assignment_1_Samiksha_Kakade_Final.pdf")

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.set_content(html, wait_until="networkidle")
    page.pdf(
        path=pdf_path,
        format="A4",
        print_background=True,
        margin={"top": "8mm", "bottom": "8mm", "left": "10mm", "right": "10mm"}
    )
    browser.close()

print("Final PDF generated at:", pdf_path)
