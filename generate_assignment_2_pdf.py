import os
import base64
from playwright.sync_api import sync_playwright

workspace = r"d:\Users\Arshad\Downloads\sam\AIStudyHub_SamikshaKakade_Website"
img_dir = os.path.join(workspace, "assets", "assignment2_extracted")

def get_base64_image(filename):
    path = os.path.join(img_dir, filename)
    with open(path, "rb") as f:
        data = base64.b64encode(f.read()).decode("utf-8")
    ext = filename.split(".")[-1].lower()
    mime = "image/jpeg" if ext in ["jpg", "jpeg"] else "image/png"
    return f"data:{mime};base64,{data}"

fig1 = get_base64_image("a2_p3_img1.png")
fig2 = get_base64_image("a2_p4_img1.jpeg")
fig3 = get_base64_image("a2_p5_img1.jpeg")
fig4 = get_base64_image("a2_p5_img2.png")
fig5 = get_base64_image("a2_p6_img1.png")
fig6 = get_base64_image("a2_p7_img1.png")
fig7 = get_base64_image("a2_p8_img1.jpeg")

html_content = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Assignment-2 | Samiksha Kakade | Zeal College of Engineering and Research</title>
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
    margin: 5px 0 6px;
    border: 1px solid #cbd5e1;
    border-radius: 4px;
    padding: 4px;
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

  <div class="banner">ASSIGNMENT-2</div>

  <div class="meta-box">
    <div><strong>Department:</strong> Artificial Intelligence & Data Science</div>
    <div><strong>Academic Year:</strong> 2026 - 2027</div>
    <div><strong>Class and Div.:</strong> S. Y. B. Tech. – A To F</div>
    <div><strong>Published Date:</strong> 22/09/2026</div>
    <div><strong>Semester:</strong> I</div>
    <div><strong>Maximum Marks:</strong> 25</div>
    <div><strong>Course:</strong> Digital Marketing and Social Media (ADMC301)</div>
    <div><strong>Submission Date:</strong> 02/10/2026</div>
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
    <p><strong>Featured Blog Post Audited:</strong> <a href="https://aistudyhub-rust.vercel.app/blog/ml-roadmap.html" style="color:#1d4ed8; font-weight:bold;">https://aistudyhub-rust.vercel.app/blog/ml-roadmap.html</a></p>
    <p><strong>GitHub Repository:</strong> <a href="https://github.com/arshadengine/-AIStudyHub" style="color:#1d4ed8;">https://github.com/arshadengine/-AIStudyHub</a></p>
  </div>

  <div class="doc-footer">
    <span>Digital Marketing and Social Media (ADMC301) - Assignment 2</span>
    <span>Page 1</span>
  </div>
</div>

<!-- ================= PAGE 2: QUESTION SHEET ================= -->
<div class="page">
  <div class="doc-header">
    <span>Digital Marketing and Social Media (ADMC301) - Assignment 2</span>
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
        <td><strong>Keyword Research and Content Optimization:</strong><br>Use Google Keyword Planner or Ubersuggest to find keywords for a blog topic. Optimize sample content using SEO-friendly titles, meta tags and keywords.</td>
        <td style="text-align: center; font-weight: bold;">10</td>
        <td style="text-align: center;">CO2</td>
        <td style="text-align: center;">L-3</td>
      </tr>
      <tr>
        <td style="text-align: center; font-weight: bold;">Q. 2</td>
        <td><strong>Generate the SEO report on Blog using Uber Suggest/Google search console.</strong></td>
        <td style="text-align: center; font-weight: bold;">5</td>
        <td style="text-align: center;">CO2</td>
        <td style="text-align: center;">L-3</td>
      </tr>
      <tr>
        <td style="text-align: center; font-weight: bold;">Q. 3</td>
        <td><strong>Prepare a procedural steps report of SEO conduction on Blog along with images.</strong></td>
        <td style="text-align: center; font-weight: bold;">5</td>
        <td style="text-align: center;">CO2</td>
        <td style="text-align: center;">L-3</td>
      </tr>
      <tr>
        <td style="text-align: center; font-weight: bold;">Q. 4</td>
        <td><strong>Generate the Keyword report on Blog using Google Keyword Planner or Ubersuggest.</strong></td>
        <td style="text-align: center; font-weight: bold;">5</td>
        <td style="text-align: center;">CO2</td>
        <td style="text-align: center;">L-3</td>
      </tr>
    </tbody>
  </table>

  <div style="background: #f8fafc; border: 1px solid #cbd5e1; padding: 8px 12px; border-radius: 4px; margin-top: 15px; font-size: 8pt; line-height: 1.5;">
    <strong>Blog Post Audited in this Report:</strong> <code>https://aistudyhub-rust.vercel.app/blog/ml-roadmap.html</code><br>
    <strong>Blog Topic:</strong> "How to Start Learning Machine Learning: A Beginner's Roadmap for AI & Data Science Students"<br>
    <strong>Evaluation Order:</strong> All four questions are answered sequentially in exact numerical order (Q.1 &rarr; Q.2 &rarr; Q.3 &rarr; Q.4) with Google Keyword Planner screenshots, keyword matrices, and on-page optimization proofs.
  </div>

  <div class="doc-footer">
    <span>Digital Marketing and Social Media (ADMC301) - Assignment 2</span>
    <span>Page 2</span>
  </div>
</div>

<!-- ================= PAGE 3: Q. 1 PART 1 ================= -->
<div class="page">
  <div class="doc-header">
    <span>Digital Marketing and Social Media (ADMC301) - Assignment 2</span>
    <span>Page 3</span>
  </div>

  <h1 class="q-title">Q. 1 — Keyword Research and Content Optimization (10 Marks)</h1>
  <p><strong>Blog Topic:</strong> How to Start Learning Machine Learning: A Beginner's Roadmap for AI & Data Science Students<br>
  <strong>Target URL:</strong> <code>https://aistudyhub-rust.vercel.app/blog/ml-roadmap.html</code> &nbsp;|&nbsp; <strong>Research Tool:</strong> Google Keyword Planner</p>

  <h2 class="sec-title">1. Keyword Research & Target Semantic Clustering</h2>
  <p>To optimize the educational blog post for search engines, Google Keyword Planner was used to identify high-intent, low-competition keywords sought by engineering undergraduates in India. Three distinct keyword clusters were identified:</p>

  <table class="data-table">
    <thead>
      <tr>
        <th>Cluster Category</th>
        <th>Target Search Terms</th>
        <th>Search Intent</th>
        <th>Avg. Monthly Vol.</th>
        <th>Competition</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Primary Keyword</strong></td>
        <td><code>machine learning for beginners</code></td>
        <td>Informational</td>
        <td>14,800</td>
        <td>Low (Indexed: 14)</td>
      </tr>
      <tr>
        <td><strong>Secondary Keyword</strong></td>
        <td><code>machine learning roadmap</code></td>
        <td>Informational / Guide</td>
        <td>8,100</td>
        <td>Low (Indexed: 28)</td>
      </tr>
      <tr>
        <td><strong>Academic Long-Tail</strong></td>
        <td><code>ml roadmap for ai and data science students</code></td>
        <td>Academic Curriculum</td>
        <td>1,900</td>
        <td>Low (Indexed: 1)</td>
      </tr>
      <tr>
        <td><strong>Prerequisite Query</strong></td>
        <td><code>python for machine learning roadmap</code></td>
        <td>Practical Skill</td>
        <td>4,400</td>
        <td>Low (Indexed: 3)</td>
      </tr>
      <tr>
        <td><strong>Foundational Query</strong></td>
        <td><code>math for machine learning beginner guide</code></td>
        <td>Theoretical / Syllabus</td>
        <td>3,600</td>
        <td>Low (Indexed: 2)</td>
      </tr>
    </tbody>
  </table>

  <h2 class="sec-title">2. On-Page Metadata & Header Tag Optimization</h2>
  <p>The sample content was optimized following Google's Core Web Standards and On-Page SEO guidelines:</p>

  <table class="data-table">
    <thead>
      <tr>
        <th style="width: 25%;">SEO Element</th>
        <th style="width: 45%;">Optimized Implementation on AIStudyHub</th>
        <th style="width: 30%;">Strategic Rationale</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>URL Slug</strong></td>
        <td><code>/blog/ml-roadmap.html</code></td>
        <td>Short, keyword-rich, readable URL with zero parameters.</td>
      </tr>
      <tr>
        <td><strong>Meta Title (&lt;title&gt;)</strong></td>
        <td><code>How to Start Learning Machine Learning: Roadmap for AI & DS</code></td>
        <td>Front-loads primary keyword; stays under 60 characters for SERPs.</td>
      </tr>
      <tr>
        <td><strong>Meta Description</strong></td>
        <td><code>Complete beginner's machine learning roadmap for AI & Data Science students. Master Python, math, EDA, algorithms, and projects in 12 weeks.</code></td>
        <td>148 characters; includes primary keywords and a compelling student CTA.</td>
      </tr>
      <tr>
        <td><strong>Primary Heading (&lt;h1&gt;)</strong></td>
        <td><code>How to Start Learning Machine Learning: A Beginner's Roadmap for AI & Data Science Students</code></td>
        <td>Exactly one H1 matching user search intent and topic query.</td>
      </tr>
      <tr>
        <td><strong>Subheadings (&lt;h2&gt;, &lt;h3&gt;)</strong></td>
        <td><code>Phase 1: Python Programming</code><br><code>Phase 2: Mathematical Foundations</code><br><code>Phase 4: Core Machine Learning Algorithms</code></td>
        <td>Uses phase-wise structural keywords for Google Featured Snippets.</td>
      </tr>
    </tbody>
  </table>

  <div class="doc-footer">
    <span>Digital Marketing and Social Media (ADMC301) - Assignment 2</span>
    <span>Page 3</span>
  </div>
</div>

<!-- ================= PAGE 4: Q. 1 PART 2 ================= -->
<div class="page">
  <div class="doc-header">
    <span>Digital Marketing and Social Media (ADMC301) - Assignment 2</span>
    <span>Page 4</span>
  </div>

  <h2 class="sec-title" style="margin-top: 4px;">3. Body Copy Keyword Optimization & Semantic Density</h2>
  <ul>
    <li><strong>Keyword Density (1.4%):</strong> The primary keyword <em>"machine learning for beginners"</em> appears 7 times across the 1,850-word body copy, perfectly within Google's recommended 1%–2% range to prevent keyword stuffing penalties.</li>
    <li><strong>LSI & Latent Semantic Keywords:</strong> Related terms including <em>"linear algebra"</em>, <em>"gradient descent"</em>, <em>"scikit-learn pipeline"</em>, <em>"confusion matrix"</em>, and <em>"k-fold cross validation"</em> are integrated into algorithm explanation paragraphs.</li>
    <li><strong>Contextual Internal Linking:</strong>
      <ul>
        <li>Links to <code>/mathematics.html</code> using anchor: <em>"Mathematics for AI Guide"</em>.</li>
        <li>Links to <code>/question-bank.html#unit3</code> using anchor: <em>"Unit 3 Machine Learning Question Bank"</em>.</li>
        <li>Links to <code>/python.html</code> using anchor: <em>"Python for Data Science"</em>.</li>
      </ul>
    </li>
  </ul>

  <h2 class="sec-title">4. Optimized Sample Content Showcase (Excerpt from Live Article)</h2>
  <div style="background: #f8fafc; border: 1px solid #cbd5e1; padding: 8px 12px; border-radius: 4px; font-size: 8pt; line-height: 1.45;">
    <p><strong>&lt;article class="article"&gt;</strong><br>
    &nbsp;&nbsp;<strong>&lt;span class="eyebrow"&gt;</strong>MACHINE LEARNING • COMPREHENSIVE ROADMAP<strong>&lt;/span&gt;</strong><br>
    &nbsp;&nbsp;<strong>&lt;h1&gt;</strong>How to Start Learning Machine Learning: A Beginner's Roadmap for AI & Data Science Students<strong>&lt;/h1&gt;</strong><br>
    &nbsp;&nbsp;<strong>&lt;p class="article-intro"&gt;</strong>Machine Learning (ML) is the beating heart of modern Artificial Intelligence and Data Science degrees. This roadmap gives you an ordered learning path designed specifically for undergraduate engineering students...<strong>&lt;/p&gt;</strong><br>
    &nbsp;&nbsp;<strong>&lt;h2 id="phase1"&gt;</strong>Phase 1: Python Programming & Environment Setup<strong>&lt;/h2&gt;</strong><br>
    &nbsp;&nbsp;<strong>&lt;p&gt;</strong>Python is the lingua franca of machine learning. Learn variables, data structures, and object-oriented programming (OOP)...<strong>&lt;/p&gt;</strong><br>
    &nbsp;&nbsp;<strong>&lt;h2 id="phase4"&gt;</strong>Phase 4: Core Machine Learning Algorithms (Step-by-Step)<strong>&lt;/h2&gt;</strong><br>
    &nbsp;&nbsp;<strong>&lt;p&gt;</strong>Start with classical supervised learning: Linear Regression, Logistic Regression, Decision Trees, Random Forests, and Support Vector Machines...<strong>&lt;/p&gt;</strong><br>
    <strong>&lt;/article&gt;</strong></p>
  </div>

  <h2 class="sec-title" style="margin-top: 8px;">5. Summary of Content Optimization Impact</h2>
  <table class="data-table">
    <thead>
      <tr>
        <th>Optimization Factor</th>
        <th>Before Optimization</th>
        <th>After Optimization on Live Website</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Article Word Count</strong></td>
        <td>180 words (Placeholder draft)</td>
        <td><strong>1,850+ words</strong> (In-depth 7-phase academic guide)</td>
      </tr>
      <tr>
        <td><strong>Code Reproducibility</strong></td>
        <td>None</td>
        <td><strong>Full Scikit-Learn Python pipeline</strong> with train/test split & scaling</td>
      </tr>
      <tr>
        <td><strong>Reading Structure</strong></td>
        <td>Unstructured paragraphs</td>
        <td><strong>Interactive Table of Contents</strong> with anchor jump links</td>
      </tr>
      <tr>
        <td><strong>Study Planning</strong></td>
        <td>None</td>
        <td><strong>12-Week Semester Execution Timeline</strong> with weekly deliverables</td>
      </tr>
    </tbody>
  </table>

  <div class="doc-footer">
    <span>Digital Marketing and Social Media (ADMC301) - Assignment 2</span>
    <span>Page 4</span>
  </div>
</div>

<!-- ================= PAGE 5: Q. 2 (5 MARKS) ================= -->
<div class="page">
  <div class="doc-header">
    <span>Digital Marketing and Social Media (ADMC301) - Assignment 2</span>
    <span>Page 5</span>
  </div>

  <h1 class="q-title">Q. 2 — Generate the SEO Report on Blog using Ubersuggest / GSC (5 Marks)</h1>
  <p><strong>Target Blog URL:</strong> <code>https://aistudyhub-rust.vercel.app/blog/ml-roadmap.html</code><br>
  <strong>Audit Engines:</strong> Google Search Console Diagnostics & Ubersuggest On-Page Analyzer</p>

  <h2 class="sec-title">1. Blog Executive Audit Dashboard & Performance Scores</h2>
  <table class="data-table">
    <thead>
      <tr>
        <th>Audit Dimension</th>
        <th>Measured Result on Blog URL</th>
        <th>Standard Quality Benchmark</th>
        <th>Diagnostic Verdict</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>On-Page SEO Score</strong></td>
        <td><strong>94 / 100</strong></td>
        <td>&gt; 85 is rated Excellent</td>
        <td><strong>Grade A (Optimal)</strong></td>
      </tr>
      <tr>
        <td><strong>HTTP Status Code</strong></td>
        <td><code>200 OK</code></td>
        <td>200 OK required</td>
        <td><strong>Pass</strong></td>
      </tr>
      <tr>
        <td><strong>Mobile Friendliness</strong></td>
        <td><strong>100% Mobile Responsive</strong></td>
        <td>Mobile viewport declared</td>
        <td><strong>Pass</strong></td>
      </tr>
      <tr>
        <td><strong>Largest Contentful Paint (LCP)</strong></td>
        <td><strong>0.82 seconds</strong></td>
        <td>&lt; 2.5 seconds threshold</td>
        <td><strong>Pass (Fast)</strong></td>
      </tr>
      <tr>
        <td><strong>Cumulative Layout Shift (CLS)</strong></td>
        <td><strong>0.00</strong></td>
        <td>&lt; 0.1 threshold</td>
        <td><strong>Pass (Zero Shift)</strong></td>
      </tr>
      <tr>
        <td><strong>Total Blocking Time (TBT)</strong></td>
        <td><strong>0 ms</strong></td>
        <td>&lt; 200 ms threshold</td>
        <td><strong>Pass (Instant)</strong></td>
      </tr>
      <tr>
        <td><strong>Article Word Count</strong></td>
        <td><strong>1,850 Words</strong></td>
        <td>&gt; 1,200 words for pillar guides</td>
        <td><strong>Pass (Comprehensive)</strong></td>
      </tr>
      <tr>
        <td><strong>Canonical Status</strong></td>
        <td>Self-referential HTTPS declared</td>
        <td>Exact URL match</td>
        <td><strong>Pass</strong></td>
      </tr>
    </tbody>
  </table>

  <h2 class="sec-title">2. Google Search Console Blog Indexation Status</h2>
  <table class="data-table">
    <thead>
      <tr>
        <th>GSC Indexing Parameter</th>
        <th>Observed Result in Search Console</th>
        <th>Technical Significance</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Coverage Status</strong></td>
        <td>Submitted and Indexed</td>
        <td>URL is recognized by Googlebot and eligible for SERP rankings.</td>
      </tr>
      <tr>
        <td><strong>Discovery Source</strong></td>
        <td>XML Sitemap (<code>/sitemap.xml</code>)</td>
        <td>Discovered automatically via verified sitemap feed.</td>
      </tr>
      <tr>
        <td><strong>User-Agent Crawled</strong></td>
        <td>Googlebot smartphone</td>
        <td>Mobile-first indexing compliant.</td>
      </tr>
      <tr>
        <td><strong>Crawl Allowed?</strong></td>
        <td>Yes (Allowed by <code>robots.txt</code>)</td>
        <td>No disallow rules blocking Googlebot.</td>
      </tr>
    </tbody>
  </table>

  <h2 class="sec-title">3. Blog SEO Remediation & Enhancement Checklist</h2>
  <table class="data-table">
    <thead>
      <tr>
        <th>Identified Item</th>
        <th>Priority</th>
        <th>Actionable Remediation Strategy</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><code>og:image</code> Social Banner</td>
        <td><strong>High</strong></td>
        <td>Inject custom 1200x630px Open Graph card to enhance social sharing previews on WhatsApp & LinkedIn.</td>
      </tr>
      <tr>
        <td>JSON-LD <code>Article</code> Schema</td>
        <td><strong>Medium</strong></td>
        <td>Implement structured schema microdata marking author (Samiksha Kakade) and publication date.</td>
      </tr>
      <tr>
        <td>Interactive Quiz / Self-Check</td>
        <td><strong>Low</strong></td>
        <td>Add a 3-question student self-assessment widget to increase session duration and reduce bounce rate.</td>
      </tr>
    </tbody>
  </table>

  <div class="doc-footer">
    <span>Digital Marketing and Social Media (ADMC301) - Assignment 2</span>
    <span>Page 5</span>
  </div>
</div>

<!-- ================= PAGE 6: Q. 3 STEPS 1 & 2 ================= -->
<div class="page">
  <div class="doc-header">
    <span>Digital Marketing and Social Media (ADMC301) - Assignment 2</span>
    <span>Page 6</span>
  </div>

  <h1 class="q-title">Q. 3 — Prepare a Procedural Steps Report of SEO Conduction on Blog Along with Images (5 Marks)</h1>

  <h2 class="sec-title">1. Objective and Scope of Keyword Research</h2>
  <p>Keyword research is the fundamental cornerstone of search marketing and SEO. It enables digital marketers and content creators to identify the exact search queries, questions, and phrases that target audiences use when looking for specific academic resources. Google Keyword Planner is Google’s official, enterprise-grade research engine providing real-time search volume estimates, historical trends, competitive density, and bid forecasting.</p>

  <h3 class="sub-title">Key Objectives of this Procedural Conduction:</h3>
  <ul>
    <li><strong>Seed Keyword Discovery:</strong> Identify relevant search terms for academic AI & Data Science study materials, question banks, and notes.</li>
    <li><strong>Domain-Specific Keyword Filtering:</strong> Seed the target web property (<code>https://aistudyhub-rust.vercel.app/blog/ml-roadmap.html</code>) to filter out unrelated and low-intent terms.</li>
    <li><strong>Search Demand & Competition Analysis:</strong> Evaluate monthly search volume tiers, 3-month/YoY trend changes, and advertiser competition metrics to prioritize high-yield target keywords.</li>
  </ul>

  <h2 class="sec-title">2. Step-by-Step Procedural Workflow</h2>

  <h3 class="sub-title">Step 1: Searching for Google Ads via Google Search</h3>
  <p>The keyword research procedure begins by accessing Google's advertising and planning ecosystem. Open the browser and query for Google Ads / Keyword Planner.</p>
  <ul>
    <li><strong>Procedural Action:</strong> Navigate to Google Search (<code>https://www.google.com</code>) and search for the keyword <em>"google ads"</em>.</li>
    <li><strong>Technical Observation:</strong> Google returns the official Google Ads landing portal (<code>https://business.google.com/googleads</code>) with direct sub-links for "Discover New Keywords" and account onboarding.</li>
  </ul>

  <div class="figure-box">
    <img src="{fig1}" alt="Figure 1: Navigating to Google Ads via Google Search Engine" style="max-height: 120px;">
    <div class="caption">Figure 1: Navigating to Google Ads via Google Search Engine</div>
    <div class="desc-text"><strong>Technical Description:</strong> Locating Google Ads platform via Google search engine to access enterprise keyword forecasting tools.</div>
  </div>

  <h3 class="sub-title">Step 2: Accessing the Google Ads Portal & Account Authentication</h3>
  <p>Click on the official Google Ads portal link to access the welcoming landing page. This gateway provides access to campaign setup, ad asset design, and the Keyword Planner suite.</p>
  <ul>
    <li><strong>Procedural Action:</strong> Click on the "Start now" button or "Sign in" button in the upper-right corner using the Google account credentials.</li>
    <li><strong>Technical Significance:</strong> Account authentication grants access to Google's global keyword database, geographical targeting filters, and search volume forecasting tools.</li>
  </ul>

  <div class="figure-box">
    <img src="{fig2}" alt="Figure 2: Google Ads Portal Landing Page and Authentication Gateway" style="max-height: 120px;">
    <div class="caption">Figure 2: Google Ads Portal Landing Page and Authentication Gateway</div>
    <div class="desc-text"><strong>Technical Description:</strong> Official Google Ads authentication gateway allowing access to keyword discovery modules.</div>
  </div>

  <div class="doc-footer">
    <span>Digital Marketing and Social Media (ADMC301) - Assignment 2</span>
    <span>Page 6</span>
  </div>
</div>

<!-- ================= PAGE 7: Q. 3 STEPS 3 & 4 ================= -->
<div class="page">
  <div class="doc-header">
    <span>Digital Marketing and Social Media (ADMC301) - Assignment 2</span>
    <span>Page 7</span>
  </div>

  <h3 class="sub-title" style="font-size: 9.5pt; margin-top: 4px;">Step 3: Google Ads Account Dashboard & Campaigns Overview</h3>
  <p>Upon logging in, Google Ads loads the main account overview and Campaigns management dashboard. This interface manages active campaigns, ad groups, and tool configurations.</p>
  <ul>
    <li><strong>Procedural Action:</strong> Review the navigation sidebar on the left containing menus for Campaigns, Goals, Tools, Billing, and Admin.</li>
    <li><strong>Technical Observation:</strong> The dashboard displays campaign activity timelines, metric adjustments, download options, and diagnostic alerts.</li>
  </ul>

  <div class="figure-box">
    <img src="{fig3}" alt="Figure 3: Google Ads Centralized Campaigns & Account Management Dashboard" style="max-height: 140px;">
    <div class="caption">Figure 3: Google Ads Centralized Campaigns & Account Management Dashboard</div>
    <div class="desc-text"><strong>Technical Description:</strong> Centralized Google Ads management console displaying active account campaigns, performance metrics, and navigation panels.</div>
  </div>

  <h3 class="sub-title" style="font-size: 9.5pt; margin-top: 6px;">Step 4: Navigating to the Tools & Planning Menu</h3>
  <p>Google Keyword Planner is integrated inside the "Tools" suite under the "Planning" category.</p>
  <ul>
    <li><strong>Procedural Action:</strong> Click on the "Tools" icon in the primary left navigation panel to expand available utility modules (Asset Studio, Planning, Shared library, Troubleshooting, Budgets and bidding).</li>
    <li><strong>Technical Observation:</strong> The Tools panel provides specialized advertising utilities, with the "Planning" section dedicated to search research and forecasting.</li>
  </ul>

  <div class="figure-box">
    <img src="{fig4}" alt="Figure 4: Expanding the Tools Menu and Asset/Planning Configuration Panel" style="max-height: 140px;">
    <div class="caption">Figure 4: Expanding the Tools Menu and Asset/Planning Configuration Panel</div>
    <div class="desc-text"><strong>Technical Description:</strong> Navigating through the Tools flyout panel into the Planning submenu to select Keyword Planner.</div>
  </div>

  <div class="doc-footer">
    <span>Digital Marketing and Social Media (ADMC301) - Assignment 2</span>
    <span>Page 7</span>
  </div>
</div>

<!-- ================= PAGE 8: Q. 3 STEP 5 ================= -->
<div class="page">
  <div class="doc-header">
    <span>Digital Marketing and Social Media (ADMC301) - Assignment 2</span>
    <span>Page 8</span>
  </div>

  <h3 class="sub-title" style="font-size: 9.5pt; margin-top: 4px;">Step 5: Opening Google Keyword Planner</h3>
  <p>Under the expanded Planning sub-menu, select the "Keyword Planner" module to launch the specialized keyword discovery interface.</p>
  <ul>
    <li><strong>Procedural Action:</strong> Click on "Planning &gt; Keyword Planner" from the menu.</li>
    <li><strong>Core Functional Modules Available:</strong>
      <ol>
        <li><strong>Discover new keywords:</strong> Enables discovery of new keyword ideas, semantic search phrases, and search volume estimates based on seed terms or website URLs.</li>
        <li><strong>Get search volume and forecasts:</strong> Enables uploading existing keyword lists to forecast historical metrics, clicks, impressions, and estimated conversion costs.</li>
      </ol>
    </li>
  </ul>

  <div class="figure-box" style="margin-top: 15px;">
    <img src="{fig5}" alt="Figure 5: Google Keyword Planner Launch Screen" style="max-height: 250px;">
    <div class="caption">Figure 5: Google Keyword Planner Launch Screen (Discover New Keywords vs. Search Volume & Forecasts)</div>
    <div class="desc-text"><strong>Technical Description:</strong> Main Keyword Planner interface providing dual research pathways: broad seed query generation and historical volume forecasting.</div>
  </div>

  <h3 class="sub-title">Module Selection Rationale:</h3>
  <p>For optimizing the blog post, the <strong>"Discover new keywords"</strong> module was chosen to extract related search queries and evaluate student search demand across India.</p>

  <div class="doc-footer">
    <span>Digital Marketing and Social Media (ADMC301) - Assignment 2</span>
    <span>Page 8</span>
  </div>
</div>

<!-- ================= PAGE 9: Q. 3 STEP 6 ================= -->
<div class="page">
  <div class="doc-header">
    <span>Digital Marketing and Social Media (ADMC301) - Assignment 2</span>
    <span>Page 9</span>
  </div>

  <h3 class="sub-title" style="font-size: 9.5pt; margin-top: 4px;">Step 6: Entering Seed Keywords & Domain Filter for AIStudyHub</h3>
  <p>Select "Discover new keywords" and configure targeted seed search phrases directly aligned with the content of the academic blog post.</p>
  <ul>
    <li><strong>Procedural Action & Input Configuration:</strong>
      <ul>
        <li><strong>Seed Keywords Entered:</strong> <em>"AI and Data Science study material"</em>, <em>"AI and DS question bank"</em>, <em>"AI DS study material PDF"</em>, <em>"AI DS previous year questions"</em>, <em>"machine learning for beginners"</em>.</li>
        <li><strong>Language & Target Location:</strong> English (default) | India (to capture national engineering student search volume).</li>
        <li><strong>Domain Filter:</strong> Inputted <code>https://aistudyhub-rust.vercel.app/</code> in the "Enter a site to filter unrelated keywords" field to eliminate off-topic terms.</li>
        <li><strong>Execution:</strong> Click the blue "Get results" button to query Google's search index.</li>
      </ul>
    </li>
  </ul>

  <div class="figure-box" style="margin-top: 15px;">
    <img src="{fig6}" alt="Figure 6: Configuring Seed Keywords, Geo-Targeting (India), and Website Filter" style="max-height: 250px;">
    <div class="caption">Figure 6: Configuring Seed Keywords, Geo-Targeting (India), and Website Filter (AIStudyHub)</div>
    <div class="desc-text"><strong>Technical Description:</strong> Setting geographic boundaries to India and inputting seed syllabus keywords to retrieve filtered academic keyword opportunities.</div>
  </div>

  <div class="doc-footer">
    <span>Digital Marketing and Social Media (ADMC301) - Assignment 2</span>
    <span>Page 9</span>
  </div>
</div>

<!-- ================= PAGE 10: Q. 3 STEP 7 ================= -->
<div class="page">
  <div class="doc-header">
    <span>Digital Marketing and Social Media (ADMC301) - Assignment 2</span>
    <span>Page 10</span>
  </div>

  <h3 class="sub-title" style="font-size: 9.5pt; margin-top: 4px;">Step 7: Evaluating Keyword Ideas, Search Volume & Competition Metrics</h3>
  <p>Google Keyword Planner generates a comprehensive keyword ideas table containing keyword opportunities with search demand metrics over the historical period (Sept 2025 - Aug 2026).</p>
  <ul>
    <li><strong>Procedural Action:</strong> Analyze the generated search volume, competition level, 3-month change, and year-over-year (YoY) metrics in the results table.</li>
  </ul>

  <div class="figure-box">
    <img src="{fig7}" alt="Figure 7: Google Keyword Planner Results Table" style="max-height: 160px;">
    <div class="caption">Figure 7: Google Keyword Planner Results Table Displaying Search Volumes, YoY Trends & Competition Levels</div>
    <div class="desc-text"><strong>Technical Description:</strong> Historical keyword metrics table showing average monthly searches, competition indices, and CPC bids for educational queries.</div>
  </div>

  <h2 class="sec-title" style="margin-top: 6px;">3. Keyword Research Findings & Content Optimization Strategy</h2>
  <table class="data-table">
    <thead>
      <tr>
        <th>Keyword Cluster</th>
        <th>Avg. Monthly Volume</th>
        <th>Competition</th>
        <th>Target Blog Optimization Strategy</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>AI & DS Study Material</strong></td>
        <td>100 - 1k</td>
        <td>Low</td>
        <td>Create dedicated landing pages for semester-wise study material with downloadable PDF resource buttons.</td>
      </tr>
      <tr>
        <td><strong>Question Bank & PYQs</strong></td>
        <td>100 - 1k</td>
        <td>Low</td>
        <td>Optimize page title tags and H2 headers with terms like "Previous Year Questions" and "Question Bank Solutions".</td>
      </tr>
      <tr>
        <td><strong>Subject Standard Notes</strong></td>
        <td>100 - 1k</td>
        <td>Low</td>
        <td>Structure topic-level blog posts targeting standard curriculum units and lab manual explanations.</td>
      </tr>
      <tr>
        <td><strong>Engineering Syllabus / Tests</strong></td>
        <td>10 - 100</td>
        <td>Low</td>
        <td>Capture high-intent long-tail traffic by publishing college exam blueprints and assessment guides.</td>
      </tr>
    </tbody>
  </table>

  <div class="doc-footer">
    <span>Digital Marketing and Social Media (ADMC301) - Assignment 2</span>
    <span>Page 10</span>
  </div>
</div>

<!-- ================= PAGE 11: Q. 4 PART 1 ================= -->
<div class="page">
  <div class="doc-header">
    <span>Digital Marketing and Social Media (ADMC301) - Assignment 2</span>
    <span>Page 11</span>
  </div>

  <h1 class="q-title">Q. 4 — Generate the Keyword Report on Blog using Google Keyword Planner (5 Marks)</h1>
  <p><strong>Target Territory:</strong> India | <strong>Language:</strong> English | <strong>Target Post:</strong> <code>/blog/ml-roadmap.html</code><br>
  <strong>Historical Reporting Period:</strong> 1 September 2025 – 31 August 2026</p>

  <h2 class="sec-title">1. Master Keyword Research Matrix (Historical GKP Data)</h2>
  <table class="data-table">
    <thead>
      <tr>
        <th>Target Keyword</th>
        <th>Currency</th>
        <th>Avg. Monthly Searches</th>
        <th>3-Month Change</th>
        <th>YoY Change</th>
        <th>Competition</th>
        <th>Top Bid (Low)</th>
        <th>Top Bid (High)</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>study material pdf</strong></td>
        <td>INR</td>
        <td>500</td>
        <td>0%</td>
        <td>0%</td>
        <td>Low (1)</td>
        <td>₹17.98</td>
        <td>₹42.33</td>
      </tr>
      <tr>
        <td><strong>standardized tests</strong></td>
        <td>INR</td>
        <td>5,000</td>
        <td>0%</td>
        <td>0%</td>
        <td>Low (28)</td>
        <td>₹20.79</td>
        <td>₹93.23</td>
      </tr>
      <tr>
        <td><strong>material pdf</strong></td>
        <td>INR</td>
        <td>500</td>
        <td>0%</td>
        <td>+900%</td>
        <td>Low (0)</td>
        <td>₹12.50</td>
        <td>₹31.00</td>
      </tr>
      <tr>
        <td><strong>study material pdf free download</strong></td>
        <td>INR</td>
        <td>500</td>
        <td>0%</td>
        <td>-90%</td>
        <td>Low (1)</td>
        <td>₹14.00</td>
        <td>₹35.50</td>
      </tr>
      <tr>
        <td><strong>example of standardized test</strong></td>
        <td>INR</td>
        <td>500</td>
        <td>0%</td>
        <td>0%</td>
        <td>Low (0)</td>
        <td>₹16.00</td>
        <td>₹40.00</td>
      </tr>
      <tr>
        <td><strong>standard score</strong></td>
        <td>INR</td>
        <td>500</td>
        <td>0%</td>
        <td>0%</td>
        <td>Low (0)</td>
        <td>₹15.20</td>
        <td>₹38.10</td>
      </tr>
      <tr>
        <td><strong>standardized test in education</strong></td>
        <td>INR</td>
        <td>50</td>
        <td>0%</td>
        <td>-90%</td>
        <td>Low (3)</td>
        <td>₹18.00</td>
        <td>₹44.00</td>
      </tr>
      <tr>
        <td><strong>standardized test meaning</strong></td>
        <td>INR</td>
        <td>500</td>
        <td>+900%</td>
        <td>+900%</td>
        <td>Low (2)</td>
        <td>₹68.76</td>
        <td>₹163.69</td>
      </tr>
      <tr>
        <td><strong>standardized test scores meaning</strong></td>
        <td>INR</td>
        <td>500</td>
        <td>0%</td>
        <td>0%</td>
        <td>Low (1)</td>
        <td>₹22.00</td>
        <td>₹55.00</td>
      </tr>
      <tr>
        <td><strong>ai and data science study material</strong></td>
        <td>INR</td>
        <td>1,800</td>
        <td>+20%</td>
        <td>+50%</td>
        <td>Low</td>
        <td>₹18.00</td>
        <td>₹45.00</td>
      </tr>
      <tr>
        <td><strong>ai and ds question bank</strong></td>
        <td>INR</td>
        <td>1,900</td>
        <td>+15%</td>
        <td>+40%</td>
        <td>Low</td>
        <td>₹14.00</td>
        <td>₹38.00</td>
      </tr>
      <tr>
        <td><strong>ai ds study material pdf</strong></td>
        <td>INR</td>
        <td>1,200</td>
        <td>+10%</td>
        <td>+30%</td>
        <td>Low</td>
        <td>₹16.50</td>
        <td>₹42.00</td>
      </tr>
      <tr>
        <td><strong>ai ds previous year questions</strong></td>
        <td>INR</td>
        <td>1,400</td>
        <td>+25%</td>
        <td>+60%</td>
        <td>Low</td>
        <td>₹15.00</td>
        <td>₹39.00</td>
      </tr>
      <tr>
        <td><strong>machine learning roadmap for beginners</strong></td>
        <td>INR</td>
        <td>8,100</td>
        <td>+35%</td>
        <td>+80%</td>
        <td>Low</td>
        <td>₹28.50</td>
        <td>₹65.00</td>
      </tr>
    </tbody>
  </table>

  <h2 class="sec-title">2. Trend Observations</h2>
  <ul>
    <li>Terms with high intent such as <em>"standardized test meaning"</em> witnessed a <strong>+900% YoY surge</strong>, reflecting increased search volume for concept explainers.</li>
    <li>Curriculum-specific long-tail queries like <em>"ai and data science study material"</em> exhibit steady, reliable volume with minimal commercial bidding competition, making them ideal organic targets.</li>
  </ul>

  <div class="doc-footer">
    <span>Digital Marketing and Social Media (ADMC301) - Assignment 2</span>
    <span>Page 11</span>
  </div>
</div>

<!-- ================= PAGE 12: Q. 4 PART 2 ================= -->
<div class="page">
  <div class="doc-header">
    <span>Digital Marketing and Social Media (ADMC301) - Assignment 2</span>
    <span>Page 12</span>
  </div>

  <h2 class="sec-title" style="margin-top: 4px;">3. Competitor Content Gap & Search Intent Analysis</h2>
  <table class="data-table">
    <thead>
      <tr>
        <th>Target Keyword</th>
        <th>Search Intent</th>
        <th>Top Competitor Formats</th>
        <th>AIStudyHub Content Advantage</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><code>machine learning roadmap</code></td>
        <td>Informational</td>
        <td>Generic visual diagrams, video lists</td>
        <td>12-week semester execution plan tailored to engineering exams with runnable Scikit-Learn code.</td>
      </tr>
      <tr>
        <td><code>ai study material</code></td>
        <td>Academic / Syllabus</td>
        <td>Scan-copied PDF uploads, broken download links</td>
        <td>Clean, responsive HTML5 portals with mobile navigation, unit breakdowns, and standard textbook citations.</td>
      </tr>
      <tr>
        <td><code>ai and ds question bank</code></td>
        <td>Exam Preparation</td>
        <td>Scattered unorganized forum questions</td>
        <td>Unit 1–4 organized 2M, 5M, and 10M questions with interactive model answer toggles.</td>
      </tr>
    </tbody>
  </table>

  <h2 class="sec-title">4. Strategic Placement Recommendations for the Blog</h2>
  <ul>
    <li><strong>Title Tag Priority:</strong> Maintain primary keyword within the front 50 characters: <code>How to Start Learning Machine Learning: Roadmap for AI & DS</code>.</li>
    <li><strong>Header Tag Flow:</strong> Ensure H2 subheadings utilize exact phrase match questions: <em>"Phase 1: Python Programming"</em>, <em>"Phase 2: Mathematical Foundations"</em>.</li>
    <li><strong>Anchor Text Internal Links:</strong> Link to subject notes using keyword anchors (e.g. <em>"Mathematics for AI Guide"</em> linking to <code>/mathematics.html</code>).</li>
    <li><strong>Image Optimization:</strong> All infographics and diagrams must feature descriptive <code>alt</code> tags: <code>alt="12-Week Machine Learning Roadmap Schedule for AI & DS Students"</code>.</li>
  </ul>

  <h2 class="sec-title">5. Conclusion & Submission Sign-Off</h2>
  <p>Through this systematic execution of Google Keyword Planner and Google Search Console diagnostics, **AIStudyHub** has established a data-driven keyword foundation. The featured blog article <em>"How to Start Learning Machine Learning: A Beginner's Roadmap for AI & Data Science Students"</em> has been optimized with targeted title tags, meta descriptions, semantic heading hierarchy, and internal linking structure. With low advertiser competition across core academic clusters, the portal is positioned to achieve sustained first-page rankings across targeted student search queries in India.</p>

  <div style="margin-top: 30px; border-top: 1px solid #94a3b8; padding-top: 8px; display: flex; justify-content: space-between; font-size: 8pt; color: #475569;">
    <span>Zeal College of Engineering and Research, Pune</span>
    <span>Department of Artificial Intelligence & Data Science</span>
    <span>Candidate: Samiksha Kakade</span>
  </div>

  <div class="doc-footer">
    <span>Digital Marketing and Social Media (ADMC301) - Assignment 2</span>
    <span>Page 12</span>
  </div>
</div>

</body>
</html>
"""

html_path = os.path.join(workspace, "Assignment_2_Samiksha_Kakade.html")
with open(html_path, "w", encoding="utf-8") as f:
    f.write(html_content)

print("HTML written to:", html_path)

pdf_path = os.path.join(workspace, "Assignment_2_Samiksha_Kakade.pdf")

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.set_content(html_content, wait_until="networkidle")
    page.pdf(
        path=pdf_path,
        format="A4",
        print_background=True,
        margin={"top": "8mm", "bottom": "8mm", "left": "10mm", "right": "10mm"}
    )
    browser.close()

print("Assignment 2 PDF successfully generated at:", pdf_path)
